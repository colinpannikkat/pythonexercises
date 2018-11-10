number = int(input("Please input a number.\n"))
num = []
c = 0
for i in range(1,number+1):
    if number%i == 0:
        if i == number:
            num.append(i)
            c += 1
        elif i == 1:
            num.append(i)
            c += 1
        else:
            c += 1
    else:
        pass

if c > 2:
    print ("{} is not prime\n".format(number))
elif c <= 2:
    print ("{} is prime!\n".format(number))
