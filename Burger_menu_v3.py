"""
Program to store combo meals for a takeway business
11-4-26
Version 3: Include function to search for combo and give the option to edit combo
"""

import easygui


# burger menu nested dictionary v1
burger_menu = {
    "Value" : {
        "Main" : "Beef Burger",
        "Side" : "Fries",
        "Drink" : "Fizzy Drink"
    },
    "Cheezy" : {
        "Main" : "Cheeseburger",
        "Side" : "Fries",
        "Drink" : "Fizzy Drink"
    },
    "Super" : {
        "Main" : "Cheeseburger",
        "Side" : "Large Fries",
        "Drink" : "Smoothie"
    }
}

# nested values for prices v1

prices = {       # added some more items to encourage variety in version 2 and onwards, as well as numbered items
    "01. Beef Burger" : 5.50,
    "02. Chicken Burger" : 6.00,
    "03. Fish Fillet Burger" : 6.00,
    "04. Cheeseburger" : 6.50,
    "05. Double Cheeseburger" : 8.00,
    "06. Fries" : 1.00,
    "07. Large Fries" : 2.00,
    "08. Chicken Nuggets" : 2.00,
    "09. Onion Rings" : 1.50,
    "10. Fizzy Drink" : 1.00,
    "11. Orange Juice" : 1.50,
    "12. Smoothie" : 2.00,
    "13. Milkshake" : 2.00
}

# functions for all user options v1

def add_combo():   # add combo function, v2
    new_combo_name = easygui.enterbox("Please input the name of the new combo." \
    "\nNote: All combos must have one main, one side, and one drink.", "New combo name").title()
    if not new_combo_name:
        easygui.msgbox("Combo name is required.")
        return
        # check to see if combo is already in the menu
    if new_combo_name in burger_menu: 
        easygui.msgbox("That combo is already included in the menu.", "Error")
        return
    
    # get the items (using choicebox to ensure we have prices for them)
    available_items = list(prices.keys()) 

    main = easygui.choicebox(f"Select the Main for the {new_combo_name} combo:", "Select Main", choices = available_items)
    if not main: # if user hit cancel
        return
    side = easygui.choicebox(f"Select the Side for the {new_combo_name} combo:", "Select Side", choices = available_items)
    if not side:
        return
    drink = easygui.choicebox(f"Select the Drink for the {new_combo_name} combo:", "Select Drink", choices = available_items)
    if not drink: 
        return

    # add to menu dictionary
    burger_menu[new_combo_name] = {
            "Main" : main,
            "Side" : side,
            "Drink" : drink
            }
    easygui.msgbox(f"Combo '{new_combo_name}' has been added to the menu!", "Success")

def search_edit_menu():  # search menu function v3
    searched_combo = easygui.enterbox("Enter the name of the combo you want to check/change:").title().strip()
    
    if not searched_combo:
        return

    # ensure combo exists
    if searched_combo in burger_menu:

        # show details
        details = burger_menu[searched_combo]
        current_info = f"Combo: {searched_combo}\n"
        current_info += f"Main: {details['Main']}\n"
        current_info += f"Side: {details['Side']}\n"
        current_info += f"Drink: {details['Drink']}\n\n"
        current_info += "Do you want to make changes to this combo?"

        # ask user if changes are required
        choice = easygui.buttonbox(current_info, "Verify Details", choices=["Edit", "Keep as is"])

        
def delete_combo():
    pass

def print_menu():
    pass

# main routine v1

easygui.msgbox("Welcome to the burger menu!", "Welcome message")
while True:
    option = easygui.buttonbox("What would you like to do?\nPlease select from the options below.", "Options",
                            choices = ["Add combo", "Delete combo", "Search menu", "Print menu", "Exit program"])

    if option == "Add combo":
        add_combo()
        
    elif option == "Delete combo":
        delete_combo()

    elif option == "Search menu":
        search_edit_menu()

    elif option == "Print menu":
        print_menu()

    else:
        break

easygui.msgbox("Thank you for using this program. Goodbye!", "Program exit")





        


