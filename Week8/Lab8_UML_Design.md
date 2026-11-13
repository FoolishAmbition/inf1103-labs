# Lab 8 typed relationship design

This provisional design adapts the [PRD draft](Background/PRD_Lab8.md) for the active `Week8/` application. Supplier association, Inventory lookup/removal and Order composition are implemented and tested. Official PF-1, PF-2 and PF-3 demonstrations remain deferred. Later milestones still need a focused proposal and explicit approval. The final submission diagram must be checked against the finished source and exported legibly.

## Relationships and ownership

| Relationship | Meaning and multiplicities |
|---|---|
| PhysicalProduct and DigitalProduct inherit Product | Each concrete class is a Product. The hollow triangle points to Product. |
| PhysicalProduct implements CanBeShipped virtually | Preserve the existing ABC registration; do not imply that registration supplies methods. |
| Supplier associated with Product | Each Product references one Supplier; a Supplier may supply zero or more Products. Neither is an owned part of the other. |
| Inventory aggregates Product | Each Inventory groups zero or more Products. A Product may belong to zero or more Inventories, preserving the existing collection's allowance for shared references. Inventory does not own Product lifetimes. |
| Order composed of OrderLine | Each Order manages zero or more lines; each line belongs to exactly one Order. Order creates its lines internally and provides no API to transfer or share them between Orders. |
| OrderLine associated with Product | Each line references one independent Product; a Product may be referenced by zero or more lines. This reference does not give the line ownership of the Product. |

Multiplicity at an endpoint counts instances at that endpoint for one object at the opposite endpoint. The hollow diamond marks the aggregating whole; the filled diamond marks the composing whole. Python references and garbage collection do not automatically enforce the intended ownership rules.

## Provisional typed class diagram

```mermaid
classDiagram
    class Product {
        <<abstract>>
        #String _product_id
        #String _name
        #Real _price
        #Integer _stock
        +Supplier supplier
        +Real price
        +Product(product_id String, name String, price Real, stock Integer, supplier Supplier)
        +update_stock(quantity Integer) Boolean
        +display_information() None
        +get_fulfilment_info() String
        +to_dict() ProductRecord
    }
    class PhysicalProduct {
        #Real _weight
        +PhysicalProduct(product_id String, name String, price Real, stock Integer, weight Real, supplier Supplier)
        +display_information() None
        +get_fulfilment_info() String
        +calculate_shipping_cost() Real
        +to_dict() ProductRecord
    }
    class DigitalProduct {
        #Real _download_size
        +DigitalProduct(product_id String, name String, price Real, stock Integer, download_size Real, supplier Supplier)
        +display_information() None
        +get_fulfilment_info() String
        +to_dict() ProductRecord
    }
    class CanBeShipped {
        <<interface>>
        +calculate_shipping_cost() Real
    }
    class Supplier {
        +String supplier_id
        +String name
        +String contact_email
        +Supplier(supplier_id String, name String, contact_email String)
        +display_information() None
        +to_dict() SupplierRecord
    }
    class Inventory {
        -List~Product~ _products
        +Inventory()
        +add_product(product Product) Boolean
        +remove_product(product_id String) Boolean
        +find_product(product_id String) OptionalProduct
        +search_product(product_id String) OptionalProduct
        +display_all() None
    }
    class Order {
        +String order_id
        -List~OrderLine~ _order_lines
        +Order(order_id String)
        +add_order_line(product Product, quantity Integer) None
        +remove_order_line(index Integer) Boolean
        +calculate_total() Real
        +display_information() None
    }
    class OrderLine {
        +Product product
        +Integer quantity
        +OrderLine(product Product, quantity Integer)
        +calculate_subtotal() Real
    }
    Product <|-- PhysicalProduct
    Product <|-- DigitalProduct
    CanBeShipped <|.. PhysicalProduct : virtual registration
    Supplier "1" -- "0..*" Product
    Inventory "0..*" o-- "0..*" Product
    Order "1" *-- "0..*" OrderLine
    OrderLine "0..*" -- "1" Product
```

## Types and preserved contracts

- UML `String`, `Real`, `Integer` and `Boolean` correspond to Python `str`, `float`, `int` and `bool`. `None` indicates no returned value. Python constructors will use `-> None`; UML constructor entries name the class being constructed.
- `OptionalProduct` is shorthand for zero or one Product result, expressed as `Product | None` in Python. Callers must handle the missing result before invoking Product methods.
- `List<Product>` and `List<OrderLine>` describe collection element types. `list[Product]` supports both existing concrete Product types through their common operations.
- Implemented: `add_product(...) -> bool` preserves duplicate-ID rejection. `find_product(...) -> Product | None` contains the lookup loop; `search_product(...)` delegates to it for compatibility.
- Preserve `update_stock(...) -> bool`: a nonnegative quantity sets absolute stock and succeeds; a negative quantity leaves stock unchanged and returns false.
- Implemented: `remove_product(...) -> bool` returns true when an entry was removed, false for a missing ID. Read-only `price` access uses `_price` as its source of truth.
- `SupplierRecord` is a Python TypedDict containing string fields `supplier_id`, `name` and `contact_email`. `ProductRecord` is a TypedDict with `id: str`, `name: str`, `price: float`, `stock: int` and `supplier: SupplierRecord`. Its subtype-specific fields `type: str`, `weight: float` and `download_size: float` are `NotRequired` because the common Product serializer builds the record before each subtype extends it. These are record descriptions, not domain classes.
- Type hints communicate intent and support analysis tools. They do not automatically validate runtime values or enforce ownership.

## Decisions still required before implementation

| Milestone | Open decisions |
|---|---|
| Supplier association | Milestone 1 decisions below; the official deletion demonstration remains deferred until the student records a prediction. |
| Inventory aggregation | Typed lookup/removal implemented; lookup delegation and boolean meanings recorded above. Shared-membership allowance unchanged. Official PF-2 demonstration deferred. |
| Order composition | Milestone 3 approved design below; PF-3 identity demonstration remains deferred. |
| Type and UML review | Resolve serialization placeholders, synchronize all signatures and attributes, check multiplicities against implementation and export the complete submission diagram. |

Order checkout, order persistence and additional menu actions remain outside the proposed scope. All four official Predict First answers and the student's AI-diagram reflection (one suggestion accepted and one changed) remain to be recorded in the student's own words. This design contains no demonstration output.

## Milestone 0 review

On 13 November 2026, the student distinguished association, aggregation and composition, interpreted optional membership and empty collections, and explained why a Product-typed collection supports both subtypes. After clarification, the student selected checking `result is not None` before using an optional lookup result. This establishes the introductory design understanding; implementation and runtime evidence remain pending.

## Milestone 1 implementation decisions

- Supplier is constructed independently and injected as the final argument into Product and both subtype constructors. Product retains `supplier: Supplier`; common display includes supplier information.
- Supplier IDs and names must be nonempty strings; email is a string and may be empty to represent unavailable contact information. The reserved ID `UNKNOWN` has name `Unknown supplier` and an empty email; the CLI cannot create a real supplier using that ID.
- Missing supplier fields in otherwise typed Week 7 JSON records map to this explicitly labelled placeholder. Loading does not rewrite the input file. Saving adds nested supplier details; subsequent loading reuses one Supplier per ID within that load. Conflicting details for the same ID are rejected without modifying the file. Explicitly malformed supplier data is rejected rather than treated as missing.
- CLI add asks for supplier details after validating the product's numeric fields. An existing supplier ID reuses the object referenced by a current inventory product; a new ID asks for name and contact email. No global registry is introduced: direct model callers are responsible for consistent IDs, and CLI/load enforce reuse within their inventory/session.
- ProductRecord and SupplierRecord describe the serialized shape using standard-library TypedDict and NotRequired, compatible with the Dockerfile's Python 3.11.
- Menu options, stock semantics and shipping behavior stay unchanged. The sample JSON remains unchanged; supplier fields are added only when the user saves.

## Milestone 2 implementation review

Inventory holds `list[Product]`; constructor, add, find, search, remove and display methods have type annotations. The diagram's Inventory signatures now match the source. No transfer method or extra menu option is introduced: the existing add/remove API is the intended interface. Transfer evidence remains deferred until PF-2 is recorded.

## Milestone 3 approved design

- `Product.price` is a read-only property returning the current `_price` as a float. No second price field is stored. Order totals use current prices, not historical snapshots.
- `OrderLine` stores `product: Product` and `quantity: int`. Construction rejects zero, negative, non-integer and boolean quantities with ValueError. `calculate_subtotal() -> float` multiplies product price by quantity.
- `Order` validates a nonempty string ID. Callers supply unique IDs; no global registry is introduced. Its `_order_lines: list[OrderLine]` is internal storage. `add_order_line(product: Product, quantity: int) -> None` creates each line internally; no method accepts a prebuilt line or transfers one.
- `remove_order_line(index: int) -> bool` uses a zero-based index. It returns false for an out-of-range index, including negative indexes, and true for a removed entry. Display shows each line's zero-based index, product information, quantity and subtotal, followed by the total.
- `calculate_total() -> float` delegates to each line's subtotal method and starts from 0.0 for an empty order. Adding or removing lines does not change stock. Line inspection for tests uses the internal list; no public mutable collection is added.
- These ownership rules describe the supported API. Python does not prevent deliberate external access to underscore-prefixed storage or independently constructing an OrderLine.
- Orders are not persisted and no CLI option is added. Focused tests cover one-order behavior; the official two-order identity experiment remains deferred until PF-3 is recorded.
- Verification: 11 focused Order tests passed. Full Week7/Week8 regression discovered 67 tests: 66 passed, 1 PF-2 test skipped. The Order signatures above match the implemented API; final whole-system type/UML review remains Milestone 4.
