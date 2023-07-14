import random
import csv
from matplotlib import pyplot as plt
import statistics
import scipy

def OpenData():
  with open("./HeartDisease.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
      data.append(row)

def SortList():
  booleanList = []
  for row in range(len(data)):
    booleanList.append(data[row][3] == "Yes")
  count = 0
  for row in booleanList:
    if row == True:
      heartproblem.append(data[count])
    elif row == False and count != 0:
      noheartproblem.append(data[count])
    count = count + 1

def FrequencyHeart():
  frequencyheartproblem = len(heartproblem) / (len(noheartproblem) + len(heartproblem))
  print("The percentage of people with heart problems:", round((frequencyheartproblem * 100), 2), "% and without heart problems:", round(((1-frequencyheartproblem)*100), 2), "%\n")
  labels = "Heart Problems", "No Heart Problems"
  frequencies = [frequencyheartproblem, (1 - frequencyheartproblem)]
  explode = (0, 0.05)
  plt.figure("Frequency of Heart Problems")
  plt.title("Frequency of HeartProblems")
  plt.pie(frequencies, explode = explode, labels = labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
  plt.show()

def Analysis(num):
  MList = []
  BList = []
  for row in range(len(heartproblem)):
    M = float(heartproblem[row][num])
    MList.append(M)
  for row in range(len(noheartproblem)):
    B = float(noheartproblem[row][num])
    BList.append(B)
  stdM, stdB, MMean, BMean = MeanStD(MList, BList)
  for row in MList:
    if row > (MMean + (2.5 * stdM)) or row < (MMean - (2.5 * stdM)):
      MList.remove(row)
  for row in BList:
    if row > (BMean + (2.5 * stdB)) or row < (BMean - (2.5 * stdB)):
      BList.remove(row)
  stdM, stdB, MMean, BMean = MeanStD(MList, BList)
  print("Average",data[0][num], "for Heart Problems is:", round(MMean,2), "and No Heart Problems:", round(BMean,2))
  print("Standard Deviations for Heart Problems:", round(stdM, 2), "and No Heart Problems:", round(stdB, 2))
  if MMean > BMean:
    difference = "greater"
  elif MMean < BMean:
    difference = "lesser"
  else:
    difference = "the same"
  ttest, pvalue = scipy.stats.ttest_ind(MList, BList, axis = 0, equal_var = True, nan_policy = "propagate",
                                        permutations = None, random_state = 0, alternative = "two-sided", trim = 0)
  if pvalue < 0.001:
    print("Independent T-Test P-Value: < 0.001")
  else:
    print("Independent T-Test P-Value:", round(pvalue,3))
  if pvalue < 0.05:
    print("The Means are Significantly Different and therefore from Different Populations.\n"+
          str(data[0][num]), "is more likely", difference, "in Heart Problems compared to No Heart Problems.\n")
  else:
    print("The Means are not Significantly Different and from the Same Population.\n")
  PlotHistogram(MList, BList, num, MMean, BMean, stdM, stdB)

def MeanStD(MList, BList):
  stdM = statistics.stdev(MList)
  stdB = statistics.stdev(BList)
  BMean = statistics.mean(BList)
  MMean = statistics.mean(MList)
  return stdM, stdB, MMean, BMean

def PlotHistogram(MList, BList, num, MMean, BMean, stdM, stdB):
  title = "Histogram of " + data[0][num]
  MeanTitle = "Heart Problems Mean: " + str(round(MMean, 2)) + " and"\
              + " No Heart Problems Mean: " + str(round(BMean, 2)) \
              + "\nStandard Deviation: " + str(round(stdM, 2)) \
              + " and : " + str(round(stdB, 2))
  plt.figure(title)
  plt.hist(MList, bins = 15, alpha = 0.8, label = "Heart Problems")
  plt.hist(BList, bins = 15, alpha = 0.8, label = "No Heart Problems")
  plt.plot(BMean, 0.5, "X", color = "orange")
  plt.plot(MMean, 0.5, "X", color="blue")
  plt.suptitle(title)
  plt.legend(title = "Heart Problems:", loc = "upper right")
  plt.title(MeanTitle, fontsize = 8)
  plt.xlabel(data[0][num])
  plt.ylabel("Number of Patients")
  plt.show()

def MainProgram():
  global data, heartproblem, noheartproblem
  data, heartproblem, noheartproblem = [], [], []
  OpenData()
  SortList()
  print("Using Data from", len(data),
        "Participants, a Two-Sided Independent T-Test will be carried out to find if there is \n"
        "a difference in health factors between those with and without heart problems using a 5% Significance Value.\n")
  FrequencyHeart()
  numerical_analysis = [10, 11, 12, 13]
  for i in range(len(numerical_analysis)):
    Analysis(numerical_analysis[i])

MainProgram()
