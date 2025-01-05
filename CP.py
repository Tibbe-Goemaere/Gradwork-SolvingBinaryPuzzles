from ortools.sat.python import cp_model
import math
import timeit

def ApplyCP(originalpuzzle):
    puzzleSize =  round(math.sqrt(len(originalpuzzle)))

    model = cp_model.CpModel()
    puzzle = []
    #add variables cells to be with minimum bound 0 and maximum 1
    for i in range(len(originalpuzzle)):
        x = model.NewIntVar(0,1,f'cell_{i}')
        puzzle.append(x)
    
    #Now we need to add constraints
    #First there cannot be 3 of the same next to each other
    for i in range(puzzleSize):
        for j in range(puzzleSize - 2):
            model.Add(puzzle[i + j*puzzleSize] + puzzle[i + (j+1)*puzzleSize] + puzzle[i + (j+2)*puzzleSize] <=2)
            model.Add(puzzle[i*puzzleSize + j] + puzzle[i*puzzleSize + (j+1)] + puzzle[i*puzzleSize + (j+2)] <=2)
            model.Add(puzzle[i + j*puzzleSize] + puzzle[i + (j+1)*puzzleSize] + puzzle[i + (j+2)*puzzleSize] >=1)
            model.Add(puzzle[i*puzzleSize + j] + puzzle[i*puzzleSize + (j+1)] + puzzle[i*puzzleSize + (j+2)] >=1)

        #There has to be as much 1's as 0's in every row/column so the total amount has to be half of the size, 5*1 im a 10x10 case
        model.Add(sum(puzzle[i + j*puzzleSize] for j in range(puzzleSize)) == puzzleSize // 2)
        model.Add(sum(puzzle[i*puzzleSize + j] for j in range(puzzleSize)) == puzzleSize // 2)

        #There cannot be duplicate  rows or duplicate columns
        differentLines = [] 
        for j in range(i+1,puzzleSize):
            for k in range(puzzleSize):
                #go through every box in a line and check if there is at least 1 difference between the lines
                diffLine = model.NewBoolVar(f'diff_{i}_{j}_{k}')  # Create a helper variable
                model.Add(puzzle[i + k * puzzleSize] != puzzle[j + k * puzzleSize]).OnlyEnforceIf(diffLine)
                model.Add(puzzle[i + k * puzzleSize] == puzzle[j + k * puzzleSize]).OnlyEnforceIf(diffLine.Not())
                differentLines.append(diffLine)

            model.Add(sum(differentLines) >= 1)

 
    #I assigned the value to the puzzle if it not -1, invalid
    for i in range(len(puzzle)):
        if not (originalpuzzle[i] == -1):
            model.Add(originalpuzzle[i] == puzzle[i])
    
 

    solver = cp_model.CpSolver()    

    start = timeit.default_timer()
    #solver.parameters.search_branching = cp_model.FIXED_SEARCH
    status = solver.Solve(model)
    end = timeit.default_timer()

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        solution = [solver.Value(puzzle[i]) for i in range(len(puzzle))]
        #for i in range(0, len(puzzle), puzzleSize):  # Step through the puzzle in increments of 10 for printing more clearly
            #print(solution[i:i + puzzleSize]) 
    else:
        print("Failed")

    #return solution
    return end - start
