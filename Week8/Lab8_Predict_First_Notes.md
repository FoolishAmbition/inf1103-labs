# INF1103 Lab 8 Predict First notes

## Record sequence

The predictions below were recorded on 13 November 2026 at 21:30:41 Singapore time before running the four remaining demonstrations in this session. Observations and comparisons were added afterwards. These are proposed explanations prepared during this session, not a record of predictions made earlier in the lab.

## PF1 Supplier association

**Prediction:** I expect both products to still display the supplier information after `del supplier`. Each product stores a reference to the Supplier object, so deleting the variable does not remove the references held by the products.

**Observation:** Both products displayed S001, Demo Supplier and the contact email after `del supplier`. The identity comparison between their supplier references returned True.

**Comparison:** The result matched the prediction. Deleting the local variable removed that name, while the products still held references to the Supplier object.

## PF2 Inventory aggregation

**Prediction:** I expect the product to still work after it is removed from Inventory A. The inventory stores a reference to the product, and removing that entry does not delete the product that my test variable still refers to. I should be able to add that same object to Inventory B.

**Observation:** Removal from A returned True. The product still displayed normally and its stock update to 8 succeeded. A's lookup returned None, and B's lookup returned the original object after it was added there.

**Comparison:** The result matched the prediction. Inventory manages references rather than the lifetime of the Product, so the same product could be used and transferred.

## PF3 Order composition

**Prediction:** For a fresh example where I create one Product and add it once to each of two Orders, I expect one Product object and two OrderLine objects. Each Order creates its own line, while the lines refer to the original product. I will compare the lines and their product references using `is`.

**Observation:** The line objects were different, but both line.product references were the same original Product. The two totals were 1200.0 and 2400.0 for quantities 1 and 2. Removing the first Order's line did not change the second Order's total.

**Comparison:** The result matched the prediction: one Product and two separate OrderLines. Each Order manages its own line, while neither line owns the Product.

## PF4 Mixed product polymorphism

**Prediction:** I expect PhysicalProduct's fulfilment call to print `This product requires physical shipping.` and DigitalProduct's call to print `This product is delivered digitally.` The same loop calls the common Product methods, but each object's override provides its own behaviour.

**Observation:** The mixed loop printed `This product requires physical shipping.` for PhysicalProduct and `This product is delivered digitally.` for DigitalProduct. Their displays also included the physical weight and digital download size respectively.

**Comparison:** The result matched the prediction. The loop used the common Product operations without checking subclasses, and Python called the overrides belonging to the actual objects.

## LSP diagnosis

The proposed DigitalProduct override violates LSP because it raises an error for stock updates that Product supports, and it does not preserve the boolean result expected by callers. I would remove that override and keep the inherited stock behaviour for this inventory system. If digital products were redesigned to have no stock at all, I would review the parent responsibilities or inheritance instead of adding subtype checks to Inventory.

## UML review and AI use

**Suggestion accepted:** I kept the suggested read-only `price` property so OrderLine can read a product's price without adding a second price field or directly using `_price`.

**Draft changed:** The initial diagram did not show the Order methods for displaying information and removing a line. The revised diagram includes `display_information()` and `remove_order_line(index)` so it matches the implemented API.

Supplier–Product is association because the supplier is a collaborator, not a product part. Inventory–Product is aggregation because the products have an independent lifetime. Order–OrderLine is composition because the Order creates and manages its own lines; the line's Product reference remains an association.
