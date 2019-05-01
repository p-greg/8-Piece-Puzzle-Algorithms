Created By
Colin Gregory April 2019

This is a implemetation of the Best first and A* algorithms
using the 8-piece puzzle problem.

Usage: 

	python3 puzzle.py mode x1 x2 x3 x4 x5 x6 x7 x8 x9

	Corresponds to the following board state:
	x1 x2 x3
	x4 x5 x6
	x7 x8 x9

Notes: 
    
    -After expanding 10000 states, the program will ask the user if they want to continue.
    

Modes:
   
    The different modes determine what algorithm and heuristic to use. 
    Heuristic information avaliable below the examples.
        
        Mode 0: Best First Search Algorithm with Heuristic One
        Mode 1: A* Search Algorithm with Heuristic One
        Mode 2: Best First Search Algorithm with Heuristic Two
        Mode 3: A* Search Algoritm with Heuristic Two
        Mode 4: Best First Search Algorithm with Heuristic Three
        Mode 5: A* Search Algorithm with Heurisitc Three
    
Examples:

	To find a solution to following puzzle using A* with heuristic one:
	3 6 8
	7 0 1
	2 4 5

	python3 puzzle.py 1 3 6 8 7 0 1 2 4 5

	To find a solution to the following puzzle using Best First with heuristic Three:
	4 8 0
	6 7 5
	3 1 2
	
	python3 puzzle.py 4 4 8 0 6 7 5 3 1 2

Heuristics:

    1) Heuristic one is the total number of misplaced tiles in the state:

            4 1 2
            7 8 0  -->  1+1+1+1+1+1=6
            3 5 6

    2) Heuristic two is the Manhattan distance for each of the tiles:

            4 1 2
            7 8 0  -->  2+0+0+2+2+1+1+1=9
            3 5 6 
	
    3) Heuristic three is the average of the two previous heuristics:

            4 1 2
            7 8 0  -->  (6+9)/2= 7.5
            3 5 6

