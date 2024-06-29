import os, time, platform

class calculator:
    def __init__(self):
        pass

    def Add(self, num1, num2):
        return f'The Addition Of {num1} + {num2} = {num1+num2}'
    
    def Sub(self, num1, num2):
        return f'The Subtraction Of {num1} - {num2} = {num1-num2}'
    
    def Mul(self, num1, num2):
        return f'The Multiplication Of {num1} × {num2} = {num1*num2}'
    
    def Div(self, num1, num2):
        return f'The Division Of {num1} ÷ {num2} = {num1/num2}'
    
    def ProcessAll(self, num1, num2):
        return (f"{RunTheApp.Add(num1, num2)}\n{RunTheApp.Sub(num1, num2)}\n{RunTheApp.Mul(num1, num2)}\n{RunTheApp.Div(num1, num2)}")
    
    def Clear(self):
        os_name = platform.system()
        if os_name == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    def TakeTimeAndClear(self):
        time.sleep(3)
        RunTheApp.Clear()

    def GetNumber(self):
        while 1:
            try:
                num = float(input("Enter The Number: "))
            except:
                RunTheApp.Clear()
                print("Place enter the number")
                RunTheApp.TakeTimeAndClear()
                continue
            break
        return num


RunTheApp = calculator()
RunTheApp.Clear()
print("Welcome To Simple calculator App")
RunTheApp.TakeTimeAndClear()

while 1:
    print("Options:\n 1 - Addition\n 2 - Subtraction\n 3 - Multiplication\n 4 - Division\n 5 - For All Process\n . - To exit the process")
    Option = str(input("Enter the option: "))
    RunTheApp.Clear()

    if Option not in ["1", "2", "3", "4", "5", "."]:
        print("Please choose the valid option.")
        RunTheApp.TakeTimeAndClear()
        continue

    if Option == ".":
        break

    Num1 = RunTheApp.GetNumber()
    RunTheApp.Clear()
    Num2 = RunTheApp.GetNumber()
    RunTheApp.Clear()

    if Option == "1":
        print(RunTheApp.Add(Num1, Num2))
    elif Option == "2":
        print(RunTheApp.Sub(Num1, Num2))
    elif Option == "3":
        print(RunTheApp.Mul(Num1, Num2))
    elif Option == "4":
        print(RunTheApp.Div(Num1, Num2))
    elif Option == "5":
        print(RunTheApp.ProcessAll(Num1, Num2))
    
    print()
    ToContinue = str(input("To continu enter 1, Else enter any key: "))
    if ToContinue != "1":
        break
    RunTheApp.Clear()

RunTheApp.Clear()
print("Thanks For Using The Simple calculator App")


