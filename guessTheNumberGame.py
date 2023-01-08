import sys
import random


def guessTheNumberGame():
        
    sys.stdout.buffer.write(b"Choose your number between 1 to 5\n")
    sys.stdout.flush()

    for i in range(0, 5):
        inputNum = sys.stdin.readline()
        randomNum = random.randint(1,5)

        if int(randomNum) == int(inputNum):
            print("Number is ... " + str(randomNum))
            return print("Fantastic!! Your guess is correct!!")
        else:
            print("Number is ... " + str(randomNum))
            sys.stdout.buffer.write(b"Uh,,, not correct. you can try again!!\n")
            sys.stdout.flush()

    print("")
    return print("You can not guess correct number.....")

guessTheNumberGame()