# Codebase Map — INF1103 Lab 8

## Verified Week 7 snapshot

Source is the uploaded `Week7.zip`, rooted at `Week7/`. It has no Git metadata. The active checkout, branch, remote and history need to be checked before implementation.

| File | Verified role | Proposed Lab 8 touchpoint |
|---|---|---|
| `main.py` | Models, inventory, JSON load/save, CLI | Keep the existing layout unless a split is approved. Update constructor call sites, introduce relationships and annotate the model. |
| `test_products.py` | 16 standard-library `unittest` tests in two classes | Keep regression assertions, update fixtures for supplier injection and add focused Lab 8 tests. |
| `inventory.json` | Three typed records, P001 Laptop, D001 Antivirus and P002 Keyboard | Approve handling of records without supplier fields before editing persistence. |
| `Dockerfile` | `python:3.11-slim`, workdir `/usr/src/app`, copies main, tests and JSON, starts `python main.py` | Keep build runnable. Update copy rules if approved new modules or test files require it. |
| `Lab7_UML.png`, `Week7Submission.docx` | Prior UML and submission artifacts in archive | Create the updated UML and Lab 8 evidence during their approved milestones. |
| `__pycache__/` | Generated Python 3.12 bytecode | Keep generated files out of staged Lab 8 changes. |

## Verified behavior and dependencies

- `Product(ABC)` has constructor `(product_id, name, price, stock)` and stores `_product_id`, `_name`, `_price`, `_stock`. `update_stock(quantity)` sets the absolute stock for a nonnegative quantity and returns `True`. For a negative quantity it preserves stock and returns `False`. `display_information()` prints the common fields, `to_dict()` serializes them, and `get_fulfilment_info()` is abstract.
- `PhysicalProduct(..., weight)` and `DigitalProduct(..., download_size)` call `super().__init__`, extend display and serialization, and each supplies fulfilment behavior. The physical product alone implements weight × 5.00 shipping and is registered as a virtual subclass via `CanBeShipped.register(PhysicalProduct)`. `CanBeShipped(ABC)` declares the abstract shipping operation.
- `Inventory._products` is an unannotated list. `add_product` returns a boolean, prints a duplicate-ID error and uses `search_product`. Lookup returns the existing object or `None`. `display_all` handles the empty case and already dispatches `display_information()` through a single loop. The Week 7 snapshot has no `find_product`, `remove_product`, supplier or order models, or public `price` property.
- `main()` calls `load_inventory()`, then offers display, add, update stock, search, save and exit with save. Menu add constructs both subtypes. Update and search rely on `search_product`. Menu validation handles invalid numeric input, negative price/stock and nonpositive weight/download size.
- `load_inventory()` reads `INVENTORY_FILE` relative to the current directory and constructs subtypes using each record's `type`. A missing file starts an empty inventory. Malformed data or unknown/missing type causes a logged failure and re-raise without writing the file. `save_inventory()` serializes every item in `inventory._products` through `to_dict()`. All three valid sample records lack supplier fields. The test for a legacy record without a **type** covers a distinct failure case.
- Baseline verification on 13 November 2026 ran the extracted, unchanged suite with Python and workspace-local temporary storage. All 16 passed. The initial run reported two temporary-file permission errors, resolved by redirecting `TEMP` and `TMP`. Docker and Git history remain unverified.

## Proposed integration

1. Draw the relationship and types before editing. Introduce `Supplier` and update all constructor callers together. Approve how the CLI creates/reuses suppliers and how typed records without supplier data load and round-trip. Supplier records reconstructed by ID may share one instance where appropriate. Avoid inventing real supplier data.
2. Add typed `find_product` and `remove_product` to the existing collection. Preserve `add_product`'s boolean and duplicate semantics. Reuse one lookup implementation and keep `search_product` as a compatibility wrapper if callers still use it.
3. Use a read-only `Product.price` property as a proposed way to expose price for `OrderLine` while keeping `_price` as the source of truth. Have `Order` create each line internally, and let each line calculate its own subtotal from its referenced product.
4. Keep subtype branching at reconstruction and menu construction where a concrete class must be selected. For operations on existing products, call the common Product methods directly. Demonstrate order and transfer behavior in focused tests unless additional menu actions are approved.

See the [requirements and proposed UML](PRD_Lab8.md) and [milestone tracker](Lab8_Project_Plan_and_Progress.md). The EventWise codebase example supplied the baseline, file map, contracts and integration structure.
