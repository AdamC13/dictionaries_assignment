
#1 Real-World Python Dictionary Applications
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
restaurant_menu["Beverages"] = ["Celsius", "Water"]
restaurant_menu["Main Course"].update({"Steak" : 17.99})
restaurant_menu["Starters"].pop("Bruschetta")
print(restaurant_menu)



#2 Advanced Data Handling with Python
# Hotel Room Booking Tracker

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "available", "customer": ""},
    "103": {"status": "booked", "customer": "John Doe"},
    "104": {"status": "available", "customer": ""},
    "105": {"status": "booked", "customer": "John Doe"},
    "106": {"status": "available", "customer": ""},
    "107": {"status": "booked", "customer": "John Doe"}
}

def book(customer):
    print("\n")
    for room in hotel_rooms.items():
        print(f"Room {room[0]} is {room[1]["status"]}")
    b_room = input("\nWhat room would you like to book? ")
    if hotel_rooms[b_room]["status"] == "booked":
        input("\nThat room is already booked")
        return
    elif hotel_rooms[b_room]["status"] == "available":
        hotel_rooms[b_room]["status"] = "booked"
        hotel_rooms[b_room].update({"customer": customer})
        input("\nYou booked the room!")
    else:
        input("error")

        return

def checkout():
    print("\n")
    for room in hotel_rooms.items():
        print(f"Room {room[0]} is {room[1]["status"]}")
    room = input("\nWhich room will you be checking out of? ")
    if hotel_rooms[room]["status"] == "available":
        input("\nThat room was already checked out!")
        return

    elif hotel_rooms[room]["status"] == "booked":
        hotel_rooms[room].update({"status": "available"})
        hotel_rooms[room].update({"customer": ""})
        input("\nYou have successfully checked out!")
        return
    else:
        input("error")
        return

def display_rooms():
    print("\n")
    for room in hotel_rooms.items():
        print(f"Room {room[0]} is {room[1]["status"]}")
    input("\nPress enter when ready")


def cli():
    while True:
        user_input = input('''
    Welcome! What would you like to do?
                        
    1: Book a room
    2: Checkout
    3: View room availability   
    4: Quit                                          

    ''')

        if user_input == "1":
            name = input("\nWho will be booking a room today? ")
            book(name)
        elif user_input == "2":
            checkout()
        elif user_input == "3":
            display_rooms()
        elif user_input == "4":
            break
        else:
            print("Error")


#cli()


# E-commerce Product Search Feature

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}
def search():
    products_found = []
    user_input = input("What are you interested in buying? ")
    for product in products.keys():
        if products[product]["name"].casefold() == user_input.casefold():
            products_found.append(product)
    if products_found == []:
        return False
    else:
        return products_found
print(search())


#3 Customer Service Ticket Tracker
service_tickets = {
    "1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def new_ticket(customer, issue):
    key_list = []
    for key in service_tickets.keys():
        key_list.append(int(key))
    service_tickets[str(max(key_list) + 1)] = {"Customer": customer, "Issue": issue, "Status": "open"}

new_ticket("Adam", "Python")
print(service_tickets)


def update_status(ticket_number, new_status):
    service_tickets[ticket_number]["Status"] = new_status




def display_tickets():
    for ticket_number in service_tickets.items():
        print(f'Ticket number {ticket_number[0]}, with the issue "{ticket_number[1]["Issue"]}", Filed by {ticket_number[1]["Customer"]}, is {ticket_number[1]["Status"]}')


update_status("3", "almost done with the assignment")
display_tickets()

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

import copy
copy_of_weekly_sales = copy.deepcopy(weekly_sales)
copy_of_weekly_sales["Week 2"]["Electronics"] = 18000
print(copy_of_weekly_sales)
print(weekly_sales)