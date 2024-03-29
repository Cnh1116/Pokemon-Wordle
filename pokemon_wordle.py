from tkinter import *
import random


# Target Name Rules: Character Length < 10, No Spaces, No Hyphens

names_file_path = r'C:\Users\cholland\OneDrive - Advanced Micro Devices Inc\Desktop\C0DE\My Python Files\Pokemon Wordle\pokemon-names.txt'

#Methods() ...
def Draw_Initial_Grid():
    list_of_cell_rows = []
    
    for iterator_row in range(number_of_guesses):
        list_of_cells = []
        for iterator_column in range(characters_in_word):
            start_x = iterator_column * scale_factor
            start_y = iterator_row * scale_factor
            list_of_cells.append(canvas_object.create_rectangle(start_x, start_y, start_x + scale_factor, start_y + scale_factor, fill = 'gray', outline = 'black'))
        list_of_cell_rows.append(list_of_cells)
    return(list_of_cell_rows)

def Draw_Text_On_Row(word_entered, row_number):
    Draw_Text_On_Row.counter += 1 #Every time this method is called, implies a guess
    if Draw_Text_On_Row.counter == number_of_guesses: #If counter > guesses allowed, game ends
        print(f'Guesses EXCEEDED. Lost..., the Pokemon was: {target_word}')
    else:   
        for iterator in range(characters_in_word):
            canvas_object.create_text((iterator*scale_factor + (int(scale_factor/2))), (row_number*scale_factor + (int(scale_factor/2))), font = 'Purisa', text = word_entered[iterator])
            
            if word_entered[iterator].upper() == target_word[iterator].upper():
                canvas_object.itemconfig(cells[Draw_Text_On_Row.counter-1][iterator], fill='green')
            elif word_entered[iterator].upper() in target_word.upper():
                canvas_object.itemconfig(cells[Draw_Text_On_Row.counter-1][iterator], fill='yellow')

def Get_Entry_Text():
    word_entered = entry_box.get()
    if Is_Valid_Entry(word_entered):
        print(f'WORD Entered: {word_entered}')
        Draw_Text_On_Row(word_entered, Draw_Text_On_Row.counter)
    if word_entered.upper() == target_word:
        print('========  You Win  ==========')

def Get_Names():
    with open(names_file_path) as fin:
        names = fin.readlines()
        for iterator in range(len(names)):
            names[iterator] = names[iterator].strip()
            names[iterator] = names[iterator].upper()
        return(names)
    
def Get_Target_Name(names):
        while True:
            target_name = names[random.randint(0, len(names)-1)].strip()
            if " "  not in target_name and '-' not in target_name and len(target_name) < 10:
                return target_name
        
def Is_Valid_Entry(word_entered):
    if ((word_entered.upper() not in Get_Names()) and (len(word_entered) != characters_in_word)):
        print(f'Word entered is both NOT a Pokemon and not {characters_in_word} characters long.')
        return False
    elif ((len(word_entered) != characters_in_word)):
        print(f'ERROR: Word Entered is not {characters_in_word} characters long.')
        return False
    elif((word_entered.upper() not in Get_Names())):
        print(f'ERROR: Word Entered is not a Pokemon')
        return False
    else:
        return True

#Target Word
target_word = Get_Target_Name(Get_Names())

#Parameters
scale_factor = 43
characters_in_word = len(target_word)
number_of_guesses = 6
screen_width = scale_factor * characters_in_word
screen_height = scale_factor * number_of_guesses
text_entry_box_pixel_height = 20

#Foundational Pieces
root = Tk()
root.resizable(width=False, height=False)
root.title("Pokemon - Wordle by Venizz")
root.geometry(f'{screen_width}x{screen_height + text_entry_box_pixel_height}')
canvas_object = Canvas(root, width = screen_width, height = screen_height)
canvas_object.pack()

#Returns a list of the cell objects so we can call them later to recolor
cells = Draw_Initial_Grid()

#Draw Entry Box
entry_box = Entry(root, width=(int(scale_factor*0.3)), background = 'blue')
entry_box.place(x = 0, y = screen_height)

#Draw Button
enter_button = Button(root, text = 'Enter HERE', command = Get_Entry_Text, width = int(screen_width/5), background = 'orange')
enter_button.place(x = int(screen_width * 0.7), y = screen_height)

Draw_Text_On_Row.counter = 0

root.mainloop()