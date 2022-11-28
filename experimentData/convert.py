import csv

with open("fixed-maven-dependency-plugin.csv", 'r') as fr:
  reader = csv.reader(fr)
  with open("fixed-label-dir/first/fixed-maven-dependency-plugin1.csv", 'w') as fw:
    writer = csv.writer(fw)
    for row in reader:
      if row[0] == "close":
        row[0] = "unknown"
      elif row[0] == "unknown":
        row[0] = "close"
      writer.writerow(row)

