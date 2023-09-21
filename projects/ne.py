from random import randint

class InventoryManagement:

    def __init__(self):

        self.inventory = {}


    def add_product(self):

        product_id = int(input("Enter the product ID: "))
        product_name = input("Enter the product name: ")
        quantity = int(input("Enter the quantity:"))
        price = float(input("Enter the price: "))

        if product_id in self.inventory:

            print(f"{product_id} already exist in Inventory")

        else:

            self.inventory[product_id] = {

                "product_id": product_id,
                "product_name": product_name,
                "quantity": quantity,
                "price": price

            }

            print(f"{product_id} added successfully")

    def view_product(self):

        print(self.inventory)

        product_id = input("Enter the product ID to view: ")

        # Convert product_id to an integer
        product_id = int(product_id)

        if product_id in self.inventory:
            product = self.inventory[product_id]
            print("\nProduct Details:")
            print(f"Product ID: {product_id}")
            print(f"Name: {product['product_name']}")
            print(f"Quantity: {product['quantity']} Kg")
            print(f"Price: {product['price']} Rupees")
        else:
            print(f"Product ID {product_id} does not exist.")


inventory = InventoryManagement()

while True:
        print("\nMenu:")
        print("1. Display product")
        print("2. add a product")
        print("3. Stop")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.view_product()

        elif choice == "2":
            inventory.add_product()

        elif choice == "3":
            break

        else:

            print(f"Invalid choice")












