import numpy as np
import random

def labyrinthBuilder(labyrinthNumberOfLevels, labyrinthNumberOfRows, labyrinthNumberOfColumns):
 
    if(labyrinthNumberOfLevels == 0 and labyrinthNumberOfRows == 0 and labyrinthNumberOfColumns == 0):   
        return "0 0 0"
    if(labyrinthNumberOfLevels == 0 or labyrinthNumberOfRows == 0 or labyrinthNumberOfColumns == 0):
        return "Only use 0 for all 3 inputs or none of them, pls try again\n"
    if(labyrinthNumberOfRows + labyrinthNumberOfColumns < 3):
        return "The sum of labyrinth rows and columns should not be less than 3, pls try again"
 
    labyrinthLevelList = []
    while(len(labyrinthLevelList) < labyrinthNumberOfLevels):
        labyrinthLevel = labyrinthLevelDesigner(labyrinthNumberOfRows, labyrinthNumberOfColumns)
        labyrinthLevelList.append(labyrinthLevel)
    
    labyrinthLevelList = labyrinthSetStartAndExit(labyrinthLevelList, labyrinthNumberOfRows, labyrinthNumberOfColumns)
    
    print("\n")
    print(labyrinthLevelList[0])
    print("\n")
    print(labyrinthLevelList[1])



def labyrinthLevelDesigner(labyrinthNumberOfRows, labyrinthNumberOfColumns):
    
    labyrinthWall = "#"
    labyrinthAir = "."
    labyrinthLevel = np.chararray((labyrinthNumberOfRows, labyrinthNumberOfColumns), unicode = True)    

    labyrinthComponentList = [labyrinthWall, labyrinthAir]
    
    for labyrinthRow in range(labyrinthNumberOfRows):
        for labyrinthColumn in range (labyrinthNumberOfColumns):
            labyrinthComponent = random.choice(labyrinthComponentList)
            labyrinthLevel[labyrinthRow][labyrinthColumn] = labyrinthComponent 
            
    return labyrinthLevel


def labyrinthSetStartAndExit(labyrinthLevelList, labyrinthNumberOfRows, labyrinthNumberOfColumns):
    
    labyrinthStart = "S"
    labyrinthExit = "E"    
    
    labyrinthLevelFirst = 0
    labyrinthRowFirstIdx = 0
    labyrinthColumnFirstIdx = 0
    
    labyrinthLevelLast = len(labyrinthLevelList)-1
    labyrinthRowLastIdx = labyrinthNumberOfRows-1
    labyrinthColumnLastIdx = labyrinthNumberOfColumns-1

    labyrinthLevelList[labyrinthLevelFirst][labyrinthRowFirstIdx][labyrinthColumnFirstIdx] = labyrinthStart
    labyrinthLevelList[labyrinthLevelLast][labyrinthRowLastIdx][labyrinthColumnLastIdx] = labyrinthExit

    return labyrinthLevelList

#def canIGetOut():


#------------------- Main ---------------------#

print("Welcome to the Labyrinth Maker where you can create your own Labyrinth\nPls enter how many levels, rows and columns you want for your Labyrinth\nAllowed Numbers are integers from 0 to 30\n\n")

while (True):
    labyrinthNumberOfLevels = input("Pls enter the number of Levels for this Labyrinth.  \n")
    labyrinthNumberOfLevels = int(labyrinthNumberOfLevels)
    if (labyrinthNumberOfLevels >= 0 and labyrinthNumberOfLevels < 31):
        break
    print("Invalid Input, use integer from 0 to 30\n")

while (True):
    labyrinthNumberOfRows = input("How many rows should it have?\n")
    labyrinthNumberOfRows = int(labyrinthNumberOfRows)
    if (labyrinthNumberOfLevels >= 0 and labyrinthNumberOfLevels < 31):
        break
    print("Invalid Input, use integer from 0 to 30\n")

while (True):
    labyrinthNumberOfColumns = input("How many columns do you want to have?\n")
    labyrinthNumberOfColumns = int(labyrinthNumberOfColumns)
    if (labyrinthNumberOfLevels >= 0 and labyrinthNumberOfLevels < 31):
        break
    print("Invalid Input, use integer from 0 to 30\n")
    
#print(labyrinthNumberOfLevels)
#print(labyrinthNumberOfRows)
#print(labyrinthNumberOfColumns)

labyrinthBuilder(labyrinthNumberOfLevels, labyrinthNumberOfRows, labyrinthNumberOfColumns)