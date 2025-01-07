def CalculateAveragePercentage(firstvalue, secondvalue):
    return (firstvalue - secondvalue) / (min(firstvalue,secondvalue)) * 100

def GetAverage(list):
    return sum(list) / len(list)

#Quick function to calculate averages of times
#First 5 puzzles
percentages = []
percentages.append(CalculateAveragePercentage(8.87676913000323,0.141572299996914))
percentages.append(CalculateAveragePercentage(0.24777357999701,0.139290700000128))
percentages.append(CalculateAveragePercentage(3.87859862000041,0.139829740001005))
percentages.append(CalculateAveragePercentage(3.59747354000137,0.13927643999923))
percentages.append(CalculateAveragePercentage(0.770025500000338,0.139533500000834))

for percentage in percentages:
    print(percentage)

#Average of runtimes
print(GetAverage(percentages))