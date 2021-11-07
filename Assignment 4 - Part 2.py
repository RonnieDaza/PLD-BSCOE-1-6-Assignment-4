# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if the apple price is 20 pesos and the orange price is 25 pesos.
# Display the output in the following format.
# The total amount is __________.

def getTotal():
    _appleQuestion = int(input("How many apples you want to buy? "))
    _orangeQuestion = int(input("How many oranges you want to buy? "))
    _applePrice = 20
    _orangePrice = 25
    _appleTotal = _appleQuestion * _applePrice
    _orangeTotal = _orangeQuestion * _orangePrice
    _total = _appleTotal * _orangeTotal