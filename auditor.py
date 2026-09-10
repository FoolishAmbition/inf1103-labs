inventory = int(0)
failed_entries = 0

while True:
   user_input = input("Enter the number of items of stock quantity please use integers (or type 'quit' to quit): ")
   if user_input.lower() == 'quit':
       print("Total Units Processed: ", inventory, "\n"
           "Number of Failed/Rejected Entries: ", failed_entries)
       break
   if user_input.isdigit():
        inventory += int(user_input)
   elif user_input.startswith('-') and user_input[1:].isdigit():
        failed_entries += 1
        print("Error: Please use positive integers only.")
   else:
        failed_entries += 1
        print("Error: Please use integers only.")

   if inventory > 500:
      print("Total Units Processed: ", inventory, "\n"
           "Number of Failed/Rejected Entries: ", failed_entries)
      break

