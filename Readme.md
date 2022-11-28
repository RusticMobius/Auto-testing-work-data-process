# 自动化测试实验报告

#### 项目地址—— https://github.com/RusticMobius/Auto-testing-work-data-process

### 0. 组员信息

|  姓名  |   学号    |
| :----: | :-------: |
| 贺思嘉 | 181250044 |
|        |           |
|        |           |
|        |           |



### 1. 文件数据结构

#### 1.1 raw_data.zip

- 包含使用开源项目 https://github.com/lxyeah/findbugs-violations.git 工具扫描得到的初始报告等
- <img src="https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-28%2022.16.27.png" alt="截屏2022-11-28 22.16.27" style="zoom:10%;" />
- 部分项目并没有得到扫描结果，受时间限制部分扫描出来的report没能进行tracking得到正误报，在压缩包里包含了所有扫描到的报告
- 最终扫描得到正误报的项目共4个：nutch, maven-dependency-plugin, commons-collections, commons-imaging

#### 1.2 experimentData

在实验中因为收集到正报和误报数量规模差距较大，共298条正报，14000余条误报，为了探究数据规模分布对学习结果的影响我们对不同标签的数据规模进行平衡处理，处理结果对应文件文件名包含balanced

- clean_data

  置信学习去噪处理的数据文件

- data-phases-1

  扫描得到的初始数据

- fixed-label-dir

  正报标记结果文件

- unfixed-label-dir

  误报标记结果文件

- model_data

  置信学习使用的数据文件

- html

  使用echarts实现实验结果对比可视化得到的文件

- img

  比较结果图表图片



### 2. 数据预处理

#### 2.1 数据标注

警告标注工具代码及使用方式详情可见项目experimentData目录下readme文件

- 对机器扫描得到的全部正报数据进行人工标注，共标记数据298条

  - 通过人工比对正报中监测到警告的commit和监测到警告修复的commit，结合标注标准进行标注

  - fixed-label-dir目录下文件，first为第一组人工标注，second为第二组人工标注

- 对机器扫描得到的误报数据进行抽样标注，共标记数据512条

  - 通过人工比对正报中监测到警告的commit和前一次commit，结合标注标准进行标注

  - unfixed-label-dir目录下文件
  - sample-unfixed-label-dir目录下为所有抽样标注的文件

- 为了缓解人工标注过于主观的问题，我们组不同同学对数据共进行两轮标注



### 3. 置信学习

#### 3.1 代码 clean.py

#### 3.2 数据输入

- model_data目录下的文件

- 不对不同标签的数据规模进行平衡处理，直接输入所有的正报和误报，正报默认标签为“close”，误报默认标签为“open”，共14800余条数据
- 对不同标签的数据进行规模平衡处理，共1700余条数据

#### 3.3 分类器模型

- 本实验尝试了sklearn中的三种分类模型：DecisionTreeClassifier，MultinomialNB，LogisticRegression

- 由于警告数据本身的特征，缺乏语义逻辑关系，我们认为不需要过于复杂的模型


#### 3.4 警告数据去噪

- 数据去噪工具使用了开源项目cleanlab

#### 3.4 关键代码

- ```python
  # 后续实验结果对比基于使用MultinomialNB得到的去噪结果
  mnb_model = MultinomialNB()

  def model_clean(model):

    num_crossval_folds = 5
    pred_probs = cross_val_predict(model, vec_warnings, labels,
                                   cv=num_crossval_folds, method="predict_proba")

    loss = log_loss(labels, pred_probs)  # score to evaluate probabilistic predictions, lower values are better
    print(f"Cross-validated estimate of log loss: {loss:.3f}")

    predicted_labels = pred_probs.argmax(axis=1)

    # print(predicted_labels)

    acc = accuracy_score(labels, predicted_labels)

    print(f"Cross-validated estimate of accuracy on held-out data: {acc}")

    issues = CleanLearning(model).find_label_issues(vec_warnings, labels)

    print(issues)

    ranked_label_issues = find_label_issues(labels, pred_probs,
                                            return_indices_ranked_by="self_confidence")

    print(f"Cleanlab found {len(ranked_label_issues)} label issues.")
    print("Here are the indices of the top 15 most likely label errors:\n"
          f"{ranked_label_issues[:15]}")

    check_issues_labels(ranked_label_issues)


  ```

​		<img src="https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-28%2019.02.07.png" alt="截屏2022-11-28 19.02.07" style="zoom:50%;" />

​		<img src="https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-28%2019.03.17.png" alt="截屏2022-11-28 19.03.17" style="zoom:50%;" />

### 4. 实验结果对比

#### 4.1 正误报警告类型统计 —— open_warning_pie.html  close_warning_pie.html

- 正报类型统计

  ![截屏2022-11-28 17.10.10](https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-28%2017.10.10.png)

- 误报类型统计

  ![截屏2022-11-28 17.09.50](/Users/scarlett/Desktop/截屏2022-11-28 17.09.50.png)

#### 4.2 工具标注结果与人工标注结果对比 —— open_mark_bar.html close_mark_bar.html

- 正报数据标注结果对比

  <img src="https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-28%2023.21.55.png" alt="截屏2022-11-28 23.21.55" style="zoom:50%;" />

- 误报数据抽样标注结果对比

  <img src="/Users/scarlett/Library/Application Support/typora-user-images/截屏2022-11-28 23.23.23.png" alt="截屏2022-11-28 23.23.23" style="zoom:50%;" />

- 两次人工标注结果对比

  - 正报标记结果

    <img src="https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-28%2023.25.50.png" alt="截屏2022-11-28 23.25.50" style="zoom:50%;" />误报标记结果

    <img src="https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-28%2023.24.17.png" alt="截屏2022-11-28 23.24.17" style="zoom:50%;" />

#### 4.3 工具标注结果和置信学习去噪结果对比 —— clean_contrast_pie.html

- <img src="https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/%E6%88%AA%E5%B1%8F2022-11-28%2022.11.32.png" alt="截屏2022-11-28 22.11.32" style="zoom:50%;" />

#### 4.4 置信学习去噪结果和人工标记结果对比 —— clean_match_pie.html

- match表示置信学习得到的噪声数据和人工标记的噪声数据重合，miss表示置信学习得到的噪声数据未被人工标记

  <img src="https://raw.githubusercontent.com/RusticMobius/MyPicGo/main/截屏2022-11-28 23.35.01.png" alt="截屏2022-11-28 23.35.01" style="zoom:50%;" />

### 5. 实验结果分析

从图表数据可知，基于置信学习发现的噪声数据和人工标注的噪声数据重合度较高，因此我们认为置信学习能够对现有的自动化警告标记去噪
