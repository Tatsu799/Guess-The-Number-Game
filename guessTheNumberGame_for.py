import sys
import random


def guessTheNumberGame():
    try:
        minNum = int(input("Put minimum number\n"))
        maxNum = int(input("Put maximum number\n"))

    except ValueError:
        print("Please put a number")
        sys.exit()

    if int(minNum) >= int(maxNum):
        return print("You must choose a Number which 'Minimum Number' is smaller than 'Maximum Number'")

    else:
        sys.stdout.buffer.write(b"Guess the number\n")
        sys.stdout.flush()

        try:
            for i in range(0, 5):
                inputNum = int(sys.stdin.readline())
                randomNum = int(random.randint(int(minNum), int(maxNum)))

                if int(randomNum) == int(inputNum):
                    print("Number is ... " + str(randomNum))
                    return print("Fantastic!! Your guess is correct!!")
                else:
                    print("Number is ... " + str(randomNum))
                    sys.stdout.buffer.write(b"Uh,,, not correct. You can try again!!\n")
                    sys.stdout.flush()
        
        except ValueError:
            print("Please put a number")
            sys.exit()

    print("")
    return print("You can not guess correct number.....")

guessTheNumberGame()