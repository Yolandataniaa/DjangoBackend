import csv

with open('polls/ft19.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  row = 0
  maxlen = 0
  nim = 0
  for column in csv_reader:
    if row == 0:
      row += 1
      continue
    nims.append(column[0])
    users.append(column[1])
    # print(f'{column[0]}\t{column[1]}')
    if len(column[1]) > maxlen:
      maxlen = len(column[1])
      nim = row
    row += 1
  print(nim, maxlen)