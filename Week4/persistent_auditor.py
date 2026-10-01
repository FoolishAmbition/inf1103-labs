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

"""
def get_valid_input():
    user_input = input("Enter the number of items of stock quantity please use integers (or type 'quit' to quit): ")

    if user_input.lower() == 'quit':
        return "quit"

    if user_input.isdigit():
        return int(user_input)

    if user_input.startswith('-') and user_input[1:].isdigit():
        print("Error: Please use positive integers only.")
        return None

    print("Error: Please use integers only.")
    return None

def process_delivery(current_total, new_value):
     return current_total + new_value #Calculates the new total of inventory after adding the new value



def calculate_tax(amount):
    return round(amount * 0.10, 2) #Calculates the tax amount based on a 10% tax rate

def generate_report(total_units, failed_attempts): 
    print("Total Units Processed: ", total_units)
    print("Number of Failed/Rejected Entries: ", failed_attempts)

def main():
    inventory = 0
    failed_entries = 0
    total_tax = 0

    while True:
        result = get_valid_input()
        if result == "quit":
            break
        if result is None:
            failed_entries += 1
            continue

        inventory = process_delivery(inventory, result)
        total_tax += calculate_tax(result)

        if inventory > 500:
            print("Alert: Inventory limit exceeded.")
            break
    generate_report(inventory, failed_entries)
    print("Total Tax Collected: ", round(total_tax, 2))

if __name__ == "__main__":
    main()

"""

def main():
    inventory = load_inventory()
    print("Loaded Inventory:", inventory)

    save_inventory(inventory)

main()