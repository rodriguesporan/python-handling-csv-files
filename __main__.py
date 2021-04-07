import csv

with open('innovators.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
      for cell in row:
        print(cell)
