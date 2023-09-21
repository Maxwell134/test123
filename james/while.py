"""

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *


for i in range(1,6):
    for j in range(6,i, -1):
        print(" ", end=" ")
    for k in range(1, i*2):
        print("*", end=" ")

    print()
"""
""""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""
"""
for i in range(1,6):
    for j in range(6,i, -1):
        print(" ", end=" ")
    for k in range(1, i*2):
        print("*", end=" ")

    print()

for i in range(1, 6):
    for j in range(1, i+1):
        print(" ", end=" ")
    for k in range(11, i*2, -1):
        print("*", end=" ")
    print()
"""
"""
* * * * *
*       *
*       *
*       *
* * * * *

    

"""
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or i == 5 or j == 1 or j == 5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

for i in range(0, 3):
    num = int(input("Enter the numbers: "))


