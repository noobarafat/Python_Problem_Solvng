# input four peoples age and print the youngest oldest man age
age=[]
a = int(input("Age of 1st person: "))
age.append(a)
b = int(input("Age of 2nd person: "))
age.append(b)
c = int(input("Age of 3rd person: "))
age.append(c)
d = int(input("Age of 4th person: "))
age.append(d)
print(age)

print("The youngest man age is", min(age))
print("The oldest man age is", max(age))



