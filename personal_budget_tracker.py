import time
import csv
import matplotlib.pyplot as plt


# check whether the user's transaction input is valid or not
def validate_input():
    while True:
        val = input("Please Enter your input your amount:\n")
        
        try:
            num = float(val)
            return num
        except:
            val = input("Invalid input. Please enter a number:\n")

# returns the last balance user had before the current transaction
def last_balance():
    with open('database.csv','r') as read_file:
        data = list(csv.reader(read_file))
        if len(data) == 1:
            return 0
        return data[-1][-1]



# calculate the new balance and store in the csv file
def calculate_new_balance(transaction_type,prev_balance,val):

    with open('database.csv','a') as written_file:

        # format time into dd-mm-yy format
        current_time = time.time()
        time_struct = time.gmtime(current_time)
        formatted_date = time.strftime("%d-%m-%y", time_struct)
        new_balance = float(prev_balance) + val
        last_line = [formatted_date, transaction_type, str(val), str(new_balance)]
        written_file.write("\n"+",".join(last_line))


def handle_data_visualization(data):
    total_spent = [0]*4
    for line in data:
        if line[1] == "Grocery":
            total_spent[0] +=float(line[2])
        elif line[1] == "Rent":
            total_spent[1] +=float(line[2])
        elif line[1] == "Transportation":
            total_spent[2] +=float(line[2])
        elif line[1] == "Entertainment":
            total_spent[3] +=float(line[2])

        print(" ".join(line))
    return total_spent


# display the final report
def show_report():
    with open('database.csv', 'r') as read_file:
        data = list(csv.reader(read_file))
        total_spent = handle_data_visualization(data)
        total_spent = [-1*val for val in total_spent]
        my_labels = ["Grocery", "Rent", "Transportation", "Entertainment"]
        plt.pie(total_spent, labels = my_labels)
        plt.show()

    

def show_menu():
    print("1. Grocery")
    print("2. Rent")
    print("3. Transportation")
    print("4. Entertainment")
    print("5. Deposit")

def type_of_transaction():
    print("Please choose the type of transaction you want to record!")
    show_menu()

    while True:
        try:
            key = input()
            print(key)
            if key in map(str,range(1,6)):
                choice = int(key)
                break
            else:
                print("Invalid choice. Please press 1, 2, 3, 4, 5.")
        except Exception as e:
            print(f"Error: {e}")
    
    if choice == 1:
        return "Grocery"
    elif choice == 2:
        return "Rent"
    elif choice == 3:
        return "Transportation"    
    elif choice == 4:   
        return "Entertainment" 
    elif choice == 5:
        return "Deposit"



if __name__ == "__main__":
    print("Hello👋, wellcome to your very own expenses tracker")
    transaction_type = type_of_transaction()

    val = validate_input()
    prev_balance = last_balance()
    calculate_new_balance(transaction_type,prev_balance,val)
    
    show_report()

