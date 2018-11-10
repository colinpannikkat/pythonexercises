number = int(input("Please input a number.\n"))

for i in range(2,number+1):
    if number%i == 0:
        print (number/i)
    pass
