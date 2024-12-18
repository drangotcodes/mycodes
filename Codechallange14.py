#Kuripot Bank Services
may_account = False
takbo = True

import os

bal = 0
#Peso denominations of the amount entered


def deposit_money():
    global bal
    os.system('cls')
    amount = eval(input("How much would you like to deposit?"))

    libo = amount // 1000
    libo2 = amount % 1000
    paybdaan = libo2 // 500
    paybdaan2 = libo2 % 500
    dalwadaan = paybdaan2 // 200
    dalwadaan2 = paybdaan2 % 200
    sandaan = dalwadaan2 // 100
    sandaan2 = dalwadaan2 % 100
    pepte = sandaan2 // 50
    pepte2 = sandaan2 % 50
    benti = pepte2 // 20
    benti2 = pepte2 % 20
    sampu = benti2 // 10
    sampu2 = benti2 % 10
    lima = sampu2 // 5
    lima2 = sampu2 % 5
    piso = lima2 // 1
    piso2 = lima2 % 1


    os.system('cls')
    print("Peso denominations of the amount you would depositing is shown below:")
    print(f"1000 = {libo}\n500 = {paybdaan}\n200 = {dalwadaan}\n100 = {sandaan}\n50 = {pepte}\n20 = {benti}\n10 = {sampu}\n5 = {lima}\n1 = {piso}")
    print(f"Amount entered: {amount}")
#depositing

    choice1 = input("Would you like to deposit the amount? (yes or no)")
    if choice1.lower() == "yes":
        os.system('cls')
        bal += amount
        print(f"You have successfully deposited {amount} pesos to your account.")
        bla = input("Enter any input to continue.")
        return bal
    elif choice1.lower() == "no":
        os.system('cls')
        print("Deposit session has ended, Thank you.")
        print()
        return bal
#checking balance

def check_balance():
    os.system('cls')
    print(f"Your total balance is {bal} pesos.")
    bla = input("Enter any input to continue.")
#withdrawing money

def withdraw_money():
    global bal
    os.system('cls')
    amount = eval(input("How much would you like to withdraw? "))
    if amount >= bal:
        print("The amount must not be greater than the available balance.")
        print(f"Amount entered: {amount}")
        bla = input("Enter any input to continue.")
    elif amount == bal or amount <= bal:
        bal -= amount
        os.system('cls')
        print(f"{amount} has been withdrawn from your account, your current balance is now {bal}.")
        bla = input("Enter any input to continue. ")
        return bal
    else:
        print("Invalid input.")
        print()
#kuripot Bank Services

while takbo == True:
    os.system('cls')
    print("Welcome to Kuripot Bank Services the best bank to hide your money to your relatives and debtor.")
    if may_account == False:
        os.system('cls')
        sign_in = input("You need to have an account to use Kuripot Bank Services.\nWould you like to create an account? (yes or no)")
        if sign_in.lower() == "yes":
            os.system('cls')
            print("Account Sign-in")
            print()
            name = input("Please enter your name. ")
            password = input("Create your password. ")
            pass_confirm = input("Re-enter password. ")
            if pass_confirm == password :
                os.system('cls')
                print("Account successfully created")
                may_account = True
                bla = input("Enter any input to continue.")
        elif sign_in.lower() == "no":
            print("Thank you for using our system.")
            takbo = False
            break

    elif may_account == True:
        while takbo == True:
            os.system('cls')
            print("Please login your account to access our Kuripot Bank Services.")
            whatname = input("Name: ")
            if whatname == name:
                whatpass = input("Password: ")
                if whatpass == password:
                    while takbo == True:
                        os.system('cls')
                        print(f"Hi {name}! What would you like to do?")
                        print("1.Check your balance\n2.Deposit money\n2.Withdraw money\n4.End the program")
                        choice = input("")
                        if choice == "1":
                            check_balance()
                        elif choice == "2":
                            deposit_money()
                        elif choice == "3":
                            withdraw_money()
                        elif choice == "4":
                            os.system('cls')
                            print("Thank you for using our services.")
                            print("Please come again.")
                            takbo = False
                            break
                elif whatpass != password:
                    os.system('cls')
                    print("Incorrect password.")
                    bla = input("Enter any input to continue.")
            elif whatname != name:
                os.system('cls')
                print("Account does not exist.")
                bla = input("Enter any input to continue.")
