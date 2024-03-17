# # fruits = ["Apple", "Orange", "banana"' "Cocunut']
# # vegetables = ["ladies finger", "carrots", "potatoes"]
# # meats = ["chicken", "beaf", "mutton"]
# #
# # groceries = [fruits, vegetables, meats]
# #
# # print(groceries[2][1])
#
# groceries = [
#     ["Apple", "Orange", "banana" "Cocunut"],
#     ["ladies finger", "carrots", "potatoes"],
#     ["chicken", "beaf", "mutton"]
# ]
#
# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()
#
#
# print()
# print()
# print()
#
# groceries = (
#     ("Apple", "Orange", "banana" "Cocunut"),
#     ("ladies finger", "carrots", "potatoes"),
#     ("chicken", "beaf", "mutton")
# )
#
# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()
#
#
#
#


num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()