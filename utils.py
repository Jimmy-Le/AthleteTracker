import os
from hockey import HockeyPlayer
from swimmer import Swimmer
from ball import FootballPlayer, BasketballPlayer
from operator import attrgetter
from collections import Counter


__filename = ""
__playerList = []

# This function will clear out the screen
def clearLogs():
    if (os.name == "nt"):       # For windows
        os.system("cls")
    else:                       # For Mac / Linux
        os.system("clear")  

# This function will parse data based on what type of player it is and return the correspoding athlete
def parseByType(type, data):

    if(type == "HockeyPlayer"):
        hockeyPlayer = HockeyPlayer.parse(data)
        return hockeyPlayer
    elif(type == "Swimmer"):
        swimmerPlayer = Swimmer.parse(data)
        return swimmerPlayer
    elif(type == "BasketballPlayer"):
        basketPlayer = BasketballPlayer.parse(data)
        return basketPlayer
    elif(type == "FootballPlayer"):
        footballPlayer = FootballPlayer.parse(data)
        return footballPlayer
    else:
        print("error parsing: ",type)


def multiSort(playerList, attributeList):
    """Sorts a list by multiple different attributes"""
    for attribute, revBool in reversed(attributeList):
        playerList.sort(key=lambda player, att=attribute: (getattr(player, att) is None, getattr(player, att)), reverse = revBool)
    return playerList



def printSportStat():
    """This Function will separate the playerlist into the different sports, sort the results and print the required information"""
    hockeyList = []
    basketballList = []
    footballList = []
    swimmerList = []

    for player in __playerList:
        if(isinstance(player, HockeyPlayer)):
            hockeyList.append(player)
        elif(isinstance(player, BasketballPlayer)):
            basketballList.append(player)
        elif(isinstance(player, FootballPlayer)):
            footballList.append(player)
        elif(isinstance(player, Swimmer)):
            swimmerList.append(player)

    hockeyList = multiSort(hockeyList, (("goals_scored", True), ("name", False)))
    basketballList.sort(key=lambda athlete: athlete.endorsement)
    footballList= multiSort(footballList, (("touchdowns", True), ("name", False)))

    print("Statistics")
    print("--------------------")
    print(len(__playerList), "Athletes")
    print(len(hockeyList), "Hockey Players")
    print((len(basketballList) + len(footballList)), f"Ball Players ({len(basketballList)} Basketball and {len(footballList)} Football Players)")
    print(len(swimmerList), "Swimmers")
    print("")

    print("Endorsements")
    print("--------------------")

    endorsementList = []
    for player in basketballList:
        if (player.endorsement):
            endorsementList.append(player.endorsement)

    endorsementList = Counter(endorsementList)

    for key, value in endorsementList.items():
        print(key, f"({value})")    
    print("")
    
    print("Goals Scored")
    print("--------------------")
    for player in hockeyList:
        if(player.goals_scored is not None or ""):
            player.printStats()
    print("")

    print("Touchdowns")
    print("--------------------")
    for player in footballList:
        if(player.touchdowns is not None or ""):
            player.printStats()
    print("")
    

def deleteFromList():
    """This function will delete all instances of a given Athlete from the memory"""
    global __playerList
    sortedList = sorted( __playerList, key=lambda athlete: athlete.name)
    printAll()
    print("")
    chosenAthlete = input("Please enter the name of the athlete you wish to delete: ")

    foundResults = []
    newList = []
    for player in sortedList:
        if(player.name.lower() == chosenAthlete.lower()):
            foundResults.append(player)
        else:
            newList.append(player)
    
    if(len(foundResults) == 0):
        print("No Athlete Found")
    else:
        print(f"{len(foundResults)} result(s) found:")
        print("")
        for chosenAthlete in foundResults:
            print(chosenAthlete)
        print("")
        deletionChoice = input("Would you like to continue deleting all entries? (y/n): ")

        if (deletionChoice == "y" or deletionChoice == "Y"):
            setPlayerList(newList)
            print("Deletion completed")
        elif (deletionChoice == "n" or deletionChoice == "N"):
            print("Canceling operation...")
        else:
            print("Invalid input. Canceling operation...")


def saveListToFile():
    """This function will save the player list from memory into the original file"""
    global __playerList
    result = input("Would you like to save all changes made to the file? (y/n): ")
    if (result == "y" or result == "Y"):
        with open(__filename, "w") as file:
            for player in __playerList:
                file.write(player.__str__())

        print("Saved File")
    elif (result == "n" or result == "N"):
        print("Canceling operation...")
    else:
        print("Invalid input. Canceling operation...")


def displayAthleteInfo():
    global __playerList
    printAll()
    print("")
    chosenAthlete = input("Please enter the name of an Athlete you want to learn more of: ")

    foundResults = []
    for player in __playerList:
        if(player.name.lower() == chosenAthlete.lower()):
            foundResults.append(player)
    
    if(len(foundResults) == 0):
        print("No Athlete Found")
    else:
        print(f"{len(foundResults)} result(s) found:")
        print("")
        for chosenAthlete in foundResults:
            print(f"{chosenAthlete.name}'s stats and endorsments: ")
            chosenAthlete.printStats()
            chosenAthlete.printEndorsement()
            print("")
        print("")








# ------------------------------------ Getters, Setters and Variable Manipulation ------------------------------------

# Getter for filename
def getFilename():
    """Returns the File Name"""

    return __filename

# Setter for filename
def setFilename(newFile):
    """Updates the File Name stored"""
    global __filename
    __filename = newFile

# Getter for playerList
def getPlayerList():
    """Returns the list of athlete stored"""
    return __playerList

# Setter for playerList
def setPlayerList(newList):
    """Replaces the list of athlete stored with a new one"""
    global __playerList
    __playerList = newList

# Add an athlete to the list
def addToList(athlete):
    """Appends an athlete to the list of athletes"""
    global __playerList
    __playerList.append(athlete)

def printAll():
    """Prints all of the athlete stored in the list"""
    global __playerList
    sortedList = sorted( __playerList, key=lambda athlete: athlete.name)
    for item in sortedList:
        print(item.name)