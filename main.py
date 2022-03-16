# =========================== #
# Taine Reader                #
# 12DGT Python Assessment     #
# Freddy's Fast Fish Task     #
# Started 11.2.22             #
# =========================== #

# ========== SPECS ========== #
# 6x cheaper fish: $4.10
# Shark, Flounder, Cod, Gurnet, Mackerel, Tilapia
# 6x deluxe fish: $7.20
# Snapper, Pink Salmon, Tuna, Smoked Marlin, Prawns, Bass
# Frozen option, $1.05
# Delivery Fee, $5.00
# If delivery, needs: name, address & phone number.
# =========================== #

# Imports
import time
from xml.etree.ElementInclude import default_loader

# Declaring the order dict in a way I can refer back to later if I need to
order = {
    "items": [],
    "frozen": False,
    "delivery": False,
    # "name": "",
    # "address": "",
    # "phone": 0,
}

# menu = fish options (in list, containing prices for each individual one)
menu = {
    "Shark": 4.10,
    "Flounder": 4.10,
    "Cod": 4.10,
    "Gurnet": 4.10,
    "Mackerel": 4.10,
    "Tilipia": 4.10,
    "Snapper": 7.20,
    "Pink Salmon": 7.20,
    "Tuna": 7.20,
    "Smoked Marlin": 7.20,
    "Prawns": 7.20,
    "Bass": 7.20,
    "Chips (In Scoops)": 3.00
}

# editable variables
delivery_cost = 5.00
frozen_discount = 1.05
quantity_limit = 7
custom_item_limits = {  # Custom limits for certain items if required 
    "Chips (In Scoops)": 999
}
non_fish_items = ["Chips (In Scoops)"]  # These do not get affected by the frozen discount

# editable message variables
message_thanks = "Thank you for shopping at Freddies Fast Fish"
invalid_message_yn = "Invalid input, please enter a yes or no answer"
invalid_message = "Invalid input"
invalid_message_num = "Invalid input, please enter a valid number value"

# variables that shouldn't need changing
yes = ["y", "Y", "yes", "YES", "Yes", "True", "true", "1"]
no = ["n", "N", "No", "no", "NO", "false", "False", "0"]
spacer = "\n# ====================== #\n"
delivery = False
frozen = False


title = """
███████╗██████╗ ███████╗██████╗ ██████╗ ██╗███████╗███████╗    ███████╗ █████╗ ███████╗████████╗    ███████╗██╗███████╗██╗  ██╗
██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔════╝██╔════╝    ██╔════╝██╔══██╗██╔════╝╚══██╔══╝    ██╔════╝██║██╔════╝██║  ██║
█████╗  ██████╔╝█████╗  ██║  ██║██║  ██║██║█████╗  ███████╗    █████╗  ███████║███████╗   ██║       █████╗  ██║███████╗███████║
██╔══╝  ██╔══██╗██╔══╝  ██║  ██║██║  ██║██║██╔══╝  ╚════██║    ██╔══╝  ██╔══██║╚════██║   ██║       ██╔══╝  ██║╚════██║██╔══██║
██║     ██║  ██║███████╗██████╔╝██████╔╝██║███████╗███████║    ██║     ██║  ██║███████║   ██║       ██║     ██║███████║██║  ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═════╝ ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝"""
version = "1.0.0"


# ====================================================== FUNCTIONS ============================================================== #


# Main Menu Function
def main_menu():
    print("Welcome to Freddie's Fast Fish\nPlease choose an option:")
    print("1) Add item to order\n2) Edit items in order\n3) Finish order and pay\n4) Cancel order")

    while True:
        userinput = input("\nInput Number Selection: ")  # gets number selection for menu choice

        if userinput == "1":  # User selected to add item
            print(spacer)
            add_item()
            break
        elif userinput == "2":  # User selected to edit their order
            print(spacer)
            edit_order()
            break
        elif userinput == "3":  # User selected to finish order
            print(spacer)
            finish_order()
            break
        elif userinput == "4":  # User selected to cancel order
            print(spacer)
            print("Order cancelled, thank you for your time\n")
            time.sleep(5)
            quit()
        else:  # invalid input
            print(invalid_message_num)
            time.sleep(1)


# Edit Order
def edit_order():  # to remove items from order
    while True:
        if len(order["items"]) > 0:  # checks if order > 0
            i = 0
            for item in order["items"]:  # prints all the items
                i += 1
                formatted_item = str(i) + ") " + item[0]
                spaces = 25 - len(formatted_item)
                print(formatted_item + " " * spaces + "QTY: " + str(item[1]))

            userinput = input("\nRemove item? (Input nothing to return to menu)\nSelection: ")
            if userinput == "":  # if no input, return to menu without doing anything
                print(spacer)
                main_menu()  # back to menu
                return

            try:
                userinput = int(userinput)  # converts to int
            except:  # failed to convert to integer
                print(invalid_message_num)
                time.sleep(1)
                print(spacer)
                continue  # continue loop

            if len(order["items"]) >= userinput >= 1:  # if in the valid range of selections
                del[order["items"][userinput - 1]]  # removes item from selections
                print(spacer)
                continue  # restart loop
        else:
            main_menu()  # return to menu
            return


# Finish Order
def finish_order():
    if not order["items"]:  # if there are no items in the order, don't do anything
        print("There were no items on this order, cancelling order")
        time.sleep(5)
        exit()

    subtotal = 0
    total = 0
    total_fish_items = 0

    # Time to print receipt
    print("\n\n\n# =========== FINAL ORDER RECEIPT =========== #\n")

    print("Details:")  # printing details
    print("  Delivery: " + str(delivery))
    print("  Frozen: " + str(frozen))

    if delivery:
        print("  Name: " + name)
        print("  Address: " + address)
        print("  Phone: " + str(phone_number))

    print("\nItems:")
    for item in order["items"]:  # for each item in the order
        spaces = 25 - len(item[0])  # get correct spacing to look nice
        spaces2 = 8 - len(str(item[1]))  # ^^^
        subtotal = subtotal + menu[item[0]]*item[1]  # calculate cost

        if(item[0] not in non_fish_items):  # not a fish item, no need to subtract frozen discount
            total_fish_items = total_fish_items + item[1]  # total items to then subtract the frozen cost off

        print("  " + item[0] + " " * spaces + "QTY: " + str(item[1]) + " " * spaces2 + "Each: " + str("{:.2f}".format(menu[item[0]]))) #print the item, spaces, then the item quantity, spaces2 and then price each

    print("\nSubtotal: $" + str("{:.2f}".format(subtotal)))  # subtotal before delivery and frozen costs applied ({:.2f} is used for 2 decimal places)
    if delivery:  # if it's delivery add the delivery cost (default $5)
        subtotal = subtotal + delivery_cost
        print("Delivery cost: $" + str("{:.2f}".format(delivery_cost)))
    if frozen: #if frozen subtract the frozen discount * amount of items (by default discount is -$1.05 per item)
        subtotal = subtotal - frozen_discount * total_fish_items
        print("Frozen discount: $" + str("{:.2f}".format(frozen_discount * total_fish_items)))
    total = subtotal

    print("\nTotal: $" + str("{:.2f}".format(total))) #print total
    print(message_thanks) #print thank you message

    print("\n# =========== FINAL ORDER RECEIPT =========== #\n")

# Add Items Function
def add_item(): #add item to order
    while True:
        i = 0
        for item in menu:  # Prints all the items and costs
            i += 1
            formatted_item = str(i) + ") " + item #formats the item to be printed
            spaces = 25 - len(formatted_item) #calculates spaces amount for perfect order aesthetics
            print(formatted_item + " " * spaces + "$" + str("{:.2f}".format(menu[item]))) #prints the item + cost

        try:
            userinput = input("\nInput number selection (Input nothing to return to menu)\nSelection: ")
            if userinput == "": #if nothing, return to menu
                print(spacer)
                main_menu()
                return
            userinput = int(userinput)
        except:  # invalid input (could not convert to int)
            print(invalid_message_num)
            time.sleep(1)
            print(spacer)
            continue

        if len(menu) >= userinput >= 1:
            # Getting quantity
            quantity = 0  # This is here so my PyCharm doesn't yell at me

            i = 0
            for item in order["items"]: # goes through order to see if the item is already in the order, if it is it changes the item qty instead of adding another item of it (important for quantity limit)

                if item[0] == list(menu.keys())[userinput - 1]:
                    while True:

                        try:
                            quantity = int(input("How many " + list(menu.keys())[userinput - 1] + " items would you like?\nAdjust order quantity: ")) #asks for quantity
                        except: # was not a valid integer
                            print(invalid_message_num)
                            time.sleep(1)
                            continue #restarts qty loop

                        if list(menu.keys())[userinput - 1] in list(custom_item_limits.keys()):  # if it's in the custom item quantity variable set the custom item quantity
                            item_quantity_limit = custom_item_limits[list(menu.keys())[userinput - 1]]
                        else:
                            item_quantity_limit = quantity_limit

                        if item_quantity_limit >= quantity >= 1: #if it's within 1 - quantity_limit
                            order["items"][i] = item[0], quantity #sets the order to have item
                            print(spacer)
                            main_menu() #return to menu
                            return
                        else:
                            print(invalid_message_num + " from 1 - " + str(item_quantity_limit)) #out of range
                            time.sleep(1)
                            continue  # continue loop
                i += 1

            while True:  # getting quantity loop
                try:
                    quantity = int(input("How many " + list(menu.keys())[userinput - 1] + " items would you like?\nEnter number selection: ")) #asks for quantity
                except:  # was not a valid int
                    print(invalid_message_num)
                    time.sleep(1)
                    continue  # restart loop

                if list(menu.keys())[userinput - 1] in list(custom_item_limits.keys()):  # if it's in the custom item quantity variable set the custom item quantity
                    item_quantity_limit = custom_item_limits[list(menu.keys())[userinput - 1]]
                else:
                    item_quantity_limit = quantity_limit

                if item_quantity_limit >= quantity >= 1: # if within correct range
                    order["items"].append([list(menu.keys())[userinput - 1], quantity])  # add to order
                    print(spacer)
                    main_menu()  # return to menu
                    return

                else:
                    print(invalid_message_num + " from 1 - " + str(item_quantity_limit))  # was invalid :(
                    time.sleep(1)
                    continue  # continue loop

        else:  # was out of menu range
            print(invalid_message_num)
            time.sleep(1)
            print(spacer)
            continue  # continue loop

def get_user_details():
    # Get customer's name
    while True:  # Loop until user enters a valid name (eg. not nothing)
        name = input("Please enter your name: ").title()
        if name == "":
            # Nothing entered message
            print("Please enter a name!")
            time.sleep(1)
        else:
            if input("Is this correct: " + name + " [Y/N]: ") in yes:
                # Exit out of loop as a valid name has been reached
                break

    print(spacer)

    # Get customer's address
    while True:  # Loop until user enters a valid address (eg. not nothing)
        address = input("Please enter your address: ").title()
        if address == "":
            # Nothing entered message
            print("Please enter an address!")
            time.sleep(1)
        else:
            if input("Is this correct: " + address + " [Y/N]: ") in yes:
                # Exit out of loop as a valid address has been reached
                break

    print(spacer)

    # Get customer's phone number
    while True:  # Loop until user enters a valid phone number (eg. a number with no letters)
        phone_number = input("Please enter your phone number (No spaces or plus, just numbers): ")
        try:
            phone_number = int(phone_number)
            if input("Is this correct: " + str(phone_number) + " [Y/N]: ") in yes:
                # Exit out of loop since correct number has been reached
                break
        except:
            print(invalid_message_num)
            time.sleep(1)

    return name, address, phone_number #return variables


# ====================================================== END OF FUNCTIONS ============================================================== #


# Starting Order
print(title)
print("      Version: " + version + "            By Taine Reader\n")

print(spacer)

# Checking if order is to be delivered or picked up
while True:  # While true is used for continuosly getting input until a valid input is reached (eg. yes or no)
    userinput = input("Is the order delivery? (Delivery orders have a $" + str("{:.2f}".format(delivery_cost)) + " delivery fee)\nDelivery? [Y/N]: ")
    if userinput in yes: #if the answer is yes, enable delivery
        delivery = True
        break
    elif userinput in no: #disable delivery
        delivery = False
        break
    else:
        print(invalid_message_yn) #invalid message
        time.sleep(1)
        print(spacer)

print(spacer)

# Checking if order is to be prepared frozen or fresh
while True:  # While true is used for continuosly getting input until a valid input is reached (eg. yes or no)
    userinput = input("Is the order frozen? (Frozen orders get a discount of $" + str("{:.2f}".format(frozen_discount)) + " per item)\nFrozen? [Y/N]: ")
    if userinput in yes: #is frozen
        frozen = True
        break
    elif userinput in no: #isn't frozen
        frozen = False
        break
    else:
        print(invalid_message_yn) #invalid input
        time.sleep(1)

print(spacer)

if delivery: #for delivery items, need delivery details
    name, address, phone_number = get_user_details()
    order["name"] = name
    order["address"] = address
    order["phone_number"] = phone_number
    print(spacer)

order["delivery"] = delivery #setting details in the order var
order["frozen"] = frozen

main_menu()
