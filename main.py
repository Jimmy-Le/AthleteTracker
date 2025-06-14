import os
from utils import clearLogs, setFilename, parseByType, addToList, printSportStat, setPlayerList, deleteFromList


appRunning = 0

def printMenu():
    print("1. Load File")
    print("2. Print Stats")
    print("3. Delete Athlete")
    print("4. Save File")
    print("5. Athlete Info")
    print("6. Display Chart")
    print("7. Exit")


def parseFile():
    """This function will ask for a file name and parse the data based on the type of athlete"""
    clearLogs()
    filename = input("Please enter the name of the file: ")          # Get file name from user
    try:
        with open(filename, "r") as file:
            setPlayerList([])
            setFilename(filename)                                   # Save the file name 
            for line in file:
                player, data = line.strip().split(":", 1)           # find the type of player
                splitData = data.strip().split(",")                 # split the rest of the data
                newAthlete = parseByType(player, splitData)         # Based on the type of player, parse the data accordingly
                addToList(newAthlete)                               # Add the new athlete to the list
        print("File loaded successfully")
            # printAll()
    except Exception as e:
        print("Error: ", e)

def printAllStats():
    clearLogs()
    printSportStat()

def deleteAthlete():
    clearLogs()
    print("Deleting Athlete:")
    print("--------------------")
    deleteFromList()


def handleMenu(choice):

    if(choice == 1):
        parseFile()
    elif(choice == 2):
        printAllStats()
    elif(choice == 3):
        deleteAthlete()
    elif(choice == 4):
        print("4")
    elif(choice == 5):
        print("5")
    elif(choice == 6):
        print("6")

    elif(choice == 7):
        print("Exiting program...")
        return 1
    else:
        print("Invalid input, please try again")
    return 0


def main():
    global appRunning

    while(appRunning == 0):
        clearLogs()
        printMenu()
        try:
            choice = int(input("Please enter your choice: "))

            appRunning = handleMenu(choice)
            print("")
            if(appRunning == 0):
                print("")
                input("Press ENTER to continue: ")
        except Exception as e:
            print("Invalid input, please try again: ", e)
        # finally:
        #     print("")
        #     input("Press ENTER to continue: ")
            

   

# Ensure to call main, if it was not the main function called
if __name__ == "__main__":
    main()