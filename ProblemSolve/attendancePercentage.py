# calculate attendance percentage

totalClass = int(input("Enter the total classes: "))
absenceClass = int(input("Enter the absent classes: "))

presentClasses = totalClass - absenceClass
totalPresentClasses = presentClasses / totalClass
attendancePercentage = totalPresentClasses * 100

print("Attendance Percentage: ", attendancePercentage)

if (attendancePercentage >= 75):
    print("Your attendance is up to 75%")
else:
    print("Your attendance is less than 74%")
