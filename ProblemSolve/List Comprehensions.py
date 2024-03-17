# num = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x*x, num))
# print(result)


# [expression for item in list]

nums = [1, 2, 3, 4, 5, 6, 7]
result = [x * x for x in nums]
print(result)

result = [x for x in nums if x % 2 == 0]
print(result)
