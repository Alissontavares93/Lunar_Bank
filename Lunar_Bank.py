def title():
    text='WELCOME TO LUNAR BANK SA'
    new_text=text.center(40)
    print(20*'-=')
    print(f'{new_text}')
    print(20*'-=')

def menu():
    print()
    print('Please, enter a option:\n')
    
    print('[1] BALANCE')
    print('[2] EXTRACT')
    print('[3] DEPOSIT')
    print('[4] WITHDRAW')
    print('[5] EXIT')
    print()

title()
menu()
transations=[]

balance = float(0)
dayly_limit = float(1000)


while True:
    option=input()

    if option=='1':
        print()
        print(f'You atual balance is: {balance:.2f}')
        print()
        menu()

    else:
        if option=='2':
            print()
            print('***** EXTRACT *****')
            print()
            if transations:
                for trans in transations:
                    print(trans)
            else:
                print('No movement.')
            print()
            menu()

        else:
            if option == '3':
                deposit_value=int(input('Whats deposit value?\n'))
                balance+=deposit_value
                transations.append(f'Deposit: R$ + {deposit_value:.2f}\n')
                transations.append(f'{"*":>25}{balance:<25.2f}')
                print(f'You new balance is: R${balance:.2f}', end='')
                print()
                menu()

            else:
                if option == '4':
                    withdraw_value=int(input('Whats withdraw value?\n'))
                    print()
                    if withdraw_value > 0 and withdraw_value <= balance and withdraw_value <= dayly_limit:
                        balance -= withdraw_value
                        dayly_limit-= withdraw_value
                        transations.append(f'Withdraw: R$ - {withdraw_value}\n')
                        transations.append(f'{'*':>25}{balance:<.2f}')
                        print('Withdrawal successful.')
                        print(f'You atual balance is: {balance:.2f}')
                    else:
                        if withdraw_value<0:
                            print(f'Enter a value greater than R$1,00.')
                        else:
                            if withdraw_value>balance:
                                print(f'Insufficient balance for this withdraw.')
                            else:
                                if withdraw_value>dayly_limit:
                                    print(f'Unauthorized withdrawal. Your remaining daily limit is: R${dayly_limit}')
                                print()
                    menu()

                else:
                    if option == '5':
                        print('Thankyou for use our system. Leaving...')
                        break

                    else:
                        print('Ivalid option. Try again.')
                        menu()