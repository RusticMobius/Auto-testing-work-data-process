# Readme

## 1. raw-data

未标记的数据

导出的正报文件夹：fixed-project-summary 

导出的误报文件夹：unfixed-project-summary

## 2. labeled-data

全标记的正报文件夹：fixed-label-dir

抽样标记的误报文件夹：unfixed-label-dir



## 3. train-data

根据要求，置信学习在导出未标记的数据上执行

现已生成文件夹：model-data

balanced_test, balanced_train 调整误报比例保持数据规模不要有极端偏差的文件

test, train 未调整比例

数据量：正报296条，误报14543条



## 4. 脚本

#### clean.py

我写的置信学习脚本，可以执行

#### fix_data_label_process.py

正报标记脚本，如果不是标记数据不需执行，进行正报标记执行

#### fixed_project_summary_process.py

无需执行，已经执行过

#### trian_data_process.py

训练数据处理，无需执行，已执行过

#### unfixed_data_label_process.py

误报抽样标记脚本，如果不是标记数据不需执行，进行正报标记执行