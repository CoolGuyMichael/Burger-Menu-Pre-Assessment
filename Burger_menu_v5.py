"""
Program to store combo meals for a takeway business
21-4-26
Version 5: Include function to print the entire burger menu
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
    "Beef Burger" : 5.50,
    "Chicken Burger" : 6.00,
    "Fish Fillet Burger" : 6.00,
    "Cheeseburger" : 6.50,
    "Double Cheeseburger" : 8.00,
    "Fries" : 1.00,
    "Large Fries" : 2.00,
    "Chicken Nuggets" : 2.00,
    "Onion Rings" : 1.50,
    "Fizzy Drink" : 1.00,
    "Orange Juice" : 1.50,
    "Smoothie" : 2.00,
    "Milkshake" : 2.00
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

        if choice == "Edit":
            available_items = list(prices.keys())
            # allow user to select new items
            main = easygui.buttonbox("Select New Main:", choices=available_items)
            if not main: return
            
            side = easygui.buttonbox("Select New Side:", choices=available_items)
            if not side: return
            
            drink = easygui.buttonbox("Select New Drink:", choices=available_items)
            if not drink: return

            # update dictionary
            burger_menu[searched_combo] = {"Main": main, "Side": side, "Drink": drink}
            easygui.msgbox(f"Combo '{searched_combo}' has been successfully updated!", "Success")
    else:
        easygui.msgbox(f"Sorry, '{searched_combo}' was not found on the menu.", "Not Found")

        
def delete_combo():  # delete combo function v4
    # get list of all combos
    combo_list = list(burger_menu.keys())
    
    # allow user to select which combo to delete
    combo_to_delete = easygui.choicebox("Select the combo you wish to REMOVE:", "Delete Combo", 
                                        choices = combo_list)
    
    # confirmation message
    if combo_to_delete:
        # 4. Double check they really want to do it
        confirm = easygui.buttonbox(f"Are you sure you want to delete '{combo_to_delete}'?\nThis cannot be undone.", 
                                    "Confirm Delete", 
                                    choices = ["Yes, Delete", "No, Cancel"])
        
        if confirm == "Yes, Delete":
            # removes the combo
            del burger_menu[combo_to_delete]
            easygui.msgbox(f"'{combo_to_delete}' has been removed from the menu.")
        else:
            easygui.msgbox("Delete cancelled.")

def print_menu(): # function to print the whole menu v5
    # add empty string to hold menu items
    menu_output = "--- CURRENT BURGER MENU ---\n\n"
    
    # loop through each combo in menu dictionary
    for combo, details in burger_menu.items():
        menu_output += f"COMBO: {combo.upper()}\n"
        
        total_price = 0
        
        # loop through each combo item (main, side, drink)
        for category, item in details.items():
            # Get the price from the prices dictionary
            # .get(item, 0) returns 0 if the item name isn't found
            price = prices.get(item, 0)
            total_price += price
            
            menu_output += f"  - {category}: {item} (${price:.2f})\n"
        
        # Add the total price for the whole combo
        menu_output += f"TOTAL COMBO PRICE: ${total_price:.2f}\n"
        menu_output += "-" * 30 + "\n"
    
    # display entire menu
    easygui.textbox("Here is the full burger menu:", "Burger Menu", menu_output)

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





        


