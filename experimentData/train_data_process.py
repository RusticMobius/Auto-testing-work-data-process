import os
import csv
import random
import math

balance = True
def fix_summary_process(dir_path):
  file_list = os.listdir(dir_path)
  data_list = []
  for file_name in file_list:
    file_path = os.path.join(dir_path, file_name)
    file = open(file_path, "r", encoding='utf8', newline='')
    lines = file.readlines()
    for line in lines:
      data = ["close"]
      spot_info = line.strip().split("=>")[0].split(":")
      spot_info.pop(1)
      data.append(" ".join(spot_info))
      data_list.append(data)
    file.close()
  train_file_writer(data_list)

def unfix_summary_process(dir_path):
  file_list = os.listdir(dir_path)
  data_list = []
  for file_name in file_list:
    file_path = os.path.join(dir_path, file_name)
    file = open(file_path, "r", encoding='utf8', newline='')
    lines = file.readlines()
    for line in lines:
      l = line.strip().split(",")
      data = ["open"]
      l.pop(1)
      data.append(" ".join(l))
      data_list.append(data)
    file.close()
  if(balance):
    data_list = random.sample(data_list, math.floor(len(data_list) * 0.1))
  train_file_writer(data_list)

def train_file_writer(data_list):

  print(len(data_list))

  if(balance):
    train_data = open("model_data/balanced_train.csv", "a+", encoding='utf8', newline='')
    test_data = open("model_data/balanced_test.csv", "a+", encoding='utf8', newline='')
  else:
    train_data = open("model_data/train.csv", "a+", encoding='utf8', newline='')
    test_data = open("model_data/test.csv", "a+", encoding='utf8', newline='')

  train_writer = csv.writer(train_data)
  test_writer = csv.writer(test_data)

  for i in range(5):
    # 打乱数据集
    random.shuffle(data_list)

  data_list_len = len(data_list)

  # 计算测试集和训练集分割点，
  split_point = math.floor(data_list_len * 0.75)

  for index in range(data_list_len):
    if index < split_point:
      train_writer.writerow(data_list[index])
    else:
      test_writer.writerow(data_list[index])


  train_data.close()
  test_data.close()

if __name__ == '__main__':
  fix_summary_process("data-phases-1/fixed-project-summary")
  unfix_summary_process("data-phases-1/unfixed-project-summary")
