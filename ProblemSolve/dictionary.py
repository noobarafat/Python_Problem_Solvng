# dictionary = a collection of {key:value} pairs
#            ordered and changeable. No duplicates


capitals = {
    "USA": "Washington D.C",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

print(capitals.get(("USA")))
# print(capitals.get(("India")))
# print(capitals.get(("japan")))

# if capitals.get("japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exists")

capitals.update({
    "Germany": "Berlin",
    "USA": "Detroit"
})

# print(capitals)

# capitals.pop("China")
# print(capitals)

# capitals.popitem()
# print(capitals)

# capitals.clear()
# print(capitals)

# keys = capitals.keys()
# # print(keys)
# for key in capitals.keys():
#     print(key)
#
# values = capitals.values()
# # print(values)
# for value in capitals.values():
#     print(value)


items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
