withdraw_value,account_balance = input().split()

withdraw_value = int(withdraw_value)
account_balance = float(account_balance)

def withdraw(withdraw_value, account_balance):
    if ((withdraw_value % 5) == 0) and (account_balance >= (withdraw_value + 0.5)):
        print("%.2f" % (account_balance - withdraw_value - 0.5))
    else:
        print("%.2f" % account_balance)

withdraw(withdraw_value, account_balance)