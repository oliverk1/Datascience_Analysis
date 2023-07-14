def OpenData():
  with open("./BreastCancer.csv", "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
      data.append(row)

def SortList():
  booleanList = []
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
  print("The Percentage of Patients with Malignant Tumours:", round((frequencyMalignant * 100), 2), "% and Benign Tumours:", round(((1-frequencyMalignant)*100), 2), "%\n")
  labels = "Malignant Tumours", "Benign Tumours"
  frequencies = [frequencyMalignant, (1 - frequencyMalignant)]
  explode = (0, 0.05)
  plt.figure("Frequency of Tumour Type")
  plt.title("Frequency of Tumour Type")
  plt.pie(frequencies, explode = explode, labels = labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
  plt.show()

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
  print("Standard Deviations for Malignant Tumours:", round(stdM, 2), "and Benign:", round(stdB, 2))
  simulation(MMean, BMean, MList, BList)
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
    print("The Means are Significantly Different and therefore from Different Populations.\n",
          data[0][num], "is more likely", difference, "in Malignant Tumours compared to Benign Tumours.\n")
  else:
    print("The Means are not Significantly Different and from the Same Population.\n")
  PlotHistogram(MList, BList, num, MMean, BMean, stdM, stdB)

def MeanStD(MList, BList):
  stdM = statistics.stdev(MList)
  stdB = statistics.stdev(BList)
  BMean = statistics.mean(BList)
  MMean = statistics.mean(MList)
  return stdM, stdB, MMean, BMean

def simulation(MMean, BMean, MList, BList):
  EqualDif = []
  MeanDif = BMean - MMean
  for i in range(1000):
    RanMList = []
    RanBList = []
    List = MList + BList
    for i in range(len(BList)):
      Element = random.choice(List)
      RanBList.append(Element)
      List.remove(Element)
    for i in range(len(MList)):
      Element = random.choice(List)
      RanMList.append(Element)
      List.remove(Element)
    RanBMean = statistics.mean(RanBList)
    RanMMean = statistics.mean(RanMList)
    RanMeanDif = RanBMean - RanMMean
    if RanMeanDif == MeanDif:
      EqualDif.append(1)
  print("Amount similar out of 1000: ", len(EqualDif))

def PlotHistogram(MList, BList, num, MMean, BMean, stdM, stdB):
  title = "Histogram of " + data[0][num]
  MeanTitle = "Malignant Tumour Mean: " + str(round(MMean, 2)) + " and"\
              + " Benign Tumour Mean: " + str(round(BMean, 2)) \
              + "\nStandard Deviation: " + str(round(stdM, 2)) \
              + " and : " + str(round(stdB, 2))
  plt.figure(title)
  plt.hist(MList, bins = 15, alpha = 0.8, label = "Malignant")
  plt.hist(BList, bins = 15, alpha = 0.8, label = "Benign")
  plt.plot(BMean, 0.5, "X", color = "orange")
  plt.plot(MMean, 0.5, "X", color="blue")
  plt.suptitle(title)
  plt.legend(title = "Tumour Type:", loc = "upper right")
  plt.title(MeanTitle, fontsize = 8)
  plt.xlabel(data[0][num])
  plt.ylabel("Number of Patients")
  plt.show()

def MainProgram():
  global data, benign, malignant
  data = []
  benign = []
  malignant = []
  OpenData()
  SortList()
  print("Using Data from", len(data), "Participants, a Two-Sided Independent T-Test will be carried out to find if there is \n"
                                      "a difference in Tumour Composition between Malignant and Benign Tumours using a 5% Significance Value.\n")
  FrequencyMalignant()
  for column in range (2,12):
    Analysis(column)

import random
import csv
from matplotlib import pyplot as plt
import statistics
import scipy
MainProgram()
