#factorial of a number
n = int(input("Enter the range:"))
fact = 1
if n < 0:
    print("Enter a Positive number")
elif n == 0:
    print("Factorial is 1")
else:
    for i in range(1, n+1):
        fact = fact* i
    print(fact)