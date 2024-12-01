n = int(input("Enter an integer: "))

for i in range(1, n + 1):
    if i % 15 == 0: # i is divisible by both 3 and 5(divisible by 15)
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)