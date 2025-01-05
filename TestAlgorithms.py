import Backtracking
import Puzzles
import CP
import timeit

def measure_time(algorithm, puzzle, num_repeats=12):
    times = []
    for _ in range(num_repeats):
        copiedPuzzle = puzzle.copy()
        start = timeit.default_timer()
        algorithm(copiedPuzzle)
        end = timeit.default_timer()
        times.append(end - start)
    
    # Sort and remove highest and lowest
    times.sort()
    filtered_times = times[1:-1]  # Remove the first and last elements (min and max)
    
    # Compute average of the remaining times
    return sum(filtered_times) / len(filtered_times)

#Example with multiple puzzles
overall_times = []
#algorithm = Backtracking.BacktrackAlgorithm
algorithm = CP.ApplyCP

for puzzle in Puzzles.puzzles10x10veryhard:
    avg_time = measure_time(algorithm, puzzle)
    print("Average time:" + str(avg_time))
    #print("Amount of Empty Cells:" + str(puzzle.count(-1)))
    #print()
    overall_times.append(avg_time)

average = sum(overall_times) / len(overall_times)
print(f"Final Average Time: {average:.8f} seconds")

#emptyavgtime = measure_time(algorithm,Puzzles.puzzles10x10mediumempty)
#print(f"Empty Puzzle Average Time: {emptyavgtime:.8f} seconds")