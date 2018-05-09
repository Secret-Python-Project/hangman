import csv

words = set()


with open('words.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        words.add(row[0])

print(words)
