a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = input("What number?\n")
for element in a:
    if int(element) < number:
        print(element)
    else:
        continue
