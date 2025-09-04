#Python Bacnking Program



def show_balance(balance):
    if balance < 0:
        print("00.00")
    else:
       print("****************************")
       print(f"Your balance: {balance:.2f}")
       print("****************************")

def deposite():
    print("****************************")
    amount= float(input("ENter the amount to be deposited: "))
    print("****************************")
    print("****************************")
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    print("****************************")
    amount = float(input("Enter amount to be withdraw: "))
    print("****************************")
    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount <0:
        print("Amount must be > 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True


    while is_running:
        print("****************************")
        print("         Banking Program     ")
        print()
        print("****************************")
        print("1. Show Balance ")
        print("2. Deposit ")
        print("3. Withdraw ")
        print("4. Exit ")

        print("****************************")
        print("****************************")

        choice = input("Enter your choice (1-4): ")
        
        print("****************************")

        if choice == '1':
            show_balance(balance)
        elif choice =='2':
            balance += deposite()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid Case")

    print("Have a nice day!!")

if __name__ == '__main__':
    main()
