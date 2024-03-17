# enter a person basic salary and service year then print bonus for
# if service is 10 year or upper 10%
# if service is 5 to less then 10 8%
# else 5% bonus

def calculateBonus(basicSalary, yearsOfService):
    if yearsOfService >= 10:
        bonus_percentage = 0.10
    elif yearsOfService >= 5:
        bonus_percentage = 0.08
    else:
        bonus_percentage = 0.05
    bonus = basicSalary * bonus_percentage
    return bonus



x = float(input("Enter basic salary: "))
y = int(input("Enter service of the year: "))

result = calculateBonus(x, y)
print("Bonus", result)

