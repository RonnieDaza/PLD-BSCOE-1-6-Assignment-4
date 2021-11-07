# Create a program that will ask for name, age, and address.
# Display those details in the following format.
# Hi, my name is __________. I am __________ years old and I live in __________.

def getNameAgeAddress():
    _name = input("Enter your name: ")
    _age = int(input("Enter your age: "))
    _address = input("Enter your address: ")
    return _name, _age, _address