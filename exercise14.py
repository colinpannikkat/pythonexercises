import random
def RemoveDup(a):
    a = a.replace(",","")
    list = []
    for i in a:
        list.append(i)
    a = set(list)
    print(a)

RemoveDup(input("What is the list? (separated by commas)\n"))
