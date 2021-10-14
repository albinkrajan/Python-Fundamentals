def loan(p, r, t):
    i = p*r*t/100
    print (i)


loan(100, 2, 3)


def loan(p, r, t):
    i = p*r*t/100
    return i


interest = loan(100, 6, 7)
#here you can use the interest variable for future purposes.
print(interest)
