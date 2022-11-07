import csv
with open("./data.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)