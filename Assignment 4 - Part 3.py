# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy __________ apples and your change is __________ pesos.

def getAppleQuantityMoneyLeft():
    _money = int(input("Enter the amount of money: "))
    _apple = int(input("Enter the price of an apple: "))
    _appleQuantity = _money // _apple
    _applePrice = _appleQuantity * _apple
    _moneyLeft = _money - _applePrice
    return _appleQuantity, _moneyLeft

def display(appleQuantityF, moneyLeftF):
    print(f"You can buy {appleQuantityF} apples and your change is {moneyLeftF} pesos.")

# Steps
# 1. Ask for the amount of money the user have and the price of an apple.
appleQuantity, moneyLeft = getAppleQuantityMoneyLeft()
# 2. Display the output.
display(appleQuantity, moneyLeft)