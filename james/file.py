
# f = open("dob.txt", 'r')
# data = f.read()
# count = 0
# for i in data:
#     if i == 'o':
#         count += 1
# print(count)
# print(data)
# f.close()

# f = open("dob.txt", "r")
# lines = f.readlines()
# for line in lines[::-1]:
#     print(line.strip())
# f.close()

# with open("dob.txt", "r") as lines:
#     data = lines.readlines()
#     for line in lines[::-1]:
#         print(line.strip())
# lines.close()

f = open("test.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.strip()
    words = line.split()
    print(words)
    words = words[::-1]
    print(words)
    # print(" ".join(w for w in words))
    for w in words:
        print(w, end=" ")
    print()
f.close()