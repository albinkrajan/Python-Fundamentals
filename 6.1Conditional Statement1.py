val = int(input("Enter the measurement"))
print("Enter M or m for converting meter to cm")
print("Enter N or n for converting cm to meter")
op = (input("Enter your choice:"))

if (op in "Mm"):
    val = val*100
    print("Cm =",val)
elif (op in "Nn"):
    val = val/100
    print("M =", val)
else:
    print("Enter the right choice!")


