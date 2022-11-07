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

def MainProgram():
  global data, benign, malignant
  data = []
  benign = []
  malignant = []
  OpenData()
  SortList()

import csv
MainProgram()

