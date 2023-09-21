menu = [
            {"item": "Burger", "price": 5.00 },
            {"item": "Pizza", "price": 10.00 },
            {"item": "Salad", "price": 7.00 }
        ]

carts = []

def add_item(menu : list):

    choice = input("Enter your items: ")
    quantity = int(input("Enter the quantity: "))

    found = False
    for items in menu:
        if choice.lower() == items['item'].lower():

            found = True
            items_in_cart = {
                "Item": items['item'],
                "Price": items['price'],
                "Quantity": quantity
            }

            carts.append(items_in_cart)
            print(f"{choice} added to the cart")

    if not found:
        print(f"{choice} not available")


    print(carts)

def view_item():

    print("Your Cart: ")
    for items in carts:

        print(f" Items: {items['Item']}")
        print(f" Price: {items['Price']}")
        print(f" Quantity: {items['Quantity']}")


def run():

    while True:

        print("\n1. Add Item to Cart")
        print("2. View Items")
        print("3. Show Cart")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(menu)

        elif choice == '2':
            view_item()

        elif choice == '4':
            print("Bye !")
            break
        else:
            print("Invalid choice. Please try again.")

run()





