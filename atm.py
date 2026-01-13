from bank import Bank

def run_atm():
    acc_num = int(input("Enter Account Number: "))
    balance = int(input("Enter Starting Balance: "))

    account = Bank(acc_num, balance)

    while True:
        print("\n--- ATM MENU ---")
        print("1. Debit")
        print("2. Credit")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            amt = int(input("Enter debit amount: "))
            print(account.debit(amt))

        elif choice == 2:
            amt = int(input("Enter credit amount: "))
            print(account.credit(amt))

        elif choice == 3:
            print("Current Balance:", account.get_balance())

        elif choice == 4:
            print("Transaction History:")
            for t in account.get_transactions():
                print("-", t)

        elif choice == 5:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")
