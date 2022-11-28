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

- ![截屏2022-11-25 14.36.21](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/截屏2022-11-25 14.36.21.png)

- 以testdemo为例

  ![截屏2022-11-25 14.37.52](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2014.37.52.png)

  修改file_name为标记的文件名，记得加csv后缀

  然后运行main函数

  ![截屏2022-11-25 14.39.23](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2014.39.23.png)

  控制台打印信息，对于正报标记，**需要点进控制台打开的链接（生成的需要比较的两次commit），比较第一行打印的文件和修改范围**

  

  **修改文件和范围在链接的上一行**

  ![截屏2022-11-25 14.48.01](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2014.48.01.png)

  

  进入链接

  ![截屏2022-11-25 14.46.59](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2014.46.59.png)

  

  **可以通过点击changed files迅速寻找你要查看的文件**

  ![截屏2022-11-25 14.47.12](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2014.47.12.png)

  ![截屏2022-11-25 14.47.08](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2014.47.08.png)

  进入文件，查看比较范围附近以及文件出现的修改，**然后根据作业要求里的标准来进行判断和打标签**，在控制台输入1、2、3，对应的标签有提示，回车之后**不能在脚本里修改**，请谨慎输入标签再回车，可能用到的判断标准以注释形式写在main函数上方

  ![截屏2022-11-25 14.52.14](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2014.52.14.png)



- **标注没有结束，请勿关闭控制台**，当然你可以修改我写的脚本来**保证中断之后文件不会写入异常导致之前的标签白打**

- 如果你一定要退出但是想写入之前的标签，请在输入标签时输入三个e然后回车

  - ”eee“   在fixed- label-dir生成相应文件

  ![截屏2022-11-25 14.56.30](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2014.56.30.png)

  

  标签在第一列，注意，**正报信息默认标签为close**

  ![截屏2022-11-25 14.57.15](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2014.57.15.png)

- #### <u>请不要直接push你标记的文件，打包发在群里</u>

  

#### fixed_project_summary_process.py

无需执行，已经执行过

#### trian_data_process.py

训练数据处理，无需执行，已执行过

#### unfixed_data_label_process.py

误报抽样标记脚本，如果不是标记数据不需执行，进行正报标记执行

样本数量控制逻辑已经写好，无需手动设置

- 执行前需要确认修改main函数file_name为相应文件，注意尾缀.csv，不用修改file_dir

- 以unfixed-testdemo为例 

  ![截屏2022-11-25 15.01.38](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2015.01.38.png)

- 运行main函数后控制台开始打印信息

![截屏2022-11-25 15.04.59](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2015.04.59.png)

控制台打印信息，对于误报标记，**需要点进控制台打开的链接（生成的需要比较的两次commit，在误报里默认比较前一个版本的commit，因为github无法提供比较后一个版本的commit），比较第一行打印的文件和修改范围**误报的标记比较简单，一般都为open（**误报默认标签是open**）但也需要认真比较，防止出现其他情况

![截屏2022-11-25 15.09.41](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2015.09.41.png)



**可以通过点击changed files迅速寻找你要查看的文件**

![截屏2022-11-25 15.09.55](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2015.09.55.png)





- 进入文件，查看比较范围附近以及文件出现的修改，**然后根据作业要求里的标准来进行判断和打标签**，在控制台输入1、2、3，对应的标签有提示，回车之后**不能在脚本里修改**，请谨慎输入标签再回车，可能用到的判断标准以注释形式写在main函数上方

- **标注没有结束，请勿关闭控制台**，当然你可以修改我写的脚本来**保证中断之后文件不会写入异常导致之前的标签白打**

- 如果你一定要退出但是想写入之前的标签，请在输入标签时输入三个e然后回车

  - ”eee“   在fixed- label-dir生成相应文件，这里生成两个文件，一个是包含抽样的总文件，另外一个是仅包含抽样的sample-x文件

    ![截屏2022-11-25 15.08.10](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2015.08.10.png)

​				

![截屏2022-11-25 15.12.22](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-25%2015.12.22.png)	

- #### <u>请不要直接push你标记的文件，打包发在群里</u>

  