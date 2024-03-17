# count equal numbers :
# if all three inputs are equal print Equilatoral
# if two inputs are equal print Isoslus
# otherwise Sclane
def equilatoral(a, b, c):
    if a == b and a == c and b == c:
        print("Equilatoral")
    elif a == b and a == c or b == c:
        print("Isoslus")
    elif a == c and b == c or a == b:
        print("Isoslus")
    elif a == b and b == c or a == c:
        print("Isoslus")
    else:
        print("Sclane")

x = int(input("Enter a:"))
y = int(input("Enter b:"))
z = int(input("Enter c:"))

equilatoral(x, y, z)