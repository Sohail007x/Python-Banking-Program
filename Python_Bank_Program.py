# Python Banking Program

Balance =  100

while True:
    print("**********************")
    print("Banking Program")
    print("**********************")
    print("1. Show Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    print("**********************")
    
    choice = float(input("Enter the option:- "))
    print("**********************")
    
    if choice == 1:
        print(f"Your balance is: $ {Balance:.2f}")
        
    elif choice == 2:
        withdraw = float(input("Enter the amount to withdraw: $ "))
        if withdraw > Balance:
            print("**********************")
            print("Insufficient Funds")
            
        else:
            Balance = Balance - withdraw
            print("**********************")
            print(f"Withdrawal Successful.\nYour current balance is $ {Balance:.2f}")
    
    elif choice == 3:
        deposit = float(input("Enter the amount to deposit:- $ "))
        print("**********************")
        Balance = Balance + deposit
        print(f"Deposit Successful.\nYour current balance is $ {Balance:.2f}")

    elif choice == 4:
        print("Thank you for using our Banking Sysytem.")
        print("**********************")
        break
    
    else:
        print("**********************")
        print("Invalid option. Please choose a valid option.")
        
    