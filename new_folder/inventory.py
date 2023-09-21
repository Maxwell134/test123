# Create an empty inventory dictionary to store product details
inventory = {}


def add_product():
    product_id = input("Enter the product ID: ")
    product_name = input("Enter the product name: ")
    quantity = int(input("Enter the quantity: "))

    # Check if the product ID already exists in the inventory
    if product_id in inventory:
        print("Product ID already exists. Use the 'Update' option to modify the product.")
    else:
        inventory[product_id] = {"Product Name": product_name, "Quantity": quantity}
        print("Product added to the inventory.")


def update_product():
    product_id = input("Enter the product ID to update: ")

    # Check if the product ID exists in the inventory
    if product_id in inventory:
        new_product_name = input("Enter the new product name (press Enter to keep the existing name): ")
        new_quantity = input("Enter the new quantity (press Enter to keep the existing quantity): ")

        if new_product_name:
            inventory[product_id]["Product Name"] = new_product_name
        if new_quantity:
            inventory[product_id]["Quantity"] = int(new_quantity)

        print("Product updated successfully.")
    else:
        print("Product ID not found.")


def delete_product():
    product_id = input("Enter the product ID to delete: ")

    # Check if the product ID exists in the inventory
    if product_id in inventory:
        del inventory[product_id]
        print("Product deleted from the inventory.")
    else:
        print("Product ID not found.")


def view_product():
    product_id = input("Enter the product ID to view: ")

    # Check if the product ID exists in the inventory
    if product_id in inventory:
        product = inventory[product_id]
        print("\nProduct Details:")
        print(f"Product ID: {product_id}")
        print(f"Product Name: {product['Product Name']}")
        print(f"Quantity: {product['Quantity']}")
    else:
        print("Product ID not found.")


# Main loop for the inventory management system
while True:
    print("\nInventory Management Menu:")
    print("1. Add a product")
    print("2. Update a product")
    print("3. Delete a product")
    print("4. View a product")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_product()
    elif choice == "3":
        delete_product()
    elif choice == "4":
        view_product()
    elif choice == "5":
        print("Exiting the Inventory Management System.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
