import range

for x range(0, 100):
    if x % 3 == 0:
        print("Fizz", end=" ")
    elif x % 1 == 0:
        print(x, end = " ")
    elif x % 5 == 0:
        print("Buzz", end = " ")
