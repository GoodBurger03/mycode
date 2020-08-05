


def bottle():
    for x in range(0, 10):
     print(x, end=" ")

    for x in range(4, 31):
     if x % 2 == 0:
      print(x, end = " ")


    for x in range(99, 0, -1):
     if x > 1:
      print(f"{x} bottles of beer on the wall! {x}")
      print(f"{x}, bottles of beer! you take one down pass it around!")

bottle()

