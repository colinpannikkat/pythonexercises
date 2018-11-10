string = input("Input String:\n")
string = string.replace(" ", "")
list = list(string)
a = int(len(list))
x = a-1
c = []

while x > -1:
    b = string[x]
    c.append(b)
    x = x-1

b = int(len(c))
z = list[0:a]
y = c[0:b]
print (z,y)

if z == y:
    print("The string is a palendrome!\n")
else:
    print("The string is not a palendrome.\n")
