import random

def listEnds():
    number = int(input("How long do you want the list to be?\n"))
    a = []
    n = 0
    while n < number:
        a.append(random.randint(1, 100))
        n += 1
    print ("Your list is {}\n".format(a))

    alen = (len(a)-1)
    c = []
    z = a[0]
    y = a[alen]
    c.append(z)
    c.append(y)
    print (c)

listEnds()
