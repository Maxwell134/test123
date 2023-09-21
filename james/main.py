input_file = "dob.txt"

with open(input_file, mode="r") as file:
    lines = file.readlines()

# Finding the index of "Name" and "Date" in the header
header = lines[0].strip().split(", ")
name_index = header.index("Name")
date_index = header.index("Date")

# Extracting the rows under "Name" and "Date"
name_rows = []
date_rows = []
for line in lines[1:]:
    values = line.strip().split(", ")
    print(values)
    name_rows.append(values[name_index])
    date_rows.append(values[date_index])

# Printing the extracted rows
#print("Name Rows:")
with open("name.txt", mode='w') as r:
    for name in name_rows:
        r.write(name + "\n")


#print("Date Rows:")
with open("date.txt", mode='w') as d:
    for date in date_rows:
        d.write(date + "\n")


