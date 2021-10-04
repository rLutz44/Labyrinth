import numpy as np

#import random

from labyrinth_builder import labyrinth_builder


#--------Part of the Code to get out of the labyrinth---------
class Node:
    """
    | Nodes are any places in the labyrinth you can visit (in this case "." air)
    
    """
    def __init__(
           self, 
           level: int,
           row: int, 
           column: int,
           total_levels: int,
           total_rows: int,
           total_columns: int,
           compound: str):
       
        self.level: int = level     #z
        self.row: int = row         #y
        self.column: int = column   #x
        self.total_levels: int = total_levels
        self.total_rows: int = total_rows
        self.total_columns: int = total_columns
        self.compound: str = compound
        self.neighbors: list = []

    
    def is_wall(self):
        return self.compound == "X"
    
    def is_air(self):
        return  self.compound == "."
    
    def update_neighbors(self, labyrinth_node_grid): #level implementation missing
        """
        |Every instance of Node has a list, consisting of another instances 
         right next to them (north, east, south, west, up, down).
         This method checks if they are visitable (air) and includes them 
         in this list.
        
        """
        self.neighbors = []
        
        if ((self.level < self.total_levels-1) and (labyrinth_node_grid[self.level + 1][self.row][self.column].is_air())): #UP
            self.neighbors.append(labyrinth_node_grid[self.level + 1][self.row][self.column])
            
        if ((self.level > 0) and (labyrinth_node_grid[self.level - 1][self.row][self.column].is_air())): #DOWN
            self.neighbors.append(labyrinth_node_grid[self.level - 1][self.row][self.column])
        
        if ((self.row < self.total_rows-1) and (labyrinth_node_grid[self.level][self.row + 1][self.column].is_air())): #SOUTH
            self.neighbors.append(labyrinth_node_grid[self.level][self.row + 1][self.column])
            
        if ((self.row > 0) and (labyrinth_node_grid[self.level][self.row - 1][self.column].is_air())): #NORTH
            self.neighbors.append(labyrinth_node_grid[self.level][self.row - 1][self.column])
            
        if ((self.column < self.total_columns-1) and (labyrinth_node_grid[self.level][self.row][self.column + 1].is_air())): #EAST
            self.neighbors.append(labyrinth_node_grid[self.level][self.row][self.column + 1])
            
        if ((self.column > 0) and (labyrinth_node_grid[self.level][self.row][self.column - 1].is_air())): #WEST
            self.neighbors.append(labyrinth_node_grid[self.level][self.row][self.column - 1])
    

    
    
def canIGetOutOfLabyrinth(
        labyrinth_level_list : list,
        labyrinth_number_of_levels: int, 
        labyrinth_number_of_rows: int, 
        labyrinth_number_of_columns: int):
    """
    | Searching shortest path from start to exit with A* algorithm if it's possible
    
    """
    labyrinth_node_grid: list = create_labyrinth_node_grid(labyrinth_level_list,
                                                           labyrinth_number_of_levels, 
                                                           labyrinth_number_of_rows, 
                                                           labyrinth_number_of_columns)
    
    LABYRINTH_START_LEVEL: int = 0
    LABYRINTH_START_ROW: int = 0
    LABYRINTH_START_COLUMN: int = 0
    
    labyrinth_exit_level: int = (labyrinth_number_of_levels - 1)
    labyrinth_exit_row: int = (labyrinth_number_of_rows - 1)
    labyrinth_exit_column: int = (labyrinth_number_of_columns - 1)
    
    distance_node_to_exit: int = calculate_distance_node_to_exit(labyrinth_node_grid[LABYRINTH_START_LEVEL][LABYRINTH_START_ROW][LABYRINTH_START_COLUMN],
                                                                 labyrinth_node_grid[labyrinth_exit_level][labyrinth_exit_row][labyrinth_exit_column])
    
    labyrinth_node_grid = update_neighbor_of_every_node(labyrinth_node_grid,
                                                        labyrinth_number_of_levels, 
                                                        labyrinth_number_of_rows, 
                                                        labyrinth_number_of_columns)
   # test1 = labyrinth_node_grid[0][0][0].neighbors
    #test2 = labyrinth_node_grid[0][0][1].neighbors
    # LABYRINTH_START: int = 0
    # h_distance_from_node_to_exit = ((labyrinth_number_of_levels-1) 
    #                                                    + (labyrinth_number_of_rows-1) 
    #                                                    + (labyrinth_number_of_columns-1) 
    #                                                    + LABYRINTH_START)
    
    # #g_distance_start_to_node
    # f_priority_score: int = (h_distance_from_node_to_exit 
    #                     + g_distance_start_to_node) #the lower the score the higher the priority
    #bei start node ist f score = 0
    

    
    

def create_labyrinth_node_grid(labyrinth_level_list : list,
                               labyrinth_number_of_levels: int, 
                               labyrinth_number_of_rows: int, 
                               labyrinth_number_of_columns: int) -> list:
    """
    | Creating numpy array that contains in each element a instance from node, representing the labyrinth
    
    """
    labyrinth_node_grid = ([ [ [ [] for column in range(labyrinth_number_of_columns)] for row in range(labyrinth_number_of_rows)] for level in range(labyrinth_number_of_levels)])
    
    for level in range (labyrinth_number_of_levels):
        for row in range(labyrinth_number_of_rows):
            for column in range(labyrinth_number_of_columns):
                labyrinth_node_grid[level][row][column] = Node(level, 
                                                               row, 
                                                               column, 
                                                               labyrinth_number_of_levels,
                                                               labyrinth_number_of_rows,
                                                               labyrinth_number_of_columns,
                                                               labyrinth_level_list[level][row][column])
    
    return labyrinth_node_grid




def calculate_distance_node_to_exit(labyrinth_node: Node, 
                                    labyrinth_exit: Node) -> int:
    """
    |Returns the quickest possible route from the current note to the exit of the labyrinth 
     without considering if the path is blocked by a wall (manhattan distance)
    
    """
    level_start = labyrinth_node.level
    row_node =  labyrinth_node.row
    column_node = labyrinth_node.column
    
    level_exit = labyrinth_exit.level
    row_exit = labyrinth_exit.column
    column_exit = labyrinth_exit.column

    return abs(level_start - level_exit) + abs(row_node-row_exit) + abs(column_node-column_exit) #abs = absolute



def update_neighbor_of_every_node(labyrinth_node_grid: list,
                                  labyrinth_number_of_levels: int, 
                                  labyrinth_number_of_rows: int, 
                                  labyrinth_number_of_columns: int) -> np:
    """
    | updates the neighbor attribute for every node in the node_grid

    """
    #test=labyrinth_node_grid[0][0][0].compound
    #labyrinth_node_grid[0][0][0].update_neighbors(labyrinth_node_grid)
    for level in range (labyrinth_number_of_levels):
        for row in range(labyrinth_number_of_rows):
            for column in range(labyrinth_number_of_columns):
                labyrinth_node_grid[level][row][column].update_neighbors(labyrinth_node_grid)
    
    return labyrinth_node_grid



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
        
    
    labyrinth_level_list = labyrinth_builder(labyrinth_number_of_levels, 
                                             labyrinth_number_of_rows, 
                                             labyrinth_number_of_columns)
    
    canIGetOutOfLabyrinth(labyrinth_level_list, 
                          labyrinth_number_of_levels, 
                          labyrinth_number_of_rows, 
                          labyrinth_number_of_columns)
    