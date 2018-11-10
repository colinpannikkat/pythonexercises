import random

print("-----------------------------------\n")
print("To exit, type 'exit'.\n")
print("-----------------------------------\n")
a = random.randint(1,9)
guesnum = 0
nl = "\n"

while True:

    def exit():
        if guesnum == 1:
            print("You guessed 1 time!\n")
        else:
            print("And it only took you {} tries!".format(guesnum))

    guess = input("Guess the number!\n")

    if str(guess) == "":
        continue
    elif str(guess) == "exit":
        exit()
    elif int(guess) == a:
        print("You guessed correct!")
        guesnum = guesnum + 1
        exit()
    elif int(guess) > a:
        print("You guessed too high!\n")
        guesnum = guesnum + 1
    elif int(guess) < a:
        print("You guessed too low!\n")
        guesnum = guesnum + 1
