import os, time, platform

class ToDoList:
    def __init__(self):
        self.NotCompletedData = []
        self.CompletedData = []

    def Clear(self):
        os_name = platform.system()
        if os_name == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    def TakeTimeAndClear(self, Time):
        time.sleep(Time)
        RunTheApp.Clear()
    
    def LoadTheData(self):
        with open("D:/skill_upgrad/python/to_do_list/Data.txt", 'r') as file:
            lines = file.readlines()
        
        tag = 0
        for line in lines:
            stripped_line = line.strip()

            if stripped_line == "NotCompleted" or stripped_line == "":
                continue

            elif stripped_line == "Completed":
                tag = 1
                continue

            elif tag == 0:
                self.NotCompletedData.append(stripped_line)
            else:
                self.CompletedData.append(stripped_line)
        
        file.close()
    
    def AddTheTask(self):
        UserTask = str(input("Enter Your Task: "))
        RunTheApp.Clear()
        self.NotCompletedData.append(UserTask)
        print("The task is added")
        RunTheApp.TakeTimeAndClear(2)
    
    def RemoveTheTask(self):   
        while 1:
            print("Example if you need to remove the 1st one in completed section Than Enter 'c1' and it for notcompleted section 'n1', Move to main menu Enter 'j'")
            print()
            self.ShowTheTask(1)
            print()

            UserInput = str(input("Enter the task code: "))
            self.Clear()

            if UserInput == "j":
                break

            try:
                Section, Position = UserInput[0], int(UserInput[1:])
                if Section not in ["c", "n"]:
                    print("Place enter the vaild input")
                    self.TakeTimeAndClear(2)
                    continue
                
                if Section == "c":
                    if Position > len(self.CompletedData) or Position < 0:
                        print("Place enter the vaild input")
                        self.TakeTimeAndClear(2)
                        continue
                elif Section == "n":
                    if Position > len(self.NotCompletedData) or Position < 0:
                        print("Place enter the vaild input")
                        self.TakeTimeAndClear(2)
                        continue

            except:
                print("Place enter the vaild input")
                self.TakeTimeAndClear(2)
                continue

            if Section == "c":
                del self.CompletedData[Position-1]
            elif Section == "n":
                del self.NotCompletedData[Position-1]
            
            print("The data is removed")
            self.TakeTimeAndClear(2)
            break


    def ComplateTask(self):
        while 1:
            print("NotCompleted")
            count = 1
            for i in self.NotCompletedData:
                print(f"{count}. {i}")
                count += 1
            print()

            UserInput = str(input("Enter the task number are Move to main menu Enter 'j': "))
            self.Clear()

            if UserInput == "j":
                break

            try:
                Position = int(UserInput)
                if Position > len(self.NotCompletedData) or Position < 0:
                    print("Place enter the vaild input")
                    self.TakeTimeAndClear(2)
                    continue

            except:
                print("Place enter the vaild input")
                self.TakeTimeAndClear(2)
                continue

            Position -= 1
            Value = self.NotCompletedData[Position]
            del self.NotCompletedData[Position]
            self.CompletedData.append(Value)
            break

    def ShowTheTask(self, tag=0):
        count = 1
        print("NotCompleted")
        for i in self.NotCompletedData:
            print(f" {count} "+i)
            count += 1
        
        print()
        count = 1

        print("Completed")
        for i in self.CompletedData:
            print(f" {count} "+i)
            count += 1
        
        if tag == 0:
            UserInput = str(input("Enter any key: "))
            self.Clear()
    
    def UnComplateTask(self):
        while 1:
            print("Completed")
            count = 1
            for i in self.CompletedData:
                print(f"{count}. {i}")
                count += 1
            print()

            UserInput = str(input("Enter the task number are Move to main menu Enter 'j': "))
            self.Clear()

            if UserInput == "j":
                break

            try:
                Position = int(UserInput)
                if Position > len(self.CompletedData) or Position < 0:
                    print("Place enter the vaild input")
                    self.TakeTimeAndClear(2)
                    continue

            except:
                print("Place enter the vaild input")
                self.TakeTimeAndClear(2)
                continue

            Position -= 1
            Value = self.CompletedData[Position]
            del self.CompletedData[Position]
            self.NotCompletedData.append(Value)
            break
        

        
        
RunTheApp = ToDoList()
RunTheApp.LoadTheData()
RunTheApp.Clear()
print("Welcome To To-Do List")
RunTheApp.TakeTimeAndClear(3)
print("Warning\nPROPERLY EXIT THE PROGRAM TO SAVE THE DATA")
RunTheApp.TakeTimeAndClear(4)

while 1:
    print(f"Options:\n 1 - Add The Task\n 2 - Remove The Task\n 3 - Make The Task Complate\n 4 - Make The Task Uncomplate\n 5 - View The Tasks\n 6 - To Clear All Data\n 7- To Exit The Program\n")
    Option = str(input("Enter the option: "))
    RunTheApp.Clear()

    if Option not in ['1', '2', '3', '4', '5', '6', "7"]:
        print("Place enter vaild input")
        RunTheApp.TakeTimeAndClear(3)
        continue

    if Option == "1":
        RunTheApp.AddTheTask()

    elif Option == "2":
        RunTheApp.RemoveTheTask()

    elif Option == "3":
        RunTheApp.ComplateTask()

    elif Option == "4":
        RunTheApp.UnComplateTask()
    
    elif Option == "5":
        RunTheApp.ShowTheTask()
        print()

    elif Option == "6":
        file = open("D:/skill_upgrad/python/to_do_list/Data.txt", 'w')
        file.writelines("NotCompleted\n\nCompleted")
        file.close()
        RunTheApp.LoadTheData()
        print("The data is deleted")
        RunTheApp.TakeTimeAndClear(2)
    
    elif Option == "7":
        file = open("D:/skill_upgrad/python/to_do_list/Data.txt", 'w')

        file.writelines("NotCompleted\n")
        for i in RunTheApp.NotCompletedData:
            file.writelines((i+"\n"))

        file.writelines("\nCompleted\n")
        for i in RunTheApp.CompletedData:
            file.writelines((i+"\n"))
        
        file.close()
        break
    

print("Thanks For Using The To To-Do List")
