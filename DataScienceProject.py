def OpenData():
  with open("./data.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
      data.append(row)

def SortList():
  booleanList=[]
  for row in range(len(data)):
    booleanList.append(data[row][1] == "M")
  count = 0
  for row in booleanList:
    if row == True:
      malignant.append(data[count])
    elif row == False and count != 0:
      benign.append(data[count])
    count = count + 1

def FrequencyMalignant():
  frequencyMalignant = len(malignant) / (len(benign) + len(malignant))
  print("Percentage of patients with Malignant Tumours:", round((frequencyMalignant * 100), 2), "%\n")

def Analysis(num):
  MList = []
  BList = []
  for row in range(len(malignant)):
    M = float(malignant[row][num])
    MList.append(M)
  for row in range(len(benign)):
    B = float(benign[row][num])
    BList.append(B)
  stdM, stdB, MMean, BMean = MeanStD(MList, BList)
  for row in MList:
    if row > (MMean + (2.5 * stdM)) or row < (MMean - (2.5 * stdM)):
      MList.remove(row)
  for row in BList:
    if row > (BMean + (2.5 * stdB)) or row < (BMean - (2.5 * stdB)):
      BList.remove(row)
  stdM, stdB, MMean, BMean = MeanStD(MList, BList)
  print(data[0][num], "for Malignant Tumours is:", round(MMean,2), "and Benign:", round(BMean,2))
  print("Standard Deviations for Malignant Tumours:", round(stdM, 2), "and Benign:", round(stdB, 2), "\n")
  PlotHistogram(MList, BList)

def MeanStD(MList, BList):
  stdM = statistics.stdev(MList)
  stdB = statistics.stdev(BList)
  BMean = statistics.mean(BList)
  MMean = statistics.mean(MList)
  return stdM, stdB, MMean, BMean

def PlotHistogram(MList, BList):
  plt.hist(MList, bins = 15, alpha = 0.8)
  plt.hist(BList, bins = 15, alpha = 0.8)
  plt.show()

def MainProgram():
  global data, benign, malignant
  data = []
  benign = []
  malignant = []
  OpenData()
  SortList()
  FrequencyMalignant()
  for column in range (2,12):
    Analysis(column)

import csv
from matplotlib import pyplot as plt
import statistics
MainProgram()

