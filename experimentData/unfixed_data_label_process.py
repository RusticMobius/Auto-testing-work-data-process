import csv
import math
import random




def sort_and_sampling(file_dir, file_name):
  type_dict = {}
  sampling_list = []
  file_path = file_dir + file_name
  output_file_path = "unfixed-label-dir/label-" + file_name
  sample_file_path = "unfixed-label-dir/sample-unfixed-label-dir/sample-unfixed-" + file_name

  sample_file = open(sample_file_path, "a+", encoding='utf8', newline='')
  output_file = open(output_file_path, "a+", encoding='utf8', newline='')
  output_writer = csv.writer(output_file)
  sample_writer = csv.writer(sample_file)
  label_list = ["close", "open", "unknown"]
  count = 0

  with open(file_path) as f:
    reader = csv.reader(f)

    for row in reader:
      if row[0] not in type_dict:
        type_dict[row[0]] = []

      type_dict[row[0]].append(row)

    for list in type_dict.values():
      # print(len(list))
      ratio_num = math.floor(len(list) * 0.2)
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

      for i in range(len(list)):
        if i not in sample_index:
          line = ["open"] + list[i]
          output_writer.writerow(line)
        else:
          row = list[i]
          count += 1
          project_name = row[1]
          spot_commit_id = row[2]
          waring_spot = row[-3].split("/")[-1] + " (" + row[-2] + ":" + row[-1] + ")"
          print(waring_spot)
          github_commit_url = "https://github.com/apache/" + project_name + "/commit/" + spot_commit_id
          print(github_commit_url)

          while (True):
            input_index = input(
              "close: 1   open: 2   unknown: 3\nenter label: ")
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
          output_writer.writerow(line)
          sample_writer.writerow(line)
          print("\n------------------- " + str(
            count) + "th item-----------------------\n")
  output_file.close()
  sample_file.close()


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
  sort_and_sampling(file_dir,file_name)
