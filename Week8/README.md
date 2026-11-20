# Lab 9 inventory manager

From the repository root:

```powershell
python Week8/main.py
Push-Location Week8
python -m unittest discover -s tests -v
Pop-Location
```

Choose **7** to import the sample CSV into the inventory. The starter inventory is empty so the first import loads three rows and skips two. Importing the same catalogue again reports duplicate IDs. The CLI reads and saves `inventory.json` alongside the Python files.

The CSV has five columns: `product_type,product_id,name,price,stock_quantity`. The supplied rows have no weight or download size. Those fields are saved as JSON `null` and shown as unknown. A shipping cost requires a known weight.

The order model takes a discount at construction and supports changing it later with `set_discount()`. Use `Order.add_product(product, quantity)` to add lines and `calculate_total()` to check the result. Orders are covered by the automated tests.

```powershell
docker build -t inf1103-lab9 ./Week8
docker run --rm inf1103-lab9 python -m unittest discover -s tests -v
docker run --rm -it inf1103-lab9
```

The disposable container keeps saved inventory until it exits.

See [UML.md](UML.md) for the class diagram and [Predict First.docx](Predict%20First.docx) for the completed prediction report. See [screenshots](screenshots/) for the Git and Docker evidence.
