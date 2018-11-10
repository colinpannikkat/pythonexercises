number = int(input("How many Fibonacci numbers to generate?\n"))

if number == 1:
    list = [1]
elif number != 1:
    list = [0, 1]

for i in range(1, number):
    list.append(list[i]+list[i-1])
print (list)
