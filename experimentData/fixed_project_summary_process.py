import csv

def create_project_summary(file_path):
  with open(file_path) as f:
    reader = csv.reader(f)
    project_list=[]
    for row in reader:
      commits_info = row[0].split("=>")
      spot_commit_info = commits_info[0].split(":")
      project_name = spot_commit_info[1]
      if project_name not in project_list:
        project_list.append(project_name)
        new_file_path = "data-phases-1/fixed-project-summary/fixed-"+ project_name + ".csv"
        with open (new_file_path,"a") as new_file:
          writer = csv.writer(new_file)
          writer.writerow(row)
      else:
        new_file_path = "data-phases-1/fixed-project-summary/fixed-" + project_name + ".csv"
        with open(new_file_path, "a") as new_file:
          writer = csv.writer(new_file)
          writer.writerow(row)


if __name__ == '__main__':
    create_project_summary("data-phases-1/fixed-alarms.csv")
