import random

repeat = True

while repeat == True:
    
    password = input(("Input desired password: "))

    new_password = ""

    reverse = input(("Do you want to reverse it?\n"))

    if reverse == "yes":
        password = (password [ : :-1])
    else:
        pass

    print(password)

    reorganize = input(("Wanna shuffle?\n"))

    if reorganize == "yes":
        shuffled = list(password)
        random.shuffle(shuffled)
        password = ''.join(shuffled)
    else:
        pass

    print(password)

    confirmation = input("Want to encrypt?\n")

    if confirmation == "yes":

        shift = int(input("What is your shift: "))

        for ch in password:
            if ch.isalpha():
                stayInAlphabet = ord(ch) + shift 
                if stayInAlphabet > ord('z'):
                    stayInAlphabet -= 26
                finalLetter = chr(stayInAlphabet)
                new_password += finalLetter

    if confirmation == "yes":
        password = new_password
    else:
        pass
        
    print(password)

    again = input("Wanna do it again?\n")

    if again == "yes":
        pass
    else:
        repeat = False
input()
