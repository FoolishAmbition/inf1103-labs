import csv
import json
from pathlib import Path
from tempfile import NamedTemporaryFile

from products import Inventory, ProductFactory


def load_inventory(path: Path) -> Inventory:
    inventory = Inventory()
    try:
        with path.open(encoding="utf-8-sig") as file:
            items = json.load(file)
    except FileNotFoundError:
        return inventory

    if not isinstance(items, list):
        raise ValueError("Expected a list of products in inventory.json.")
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("Expected a product object in inventory.json.")
        product = ProductFactory.create(
            item.get("type"), item["id"], item["name"], item["price"], item["stock"],
            weight=item.get("weight"), download_size=item.get("download_size"),
        )
        if not inventory.add_product(product):
            raise ValueError(f"Duplicate product ID: {product.product_id}")
    return inventory


def save_inventory(path: Path, inventory: Inventory) -> None:
    records = [product.to_dict() for product in inventory.products()]
    # Replace the saved inventory only after the new file has been written.
    with NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as file:
        temporary_path = Path(file.name)
        try:
            json.dump(records, file, indent=4, allow_nan=False)
            file.close()
            temporary_path.replace(path)
        finally:
            file.close()
            temporary_path.unlink(missing_ok=True)


def load_products(path: str | Path, inventory: Inventory) -> None:
    try:
        file = open(path, newline="", encoding="utf-8-sig")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    except OSError as error:
        print(f"Could not open products file: {error}")
    else:
        loaded = 0
        with file:
            rows = csv.reader(file, strict=True)
            try:
                next(rows, None)  # The provided CSV starts with a header.
                for row in rows:
                    try:
                        product_type, product_id, name, price, stock = row
                        product = ProductFactory.create(
                            product_type, product_id, name, float(price), int(stock)
                        )
                        if not inventory.add_product(product):
                            raise ValueError(f"Duplicate product ID: {product_id}")
                    except ValueError as error:
                        print(f"Row {rows.line_num} skipped: {error}")
                    else:
                        loaded += 1
            except (csv.Error, UnicodeError, OSError) as error:
                print(f"Could not finish reading products file: {error}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")
