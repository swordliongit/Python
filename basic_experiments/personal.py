
import os

last_date_list = []
amount_list = []
temp_list = []
_dict = {}
total = 0

# Create the file
file = open("total amount.txt", "w")
file.close()

# Check if the file is empty or not, if empty, write a placeholder format
if os.stat("total amount.txt").st_size == 0:
    with open("total amount.txt", "w") as file:
        file.write("0-0-0 0")

while True:
    var = int(input("Choose your option,\n" 
                "1 : Adder\n"
                "2 : Remove last\n"
                "3 : Show: "))

    match var:

        case 1:
            amount_list.clear() # Clear buffers
            temp_list.clear()
            _dict.clear()
            while True:
                num = input("Enter date and num, exit to return main menu: ")
                if num == "exit":
                    break
                temp_list = num.split(" ")
                _dict[temp_list[0]] = temp_list[1]

                amount_list.append(int(temp_list[1]))
                last_date_list.append(temp_list[0])

            temp_total = 0

            with open("total amount.txt") as file:
                temp_total = int(file.read().split(" ")[1])

            with open("total amount.txt", "w") as file:
                file.write(f"{last_date_list[-1]} {str(sum(amount_list) + temp_total)}")

        case 2:
            temp_removed = 0
            with open("total amount.txt") as file:
                temp_removed = int(file.read().split(" ")[1]) - int(temp_list[1])
                last_date_list.pop()

            with open("total amount.txt", "w") as file:
                file.write(f"{last_date_list[-1]} {str(temp_removed)}")

        case 3:
            with open("total amount.txt") as file:
                print(file.read())
        


