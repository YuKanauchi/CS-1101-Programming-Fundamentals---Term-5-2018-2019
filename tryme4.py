#This function prints out a new_line
def new_line():
    print('.')

#This function prints out three_lines by calling new_line()
def three_lines():

    new_line()

    new_line()

    new_line()

#This function prints out nine_lines by calling three_lines()
def nine_lines():
    three_lines()
    three_lines()
    three_lines()
    
#This function prints out clear_screen lines by calling nine_lines()
def clear_screen():
    new_line()
    three_lines()
    three_lines()
    nine_lines()
    nine_lines()
    
print("Printing nine lines" )    
nine_lines()

print("\nCalling clearScreen()")
clear_screen()