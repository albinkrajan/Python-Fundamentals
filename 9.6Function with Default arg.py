def loan(p, r, t, f = 1000):
    i = p*r*t/100
    amt = i + f
    return amt


p = loan(100, 2, 3)
print(p)
