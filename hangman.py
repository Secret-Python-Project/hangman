import csv

with open('words.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)