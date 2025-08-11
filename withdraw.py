
class NegativeWithdraw(Exception):
    pass

balance = 1000

try:
    withdraw = int(input())
    if withdraw>balance:
        raise NegativeWithdraw("Insufficient funds")
except NegativeWithdraw as e:
    print("Error",e)
        