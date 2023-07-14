import csv
import random

def OpenData():
  data = []
  with open("./Prisoners_data.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
      data.append(row)
  return data

def getTotal(data, column, row):
  total = data[column]
  total = total[row]
  return total

def simulation(total, chance, actual, title):
  repeat = 100
  simulated_equal = 0
  for num in range(repeat):
    simulated_total = 0
    for i in range(total):
      random_chance = random.random()
      if random_chance <= chance:
        simulated_total += 1
    if simulated_total == actual:
      simulated_equal += 1
  print("Out of",repeat,"simulations using the population average of"
        "\n"+title,"rates",
        "\n"+str(simulated_equal),"simulations were the same as reality."
        "\nThe population average is",str(round((chance*100),2))+"%",
        "\nThe average in prisons is",str(round(((actual/total)*100),2))+"%\n")

def GetData(data, chance, column, total):
  total_prison = int(getTotal(data, 39, total))
  factor_prison = int(getTotal(data, 39, column))
  title = getTotal(data, 0, column)
  simulation(total_prison, chance, factor_prison, title)

def MainProgram():
  factor = [["Illiterate", 0.0598, 2, 8],
            ["Post Graduate", 0.0349120917516, 7, 8],
            ["Christian", 0.023, 28, 30],
            ["Hindu", 0.798, 25, 30],
            ["Muslim", 0.142, 26, 30],
            ["Sikh", 0.0172, 27, 30]]
  data = OpenData()
  for row in factor:
    GetData(data, row[1], row[2], row[3])

MainProgram()
