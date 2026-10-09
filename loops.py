#while loop

number= 20

while number <=25:
    print(number)
    number += 1

    #for loop
for x in range(1, 6):
        print(x)

        for i in range(1, 9):
            if i==5 :
                continue
            print(i)

            for number in range(1, 50):
                if number == 47:
                    break
                print(number)

        #break and continue statements
