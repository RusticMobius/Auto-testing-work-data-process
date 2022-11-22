import csv

def label_process(file_dir, file_name):

  file_path = file_dir + file_name

  output_file_path = "fixed-label-dir/fixed-" + file_name

  write_file = open(output_file_path, "a+", encoding='utf8', newline='')
  writer = csv.writer(write_file)



  with open(file_path) as f:
    reader = csv.reader(f)
    label_list = ["close","open","unknown"]
    count = 0
    # lenth = len(f.readlines())
    for row in reader:
      count += 1;
      commits_info = row[0].split("=>")
      spot_commit_info = commits_info[0].split(":")
      fix_commit_info = commits_info[1].split(":")

      project_name = spot_commit_info[1]
      spot_commit_id = spot_commit_info[2]
      spot_target_file = spot_commit_info[3].split("/")[-1]
      spot_commit_start_line = spot_commit_info[-2]
      spot_commit_end_line = spot_commit_info[-1]

      fix_commit_id = fix_commit_info[1]
      fix_target_file = fix_commit_info[2].split("/")[-1]

      file_compare = spot_target_file + "(" + spot_commit_start_line + ":" + spot_commit_end_line + ")" + " => " + fix_target_file
      git_compare_url = "https://github.com/apache/" + project_name + "/compare/" + spot_commit_id + ".." + fix_commit_id

      print(file_compare)
      print(git_compare_url)

      while(True):
        input_index = input("close: 1   open: 2   unknown: 3\nenter label: ")
        if (input_index) == "eee":
          return
        try:
          label_index = int(input_index) - 1
          if(label_index > 2 or label_index < 0):
            print("check your input!\n")
            continue
          else:
            break
        except:
          print("check your input!\n")

      label = label_list[label_index]
      line = [label] + spot_commit_info
      writer.writerow(line)
      print("\n------------------- " + str(count) + "th item-----------------------\n")


  write_file.close()
# 1. If method/file containing a warning was removed, label the warning as
# "unknown"

# 2. If the warning was removed, but a large amount of code was changed
# (e.g. a refactoring of the entire class, a change in functionality),
# label the warning as
# "unknown".

# 3. If the warning was removed, but the code is still similar to the original code,
# and the warning/bug still appears to be present, label the warning as
# "open"

# 4. If the warning was removed, but the original code looked to be a
# false positive, and you believe that the code was changed just to
# silence the false alarm from findbugs/spotbugs, label the warning
# "open"

# 5. If the code appears to be automatically generated, label the  warning
# "unknown"



if __name__ == '__main__':
    # e. for file "data-phases-1/fixed-project-summary/maven-dependency-plugin.csv"
    # --> parameter filr_dir: "data-phases-1/fixed-project-summary/"
    # --> parameter file_name: "maven-dependency-plugin.csv"

    file_dir = "data-phases-1/fixed-project-summary/"
    file_name = "maven-dependency-plugin.csv"

    label_process(file_dir, file_name)
