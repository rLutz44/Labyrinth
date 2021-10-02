import numpy as np

# def labyrinthBuilder(labyrinthLevels, labyrinthRows, labyrinthColumns):
    
#     if (labyrinthlevels)
    
#     labyrinthStart = "S"
#     labyrinthExit = "E"
#     labyrinthWall = "#"
#     labyrinthAir = "."
    

#def inputValidation(userInput):
    




#------------------- Main ---------------------#

print("Welcome to the Labyrinth Maker where you can create your own Labyrinth\nPls enter how many levels, rows and columns you want for your Labyrinth\nAllowed Numbers are integers from 0 to 30\n\n")

while (True):
    labyrinthLevels = input("Pls enter the number of Levels for this Labyrinth.  \n")
    labyrinthLevels = int(labyrinthLevels)
    if (labyrinthLevels >= 0 and labyrinthLevels < 31):
        break
    print("Invalid Input, use integer from 0 to 30\n")

while (True):
    labyrinthRows = input("How many rows should it have?\n")
    labyrinthRows = int(labyrinthRows)
    if (labyrinthLevels >= 0 and labyrinthLevels < 31):
        break
    print("Invalid Input, use integer from 0 to 30\n")

while (True):
    labyrinthColumns = input("How many columns do you want to have?\n")
    labyrinthColumns = int(labyrinthColumns)
    if (labyrinthLevels >= 0 and labyrinthLevels < 31):
        break
    print("Invalid Input, use integer from 0 to 30\n")
    
print(labyrinthLevels)
print(labyrinthRows)
print(labyrinthColumns)
#labyrinthBuilder(labyrinthLevels, labyrinthRows, labyrinthColumns)