# Create a program that will ask for name, age, and address.
# Display those details in the following format.
# Hi, my name is __________. I am __________ years old and I live in __________.

def getNameAgeAddress():
    _name = input("Enter your name: ")
    _age = int(input("Enter your age: "))
    _address = input("Enter your address: ")
    return _name, _age, _address

def display(nameF, ageF, addressF):
    print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addressF}.")

# Steps
# 1. Ask for name, age, and address.
name, age, address = getNameAgeAddress
