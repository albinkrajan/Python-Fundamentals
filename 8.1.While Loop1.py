num=int(input("Enter the range"))
s1 = 0
i = 1
while i < num + 1:
    if i % 2 != 0:
        s1 += i
    i += 1
print(s1)

#using builtin function sum
n = int(input("Enter the range:"))
s = sum(range(1, n+1, 2))
print(s)