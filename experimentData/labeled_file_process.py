import os
import csv

def file_concat(dir_path, out_path):
  write_file = open(out_path, "w", encoding='utf8', newline='')
  writer = csv.writer(write_file)
  file_list = os.listdir(dir_path)
  for file_name in file_list:
    file_path = os.path.join(dir_path, file_name)
    file = open(file_path, "r", encoding='utf8', newline='')
    reader = csv.reader(file)
    for row in reader:
      writer.writerow(row)

if __name__ == '__main__':
  dir_path = "fixed-label-dir/first"
  out_path = "fixed-label-dir/first_fixed_label.csv"
  file_concat(dir_path, out_path)
