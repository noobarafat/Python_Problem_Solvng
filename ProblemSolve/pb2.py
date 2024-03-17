# print total sum until 10
# print odd sum and even sum until 10
# print even number using range increment

totalSum = 0
oddSum = 0
evenSum = 0

for i in range(1, 11):
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
    totalSum += i

print("Total sum",totalSum)
print("Total even number sum", evenSum)
print("Total odd number sum", oddSum)

for i in range(1, 10, 2):
    print(i)
