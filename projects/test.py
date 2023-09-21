import time
from datetime import datetime
order = []

from random import randint

def FoodDeliverySystem():

    def generate_order_id():

        return randint(1000, 9999)

    def place_order(customer_name, delivery_address, order_items):

        order_id = generate_order_id()
        if order_id in order:
            print(f"{order_id} order is already placed. Please wait")

        else:

            order_details = {

                "order_id": order_id,
                "customer_name": customer_name,
                "order_items": order_items.split(', '),
                "delivery_address": delivery_address,
                "status": "preparing"
            }

            order.append(order_details)
            print(f"{order_id} Order ID placed successfully")

    def track_delivery(order_id):

        for order_items in order:

            if order_items["order_id"] == order_id:

                print(f"Order ID : {order_items['order_id']}")
                print(f"Order Items: {', '.join(order_items['order_items'])}")
                print(f"Delivery Address  : {order_items['delivery_address']}")
                print(f"Status  : {order_items['status']}")
                print("_ " * 20)
                break
        else:

            print(f"Invalid  Order ID : {order_id}")


    def view_order_history(cutomer_name):

        print(f"Order history of the customer : {cutomer_name}")

        for order_details in order:

            if cutomer_name in order_details['customer_name']:

                print(f"Order ID : {order_details['order_id']}")
                print(f"Order Items: {', '.join(order_details['order_items'])}")
                print(f"Delivery Address  : {order_details['delivery_address']}")
                print(f"Status  : {order_details['status']}")
                print("_ " * 20)


    def update_order_status():
        count = 0
        statuses = ["In progress", "Delivery", "Delivered"]

        while count < len(statuses):

            for order_details in order:

                print(f"Order ID : {order_details['order_id']}")
                print(f"Order Items: {', '.join(order_details['order_items'])}")
                print(f"Delivery Address  : {order_details['delivery_address']}")
                print(f"Status  : {count + 1}")
                print(f"Status: {statuses[count]}")
                print("_ " * 20)

                count += 1
                time.sleep(10)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Time and Date of Delivery: {current_time}")
        print("All statuses displayed. Exiting the loop.")


    while True:

        print("\nMain Menu:")
        print("1. Place an Order")
        print("2. Track Delivery")
        print("3. Update Delivery Status")
        print("4. View Order History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':

            customer_name = input("Enter your name: ")
            order_items = input("Enter order items (comma-separated): ")
            delivery_address = input("Enter delivery address: ")
            place_order(customer_name, delivery_address, order_items)

        elif choice == "2":

            order_id = int(input("Enter your order ID: "))
            track_delivery(order_id)

        elif choice == "3":


            update_order_status()

        elif choice == '4':
            customer_name = input("Enter your name: ")
            view_order_history(customer_name)

        elif choice == '5':
            print("Exiting the Food Delivery Tracking System.")
            break
        else:
            print("Invalid choice. Please try again.")

FoodDeliverySystem()

















