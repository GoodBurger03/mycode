#!/usr/bin/env python3

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    return x / y
go_again = 'yes'

while go_again == 'yes' or go_again == 'Yes':
    print("Welcome to the Calculator")
    num = float(input("What number do you choose?"))
    num1 = float(input("What about a second number?"))
    op = input("What would you like to do? add, subtract, multiply, or divide?")


if op == "subtract":
    sub(num,num1)
    print("Your answer is: {num - num1}")
elif op == "multiply":
    mult(num, num1)
    print("Your answer is:  {num * num1}")
elif op == "add":
    add(num,num1)
    print("Your answer is:  {num + num1}")
elif op =="divide":
    div(num,num1)
    print("Your answer is: { num / num1}")
else:
    print("That is not a valid entry.")
    r = input("did you want to go again? yes/no: ")
    if r == yes







