def ReverseWord():
    choice = input("Input a string:\n")
    result = choice.split(" ")
    a = result[::-1]
    str1 = ' '.join(a)
    print(str1)
ReverseWord()
