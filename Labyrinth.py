import numpy as np

from queue import PriorityQueue

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
        return  (self.compound == "." or self.compound == "E")
    
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
    
    labyrinth_node_grid = update_neighbor_for_every_node(labyrinth_node_grid,
                                                        labyrinth_number_of_levels, 
                                                        labyrinth_number_of_rows, 
                                                        labyrinth_number_of_columns)
   
    calculate_shortest_path_to_exit(labyrinth_node_grid,
                                    labyrinth_node_grid[LABYRINTH_START_LEVEL][LABYRINTH_START_ROW][LABYRINTH_START_COLUMN],
                                    labyrinth_node_grid[labyrinth_exit_level][labyrinth_exit_row][labyrinth_exit_column])
    
    
    

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



def update_neighbor_for_every_node(labyrinth_node_grid: list,
                                  labyrinth_number_of_levels: int, 
                                  labyrinth_number_of_rows: int, 
                                  labyrinth_number_of_columns: int) -> np:
    """
    | updates the neighbor attribute for every node in the node_grid

    """

    for level in range (labyrinth_number_of_levels):
        for row in range(labyrinth_number_of_rows):
            for column in range(labyrinth_number_of_columns):
                labyrinth_node_grid[level][row][column].update_neighbors(labyrinth_node_grid)
    
    return labyrinth_node_grid



def calculate_shortest_path_to_exit(labyrinth_node_grid: list,
                                    start_node: Node,
                                    exit_node: Node) -> str:
    """
    | Use the A*star algorithm to calculate the shortest path from start to exit

    """
    count = 0 #tiebreaker if multiple priority scores have the same value it should take the score with the lowest count
    path_length: int = 0
    open_set = PriorityQueue()  #from queue library
    open_set.put((0, count, start_node)) #f_score, count, node. contains every node that hasn't been cheked if it's neighbors are closer to exit
    came_from = {} # previous nodes from open_set
    distance_start_to_node = {node: float("inf") for level in labyrinth_node_grid for row in level for node in row} #g_score
    distance_start_to_node[start_node] = 0 #g_score for start
    priority_score = {node: float('inf') for level in labyrinth_node_grid for row in level for node in row} #f_score
    priority_score[start_node] = calculate_distance_node_to_exit(start_node, exit_node) #f_score = h_score for start

    open_set_hash = {start_node} #same as open_set but we can look into it, cotains nodes we havent visited yet
    
    while not open_set.empty(): #runs until open_set is empty --> there is no path from start to exit
        current_node = open_set.get()[2] #node with highest priority becomes current_node
        open_set_hash.remove(current_node) #delete node from set that we are currently exploring

        if current_node == exit_node: #if shortest route has been found
            while current_node in came_from:
                current_node = came_from[current_node]
                path_length += 1
        
            print("Ausbruch in",str(path_length),"Minuten")
            return True

        for neighbor in current_node.neighbors:
            temp_distance_start_to_node: int = distance_start_to_node[current_node] + 1 #steps are 1 Unit. make 1 step from current note
            
            if temp_distance_start_to_node < distance_start_to_node[neighbor]: #checks if current_node is closer to start than it's current neighbor
                came_from[neighbor] = current_node #Neighbor comes from current_node. this information will be put in a dictionary
                distance_start_to_node[neighbor] = temp_distance_start_to_node #noting distance from start to neighbor in dict
                priority_score[neighbor] = temp_distance_start_to_node + calculate_distance_node_to_exit(neighbor, exit_node) #the lower the priority_score the higher the priority
                
                if neighbor not in open_set_hash:
                    count += 1 #is also considered in priority
                    open_set.put((priority_score[neighbor], count, neighbor)) #save neighbor in set
                    open_set_hash.add(neighbor) #into hash too
                    #neighbor.make_open()

      #if current_node != start_node:
         #current_node.make_closed()

    return print("Gefangen :(")
        

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
    