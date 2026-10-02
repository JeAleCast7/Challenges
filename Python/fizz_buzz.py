for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz\n")
    elif x % 3 == 0:
        print("fizz\n")
    elif x % 5 == 0:
        print("buzz\n")
    else:
        print(x, "\n")