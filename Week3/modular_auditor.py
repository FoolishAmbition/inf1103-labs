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