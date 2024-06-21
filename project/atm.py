import time

print("Please insert Your CARD")

# Simulate card processing
time.sleep(5)

password = 1234

# Taking ATM pin from user
pin = int(input("Enter your ATM pin: "))

# User account balance
balance = 5000

# Checking if the pin is valid
if pin == password:
    while True:
        # Showing options to the user
        print(""" 
        1 == Check balance
        2 == Withdraw balance
        3 == Deposit balance
        4 == Exit
        """)

        option = int(input("Please enter your choice: "))
        
        if option == 1:
            print(f"Your current balance is {balance}")
        
        elif option == 2:
            withdraw_amount = int(input("Please enter the withdraw amount: "))
            if withdraw_amount > balance:
                print("Insufficient funds")
                print("Please check your balance")
            else:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your updated balance is {balance}")
        
        elif option == 3:
            deposit_amount = int(input("Please enter the deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {balance}")

        elif option == 4:
            break

        else:
            print("Please enter a valid option")

else:
    print("Wrong pin. Please try again.")
