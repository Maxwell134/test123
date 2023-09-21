from random import randint

class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self):

        product_id = input("Enter the product ID: ")
        name = input("Enter the name of the product: ")
        quantity = float(input("Enter the quantity: "))
        price = float(input("Enter the price: "))


        if product_id in self.inventory:
            print(f"Product ID {product_id} already exists.")
        else:
            self.inventory[product_id] = {
                "name": name,
                "quantity": quantity,
                "price": price
            }
            print(f"Product ID {product_id} added successfully.")

    def update_product(self):
        product_id = input("Enter the product ID to update: ")
        if product_id in self.inventory:
            name = input("Enter the new name of the product: ")
            quantity = float(input("Enter the new quantity: "))
            price = float(input("Enter the new price: "))

            self.inventory[product_id] = {
                "name": name,
                "quantity": quantity,
                "price": price
            }
            print(f"Product ID {product_id} updated successfully.")
        else:
            print(f"Product ID {product_id} does not exist.")

    def delete_product(self):
        product_id = input("Enter the product ID to delete: ")
        if product_id in self.inventory:
            del self.inventory[product_id]
            print(f"Product ID {product_id} deleted successfully.")
        else:
            print(f"Product ID {product_id} does not exist.")

    def view_product(self):
        product_id = input("Enter the product ID to view: ")
        if product_id in self.inventory:
            product = self.inventory[product_id]
            print("\nProduct Details:")
            print(f"Product ID: {product_id}")
            print(f"Name: {product['name']}")
            print(f"Quantity: {product['quantity']} Kg")
            print(f"Price: {product['price']} Rupees")
        else:
            print(f"Product ID {product_id} does not exist.")

inventory = Inventory()

while True:
    print("\nInventory Management Menu:")
    print("1. Add a product")
    print("2. Update a product")
    print("3. View a product")
    print("4. Delete a product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.add_product()
    elif choice == "2":
        inventory.update_product()
    elif choice == "3":
        inventory.view_product()
    elif choice == "4":
        inventory.delete_product()
    elif choice == "5":
        print("Thank you for visiting us.")
        break
    else:
        print("Invalid choice.")
