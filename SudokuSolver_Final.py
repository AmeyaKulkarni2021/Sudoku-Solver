###############################################################################################################################################
###############################################################################################################################################
# 1. Importing libraries
###############################################################################################################################################
###############################################################################################################################################

import numpy as np
import tkinter as tk
from tkinter import Button
from tkinter import Label
from tkinter import Frame
from tkinter import ttk

###############################################################################################################################################
###############################################################################################################################################
# 2. Setting up global variables
###############################################################################################################################################
###############################################################################################################################################

base = np.zeros([9,9],dtype=int)
layers = np.zeros([9,9,9],dtype=int)
box_value = np.zeros([9,9,2],dtype=float)
entries = []


###############################################################################################################################################
###############################################################################################################################################
# 3. Main Menu
###############################################################################################################################################
###############################################################################################################################################

# creating the main window for hosting the GUI of the solver program
window_main = tk.Tk()
    
window_main.title("Sudoku Solver")

window_main.resizable(True, True)
window_main.geometry("200x200")
window_main.configure(background = 'gray74')

# creating frame to host the main menu
frame_main_menu = Frame(window_main, height = 250, width = 250, bg = 'gray74')
frame_main_menu.grid(row = 0, column = 0)

Label(frame_main_menu, text = "Main Menu", font = ('Arial', 15), bg = 'gray74').grid(row = 0, column = 0, padx = 25, pady = 5)

button_capture_input = Button(frame_main_menu, text = "Manual Input", height = 1, width = 20, command = lambda: manual_input(base))
button_capture_input.grid(row = 1, column = 0, padx = 25, pady = 10)
    
button_run_solver = Button(frame_main_menu, text = "Sudoku Solver", height = 1, width = 20, command = lambda: solver(base, layers, box_value))
button_run_solver.grid(row = 2, column = 0, padx = 25, pady = 10)

button_exit = Button(frame_main_menu, text = "Exit", height = 1, width = 20, command = lambda: exit_all())
button_exit.grid(row = 3, column = 0, padx = 25, pady = 10)

# function to exit the solver program
def exit_all():
    
    window_main.destroy()
    
    return

# function to display grid that will be used in the solver
def show_grid(base, base_og, frame):
    
    show_input_var = 0
    entires_display = []
    
    # 1,2,3,5,6,7,9,10,11
    # 0,1,2,3,4,5,6,7,8
    
    for i in range(13):
        for j in range(13):
            if i in [0,4,8,12]:
                ttk.Separator(frame, orient='horizontal').grid(column=j, row=i, pady = 1)
            else:
                if j in [0,4,8,12]:
                   ttk.Separator(frame, orient='vertical').grid(column=j, row=i, padx = 1)
                else:
                    entires_display.append(show_input_var)
                    
                    a,b = 0,0
                    
                    if i in [1,2,3]:
                        a = i - 1
                    elif i in [5,6,7]:
                        a = i - 2
                    else:
                        a = i - 3
                    
                    if j in [1,2,3]:
                        b = j - 1
                    elif j in [5,6,7]:
                        b = j - 2
                    else:
                        b = j - 3
                    
                    if base[a][b] > 0 and base[a][b] == base_og[a][b]:
                        entires_display[show_input_var] = Label(frame, text = str(base[a][b]), bd = 0, bg = 'yellow green', width = 4, justify = 'center')
                    elif base[a][b] > 0 and base[a][b] != base_og[a][b]:
                        entires_display[show_input_var] = Label(frame, text = str(base[a][b]), bd = 0, bg = 'lime green', width = 4, justify = 'center')
                    else:
                        entires_display[show_input_var] = tk.Entry(frame, width = 5, justify = 'center')
                    
                    entires_display[show_input_var].grid(row = i, column = j)
                    
                    show_input_var = show_input_var + 1
                    
                    if show_input_var == 81:
                        break
    
    return

###############################################################################################################################################
###############################################################################################################################################
# 4. Manual Inputs
###############################################################################################################################################
###############################################################################################################################################

# function to receive inputs from user
def manual_input(base):
    
    # function to remove all users entries
    def clear_input_space(frame):
        
        frame.destroy()
        manual_input(base)
        return
    
    # function to exit manual input frame
    def exit_manual_input(frame):
        
        frame.destroy()
        window_main.geometry("200x200")
        return
    
    # function to store user inputs
    def store_value(base, frame):
    
        base_temp = np.zeros([9,9], dtype = int)
        
        for i in range(9):
            for j in range(9):
                base[i][j] = 0
        
        # function to check if there are any contradictions in user inputs
        def input_checker(user_inputs):
            
            for i in range(9):
                for j in range(9):
                    
                    count_r, count_c, count_b = 0,0,0
                    
                    if user_inputs[i][j] > 0:
                        
                        for k in range(9):
                            
                            if user_inputs[i][j] == user_inputs[i][k] and j != k:
                                count_r += 1
                                
                            if user_inputs[i][j] == user_inputs[k][j] and i != k:
                                count_c += 1
                        
                        a,b = i+1,j+1
                        
                        while a%3 != 0:
                            a += 1
                        
                        while b%3 != 0:
                            b += 1
                            
                        for x in range(a-3,a):
                            for y in range(b-3,b):
                                
                                if user_inputs[i][j] == user_inputs[x][y] and [i,j] != [x,y]:
                                    count_b += 1
                        
                        if count_r > 0 or count_c > 0 or count_b > 0:
                            return False
            
            return True
                
        # storing user inputs
        store_value_var = 0
        
        for i in range(9):
            for j in range(9):
                
                try:
                    user_entry = int(entries[store_value_var].get())
                except:
                    user_entry = ''
                
                if user_entry == ' ' or user_entry == '':
                    base_temp[i][j] = 0 
                elif user_entry in [0,1,2,3,4,5,6,7,8,9]:
                    base_temp[i][j] = user_entry
                else:
                    base_temp[i][j] = 0
                
                entries[store_value_var].delete(0, 'end')
                if base_temp[i][j] == 0:
                    entries[store_value_var].insert(0, "")
                else:
                    entries[store_value_var].insert(0, str(base_temp[i][j]))
                
                store_value_var = store_value_var + 1
                
                if store_value_var == 81:
                    break
        
        if input_checker(base_temp):
            
            for i in range(9):
                for j in range(9):
                    base[i][j] = base_temp[i][j]
            
            # removing any previous labels
            frame_children = frame.winfo_children()
            
            for element in frame_children:
                if element.winfo_class() == 'Label':
                    element.destroy()
            
            Label(frame, text = "Valid inputs. Proceed with Solver", bg = 'gray48', fg = 'white', justify = 'center').grid(row = 13, column = 0, columnspan = 13)
        
        else:
            Label(frame, text = "Conflict in inputs provided!", bg = 'gray48', fg = 'white', justify = 'center').grid(row = 13, column = 0, columnspan = 13)
        
        return
    
    # function to setup predefined sudoku
    def hardest_puzzle():
        
        h_puzzle = [[0,8],
                    [11,3],
                    [12,6],
                    [19,7],
                    [22,9],
                    [24,2],
                    [28,5],
                    [32,7],
                    [40,4],
                    [41,5],
                    [42,7],
                    [48,1],
                    [52,3],
                    [56,1],
                    [61,6],
                    [62,8],
                    [65,8],
                    [66,5],
                    [70,1],
                    [73,9],
                    [78,4]]
        
        for value in h_puzzle:
            entries[value[0]].insert(0,str(value[1]))
        
        return
    
    # deleting any existing frames to prevent overlap
    frames = window_main.winfo_children()
    
    if len(frames) > 1:
        frames[1].destroy()
    
    # resizing the main window to accomodate the input space
    window_main.geometry("600x400")
    
    # creating new frame to host input space
    frame_manual_input = Frame(window_main, height = 750, width = 500, bg = 'gray74')
    frame_manual_input.grid(row=0, column = 1)
    
    Label(frame_manual_input, text = "Manual Input", font = ('Arial', 10), bg = 'gray74').grid(row = 0, column = 1, padx = 10, pady = 10)
    
    frame_entries = Frame(frame_manual_input, height = 270, width = 270, bg = 'gray48')
    frame_entries.grid(row = 1, column = 1, padx = 10, pady = 10)
    
    capture_input_var = 0
    entries = []
    

    for i in range(13):
        for j in range(13):
            
            if i in [0,4,8,12]:
                ttk.Separator(frame_entries, orient='horizontal').grid(column=j, row=i, pady = 1)
            else:
                if j in [0,4,8,12]:
                   ttk.Separator(frame_entries, orient='vertical').grid(column=j, row=i, padx = 1)
                else:
                    entries.append(capture_input_var)
                    entries[capture_input_var] = tk.Entry(frame_entries, width = 5, justify ='center')
                    entries[capture_input_var].grid(row = i, column = j)
                    capture_input_var = capture_input_var + 1
                    
                    if capture_input_var == 81:
                        break
    
    frame_options = Frame(frame_manual_input, height = 100, width = 500, bg = 'gray74')
    frame_options.grid(row= 2, column = 1, padx = 10, pady = 10)
    
    button_store = Button(frame_options, text = 'Store', height = 1, width = 20, command = lambda: store_value(base, frame_entries))
    button_store.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    button_hardest_puzzle = Button(frame_options, text = 'Hardest Puzzle', height = 1, width = 20, command = lambda: hardest_puzzle())
    button_hardest_puzzle.grid(row = 0, column = 1, padx = 10, pady = 10)
    
    button_clear = Button(frame_options, text = 'Clear', height = 1, width = 20, command = lambda: clear_input_space(frame_entries))
    button_clear.grid(row = 1, column = 0, padx = 10, pady = 10)
    
    button_exit_manual_input = Button(frame_options, text = 'Exit', height = 1, width = 20, command = lambda: exit_manual_input(frame_manual_input))
    button_exit_manual_input.grid(row = 1, column = 1, padx = 10, pady = 10)
    
    return

###############################################################################################################################################
###############################################################################################################################################
# 5. Sudoku Solver
###############################################################################################################################################
###############################################################################################################################################

# creating main view for solver
def solver(base, layers, box_value):
    
    # function to exit solver frame
    def clear_solver_view(frame):
        
        frame.destroy()
        window_main.geometry("200x200")
        
        return
    
    # cleaning layers and box_value
    for i in range(9):
        for j in range(9):
            for k in range(9):
                layers[i][j][k] = 0
            
            box_value[i][j][0] = 0.0
            box_value[i][j][1] = 0.0
    
    # deleting any existing frames to prevent overlap
    frames = window_main.winfo_children()
    
    if len(frames) > 1:
        frames[1].destroy()
    
    # resizing the main window to accomodate the input space
    window_main.geometry("600x450")
    
    # creating new frame to host input space
    frame_solver = Frame(window_main, height = 750, width = 500, bg = 'gray74')
    frame_solver.grid(row=0, column = 1)
    
    Label(frame_solver, text = "Solver", font = ('Arial', 10), bg = 'gray74').grid(row = 0, column = 1, padx = 10, pady = 10)
    
    frame_display = Frame(frame_solver, height = 270, width = 270, bg = 'gray48')
    frame_display.grid(row = 1, column = 1, padx = 10, pady = 10)
    
    show_grid(base, base, frame_display)

    button_basic_solver = Button(frame_solver, text = 'Basic Solver',  height = 1, width = 20, command = lambda: run_solver(base, layers, box_value, frame_solver))
    button_basic_solver.grid(row = 2, column = 1, padx = 10, pady = 10)
    
    button_PPS = Button(frame_solver, text = 'PPS Approach',  height = 1, width = 20, command = lambda: PPSRun(base, layers, box_value, frame_solver))
    button_PPS.grid(row = 3, column = 1, padx = 10, pady = 10)
    
    button_exit_solver = Button(frame_solver, text = 'Exit',  height = 1, width = 20, command = lambda: clear_solver_view(frame_solver))
    button_exit_solver.grid(row = 4, column = 1, padx = 10, pady = 10)
    
    return

###############################################################################################################################################
# 5.1. Basic Sudoku Solver
###############################################################################################################################################

# function for basic solver
def run_solver(base, layers, box_value, frame_main):
    
    base_og = base.copy()
    
    blanks = blankCounter(layers)
   
    while blanks > 0:
        
        solver_layer_updater(base, layers)
        solver_row_column_check(layers)
        solver_box_check(layers)
        solver_comp_box(layers)
        matches_updates(layers,box_value)
        matches(layers, box_value)
        naked_single(base, layers)
        
        blankCheck = blankCounter(layers)
        
        if blankCheck == 0:

            print(base)
            
            frames = frame_main.winfo_children()
            
            for element in frames:
                if element.winfo_class() == 'Frame':
                    element.destroy()
            
            frame_display = Frame(frame_main, height = 270, width = 270, bg = 'gray48')
            frame_display.grid(row = 1, column = 1, padx = 10, pady = 10)
    
            show_grid(base, base_og, frame_display)
            Label(frame_display, text = "Sudoku Complete", bg = 'gray48', fg = 'white', justify = 'center').grid(row = 13, column = 0, columnspan = 9)
            
            return
            
        elif blanks == blankCheck:

            print("Blanks = ",blankCheck)
            print(base)

            frames = frame_main.winfo_children()
            
            for element in frames:
                if element.winfo_class() == 'Frame':
                    element.destroy()
            
            frame_display = Frame(frame_main, height = 270, width = 270, bg = 'gray48')
            frame_display.grid(row = 1, column = 1, padx = 10, pady = 10)
    
            show_grid(base, base_og, frame_display)
            Label(frame_display, text = "No solution found yet. Try PPS Approach.", bg = 'gray48', fg = 'white', justify = 'center').grid(row = 13, column = 0, columnspan = 9)
            
            return
        else:
            blanks = blankCheck
    
    return

###############################################################################################################################################
# 5.2. Basic Sudoku Solver - Additional Functions
###############################################################################################################################################

# function to count possibilites at a position
def layerCounter(layers):
    
    loop_vec = np.zeros([9,9], dtype = int)
    
    for i in range(9):       
        for j in range(9):           
            for k in range(9):
                
                if layers[k][i][j] == 0:
                    loop_vec[i][j] += 1

    return  loop_vec

# function to count all possibilities/open spaces in the layers
def blankCounter(layers):
    
    blanks = 0
    
    for i in range(9):
        for j in range(9):
            for k in range(9):
              
                if layers[i][j][k] == 0:
                    blanks += 1
                    
    return blanks

# function for updating layer based on digit present in base table
def solver_layer_updater(base, layers):

    for i in range(9):
        for j in range(9):
        
            if base[i][j] > 0:
                for k in range(9):
                    if base[i][j] == k+1:
                        layers[k][i][j] = 1
                    else:
                        layers[k][i][j] = 2
               
    return

# function for updating each layer for blocked cells
def solver_row_column_check(layers):
    
    for i in range(9):
        for j in range(9):
            for k in range(9):
                
                if layers[i][j][k] == 1:
                    
                    for l in range(9):
                        if layers[i][j][l] == 0:
                            layers[i][j][l] = 2
                                
                        if layers[i][l][k] == 0:
                            layers[i][l][k] = 2  
    
    return

# function for updating each box for blocked cells
def solver_box_check(layers):
    
    for i in range(9):
        for j in range(9):
            for k in range(9):
                
                if layers[i][j][k] == 1:
                    a,b = j+1,k+1
                                          
                    while a%3 != 0:
                        a = a + 1
                    while b%3 != 0:
                        b = b + 1

                    for x in range(a-3,a,1):
                        for y in range(b-3,b,1):
                            if layers[i][x][y] == 0:
                                layers[i][x][y] = 2
    
    return

# function for checking complimentary boxes for limiting possibility placements
def solver_comp_box(layers):
    
    # function for checking possibility placements in rows of complimentary boxes
    def comp_box_row_sum(p,q,digit,row):
        
        count_open_box = 0
            
        for i in range(p-3,p,1):
            for j in range(q-3,q,1):
                if layers[digit][i][j] == 0:
                    count_open_box += 1
    
        if count_open_box > 3 or count_open_box == 0:
            return 0
        
        count_open_row = 0
        
        for i in range(q-3,q,1):
            
            if layers[digit][row][i] == 0:
                count_open_row += 1
                
        if count_open_box == count_open_row:
            return 1
        else:
            return 0
        
        return

    # function for checking possibility placements in columns of complimentary boxes
    def comp_box_col_sum(p,q,digit,col):
        
        count_open_box = 0
            
        for i in range(p-3,p,1):
            for j in range(q-3,q,1):
                if layers[digit][i][j] == 0:
                    count_open_box += 1
    
        if count_open_box > 3 or count_open_box == 0:
            return 0
        
        count_open_col = 0
        
        for i in range(p-3,p,1):
            
            if layers[digit][i][col] == 0:
                count_open_col += 1
                
        if count_open_box == count_open_col:
            return 1
        else:
            return 0
        
        return


    # checking parallel boxes for definte placements   
    for i in range(9):
        for j in range(9):
            for k in range(9):
                
                if layers[i][j][k] == 0:
                    
                    a,b = j+1,k+1
                    u = 0
                    
                    while u == 0:
                                          
                        if a%3 > 0:
                            a = a + 1
                        if b%3 > 0:
                            b = b + 1
                    
                        if a%3 == 0 and b%3 == 0:
                            u = a * b

                    # checking row wise parallel boxes
                    if (b-(a/3)) <= 2: 
                        if comp_box_row_sum(a,b+3,i,j):
                            layers[i][j][k] = 2
                            
                        if comp_box_row_sum(a,b+6,i,j):
                            layers[i][j][k] = 2
                    
                    elif (b-(a/3)) >= 6:
                        if comp_box_row_sum(a,b-3,i,j):
                            layers[i][j][k] = 2
                            
                        if comp_box_row_sum(a,b-6,i,j):
                            layers[i][j][k] = 2
                    
                    else:
                        if comp_box_row_sum(a,b-3,i,j):
                            layers[i][j][k] = 2
                            
                        if comp_box_row_sum(a,b+3,i,j):
                            layers[i][j][k] = 2
                    
                    # checking column wise parallel boxes
                    if (a-(b/3)) <= 2: 
                        if comp_box_col_sum(a+3,b,i,k):
                            layers[i][j][k] = 2
                            
                        if comp_box_col_sum(a+6,b,i,k):
                            layers[i][j][k] = 2
                    
                    elif (a-(b/3)) >= 6:
                        if comp_box_col_sum(a-3,b,i,k):
                            layers[i][j][k] = 2
                            
                        if comp_box_col_sum(a-6,b,i,k):
                            layers[i][j][k] = 2
                    
                    else:
                        if comp_box_col_sum(a-3,b,i,k):
                            layers[i][j][k] = 2
                            
                        if comp_box_col_sum(a+3,b,i,k):
                            layers[i][j][k] = 2
                                               
    return

# function for prefinalisation of possibility formations
def matches_updates(layers,box_value):
     
    for i in range(9):
        for j in range(9):
            
            box_value[i][j][0] = 0
            box_value[i][j][1] = 1.0
    
    
    # capturing count of missing and value of formation   
    for i in range(9):
        for j in range(9):
            
            a = j + 1
            u = 0
            
            while u == 0:
                
                if a%3 > 0:
                    a = a + 1
                elif a%3 == 0:
                    u = a
            
            b = int(3*(a-j))
            
            for k in range(a-3,a,1):
                for l in range(b-3,b,1):
                    if layers[i][k][l] == 0:
                        box_value[i][j][0] = box_value[i][j][0] + 1    
                        box_value[i][j][1] = box_value[i][j][1]*(((k+1)*(l+1))+((1/(k+1))-((1/(l+1)))))

    return

# function to match and eliminate possibilities based on possibility formations
def matches(layers, box_value):        

    # comparing missing counts and formation values for 2
    for i in range(9):
        for j in range(i+1,9,1):
            for k in range(9):#comparing all 9 boxes for matching pairs
                
                if box_value[i][k][0] == 2 and box_value[j][k][0] == 2 and box_value[i][k][1] == box_value[j][k][1]:
                    
                    a = k+1
                    u = 0
                    
                    while u == 0:
                        
                        if a%3 > 0:
                            a = a + 1
                        elif a%3 == 0:
                            u = a
                    
                    b = int(3*(a - k))
                    
                    for x in range(a-3,a,1):
                        for y in range(b-3,b,1):
                            for z in range(9):
                                
                                if z != i and z != j and layers[i][x][y] == 0:
                                    if layers[z][x][y] == 0:
                                        layers[z][x][y] = 2
                                        

    # comparing missing counts and formation values for 3
    for i in range(9):
        for j in range(i+1,9,1):
            for k in range(j+1,9,1):
                for l in range(9):
                
                    if box_value[i][l][0] == 3 and box_value[j][l][0] == 3 and box_value[k][l][0] == 3 and box_value[i][l][1] == box_value[j][l][1] and box_value[i][l][1] == box_value[k][l][1]:
                    
                        a = l+1
                        u = 0
                    
                        while u == 0:
                        
                            if a%3 > 0:
                                a = a + 1
                            elif a%3 == 0:
                                u = a
                    
                        b = int(3*(a - l))
                    
                        for x in range(a-3,a,1):
                            for y in range(b-3,b,1):
                                for z in range(9):
                                
                                    if z != i and z != j and z != k and layers[i][x][y] == 0:
                                        if layers[z][x][y] == 0:
                                            layers[z][x][y] = 2 


    # comparing missing counts and formation values for 4
    for i in range(9):
        for j in range(i+1,9,1):
            for k in range(j+1,9,1):
                for l in range(k+1,9,1):
                    for m in range(9):
                
                        if box_value[i][m][0] == 4 and box_value[j][m][0] == 4 and box_value[k][m][0] == 4 and box_value[l][m][0] == 4 and box_value[i][m][1] == box_value[j][m][1] and box_value[i][m][1] == box_value[k][m][1] and box_value[i][m][1] == box_value[l][m][1]:
                    
                            a = m+1
                            u = 0
                    
                            while u == 0:
                        
                                if a%3 > 0:
                                    a = a + 1
                                elif a%3 == 0:
                                    u = a
                    
                            b = int(3*(a - m))
                    
                            for x in range(a-3,a,1):
                                for y in range(b-3,b,1):
                                    for z in range(9):
                                
                                        if z != i and z != j and z != k and z != l and layers[i][x][y] == 0:
                                            if layers[z][x][y] == 0:
                                                layers[z][x][y] = 2 


    # comparing missing counts and formation values for 5
    for i in range(9):
        for j in range(i+1,9,1):
            for k in range(j+1,9,1):
                for l in range(k+1,9,1):
                    for n in range(l+1,9,1):
                        for m in range(9):
                    
                            if box_value[i][m][0] == 5 and box_value[j][m][0] == 5 and box_value[k][m][0] == 5 and box_value[l][m][0] == 5 and box_value[n][m][0] == 4 and box_value[i][m][1] == box_value[j][m][1] and box_value[i][m][1] == box_value[k][m][1] and box_value[i][m][1] == box_value[l][m][1] and box_value[i][m][1] == box_value[n][m][1]:
                        
                                a = m+1
                                u = 0
                        
                                while u == 0:
                            
                                    if a%3 > 0:
                                        a = a + 1
                                    elif a%3 == 0:
                                        u = a
                        
                                b = int(3*(a - m))
                        
                                for x in range(a-3,a,1):
                                    for y in range(b-3,b,1):
                                        for z in range(9):
                                    
                                            if z != i and z != j and z != k and z != l and z != n and layers[i][x][y] == 0:
                                                if layers[z][x][y] == 0:
                                                    layers[z][x][y] = 2
                                                
    return

# function for identifying and filling digits where possible
def naked_single(base, layers):
    
    for i in range(9):
        for j in range(9):
            
            row_check = 0
            col_check = 0
            box_check = 0
            dep_check = 0
            
            row,col,b_row,b_col,digit = 0,0,0,0,0
            
            p = j+1
            
            while p%3 != 0:
                p += 1
            
            q = 3*int(p-j)
            
            for x in range(p-3,p,1):
                for y in range(q-3,q,1):
                    
                    if layers[i][x][y] == 0:
                        box_check += 1
                        b_row, b_col = x,y
            
            for k in range(9):
                
                if layers[i][j][k] == 0:
                    row_check += 1
                    col = k
                
                if layers[i][k][j] == 0:
                    col_check += 1
                    row = k
                
                if layers[k][i][j] == 0:
                    dep_check += 1
                    digit = k
            
            if box_check == 1:
                base[b_row][b_col] = i+1
                layers[i][b_row][b_col] = 1
            
            if row_check == 1:
                base[j][col] = i+1
                layers[i][j][col] = 1
            
            if col_check == 1:
                base[row][j] = i+1
                layers[i][row][j] = 1
                
            if dep_check == 1:
                base[i][j] = digit+1
                layers[digit][i][j] = 1
                
            if box_check == 1 or row_check == 1 or col_check == 1 or dep_check == 1:
                return
                     
    return

###############################################################################################################################################
# 5.3. Possibility Position Score (PPS) Sudoku Solver
###############################################################################################################################################

# function to run PPS Approach
def PPSRun(base, layers, box_value, frame_main):
    
    base_og = base.copy()  
     
    PPS_set = PPS_gen(layers)
    print("Initializied Possibility Map..")    
    
    PPS_set = PPS_build(PPS_set, base, layers, box_value)
    print("Built Possibility Map Elements..")       
    
    posSort(PPS_set)
    print("Possibility Map sorted..")
    
    PPS_sol_set = build_full_sol_set(PPS_set)
    print("Solution set for all digits setup..")
    
    PPS_sol_set_sorter(PPS_sol_set)
    print("Digit wise solution set sorted..")
    
    sol_set = build_sol_set_final(PPS_sol_set)
    
    print("Final solution: {}".format(sol_set))
    
    base_final = display_solution(PPS_sol_set, sol_set)
    
    print(base_final)
            
    frames = frame_main.winfo_children()
            
    for element in frames:
        if element.winfo_class() == 'Frame':
            element.destroy()
            
    frame_display = Frame(frame_main, height = 270, width = 270, bg = 'gray48')
    frame_display.grid(row = 1, column = 1, padx = 10, pady = 10)
    
    show_grid(base_final, base_og, frame_display)
    
    if len(sol_set) == 1:
        Label(frame_display, text = "Sudoku Complete", bg = 'gray48', justify = 'center').grid(row = 13, column = 0, columnspan = 9)
    else:
        Label(frame_display, text = "%s solutions found! Displaying only the first one."%(len(sol_set)), bg = 'gray48', justify = 'center').grid(row = 13, column = 0, columnspan = 9)
    
    return

###############################################################################################################################################
# 5.4. Possibility Position Score (PPS) Sudoku Solver - Additional Functions
###############################################################################################################################################

# function to digit wise possibility map
# this is constructed with the box number
# structure -> [digit 1, [box 1, [[digit,x1,y1],...[digit,xn,yn]]],..,[box 9, [[digit,x1,y1],...[digit,xn,yn]]]]
def PPS_gen(layers):
    
    PPS_set = []
    
    for i in range(9): # digit
    
        PPS_digit = [i]
        
        for j in range(9): # box number
            
            PPS_box = [j, []]
            
            a = j + 1
            u = 0
            
            while u == 0:
                
                if a%3 > 0:
                    a = a + 1
                elif a%3 == 0:
                    u = a
            
            b = int(3*(a-j))  
            
            for x in range(a-3,a):
                for y in range(b-3, b):
                    
                    if layers[i][x][y] == 0 or layers[i][x][y] == 1:
                        PPS_box[1].append([i,x,y])
                
            PPS_digit.append(PPS_box)
    
        PPS_set.append(PPS_digit)
    
    return PPS_set 

# function to generate layer score for each possibility in the digit layer
# new structure -> [digit 1, [box 1, [[[digit,x1,y1], NS_count, box_score_set],...[[digit,xn,yn], NS_count, box_score_set]]],..,[box 9..]]
def PPS_build(PPS_set, base, layers, box_value):
    
    newPPS_set = []
    
    for i in range(len(PPS_set)): # going digit wise
        
        PPS_set_digit_row = [i]
        
        for j in range(1, len(PPS_set[i])): # going through each box
        
            PPS_set_box_row = [j-1, []]
        
            for k in range(len(PPS_set[i][j][1])): # going through all possibilities within a box
           
                cords = PPS_set[i][j][1][k]
                
                loop_base = np.copy(base)
                loop_layers = np.copy(layers)
                loop_box_value = np.copy(box_value)
                
                loop_base[cords[1]][cords[2]] = cords[0] + 1
                loop_layers[cords[0]][cords[1]][cords[2]] = 1
                
                # Additional Information key
                # loop_vec_0 = array of naked singles revealed even in case of contradictions
                # loop_vec_1 = count of naked singles or -1 in case of contradictions
                
                loop_vec_0, checker = run_solver_PPS(loop_base, loop_layers, loop_box_value)
                
                if checker == 0:
                    loop_vec_1 = len(loop_vec_0)
                    
                    box_score_set = box_score_set_gen(loop_layers)
                    
                elif checker == -1:
                    print("solution found?")
                    print(loop_base)
                    print("layers full?")
                    print(layerCounter(layers))
                    
                    box_score_set = box_score_set_gen(loop_layers)
                    
                else:
                    loop_vec_1 = -1
                
                
                addInfo = [PPS_set[i][j][1][k], loop_vec_1, box_score_set]
                
                if loop_vec_1 >= 0:
                    PPS_set_box_row[1].append(addInfo)
        
            PPS_set_digit_row.append(PPS_set_box_row)
            
        newPPS_set.append(PPS_set_digit_row)
        
    return newPPS_set

# function to generate list of revealed digits for each possibility
def run_solver_PPS(base, layers, box_value):
        
    blanks = blankCounter(layers) #Number of blanks in Layers
    
    NS = []
   
    while blanks > 0: #Run while the number of blanks in Layers is greater than zero

        solver_layer_updater(base, layers)
        
        solver_row_column_check(layers)
        
        solver_box_check(layers)
        
        solver_comp_box(layers)
        
        matches_updates(layers,box_value)
        
        matches(layers, box_value)
        
        loop_vec = naked_single_PPS(base, layers) #Caputre list of Naked Singles generated

        for i in range(len(loop_vec)):
            
            NS.append(loop_vec[i]) #Simply reformatting the vector into desired shape
        
        blankCheck = blankCounter(layers) #Checking the new number of blanks in the layers
        
        if blanks > blankCheck:
            blanks = blankCheck #if number of blanks in layers has reduced, then we will run this loop again
        else:
            blanks = -1 #if number of blanks has not changed, then time to break the loop
    
    
    NS_ = cleanArray(NS) #removing duplicates from the final array of Naked Singles
    
    
    #We need to communicate if this option led to any contradictions
    
    if isContradiction(base, layers): # if the solution is a contradiction (layer has some complete position but base is empty)
        checker = -2
    elif blankCounter(layers) == 0:  # if the layers are complete
        checker = -1
    else:                           # nothing special is detected
        checker = 0
    
    return NS_, checker

# function for identifying and filling digits where possible
# also returns list of revealed digits and their positions
def naked_single_PPS(base, layers):
    
    loop_vec = []
    
    for i in range(9):
        for j in range(9):
            
            row_check = 0
            col_check = 0
            box_check = 0
            dep_check = 0
            
            row,col,b_row,b_col,digit = 0,0,0,0,0
            
            p = j+1
            
            while p%3 != 0:
                p += 1
            
            q = 3*int(p-j)
            
            for x in range(p-3,p,1):
                for y in range(q-3,q,1):
                    
                    if layers[i][x][y] == 0:
                        box_check += 1
                        b_row, b_col = x,y
            
            for k in range(9):
                
                if layers[i][j][k] == 0:
                    row_check += 1
                    col = k
                
                if layers[i][k][j] == 0:
                    col_check += 1
                    row = k
                
                if layers[k][i][j] == 0:
                    dep_check += 1
                    digit = k
            
            if box_check == 1:
                base[b_row][b_col] = i+1
                layers[i][b_row][b_col] = 1
                loop_vec.append([i,b_row,b_col])
            
            if row_check == 1:
                base[j][col] = i+1
                layers[i][j][col] = 1
                loop_vec.append([i,j,col])
            
            if col_check == 1:
                base[row][j] = i+1
                layers[i][row][j] = 1
                loop_vec.append([i,row,j])
                
            if dep_check == 1:
                base[i][j] = digit+1
                layers[digit][i][j] = 1
                loop_vec.append([digit,i,j])
                
            if len(loop_vec) > 0:
                return loop_vec
                     
    return []

# function to check list of revealed digits for duplicates, and remove the same
def cleanArray(nsSet):
    
    nsSetNew = []
    
    for i in range(len(nsSet)):
        
        checker = 0
        
        for j in range(len(nsSetNew)):
            
            if nsSet[i] == nsSetNew[j]:
                checker = 1
        
        if checker == 0:
            
            nsSetNew.append(nsSet[i])
    
    return nsSetNew

# function to check if a possibility has resulted in a contradiction
def isContradiction(base, layers):
    
    check = layerCounter(layers) # this generates count of zeros in a layer position
    
    for i in range(9):
        for j in range(9):
            
            if base[i][j] == 0 and check[i][j] == 0: # if the position in the base sudoku has a zero value but the layer position has no open values, this is a contradiction
                return True
            
    return False

# function to score each digit layer based on actual and possible positions
# this is generated box wise
def box_score_set_gen(layers):
    
    score_map = [[2,3,5,7,11,13,17,19,23],
                 [29,31,37,41,43,47,53,59,61],
                 [67,71,73,79,83,89,97,101,103],
                 [107,109,113,127,131,137,139,149,151],
                 [157,163,167,173,179,181,191,193,197],
                 [199,211,223,227,229,233,239,241,251],
                 [257,263,269,271,277,281,283,293,307],
                 [311,313,317,331,337,347,349,353,359],
                 [367,373,379,383,389,397,401,409,419]]
    
    score_set = []
    
    for index in range(9): # digit
        
        digit_layer_score = []
        
        for j in range(9): # box number
                
            PPS_box = 1
            
            a = j + 1
            u = 0
            
            while u == 0:
                
                if a%3 > 0:
                    a = a + 1
                elif a%3 == 0:
                    u = a
            
            b = int(3*(a-j))  
            
            for x in range(a-3,a):
                for y in range(b-3, b):
                    
                    if layers[index][x][y] == 0 or layers[index][x][y] == 1:
                        
                        PPS_box *= score_map[x][y]
    
            digit_layer_score.append(PPS_box)
    
        score_set.append(digit_layer_score)

    return score_set

# function to sort possibility position space based on count of digits revealed by a possibility
def posSort(posSet):
    
    for i in range(len(posSet)): # digit
        
        for j in range(1,len(posSet[i])): # box
            
            for k in range(len(posSet[i][j][1])):
                for l in range(k+1,len(posSet[i][j][1])):
                    
                    if posSet[i][j][1][k][1] < posSet[i][j][1][l][1]:
                        
                        sort_vec = posSet[i][j][1][k]
                        
                        posSet[i][j][1][k] = posSet[i][j][1][l]
                        
                        posSet[i][j][1][l] = sort_vec
    
    return

# function to generate list of potential solutions for all digits
def build_full_sol_set(PPS_set):
    
    full_sol = []
    
    for i in range(len(PPS_set)): # digit

        sol_set = build_sol_set(PPS_set[i], i)
        
        full_sol.append([i,sol_set])
    
    return full_sol
        
# function to generate list of potential solutions for a digit
def build_sol_set(PPS_sub_set, index):
    
    max_checks, checks = 1,1
    
    # generating product of box wise possibilities
    for i in range(1, len(PPS_sub_set)): # box
        
        max_checks *= len(PPS_sub_set[i][1])
        
    print("for digit {}, max checks is {}".format(index+1,max_checks))
    
    sol_set = []
    
    for i in range(len(PPS_sub_set[1][1])): # going through possibilities in box 1
        
        sol1 = PPS_sub_set[1][1][i][2] # extracting box_score_set which is a 9x9 array
        print("Checked {} of {}".format(checks, max_checks), end = "\r")
        checks += 1
        
        for j in range(len(PPS_sub_set[2][1])): # going through possibilities in box 2
            
            sol2 = PPS_sub_set[2][1][j][2]
            print("Checked {} of {}".format(checks, max_checks), end = "\r")
            checks += 1
            
            if no_contradiction(sol1, sol2):
                
                new_sol2 = sol_combine(sol1, sol2)
                
                for k in range(len(PPS_sub_set[3][1])): # going through possibilities in box 3
                    
                    sol3 = PPS_sub_set[3][1][k][2]
                    print("Checked {} of {}".format(checks, max_checks), end = "\r")
                    checks += 1
                    
                    if no_contradiction(new_sol2, sol3):
                        
                        new_sol3 = sol_combine(new_sol2, sol3)
                        
                        for l in range(len(PPS_sub_set[4][1])): # going through possibilities in box 4
                            
                            sol4 = PPS_sub_set[4][1][l][2]
                            print("Checked {} of {}".format(checks, max_checks), end = "\r")
                            checks += 1
                            
                            if no_contradiction(new_sol3, sol4):
                                
                                new_sol4 = sol_combine(new_sol3, sol4)
                                
                                for m in range(len(PPS_sub_set[5][1])): # going through possibilities in box 5
                                    
                                    sol5 = PPS_sub_set[5][1][m][2]
                                    print("Checked {} of {}".format(checks, max_checks), end = "\r")
                                    checks += 1
                                    
                                    if no_contradiction(new_sol4, sol5):
                                        
                                        new_sol5 = sol_combine(new_sol4, sol5)
                                        
                                        for n in range(len(PPS_sub_set[6][1])): # going through possibilities in box 6
                                            
                                            sol6 = PPS_sub_set[6][1][n][2]
                                            print("Checked {} of {}".format(checks, max_checks), end = "\r")
                                            checks += 1
                                            
                                            if no_contradiction(new_sol5, sol6):
                                                
                                                new_sol6 = sol_combine(new_sol5, sol6)
                                                
                                                for o in range(len(PPS_sub_set[7][1])): # going through possibilities in box 7
                                                    
                                                    sol7 = PPS_sub_set[7][1][o][2]
                                                    print("Checked {} of {}".format(checks, max_checks), end = "\r")
                                                    checks += 1
                                                    
                                                    if no_contradiction(new_sol6, sol7):
                                                        
                                                        new_sol7 = sol_combine(new_sol6, sol7)
                                                        
                                                        for p in range(len(PPS_sub_set[8][1])): # going through possibilities in box 8
                                                            
                                                            sol8 = PPS_sub_set[8][1][p][2]
                                                            print("Checked {} of {}".format(checks, max_checks), end = "\r")
                                                            checks += 1
                                                            
                                                            if no_contradiction(new_sol7, sol8):
                                                                
                                                                new_sol8 = sol_combine(new_sol7, sol8)
                                                                
                                                                for q in range(len(PPS_sub_set[9][1])): # going through possibilities in box 9
                                                                    
                                                                    sol9 = PPS_sub_set[9][1][q][2]
                                                                    print("Checked {} of {}".format(checks, max_checks), end = "\r")
                                                                    checks += 1
                                                                    
                                                                    if no_contradiction(new_sol8, sol9):
                                                                        
                                                                        new_sol9 = sol_combine(new_sol8, sol9)
                                                                        
                                                                        sol_set.append(new_sol9)
                                                                        
    
    print("")
    print("for digit {}, total sol count = {}".format(index+1, len(sol_set)))
    
    return sol_set

# function to identify contradictions between two possible solutions for a digit
# function ensures there is overlap between solutions
def no_contradiction(sol1, sol2):
    
    set1 = sol1
    set2 = sol2
    
    for i in range(9): # digit
        for j in range(9): # box
            
            if set1[i][j] != set2[i][j]:
            
                smaller, bigger = 0,0
                
                if set1[i][j] > set2[i][j]:
                    smaller = set2[i][j]
                    bigger = set1[i][j]
                else:
                    smaller = set1[i][j]
                    bigger = set2[i][j]
                
                hcf = smaller
        
                while True:
                    
                    hcf = bigger%smaller
                    
                    bigger = smaller
                    
                    if hcf == 0:
                        hcf = smaller
                        break
                    else:
                        smaller = hcf
                
                if hcf == 1:
                    return False
    
    return True

# function to combine digit solutions assuming no contradiction
def sol_combine(sol1, sol2):
    
    new_sol = []
    
    set1 = sol1
    set2 = sol2
    
    for i in range(9): # digit
        
        sol_digit_row = []    
    
        for j in range(9): # box
            
            if set1[i][j] != set2[i][j]:
            
                smaller, bigger = 0,0
                
                if set1[i][j] > set2[i][j]:
                    smaller = set2[i][j]
                    bigger = set1[i][j]
                else:
                    smaller = set1[i][j]
                    bigger = set2[i][j]
                
                hcf = smaller
        
                while True:
                    
                    hcf = bigger%smaller
                    
                    bigger = smaller
                    
                    if hcf == 0:
                        hcf = smaller
                        break
                    else:
                        smaller = hcf
                        
                sol_digit_row.append(hcf)
            
            else:
                sol_digit_row.append(set1[i][j])
        
        new_sol.append(sol_digit_row)
    
    return new_sol

# function to sort PPS for all digits in ascending order
def PPS_sol_set_sorter(PPS_sol_set):
    
    for i in range(len(PPS_sol_set)):
        for j in range(i+1, len(PPS_sol_set)):
            
            if len(PPS_sol_set[i][1]) > len(PPS_sol_set[j][1]):
                
                sort_set = PPS_sol_set[i]
                
                PPS_sol_set[i] = PPS_sol_set[j]
                
                PPS_sol_set[j] = sort_set

    return

# function to generate list of potential solutions
def build_sol_set_final(PPS_sol_set):
    
    max_checks, checks = 1,1
    
    # generating product of possible solutions for all digits
    for i in range(len(PPS_sol_set)):
        
        max_checks *= len(PPS_sol_set[i][1])
        
    print(max_checks)
    
    sol_set = []
    
    for i in range(len(PPS_sol_set[0][1])): # going through possibilities for digit with least solutions
        
        sol1 = PPS_sol_set[0][1][i]
        print("Checked {} of {}".format(checks, max_checks), end = "\r")
        checks += 1
        
        for j in range(len(PPS_sol_set[1][1])):
            
            sol2 = PPS_sol_set[1][1][j]
            print("Checked {} of {}".format(checks, max_checks), end = "\r")
            checks += 1
            
            if no_contradiction(sol1, sol2):
                
                new_sol2 = sol_combine(sol1, sol2)
                
                for k in range(len(PPS_sol_set[2][1])):
                    
                    sol3 = PPS_sol_set[2][1][k]
                    print("Checked {} of {}".format(checks, max_checks), end = "\r")
                    checks += 1
                    
                    if no_contradiction(new_sol2, sol3):
                        
                        new_sol3 = sol_combine(new_sol2, sol3)
                        
                        for l in range(len(PPS_sol_set[3][1])):
                            
                            sol4 = PPS_sol_set[3][1][l]
                            print("Checked {} of {}".format(checks, max_checks), end = "\r")
                            checks += 1
                            
                            if no_contradiction(new_sol3, sol4):
                                
                                new_sol4 = sol_combine(new_sol3, sol4)
                                
                                for m in range(len(PPS_sol_set[4][1])):
                                    
                                    sol5 = PPS_sol_set[4][1][m]
                                    print("Checked {} of {}".format(checks, max_checks), end = "\r")
                                    checks += 1
                                    
                                    if no_contradiction(new_sol4, sol5):
                                        
                                        new_sol5 = sol_combine(new_sol4, sol5)
                                        
                                        for n in range(len(PPS_sol_set[5][1])):
                                            
                                            sol6 = PPS_sol_set[5][1][n]
                                            print("Checked {} of {}".format(checks, max_checks), end = "\r")
                                            checks += 1
                                            
                                            if no_contradiction(new_sol5, sol6):
                                                
                                                new_sol6 = sol_combine(new_sol5, sol6)
                                                
                                                for o in range(len(PPS_sol_set[6][1])):
                                                    
                                                    sol7 = PPS_sol_set[6][1][o]
                                                    print("Checked {} of {}".format(checks, max_checks), end = "\r")
                                                    checks += 1
                                                    
                                                    if no_contradiction(new_sol6, sol7):
                                                        
                                                        new_sol7 = sol_combine(new_sol6, sol7)
                                                        
                                                        for p in range(len(PPS_sol_set[7][1])):
                                                            
                                                            sol8 = PPS_sol_set[7][1][p]
                                                            print("Checked {} of {}".format(checks, max_checks), end = "\r")
                                                            checks += 1
                                                            
                                                            if no_contradiction(new_sol7, sol8):
                                                                
                                                                new_sol8 = sol_combine(new_sol7, sol8)
                                                                
                                                                for q in range(len(PPS_sol_set[8][1])): # going through possibilities for digit with most solutions
                                                                    
                                                                    sol9 = PPS_sol_set[8][1][q]
                                                                    print("Checked {} of {}".format(checks, max_checks), end = "\r")
                                                                    checks += 1
                                                                    
                                                                    if no_contradiction(new_sol8, sol9):
                                                                        
                                                                        new_sol9 = sol_combine(new_sol8, sol9)
                                                                        
                                                                        sol_set.append(new_sol9)
                                                                        
    
    return sol_set

# function to compile solution and return the same
def display_solution(PPS_sol_set, sol_set):
        
    score_map = [[2,3,5,7,11,13,17,19,23],
                  [29,31,37,41,43,47,53,59,61],
                  [67,71,73,79,83,89,97,101,103],
                  [107,109,113,127,131,137,139,149,151],
                  [157,163,167,173,179,181,191,193,197],
                  [199,211,223,227,229,233,239,241,251],
                  [257,263,269,271,277,281,283,293,307],
                  [311,313,317,331,337,347,349,353,359],
                  [367,373,379,383,389,397,401,409,419]]
    
    solution = np.zeros([9,9], dtype=int)
    
    for i in range(9): # digit
        for j in range(9):
            
            digit_position = sol_set[0][i][j]
            
            for x in range(9):
                
                check = 0
                
                for y in range(9):
                    
                    if score_map[x][y] == digit_position:
                        solution[x][y] = i + 1
                        check = 1
                        break
                
                if check == 1:
                    break
                
    return solution

###############################################################################################################################################
###############################################################################################################################################
# Mainloop
###############################################################################################################################################
###############################################################################################################################################

window_main.mainloop()

