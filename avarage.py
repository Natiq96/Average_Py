# codewithmn
def average(count):
    my_list = []
    total = 0
    count_number = count
    while count > 0:
        print(f"You can enter {count} numbers !")
        numbers = int(input("Enter the number !"))
        my_list += [numbers]
        count -= 1
    for number in my_list:
        total += number
    average_number = total / count_number
    print(f"Average ; {int(average_number)}")
count = int(input("How many number do you want to enter?"))
if count > 1:
    average(count)
else:
    print("Please include the correct number!")