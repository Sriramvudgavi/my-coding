class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount}. Your new balance is: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew {amount}. Your new balance is: {self.balance}")

def atm_system():
    atm = ATM(1000)  # Initialize with a balance of $1000 for example
    print("Welcome to the ATM!")

    while True:
        print("\nPlease select an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                amount = float(input("Enter the amount to deposit: "))
                atm.deposit(amount)
            elif choice == 3:
                amount = float(input("Enter the amount to withdraw: "))
                atm.withdraw(amount)
            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the ATM system
atm_system()
