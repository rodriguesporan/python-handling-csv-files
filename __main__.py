import csv

rows = []

with open('innovators.csv', mode='r') as file:
    reader = csv.reader(file, delimiter=',')

    for row in reader:
      for cell in row:
        rows.append(cell.split(";"))

with open('innovators_new.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in rows:
      writer.writerow(row)