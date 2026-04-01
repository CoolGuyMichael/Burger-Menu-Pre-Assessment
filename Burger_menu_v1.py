"""
Program to store combo meals for a takeway business
26-3-26
Version 1: Set up main program and while loop
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

prices = {
    "Beef Burger": 5.69,
    "Cheeseburger": 6.69,
    "Fries": 1.00,
    "Large Fries": 2.00,
    "Fizzy Drink": 1.00,
    "Smoothie": 2.00
}

# functions for all user options v1

def add_combo():
    pass

def delete_combo():
    pass

def search_menu():
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
        search_menu()

    elif option == "Print menu":
        print_menu()

    else:
        break

easygui.msgbox("Thank you for using this program. Goodbye!", "Program exit")





        


