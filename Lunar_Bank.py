
# Defines title of banking system
def title():
    text='WELCOME TO LUNAR BANK SA'
    new_text=text.center(40)
    print(20*'-=')
    print(f'{new_text}')
    print(20*'-=')

# Defines function for final user menu
def menu():

    print('Please, enter a option:\n')
    
    print('[1] BALANCE')
    print('[2] EXTRACT')
    print('[3] DEPOSIT')
    print('[4] WITHDRAW')
    print('[5] EXIT')
    print()


# Function for show balance
def show_balance(balance):
    print(f'You atual balance is: {balance:.2f}')

# Shows bank statement
def show_statement(transactions):
    print('***** EXTRACT *****')
    if not transactions:
        print('No movement.')
    else:
        for trans in transactions:
            print(trans)
            

# Makes deposit and shows new balance
def make_deposit(balance, transactions):
    try:
        deposit_value = float(input('What is the deposit value? R$'))
        if deposit_value <= 0:
            print('The value must be greater than 0.00. Try again.')
        else:
            balance += deposit_value
            transactions.append(f'Deposit: R$ + {deposit_value:.2f}')
            transactions.append(f'{"*":>25}{balance:<25.2f}')
            print(f'Your new balance is: R${balance:.2f}. Thank you for using our service.\n')
            return balance, transactions
    except ValueError:
        print('Error: Please enter a valid value.')
       

# Withdraw an amount, respecting the balance and daily limit
def withdraw(balance, daily_limit, transactions):
    while True:
        try:
            withdraw_value = float(input('What is the withdrawal value? R$\n'))
            print()
            if withdraw_value > 0 and withdraw_value <= balance and withdraw_value <= daily_limit:
                balance -= withdraw_value
                daily_limit -= withdraw_value
                transactions.append(f'Withdraw: R$ - {withdraw_value:.2f}')
                transactions.append(f'{"*":>25}{balance:<25.2f}')
                print('Withdrawal successful.')
                print(f'Your current balance is: R${balance:.2f}')
                print(f'Your remaining daily limit is: R${daily_limit:.2f}')
                return balance, daily_limit, transactions
            else:
                if withdraw_value > balance:
                    print('insufficiente balance. Try Again\n')
                elif withdraw_value > daily_limit:
                    print('daily limit exceeded\n')

        except ValueError:
            print('Error: Please enter a valid value.')
        


# List to store movements
transactions=[]

# Global variables
balance = float(0)
daily_limit = float(500)


# Start of main program
title()
menu()

while True:
    option = input()

    if option == '1':
        show_balance(balance)
        menu()
    elif option == '2':
        show_statement(transactions)
        menu()
    elif option == '3':
        balance, transactions = make_deposit(balance, transactions)
        # make_deposit(balance, transactions)
        menu()
    elif option == '4':
        withdraw(balance, daily_limit, transactions)
        menu()
    elif option == '5':
        print('Thank you for using our system. Exiting...')
        break
    else:
        print('Invalid option. Try again.\n')
        menu()