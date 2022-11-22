import csv

def label_process(file_path):



  with open(file_path) as f:
    reader = csv.reader(f)
    label_list = ["close","open","unknown"]
    for row in reader:
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
      label_index = int(input("close: 1   open: 2   unknown: 3\nenter label: ")) - 1
      label = label_list[label_index]
      print("------------------------------------------")

      write_file_path = "data-phases-1/fixed-project-summary/fixed-label-dir/" + project_name + ".csv"
      with open(write_file_path,"a+",encoding='utf8',newline='') as write_file:
        writer = csv.writer(write_file)
        line = [label] + spot_commit_info
        writer.writerow(line)





if __name__ == '__main__':
    label_process("data-phases-1/fixed-project-summary/maven-dependency-plugin.csv")
