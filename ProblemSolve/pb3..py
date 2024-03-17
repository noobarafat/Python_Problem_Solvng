# take a list
# if value is divisable by 5 print in
# if greater then 500 skip and if greater then 600 stop loop

def process_list(numbers):
    for num in numbers:
        if num % 5 == 0:
            print(num, "is diviable by 5")
        if num > 600:
            print("Stopping loop as number is greater than 600")
            break
        elif num > 500:
            print("Skipping", num, "as it is greater than 500")
            continue

my_list = [100, 45, 67, 43, 21, 37, 89, 450, 510,  666, 457, 333, 234]
process_list(my_list)