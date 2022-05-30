# COSC1519 Introduction to Programming
# Assessment 3 Programming Project
# Student name: Jingxuan Feng
# Student number: s3843790
# Practical group : 8 (Thursday 14:30-16:30)

"""
References
Used Scorptec to get some product ID and pricing

[1] favtutor, ‘Sort a List of Objects in Python’, FavTutor. https://favtutor.com/blogs/sort-list-of-objects-python (accessed May 30, 2022).
[2] ‘Scorptec Computers | Online Computer Store, Huge Range of the Best Brands, Fast Delivery, Laptops and Gaming’. https://www.scorptec.com.au/ (accessed May 30, 2022).

"""

# Global dictionary for storing stock
stock_dictionary = {}

# Global variable to store column structure
column_line = None


# Define class for stock objects
class StockItem:

    def __init__(self, item_id, item_price, quantity, item_name, item_description, item_warranty):
        self.item_id = item_id
        self.item_price = item_price
        self.quantity = quantity
        self.item_name = item_name
        self.item_description = item_description
        self.item_warranty = item_warranty

    # This method prints the object's values
    def get_all_item_attributes(self):
        item_attributes = self.item_id + " " + str(self.item_price) + " " + str(self.quantity) + " " \
                          + self.item_name + " " + self.item_description + " " + str(self.item_warranty)
        return item_attributes

    # This method helps prepare for outputing csv values
    def prepare_csv_output(self):
        item_attributes = self.item_id + ", " + str(self.item_price) + ", " + str(self.quantity) + ", " \
                          + self.item_name + ", " + self.item_description + ", " + str(self.item_warranty)
        return item_attributes

    # Getters
    def get_item_id(self):
        return self.item_id

    def get_item_price(self):
        return self.item_price

    def get_quantity(self):
        return self.quantity

    def get_item_name(self):
        return self.item_name

    def get_item_description(self):
        return self.item_description

    def get_item_warranty(self):
        return self.item_warranty

    # Setters
    def set_item_price(self, price):
        self.item_price = price

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_item_name(self, name):
        self.item_name = name

    def set_item_description(self, description):
        self.item_description = description

    def set_item_warranty(self, warranty):
        self.item_warranty = warranty


# Method to calculate inventory value (total stock cost)
def get_inventory_value():
    global stock_dictionary
    value = 0.0
    for item in stock_dictionary:
        value += stock_dictionary[item].get_item_price()
    return value


# Read the stock file and initiate the data structures
def read_stock(file_name):
    global stock_dictionary
    global column_line

    # attempt to read data from file
    try:
        file_handler = open(file_name, "r")

        # Ignore the column description first line
        column_line = file_handler.readline()
        for line in file_handler:
            # split the line by ',' then create a new stock_item object with the various attributes
            data = line.rstrip('\n').split(", ")
            stock_object = StockItem(data[0], float(data[1]), int(data[2]), data[3], data[4], data[5])

            # uses item ID as dictionary key, then object as the value
            stock_dictionary[data[0]] = stock_object

        # close the file handler
        file_handler.close()
        # prints the column structure & item attributes
        heading = "----------------------------------------------\n" \
                  "Loading Original Data\n" \
                  "----------------------------------------------"
        print(heading)
        print("Loading data from file:", file_name)
        print("Column titles in loaded file is:", column_line, end="")
        show_all_items_id()
        print("Current stock value: $", get_inventory_value(), end="")
    except:
        print("File may be corrupted or contains invalid values")


# Export the changes to a given filename
def save_changes_and_exit(file_name):
    global stock_dictionary
    global column_line

    show_all_items_info()
    print("\nPlease check current stock values and confirm if you want to exit. \n")
    ret_value = confirm_exit()

    if not ret_value:
        try:
            output_file_handler = open(file_name, "w")

            # Write the column structure
            output_file_handler.write(column_line)

            # Loop through dictionary and write all items to file
            for item in stock_dictionary:
                output_file_handler.write(stock_dictionary[item].prepare_csv_output())
                # Write new line to separate items
                output_file_handler.write('\n')

            output_file_handler.close()
        except:
            print("Failed to export file")
    return ret_value


# This function gets user user_input & validates it is a correct integer
def get_user_input_int(text_prompt):
    user_in = None
    continue_loop = True

    # continue asking for user_input until user_input is correct
    while continue_loop:
        try:
            user_in = int(input(text_prompt))
            continue_loop = False
        except:
            print("You did not enter a valid integer! \n")
    return user_in


# This function gets user user_input & validates it is a correct float
def get_user_input_float(text_prompt):
    user_in = None
    continue_loop = True

    # continue asking for user_input until user_input is correct
    while continue_loop:
        try:
            user_in = float(input(text_prompt))
            continue_loop = False
        except:
            print("You did not enter a valid float! \n")
    return user_in


# This function gets a string user user_input & validates it is not blank
def get_user_input_string(text_prompt):
    user_in = None
    continue_loop = True

    # Keep asking for input until user enters a value
    while continue_loop:
        user_in = input(text_prompt)
        input_not_empty = user_in is not None and user_in != ""
        input_contains_comma = "," in user_in

        if input_not_empty and not input_contains_comma:
            continue_loop = False
        if not input_not_empty:
            print("Your input cannot be empty! \n")
        if input_contains_comma:
            print("Your input cannot contain comma! \n")

    return user_in


# This function checks if the user's choice selection is valid
def validate_userinput_int(user_input, max_option):
    is_valid = False

    if user_input is not None:
        if 0 < user_input <= max_option:
            is_valid = True

    return is_valid


# This function gets the information of a single item and prints it to the user
def show_item_info(item_id):
    global stock_dictionary
    if check_item_exists(item_id):
        print(stock_dictionary.get(item_id).get_all_item_attributes())
    else:
        print("Entered item ID does not exist")


# Check if an item with a given item_id exists, then return boolean value
def check_item_exists(item_id):
    global stock_dictionary
    name = None
    ret_value = None

    try:
        name = stock_dictionary.get(item_id).get_item_id()
    except:
        ret_value = False

    if name is not None:
        ret_value = True

    return ret_value


# This functions shows the item ID of all items loaded in memory
def show_all_items_id():
    global stock_dictionary
    print("Items in inventory are: ", end="")
    for item in stock_dictionary:
        print(stock_dictionary[item].get_item_id(), end=", ")
    print("\n")


# This function gets the information for all items and prints it to the user
def show_all_items_info():
    global stock_dictionary
    stock_list = []

    # Add all dictionary objects to list
    for item in stock_dictionary:
        stock_list.append(stock_dictionary[item])

    # Referenced [1], sorts the items based on the item name
    stock_list.sort(key=lambda x: x.item_name)

    # Store list of full item details, so we can reformat the output text
    for stock in stock_list:
        print(stock.get_all_item_attributes())


# This function tries to add a new item to stock
def add_new_item():
    new_item_id = get_user_input_string("Please enter the item ID: ")

    continue_process = False
    if check_item_exists(new_item_id):
        print("An item with this ID already exists!")
    else:
        continue_process = True

    if continue_process:
        new_item_price = get_user_input_float("Please enter the item price: ")
        new_item_quantity = get_user_input_int("Please enter the item quantity: ")
        new_item_name = get_user_input_string("Please enter the item name: ")
        new_item_description = get_user_input_string("Please enter the item description: ")
        new_item_warranty = get_user_input_int("Please enter the warranty period (integer value in years): ")

        # Create the object then store into dictionary
        new_stock_object = StockItem(new_item_id, new_item_price, new_item_quantity, new_item_name,
                                     new_item_description, new_item_warranty)
        stock_dictionary[new_item_id] = new_stock_object
        print("Item added successfully!", new_stock_object.get_item_id(), new_stock_object.item_price,
              new_stock_object.get_quantity(), new_stock_object.get_item_name(),
              new_stock_object.get_item_description(), new_stock_object.get_item_warranty())


# This function tries to update an existing item
def update_item_info():
    global stock_dictionary
    item_id = get_user_input_string("Please enter the item ID: ")
    continue_process = False
    if check_item_exists(item_id):
        continue_process = True
    else:
        print("No item found with this ID")

    if continue_process:
        # Get the object from the dictionary
        item_to_edit = stock_dictionary.get(item_id)

        # Show user the current item information
        current_item_attributes = """
        Current Price is: {}
        Current quantity of item is: {}
        Current Item Name: {}
        Current Item Description: {}
        Current Item Warranty Period (years) is: {} \n""".format(item_to_edit.get_item_price(), item_to_edit.get_quantity(),
                                                              item_to_edit.get_item_name(), item_to_edit.get_item_description(),
                                                              item_to_edit.get_item_warranty())
        print(current_item_attributes)

        # Update the attributes
        item_to_edit.set_item_price(get_user_input_float("Please enter the updated price: "))
        item_to_edit.set_quantity(get_user_input_int("Please enter the updated stock quantity: "))
        item_to_edit.set_item_name(get_user_input_string("Please enter the updated item name: "))
        item_to_edit.set_item_description(get_user_input_string("Please enter the updated item description: "))
        item_to_edit.set_item_warranty(
            get_user_input_int("Please enter the updated warranty period (integer value in years): "))

        # Save back to dictionary
        stock_dictionary[item_id] = item_to_edit
        # Show user updated item info
        show_item_info(item_id)


# This function tries to remove an existing item
def remove_item():
    global stock_dictionary
    item_id = get_user_input_string("Please enter the item ID: ")
    try:
        del stock_dictionary[item_id]
    except:
        print("Entered item ID does not exist")


# This function checks if the user really wants to leave without saving
def exit_without_saving():
    print("Are you sure you want to leave without saving? Any changes will be lost!")
    # This value tells the main program whether to continue running: true = keep running, false = end program
    return confirm_exit()


# Confirms with user if they really do want to exiT
def confirm_exit():
    incorrect_input = True
    ret_value = None
    # This loop keeps asking for user input until one of the two valid options is entered
    while incorrect_input:
        user_input = get_user_input_string("Confirm (y/n): ")
        if user_input.upper() == "Y":
            ret_value = False
            incorrect_input = False
        elif user_input.upper() == "N":
            ret_value = True
            incorrect_input = False
        else:
            print("Invalid input! y/n only! \n")
    return ret_value



# Main menu of the program
def main_menu():
    # Read data from file
    read_stock("A3_s3843790_stock.txt")

    # Set the menu options and welcome text
    menu_options = "\n" \
                   "----------------------------------------------\n" \
                   "Main Menu\n" \
                   "----------------------------------------------\n" \
                   "1. Show one item information \n" \
                   "2. Show all items' information \n" \
                   "3. Add an item to stock \n" \
                   "4. Update existing item \n" \
                   "5. Remove existing item \n" \
                   "6. Save changes and exit \n" \
                   "7. Exit without saving \n"

    continue_program = True
    while continue_program:
        print(menu_options)
        # print out all current items for user
        show_all_items_id()

        user_choice = get_user_input_int("Please enter an integer to select an option: ")

        # Check that the user's entered int is part of the available options in the menu
        if validate_userinput_int(user_choice, 7):
            if user_choice == 1:
                show_item_info(get_user_input_string("Please enter the item ID: "))
            elif user_choice == 2:
                show_all_items_info()
            elif user_choice == 3:
                add_new_item()
            elif user_choice == 4:
                update_item_info()
            elif user_choice == 5:
                remove_item()
            elif user_choice == 6:
                continue_program = save_changes_and_exit("updated_A3_s3843790_stock.txt")
            elif user_choice == 7:
                continue_program = exit_without_saving()

        else:
            print("You did not enter a valid menu option! \n")

    # Let user know the program is ending
    print("Quitting program...")


# Run the program
main_menu()
