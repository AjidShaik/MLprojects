# # # # #Nested loop
# # # # for i in range(3):
# # # #     for j in range(2):
# # # #         print(f"i={i}, j={j}")

# # # #rightangle triangle of stars
# # # row = 5
# # # for i in range(1, row + 1):
# # #     for j in range(i):
# # #         print("*", end="")
# # #     print()

# # #Number triangle 
# # rows = 5
# # for i in range(1, rows + 1):
# #     for j in range(1, i + 1):
# #         print(j, end="")
# #     print()

# #Inverted star triangle

# rows = 5 
# for i in range(rows, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()

#Pyramid pattern
row = 5 
for i in range(1, row + 1):
    for j in range(row - i):
        print(" ", end="")
    for k in range (2 * i - 1):
        print("*",end="")
    print()