import numpy as np

import random



def labyrinth_builder(labyrinth_number_of_levels: int, 
                      labyrinth_number_of_rows: int, 
                      labyrinth_number_of_columns: int) -> str or list:
    """
    | Assemble all Levels into a single labyrinth and prints the whole labyrinth
    
    """
 
    labyrinth_level_list: list = []
    while(len(labyrinth_level_list) < labyrinth_number_of_levels):
        labyrinth_level: str = labyrinth_level_designer(labyrinth_number_of_rows, labyrinth_number_of_columns)
        labyrinth_level_list.append(labyrinth_level)
    
    labyrinth_level_list = labyrinth_set_start_and_exit(labyrinth_level_list, labyrinth_number_of_rows, labyrinth_number_of_columns)
    
    labyrinth_level_list_output(labyrinth_number_of_levels,
                                labyrinth_level_list)

    return labyrinth_level_list


def labyrinth_level_designer(labyrinth_number_of_rows: int, labyrinth_number_of_columns: int) -> str:
    """
    | Designing and Creating one level of the labyrinth
    
    """
    LABYRINTH_WALL: str             = "#"
    LABYRINTH_AIR: str              = "."
    LABYRINTH_COMPONENT_LIST: str   = [LABYRINTH_WALL, LABYRINTH_AIR]
    labyrinth_level: str            = np.chararray((labyrinth_number_of_rows, labyrinth_number_of_columns), unicode = True)    
    
    for labyrinth_row in range(labyrinth_number_of_rows):
        for labyrinth_column in range (labyrinth_number_of_columns):
            labyrinth_component: str                            = random.choice(LABYRINTH_COMPONENT_LIST)
            labyrinth_level [labyrinth_row] [labyrinth_column]  = labyrinth_component 
            
    return labyrinth_level


def labyrinth_set_start_and_exit(labyrinth_level_list: str, labyrinth_number_of_rows: int, labyrinth_number_of_columns: int) -> list:
    """
    | Sets the starting point and the exit for the labyrinth
    
    """
    LABYRINTH_START: str                = "S"
    LABYRINTH_EXIT: str                 = "E"    
    
    LABYRINTH_FIRST_LEVEL: int          = 0
    LABYRINTH_FIRST_INDEX_ROW: int      = 0
    LABYRINTH_FIRST_INDEX_COLUMN: int   = 0
    
    labyrinth_last_level: int           = len(labyrinth_level_list)-1
    labyrinth_last_index_row: int       = labyrinth_number_of_rows-1
    labyrinth_last_index_column: int    = labyrinth_number_of_columns-1

    labyrinth_level_list [LABYRINTH_FIRST_LEVEL] [LABYRINTH_FIRST_INDEX_ROW] [LABYRINTH_FIRST_INDEX_COLUMN] = LABYRINTH_START
    labyrinth_level_list [labyrinth_last_level] [labyrinth_last_index_row] [labyrinth_last_index_column]    = LABYRINTH_EXIT

    return labyrinth_level_list


def labyrinth_level_list_output(labyrinth_number_of_levels: int, labyrinth_level_list: list):
    """
    | Print the labyrinth on the console 
    
    """
    
    for labyrinth_level in range(labyrinth_number_of_levels):
        print("\n")
        print(labyrinth_level_list[labyrinth_level])
