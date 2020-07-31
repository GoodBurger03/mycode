#!/usr/bin/env python3

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    return x / y

num = float(input("What number do you choose?"))
num1 = float(input("What about a second number?"))
op = input("What would you like to do? add, subtract, multiply, or divide?")

if op == "subtract":
    sub(num,num1)
     print(return)
elif op == "multiply":
    mult(num,num1)
     print(return)
elif op == "add":
    add(num,num1)
     print(return)
elif op =="divide":
    div(num,num1)
     print(return)






