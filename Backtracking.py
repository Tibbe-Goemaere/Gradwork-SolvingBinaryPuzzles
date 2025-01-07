import math

def BacktrackAlgorithm(puzzle,optimized = False):
    puzzlesize = round(math.sqrt(len(puzzle)))
    if optimized:
        puzzle = ApplyConstraintPropagation(puzzle)
        if CheckFilled(puzzle):
            return puzzle
    
    #Make row and column lists to check with later on for unique ones
    columnList = []
    rowList = []
    for i in range(0,puzzlesize):
        singleColumn = []
        for j in range(0,puzzlesize):
            singleColumn.append(puzzle[i + puzzlesize*j])
        columnList.append(singleColumn)

    for i in range(0,puzzlesize):
        rowList.append(puzzle[i*puzzlesize:i*puzzlesize + puzzlesize]) 

    for i in range(0,len(puzzle)):
        row = i//puzzlesize
        col = i%puzzlesize
        value = puzzle[i]
        #Check if this value is an empty value
        if (value == -1):
            for possibleValue in [0,1]:
                #We will do for number 0 and 1 because those are the two options
                #First we check for rule2, if we put in this number are there more then 2 0's or 1's next to each other
                #Check if there is same number left, if so check if another number left from it
                if not (IsValueNextToItselfTwice(row,col,i,puzzle,puzzlesize,possibleValue)):
                    #Next check is amount of 0's and 1's in row and col and check if it is not over value it should be
                    #We need to get a sublist of the rows and cols
                    #make a new list for the whole column and row to check for amount of values and also to later check for duplicate rows/cols
                    currentRow = rowList[row][:]
                    currentColumn = columnList[col][:]
                    if not (currentRow.count(possibleValue) >= puzzlesize/2):
                        if not (currentColumn.count(possibleValue) >= puzzlesize/2):
                            #After checking for this we check for duplicate lines, this is the harder part
                            #I will put in the number in the row and col list and check for duplicates
                            #rowList[row][i - (row * puzzlesize)] = possibleValue
                            currentRow[i - (row * puzzlesize)] = possibleValue
                            if (rowList.count(currentRow) <= 1 or (-1 in rowList)):
                                #print("no duplicate row")
                                currentColumn[i - (row * puzzlesize)] = possibleValue
                                if (columnList.count(currentColumn) <= 1 or (-1 in columnList)):
                                    #If we made it here it is a valid idx and we'll insert the value with the new
                                    #print("Setting New Value")
                                    puzzle[i] = possibleValue
                                    rowList[row] = currentRow
                                    columnList[row] = currentColumn
                                    #We check if the game is finished if it is not we call this function again 
                                    if (CheckFilled(puzzle)):
                                        #for i in range(0, len(puzzle), 10):  # Step through the puzzle in increments of 10 for printing more clearly
                                            #print(puzzle[i:i + 10]) 
                                        #print("Solved")
                                        return puzzle
                                    else:
                                        if (BacktrackAlgorithm(puzzle)): 
                                            return True
            break
    puzzle[i] = -1
    #print("Backtracking")
    #for i in range(0, len(puzzle), puzzlesize):  # Step through the puzzle in increments of 10 for printing more clearly
        #print(puzzle[i:i + puzzlesize]) 
    
def OptimizedBacktrackAlgorithm(puzzle):
    return BacktrackAlgorithm(puzzle,True) 
            
def IsValueNextToItselfTwice(row,col,idx,puzzle,size,testingValue):
    offset = 1
    currentDirection = col
    for direction in range(0,2):
        if (direction == 1):
            offset = 1
            currentDirection = col
            #this is the offset to check to the left or right
        else:
            offset = size
            currentDirection = row
            #this is the offset for bottom and top, to get value below you you have to do -amount of cols, cols == size bc its a square
        #We will do for number 0 and 1 because those are the two options
        #First we check for rule2, if we put in this number are there more then 2 0's or 1's next to each other
        #Check if there is same number left, if so check if another number left from it
        isSameNumberNext = False
        if (currentDirection >= 1):
            if (puzzle[idx - offset] == testingValue):
                isSameNumberNext = True
                if (currentDirection >= 2):
                    if (puzzle[idx - (offset*2)] == testingValue):
                        #this value is not valid
                        return True
        if (currentDirection < size - 1):
            if (puzzle[idx + offset] == testingValue):
                if (isSameNumberNext):
                    #value not valid bc at one side its same and other its same as well
                    return True
                else:
                    if (currentDirection < size - 2):
                        if (puzzle[idx + (offset*2)] == testingValue):
                            #Not valid as well
                            return True
    #if returned true the index is not valid otherwise its fine
    return False
                        
def CheckFilled(puzzle):
    if -1 in puzzle:
        return False
    return True
    
def ApplyConstraintPropagation(puzzle):

    puzzlesize = round(math.sqrt(len(puzzle)))
    changed = True
    #We add this variable to keep on repeating constraint propagation until we come int the loop and not a single variable gets filled in anymore
    while changed:
        changed = False
        for i in range(len(puzzle)):
            row = i // puzzlesize
            col = i % puzzlesize
            value = puzzle[i]

            if value == -1:
                #Only try to fill in variables that are not filled in
                possiblevalues = {0, 1}

                if IsValueNextToItselfTwice(row, col, i, puzzle, puzzlesize, 0):
                    possiblevalues.remove(0)
                elif IsValueNextToItselfTwice(row, col, i, puzzle, puzzlesize, 1):
                    possiblevalues.remove(1)
                else:
                    currentrow = puzzle[row * puzzlesize: (row + 1) * puzzlesize]
                    currentcolumn = [puzzle[r * puzzlesize + col] for r in range(puzzlesize)]

                    if currentrow.count(0) >= puzzlesize // 2:
                        possiblevalues.remove(0)
                    elif currentrow.count(1) >= puzzlesize // 2:
                        possiblevalues.remove(1)
                    elif currentcolumn.count(0) >= puzzlesize // 2:
                        possiblevalues.remove(0)
                    elif currentcolumn.count(1) >= puzzlesize // 2:
                        possiblevalues.remove(1)
                
                if len(possiblevalues) == 1:
                    puzzle[i] = possiblevalues.pop()
                    changed = True
                    break
    return puzzle
