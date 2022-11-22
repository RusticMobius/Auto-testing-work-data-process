import csv
import math
import random

def label_process(file_dir, file_name):

  file_path = file_dir + file_name
  sample_list = sort_and_sampling(file_path)

  output_file_path = "unfixed-label-dir/unfixed-" + file_name

  with open(output_file_path, "a+", encoding='utf8', newline='') as write_file:
    writer = csv.writer(write_file)
    label_list = ["close", "open", "unknown"]
    count = 0
    for row in sample_list:
      count += 1
      project_name = row[1]
      spot_commit_id = row[2]
      waring_spot = row[-3].split("/")[-1] + " (" + row[-2] + ":" + row[-1] + ")"
      print(waring_spot)
      github_commit_url = "https://github.com/apache/" + project_name + "/commit/" + spot_commit_id
      print(github_commit_url)

      while (True):
        input_index = input("close: 1   open: 2   unknown: 3\nenter label: ")
        if (input_index) == "eee":
          return
        try:
          label_index = int(input_index) - 1
          if (label_index > 2 or label_index < 0):
            print("check your input!\n")
            continue
          else:
            break
        except:
          print("check your input!\n")

      label = label_list[label_index]
      line = [label] + row
      writer.writerow(line)
      print("\n------------------- " + str(count) + "th item-----------------------\n")



def sort_and_sampling(file_path):
  type_dict = {}
  sampling_list = []
  with open(file_path) as f:
    reader = csv.reader(f)

    for row in reader:
      if row[0] not in type_dict:
        type_dict[row[0]] = []
      else:
        type_dict[row[0]].append(row)

    for list in type_dict.values():
      # print(len(list))
      ratio_num = math.floor(len(list) * 0.02)
      if ratio_num > 10:
        sample_num = 10
      elif ratio_num < 1:
        if len(list) < 5:
          sample_num = len(list)
        else:
          sample_num = 5
      else:
          sample_num = ratio_num
      sample_index = random.sample(range(len(list)),sample_num)

      for index in sample_index:
        sampling_list.append(list[index])

  print("total " + str(len(sampling_list)) + " samples")
  return sampling_list

# 1. If the method/field containing the warning/bug was renamed, but
# the warning/bug still appears to be present, label the warning as
# "unknown".

# 2. If the statements containing the warning/bug was moved to a
# different method, but the warning/bug still appears to be present
# in these statements, label the warning as
# "unknown"

# 3. If the warning was removed, but the code is still similar to the
# original code, and the warning/bug still appears to be present,
# label the warning as
# "open".

if __name__ == '__main__':
  file_dir = "data-phases-1/unfixed-project-summary/"
  file_name = "unfixed-nutch.csv"
  label_process(file_dir,file_name)
