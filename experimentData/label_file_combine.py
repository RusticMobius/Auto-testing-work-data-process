import csv

def fixed_combine():
  f1 = open("fixed-label-dir/first_fixed_label.csv",'r')
  f2 = open("fixed-label-dir/second_fixed_label.csv",'r')
  f1_list = [x for x in csv.reader(f1)]
  f2_list = [x for x in csv.reader(f2)]
  f1.close()
  f2.close()
  list = []
  match = {"open":0,"close":0,"unknown":0}
  for i in f2_list:
    for j in f1_list:
      if i == j:
        list.append(i)
        if i[0] == "open":
          match["open"] += 1
        elif i[0] == "close":
          match["close"] += 1
        else:
          match["unknown"] += 1

      elif i[1:] == j[1:]:
        i.remove(i[2])
        row = ["unknown", " ".join(i[1:])]
        list.append(row)

  with open("fixed-label-dir/fixed_label_combo.csv",'w', encoding='utf8', newline='') as out_file:
    writer = csv.writer(out_file)
    for l in list:
      writer.writerow(l)
  print(match)

if __name__ == '__main__':
    fixed_combine()
