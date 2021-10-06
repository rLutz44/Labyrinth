from labyrinth_builder import labyrinth_builder

from labyrinth_solver import can_I_get_out_of_labyrinth


def check_input(user_input: int):
    return (user_input >=0 and user_input < 31)



if (__name__ == "__main__"):
    
    print("\nWelcome to the Labyrinth Maker where you can create your own Labyrinth\n"
           + "Pls enter how many levels, rows and columns you want for your Labyrinth\n"
           + "Allowed Numbers are integers from 0 to 30\n\n")
    
    invalid_input: str = "Invalid Input, use integer from 0 to 30\n"
    
    while(True):
        try:
            while (True):
                labyrinth_number_of_levels = input("Pls enter the number of Levels for this Labyrinth.  \n")
                labyrinth_number_of_levels = int(labyrinth_number_of_levels)
                if (check_input(labyrinth_number_of_levels)):
                    break
                print(invalid_input)
            
            while (True):
                labyrinth_number_of_rows = input("How many rows should it have?\n")
                labyrinth_number_of_rows = int(labyrinth_number_of_rows)
                if (check_input(labyrinth_number_of_rows)):
                    break
                print(invalid_input)
            
            while (True):
                labyrinth_number_of_columns = input("How many columns do you want to have?\n")
                labyrinth_number_of_columns = int(labyrinth_number_of_columns)
                if (check_input(labyrinth_number_of_columns)):
                    break
                print(invalid_input)
                
            if(labyrinth_number_of_levels == 0 and labyrinth_number_of_rows == 0 and labyrinth_number_of_columns == 0):   
                print("\n0 0 0")
                break
            
            if(labyrinth_number_of_levels == 0 or labyrinth_number_of_rows == 0 or labyrinth_number_of_columns == 0):
                print("\nOnly use 0 for all 3 inputs or none of them, pls try again\n")
                continue
            
            if(labyrinth_number_of_rows + labyrinth_number_of_columns < 3):
                print ("\nThe sum of labyrinth rows and columns should not be less than 3, pls try again")
                continue
            
            
            
            labyrinth_level_list = labyrinth_builder(labyrinth_number_of_levels, 
                                                     labyrinth_number_of_rows, 
                                                     labyrinth_number_of_columns)
            
            can_I_get_out_of_labyrinth(labyrinth_level_list, 
                                       labyrinth_number_of_levels, 
                                       labyrinth_number_of_rows, 
                                       labyrinth_number_of_columns)
      
        except(ValueError, TypeError):   
            print("\nPls only use Numbers as input and try again")