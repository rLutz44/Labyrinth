import numpy as np

import random

from labyrinth_builder import labyrinth_builder


#--------Part of the Code to get out of the labyrinth---------

def canIGetOutOfLabyrinth(
        labyrinth_level_list : list,
        labyrinth_number_of_levels: int, 
        labyrinth_number_of_rows: int, 
        labyrinth_number_of_columns: int):
    """
    | Searching shortest path from start to exit with A* algorithm if it's possible
    
    """
    #create_labyrinth_node_grid(labyrinth_level_list)
    
    # LABYRINTH_START: int = 0
    # h_distance_from_node_to_exit = ((labyrinth_number_of_levels-1) 
    #                                                    + (labyrinth_number_of_rows-1) 
    #                                                    + (labyrinth_number_of_columns-1) 
    #                                                    + LABYRINTH_START)
    
    # #g_distance_start_to_node
    # f_priority_score: int = (h_distance_from_node_to_exit 
    #                     + g_distance_start_to_node) #the lower the score the higher the priority
    #bei start node ist f score = 0
    
class Node:
    """
    | Nodes are any places in the labyrinth you can visit with atleast 3 branches
    
    """
    def __init__(
           self, 
           labyrinth_level: int,
           labyrinth_row: int, 
           labyrinth_column: int, 
           labyrinth_dead_end: bool = False):
       
        self.labyrinth_level = labyrinth_level
        self.labyrinth_row = labyrinth_row
        self.labyrinth_column = labyrinth_column
        self.labyrinth_neighbors = []
        self.labyrinth_compound = "."
        self.labyrinth_dead_end = labyrinth_dead_end        # Dead_end when there is only 1 path to go or when the path has already been tested and resulted in a dead end
        
    def get_pos(self):
        return self.labyrinth_row, self.labyrinth_column
       
    def is_wall(self):
        return self.labyrinth_compound == "X"
    
    def is_air(self):
        return  self.labyrinth_air == "."
    
    def get_dead_end(self):
         return self.labyrinth_dead_end


def create_labyrinth_node_grid(labyrinth_level_list : list):
    
    












#------------------- Main ---------------------#

if (__name__ == "__main__"):
    
    print("Welcome to the Labyrinth Maker where you can create your own Labyrinth\nPls enter how many levels, rows and columns you want for your Labyrinth\nAllowed Numbers are integers from 0 to 30\n\n")
    
    while (True):
        labyrinth_number_of_levels = input("Pls enter the number of Levels for this Labyrinth.  \n")
        labyrinth_number_of_levels = int(labyrinth_number_of_levels)
        if (labyrinth_number_of_levels >= 0 and labyrinth_number_of_levels < 31):
            break
        print("Invalid Input, use integer from 0 to 30\n")
    
    while (True):
        labyrinth_number_of_rows = input("How many rows should it have?\n")
        labyrinth_number_of_rows = int(labyrinth_number_of_rows)
        if (labyrinth_number_of_levels >= 0 and labyrinth_number_of_levels < 31):
            break
        print("Invalid Input, use integer from 0 to 30\n")
    
    while (True):
        labyrinth_number_of_columns = input("How many columns do you want to have?\n")
        labyrinth_number_of_columns = int(labyrinth_number_of_columns)
        if (labyrinth_number_of_levels >= 0 and labyrinth_number_of_levels < 31):
            break
        print("Invalid Input, use integer from 0 to 30\n")
        
    
    labyrinth_level_list = labyrinth_builder(labyrinth_number_of_levels, labyrinth_number_of_rows, labyrinth_number_of_columns)
    # print("\n")
    # print(labyrinth_level_list[0])
    # print("\n")
    # print(labyrinth_level_list[1])
    
    canIGetOutOfLabyrinth(labyrinth_level_list, 
                          labyrinth_number_of_levels, 
                          labyrinth_number_of_rows, 
                          labyrinth_number_of_columns)
    