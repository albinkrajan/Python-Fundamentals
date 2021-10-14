m = int(input("Enter the marks:"))
if m < 101:
    if m >= 90:
        print("A Grade")
    elif m <= 89 and m >= 80:
        print("B grade")
    elif m <= 79 and m >= 70:
        print("C grade")
    elif m <= 69 and m >= 60:
        print("D Grade")
    else:
        print("Fail")
else:
    print("Enter the right marks!")