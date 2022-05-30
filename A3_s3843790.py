# COSC1519 Introduction to Programming
# Assessment 3 Programming Project
# Student name: Jingxuan Feng
# Student number: s3843790
# Practical group : 8 (Thursday 14:30-16:30)

# Global dictionary for storing stock
stock_dictionary = {}


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
    def display_item_attributes(self):
        # item_attributes = self.item_id + " | " + str(self.item_price) + " | " + str(self.quantity) + " | " \
        #                   + self.item_name + " | " + self.item_description + " | " + self.item_warranty
        print(self.item_id, self.item_price, self.quantity, self.item_name, self.item_description, self.item_warranty,
              end="")

    # Getters
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

    # attempt to read data from file
    try:
        file_handler = open(file_name, "r")

        # Ignore the column description first line
        column_line = file_handler.readline()
        for line in file_handler:
            # split the line by ',' then create a new stock_item object with the various attributes
            data = line.split(", ")
            stock_object = StockItem(data[0], float(data[1]), int(data[2]), data[3], data[4], data[5])

            # uses item ID as dictionary key, then object as the value
            stock_dictionary[data[0]] = stock_object

        # prints the column structure & item attributes
        print(column_line, end="")
        show_all_items_info()
        print("\n\nCurrent stock value: $", get_inventory_value())
    except:
        print("File may be corrupted or contains invalid values")


# Export the changes to a given filename
def save_changes_and_exit(file_name):
    # TODO
    print("Exported file")


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
        input_not_empty = user_in != None and user_in != ""

        if input_not_empty:
            continue_loop = False
        else:
            print("Your input cannot be empty! \n")

    return user_in


# This function checks if the user's choice selection is valid
def validate_userinput_int(user_input, max_option):
    is_valid = False

    if user_input is not None:
        if 0 < user_input <= max_option:
            is_valid = True

    return is_valid


# This function gets the information of a single item and prints it to the user
def show_item_info():
    global stock_dictionary
    item_id = get_user_input_string("Please enter the item ID: ")

    try:
        stock_dictionary.get(item_id).display_item_attributes()
    except:
        print("Entered item ID does not exist")


# This function gets the information for all items and prints it to the user
def show_all_items_info():
    global stock_dictionary
    for item in stock_dictionary:
        stock_dictionary[item].display_item_attributes()


# This function tries to add a new item to stock
def add_new_item():
    # TODO
    print("Added item!")


# This function tries to update an existing item
def update_item_info():
    item_id = get_user_input_string("Please enter the item ID: ")
    # TODO
    print("Updated item! " + item_id)


# This function tries to remove an existing item
def remove_item():
    item_id = get_user_input_string("Please enter the item ID: ")
    # TODO
    print("Removed item " + item_id)


# This function checks if the user really wants to leave without saving
def exit_without_saving():
    print("Are you sure you want to leave without saving? Any changes will be lost!")

    # This value tells the main program whether to continue running: true = keep running, false = end program
    ret_value = None

    # This loop keeps asking for user input until one of the two valid options is entered
    incorrect_input = True
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
        user_choice = get_user_input_int("Please enter an integer to select an option: ")

        # Check that the user's entered int is part of the avaliable options in the menu
        if validate_userinput_int(user_choice, 7):
            if user_choice == 1:
                show_item_info()
            elif user_choice == 2:
                show_all_items_info()
            elif user_choice == 3:
                add_new_item()
            elif user_choice == 4:
                update_item_info()
            elif user_choice == 5:
                remove_item()
            elif user_choice == 6:
                save_changes_and_exit("updated_A3_s3843790_stock.txt")
                continue_program = False
            elif user_choice == 7:
                continue_program = exit_without_saving()

        else:
            print("You did not enter a valid menu option! \n")

    # Let user know the program is ending
    print("Quitting program...")


# Run the program
main_menu()
