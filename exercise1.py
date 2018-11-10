import datetime
now = datetime.datetime.now()

name = input("What is your name?\n")
age = int(input("What is your age?\n"))
date = now.year
age100 = (date - age) + 100
print("Hello {0:s} you will turn 100 years old in {1}!".format(name, age100))
