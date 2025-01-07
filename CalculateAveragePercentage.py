def CalculateAveragePercentage(firstvalue, secondvalue):
    return (firstvalue - secondvalue) / (min(firstvalue,secondvalue)) * 100

def GetAverage(list):
    return sum(list) / len(list)

#Quick function to calculate averages of times
#First 5 puzzles
percentages = []
percentages.append(CalculateAveragePercentage(0.0029259999995701947,0.0636821))
percentages.append(CalculateAveragePercentage(0.0018797200013068505,0.06244364))
percentages.append(CalculateAveragePercentage(0.0023751999986416196,0.06246909))
percentages.append(CalculateAveragePercentage(0.001661720000265632,0.06216637))
percentages.append(CalculateAveragePercentage(0.0019226000003982335,0.06224322))

for percentage in percentages:
    print(percentage)

#Average of runtimes
print(GetAverage(percentages))