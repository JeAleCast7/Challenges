from sympy import fibonacci

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

if number > 1:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not prime")
else:
    print("Not prime")

print("Fibonacci:", fibonacci(number))