# find out minimum and maximum using if else

x = int(input("Enter first NUmber: "))
y = int(input("Enter second NUmber: "))
z = int(input("Enter third NUmber: "))

if x > y and x > z:
    max = x
elif y > x and y > z:
    max = y
else:
    max = z

if x < y and x < z:
    min = x
elif y < x and y < z:
    min = y
else:
    min = z

print("maximum", max)
print("Minimum", min)

