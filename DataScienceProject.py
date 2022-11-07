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

def RadiusComparison():
  MRadiusMean = 0
  BRadiusMean = 0
  MRadiusList = []
  BRadiusList = []
  for row in range(len(malignant)):
    MRadius = float(malignant[row][2])
    MRadiusMean = MRadiusMean + MRadius
    MRadius = round(MRadius, 0)
    MRadius = int(MRadius)
    MRadiusList.append(MRadius)
  MRadiusMean = MRadiusMean / len(malignant)
  for row in range(len(benign)):
    BRadius = float(benign[row][2])
    BRadiusMean = BRadiusMean + BRadius
    BRadius = round(BRadius, 0)
    BRadius = int(BRadius)
    BRadiusList.append(BRadius)
  BRadiusMean = BRadiusMean / len(benign)
  PlotRadius(MRadiusList, BRadiusList)

def PlotRadius(MRadiusList, BRadiusList):
  MRadiusList = np.array(MRadiusList)
  BRadiusList = np.array(BRadiusList)
  plt.hist(MRadiusList, bins = 18, alpha = 0.8)
  plt.hist(BRadiusList, bins = 12, alpha = 0.8)
  plt.show()

def MainProgram():
  global data, benign, malignant
  data = []
  benign = []
  malignant = []
  OpenData()
  SortList()
  FrequencyMalignant()
  RadiusComparison()

import csv
from matplotlib import pyplot as plt
import numpy as np
MainProgram()

