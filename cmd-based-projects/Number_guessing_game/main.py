import os, time, platform, random

class NumberGuessing:
    def _init__(self):
        pass

    def Clear(self):
        os_name = platform.system()
        if os_name == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    def TakeTimeAndClear(self, Time):
        time.sleep(Time)
        RunTheApp.Clear()
    
    def RandomNumberGenerator(self):
        return random.randint(1, 100)

RunTheApp = NumberGuessing()
RunTheApp.Clear()
print("Welcome To Number Guessing Game")
RunTheApp.TakeTimeAndClear(3)

RandomNumber = RunTheApp.RandomNumberGenerator()

LifeLine = ['💖', '💖', '💖', '💖', '💖']

tag = 0
Warning = 0

while 1:
    if tag == 1:
        RandomNumber = RunTheApp.RandomNumberGenerator()
        tag = 0
    
    LifeLineString = ""
    for i in LifeLine:
        LifeLineString += i+" "
    print(LifeLineString, "\n")

    UserInput = str(input("To exit enter '0',\nIf you are not able to find the value enter 'n',\nGuess the number this: "))
    RunTheApp.Clear()

    if UserInput == "0":
        break
    elif UserInput == "n":
        print(f"The value is {RandomNumber}")
        Continue = str(input("If you Need to continue enter '1', Else press any key: "))
        RunTheApp.Clear()
        if Continue == "1":
            tag = 1
            LifeLine = ["💖"*5]
            continue
        else:
            break

    try:
        UserInput = int(UserInput)
    except:
        if Warning == 0:
            print("Place enter valid input, Else you lose your lifeline")
            RunTheApp.TakeTimeAndClear(3)
            Warning += 1
            continue
        else:
            print("Place enter valid input and You loosed your lifeline")
            LifeLine.pop()
            RunTheApp.TakeTimeAndClear(3)
            if len(LifeLine) == 0:
                Continue = str(input("If you Need to continue enter '1', Else press any key: "))
                RunTheApp.Clear()
                if Continue == "1":
                    tag = 1
                    LifeLine = ["💖"*5]
                    continue
                else:
                    break
            continue
    
    GuessString = ""

    if (RandomNumber-UserInput) < 10:
        if (RandomNumber-UserInput) < 0:
            if (RandomNumber-UserInput) > -10:
                GuessString += "You are near the value, "
        else:
            GuessString += "You are near the value, "

    if UserInput == RandomNumber:
        print("You successfully find the value")
        Continue = str(input("If you Need to continue enter '1', Else press any key: "))
        RunTheApp.Clear()
        if Continue == "1":
            tag = 1
            LifeLine = ["💖"*5]
            continue
        else:
            break
    elif RandomNumber > UserInput:
        GuessString += f"It is greater than this {UserInput}"
    elif RandomNumber < UserInput:
        GuessString += f"It is less than this {UserInput}"

    print(GuessString)
    LifeLine.pop()
    RunTheApp.TakeTimeAndClear(3)
    if len(LifeLine) == 0:
        print(f"You fail to find the value and The value is {RandomNumber}")
        Continue = str(input("If you Need to continue enter '1', Else press any key: "))
        RunTheApp.Clear()
        if Continue == "1":
            tag = 1
            LifeLine = ["💖"*5]
            continue
        else:
            break

print("Thanks For Using The To Number Guessing Game")