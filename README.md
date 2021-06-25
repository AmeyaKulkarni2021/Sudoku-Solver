# Sudoku-Solver

### Introduction
While multiple strategies exist for solving a sudoku, beyond a point a player is required to make smart guesses to move forward.
With an algorithmic program, we can brute force a solution by checking combinations of all possibilities, but this can become computationally expense. This is due to the fact that a sudoku is an NP or Non-Polynomial type of problem, meaning with increase in open positions in the sudoku puzzle, the computational time increases exponentially.
In this solver program we attempt the puzzle using two approaches: conventional and modified brute force. Both approaches are described in details in the Methodology section.
The program has been designed in a modular fashion, allowing for easy customization to different formats of the game.
For the time being, a player needs to manually input the sudoku puzzle into the program through a Tkinter GUI. An image recognition-based approach may be considered in the future.

### Libraries used
1. Numpy
2. Tkinter

### Global Variable
1. base - 9x9 numpy array, dtype = int
2. layers - 9x9x9 numpy array, dtype = int
3. box_value - 9x9x2 numpy array, dtype = float
4. entries - array to store user inputs

### Function List

Main Menu
1. manual_input(base) - to receive inputs from user
2. solver(base, layers, box_value) - to create main view for solver
3. exit_all() - to exit the solver program
4. show_grid(base, base_og, frame) - to display grid used in the solver

Manual Input
1. clear_input_space(frame) - to remove all users entries
2. exit_manual_input(frame) - to exit manual input frame
3. store_value(base, frame) - to store user inputs
4. input_checker(user_inputs) - to check if there are any contradictions in user inputs
5. hardest_puzzle() - to setup predefined sudoku

Solver
1. run_solver(base, layers, box_value, frame_main) - to run solver based on conventional approach
2. PPSRun(base, layers, box_value, frame_main) - to run solver based on PPS approach
3. clear_solver_view(frame) - to exit solver frame

Basic Solver
1. layerCounter(layers) - to count possibilites at a position
2. blankCounter(layers) - to count all possibilities/open spaces in the layers
3. solver_layer_updater(base, layers) - to update layer based on digit present in base table
4. solver_row_column_check(layers) - to update each layer for blocked cells
5. solver_box_check(layers) - to update each box in a layer for blocked cells
6. solver_comp_box(layers) - to check complimentary boxes for limiting possibility placements
7. comp_box_row_sum(p,q,digit,row) - to check possibility placements in rows of complimentary boxes
8. comp_box_col_sum(p,q,digit,col) - to check possibility placements in columns of complimentary boxes
9. matches_updates(layers,box_value) - to prefinalize of possibility formations
10. matches(layers, box_value) - to match and eliminate possibilities based on possibility formations
11. naked_single(base, layers) - to identify and fill digits where possible

PPS Solver
1. PPS_gen(layers) - to digit wise possibility map; structure -> [digit 1, [box 1, [[digit,x1,y1],...[digit,xn,yn]]],..,[box 9, [[digit,x1,y1],...[digit,xn,yn]]]]
2. PPS_build(PPS_set, base, layers, box_value) - to generate layer score for each possibility in the digit layer; new structure -> [digit 1, [box 1, [[[digit,x1,y1], NS_count, box_score_set],...[[digit,xn,yn], NS_count, box_score_set]]],..,[box 9..]]
3. run_solver_PPS(base, layers, box_value) - to generate list of revealed digits for each possibility
4. naked_single_PPS(base, layers) - to identify and fill digits where possible; also returns list of revealed digits and their positions
5. cleanArray(nsSet) - to check list of revealed digits for duplicates, and remove the same
6. isContradiction(base, layers) - to check if a possibility has resulted in a contradiction
7. box_score_set_gen(layers) - to score each digit layer based on actual and possible positions
8. posSort(posSet) - to sort possibility position space based on count of digits revealed by a possibility
9. build_full_sol_set(PPS_set) - to generate list of potential solutions for all digits
10. build_sol_set(PPS_sub_set, index) - to generate list of potential solutions for a digit
11. no_contradiction(sol1, sol2) - to identify contradictions between two possible solutions for a digit; ensures there is overlap between solutions
12. sol_combine(sol1, sol2) - to combine digit solutions assuming no contradiction
13. PPS_sol_set_sorter(PPS_sol_set) - to sort PPS for all digits in ascending order
14. build_sol_set_final(PPS_sol_set) - to generate list of potential solutions
15. display_solution(PPS_sol_set, sol_set) - to compile solution and return the same








