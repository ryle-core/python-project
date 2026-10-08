year = int(input("enter year:"))

if year % 4 == 0:
    print("leap year")
else:
    if year % 100 == 0 :
        print(" not leap year")
