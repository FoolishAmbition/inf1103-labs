# Global Constants
ITEM_FIELDS = {"id": 0, "name": 1, "quantity": 2, "transaction_history": 3}
INVENTORY_FILE = "inventory.txt"
MAX_CAPCITY = 500
TAX_RATE = 0.1
EXIT_SIGNAL = "quit"

def load_inventory():
    """ Reads inventory.txt and then returns a list of items as well as the transaction history for each item. """
    inventory = []
    try:
        # 1. Open the file in read mode ("r")
        with open(INVENTORY_FILE, "r") as file:

            # 2. Loop through each line in the file
            for line in file:
                # Remove any trailing newline characters
                line = line.strip() 

                # Skip empty lines just in case
                if not line:
                    continue

                # 3. Split the line by comma
                parts = line.split(",")

                # 4. Extract the data
                item_id = parts[0]
                name = parts[1]
                quantity = int(parts[2])

                # 5. Handle the transaction history
                history_string = parts[3]

                # If the history is empty, handle it
                if history_string == "":
                    history = []
                else:
                    # Split by "|" and convert each to an integer
                    history = [int(x) for x in history_string.split("|")]
                    
                # 6. Create the item list
                # Use your ITEM_FIELDS constants to keep it clean
                item = [item_id, name, quantity, history]

                # 7. Add the item to the inventory list
                inventory.append(item)

    except FileNotFoundError:
                # runs if the inventory.txt file is not found
                print("No inventory file is found. Starting with an empty inventory.")
                return []

    return inventory

def save_inventory(inventory):
    """ Write the current inventory list to inventory.txt with the transaction history for each item. """
    with open(INVENTORY_FILE, "w") as file:
        for item in inventory:
            # Extract the data from the item list
            item_id = item[ITEM_FIELDS["id"]]
            name = item[ITEM_FIELDS["name"]]
            quantity = item[ITEM_FIELDS["quantity"]]
            history = item[ITEM_FIELDS["transaction_history"]]

            # Convert the history list to a string
            # Format: "id,name,quantity,history_string"
            history_string = "|".join(str(x) for x in history)
            line = f"{item_id},{name},{quantity},{history_string}\n"

            # write the line to the file
            file.write(line)

    print("Inventory saved successfully.")

def get_valid_input(item):
     """Prompts and validate the quanity to add for a given item."""
     name = item[ITEM_FIELDS["name"]]
     user__input = input(f"Enter quantity for {name} (or type 'quit' to quit): ")

     if user__input.lower() == EXIT_SIGNAL:
         return EXIT_SIGNAL

     if user__input.isdigit() and int(user__input) >= 0:
          return int(user__input)

     print("Error: Please use positive integers only.")
     return None

def process_delivery(item, new_quantity):
     """Updates the item quanity and append the transaction history. Updates the item direction. """
     item[ITEM_FIELDS["quantity"]] += new_quantity

     # append the new quanity to the history list
     item[ITEM_FIELDS["transaction_history"]].append(new_quantity)
     # return None (it modifies the list directly, so no need to return anything)

"""

def calculate_tax(amount):
    return round(amount * 0.10, 2) #Calculates the tax amount based on a 10% tax rate

"""

def generate_report(inventory, failed_attempts): 
    total_units = sum(item[ITEM_FIELDS["quantity"]] for item in inventory)
    
    print("\n--- Final Summary ---")
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)



def find_item(inventory, item_id):
     """Searches inventory by item ID. Returns the item list or None if not found."""
     for item in inventory:
          if item[ITEM_FIELDS["id"]] == item_id:
               return item
     return None 

def display_inventory(inventory):
     """Displays all inventory items"""
     print("\nCurrent Orders:")
     for item in inventory:
          print(f"{item[ITEM_FIELDS['id']]}, {item[ITEM_FIELDS['name']]}, {item[ITEM_FIELDS['quantity']]}")



def main():
    inventory = load_inventory()
    failed_entries = 0

    # Helper function to print the current list
    display_inventory(inventory)

    while True:
         # 1. Asks for item ID
         item_id = input("\nEnter Product ID (or type 'quit' to quit): ")

         if item_id.lower() == EXIT_SIGNAL:
             break

         # 2. Find the item 
         item = find_item(inventory, item_id)
         if item is None:
              print(f"Error: Item ID '{item_id}' not found.")
              failed_entries += 1
              continue

         # 3. Ask for quantity using the item
         quantity = get_valid_input(item)

         if quantity == EXIT_SIGNAL:
             break
         if quantity is None:
              failed_entries += 1
              continue

         # 4. Process the delivery (this will update the item quantity and transaction history)
         process_delivery(item, quantity)
         print(f"\nNew Order Added: {item[ITEM_FIELDS['id']]}, {item[ITEM_FIELDS['name']]}, {item[ITEM_FIELDS['quantity']]}")

         # 5. Save everything back to the file and print the report
    
    save_inventory(inventory)
    generate_report(inventory, failed_entries)

if __name__ == "__main__":
    main()