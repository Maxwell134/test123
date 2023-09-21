import time
from datetime import datetime
statuses = ["In progress", "Delivery", "Delivered"]

count = 0
for status in statuses:
    count += 1

    if status == "Delivered":

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(status)
        print(count)
        print(f"Time and Date of Delivery: {current_time}")
        time.sleep(1)
    else:

        print(status)
        print(count)
        time.sleep(5)




