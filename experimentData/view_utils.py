from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType
from pyecharts.charts import Page
import csv

open_raw_type = {}

close_raw_type = {}

with open("model_data/test.csv", 'r') as f1:
  reader = csv.reader(f1)
  for row in reader:
    # print(row)
    if row[0] == "close":
      warning = row[1].split(" ")
      if warning[0] not in close_raw_type:
        close_raw_type[warning[0]] = 1
      else:
        close_raw_type[warning[0]] += 1

    else:
      warning = row[1].split(" ")
      if warning[0] not in open_raw_type:
        open_raw_type[warning[0]] = 1
      else:
        open_raw_type[warning[0]] += 1


with open("model_data/train.csv", 'r') as f2:
  reader = csv.reader(f2)
  for row in reader:
    # print(row)
    if row[0] == "close":
      warning = row[1].split(" ")
      if warning[0] not in close_raw_type:
        close_raw_type[warning[0]] = 1
      else:
        close_raw_type[warning[0]] += 1

    else:
      warning = row[1].split(" ")
      if warning[0] not in open_raw_type:
        open_raw_type[warning[0]] = 1
      else:
        open_raw_type[warning[0]] += 1


def open_type_pie() -> Pie:
  c = (
    Pie(
        init_opts=opts.InitOpts(width="2000px",
                                height="1000px",
                                theme=ThemeType.LIGHT))
    .add(
      series_name="TYPE",
      data_pair=[list(z) for z in zip(open_raw_type.keys(), open_raw_type.values())],
      radius=["50%", "65%"],
      label_opts=opts.LabelOpts(is_show=False,
                                # position="center"),
                                )
    )
    .set_global_opts(
      legend_opts=opts.LegendOpts(pos_left="left", orient="vertical",is_show=True),
      title_opts=opts.TitleOpts(title="误报警报类型分布图",pos_right="center")
    )
    .set_series_opts(
      tooltip_opts=opts.TooltipOpts(
        trigger="item", formatter="{a} <br/>{b} : {c}  ({d}%)"
      )
    )
  )

  return c

def close_type_pie() -> Pie:
  c = (
    Pie(init_opts=opts.InitOpts(width="2000px",
                                height="1000px",
                                theme=ThemeType.LIGHT))
    .add(
      series_name="TYPE",
      data_pair=[list(z) for z in zip(close_raw_type.keys(), close_raw_type.values())],
      radius=["50%", "65%"],
      label_opts=opts.LabelOpts(is_show=False,
                                # position="center"),
                                )
    )
    .set_global_opts(
      legend_opts=opts.LegendOpts(pos_left="0%", orient="vertical",is_show=True),
      title_opts=opts.TitleOpts(title="正报警报类型分布图",pos_right="center")
    )
    .set_series_opts(
      tooltip_opts=opts.TooltipOpts(
        trigger="item", formatter="{a} <br/>{b} : {c} ({d}%)"
      )
    )
  )

  return c

type = ["close","open","unknown"]
close_raw_mark = {"close":0, "open":0, "unknown":0}
close_marked_first = {"close":0, "open":0, "unknown":0}
close_marked_second = {"close":0, "open":0, "unknown":0}

open_raw_mark = {"close":0, "open":0, "unknown":0}
open_marked_first = {"close":0, "open":0, "unknown":0}
open_marked_second = {"close":0, "open":0, "unknown":0}


noisy_balanced_data = {"close":0,"open":0,"unknown":0}
noisy_data = {"close":0,"open":0,"unknown":0}

noisy_f = open("clean_data/noisy_data.csv", 'r')
reader_nf = csv.reader(noisy_f)
nf_list = [x for x in reader_nf]
noisy_f.close()

noisy_bf = open("clean_data/noisy_balanced_data.csv", 'r')
reader_nbf = csv.reader(noisy_bf)
nbf_list = [x for x in reader_nbf]
noisy_bf.close()

for row in nf_list:
  if row[0] == "close":
    noisy_data["open"] += 1
  else:
    noisy_data["close"] += 1

for row in nbf_list:
  if row[0] == "close":
    noisy_data["open"] += 1
  else:
    noisy_data["close"] += 1

nf_analyze = {"match":0, "miss":0}
nbf_analyze = {"match":0, "miss":0}


def check_nf(row):
  for line in nf_list:
    if row[1] == line[1]:
      nf_analyze["match"] += 1
      continue
  # nf_analyze["miss"] += 1

def check_nbf(row):
  for line in nbf_list:
    if row[1] == line[1]:
      nbf_analyze["match"] += 1
      continue
  # nbf_analyze["miss"] += 1


with open("fixed-label-dir/fixed_label_combo.csv") as f0:
  reader = csv.reader(f0)
  for row in reader:
    if row[0] != "close" :
      check_nf(row)
      check_nbf(row)


def process_line(row):
  row.remove(row[2])
  data = [row[0]," ".join(row[1:])]
  return data


with open("fixed-label-dir/first_fixed_label.csv", 'r') as f3:
  reader = csv.reader(f3)
  for row in reader:
    if row[0] == "close":
      close_marked_first["close"] += 1
    elif row[0] == "open":
      close_marked_first["open"] += 1
      # check_nf(process_line(row))
      # check_nbf(process_line(row))

    elif row[0] == "unknown":
      close_marked_first["unknown"] += 1
      # check_nf(process_line(row))
      # check_nbf(process_line(row))

with open("fixed-label-dir/second_fixed_label.csv", 'r') as f4:
  reader = csv.reader(f4)
  for row in reader:
    if row[0] == "close":
      close_marked_second["close"] += 1
    elif row[0] == "open":
      close_marked_second["open"] += 1
      # check_nf(process_line(row))
      # check_nbf(process_line(row))
    elif row[0] == "unknown":
      close_marked_second["unknown"] += 1
      # check_nf(process_line(row))
      # check_nbf(process_line(row))

with open("data-phases-1/fixed-alarms.csv", 'r') as f5:
  reader = csv.reader(f5)
  for row in reader:
    close_raw_mark["close"] += 1


with open(
  "unfixed-label-dir/sample-unfixed-label-dir/first_unfixed_sample_label.csv", 'r') as f6:
  reader = csv.reader(f6)
  for row in reader:
    if row[0] == "close":
      open_marked_first["close"] += 1
    elif row[0] == "open":
      open_marked_first["open"] += 1
    elif row[0] == "unknown":
      open_marked_first["unknown"] += 1

    open_raw_mark["open"] += 1

with open(
  "unfixed-label-dir/sample-unfixed-label-dir/second_unfixed_sample_label.csv", 'r') as f7:
  reader = csv.reader(f7)
  for row in reader:
    if row[0] == "close":
      open_marked_second["close"] += 1
    elif row[0] == "open":
      open_marked_second["open"] += 1
    elif row[0] == "unknown":
      open_marked_second["unknown"] += 1
#
# with open("data-phases-1/fixed-alarms.csv",'r') as f8:
#   reader = csv.reader(f8)
#   for row in reader:
#     close_raw_mark["close"] += 1

nf_analyze["miss"] = len(nf_list) - nf_analyze["match"]
nbf_analyze["miss"] = len(nbf_list) - nbf_analyze["match"]

clean_contrast = {"noisy":0,"healthy":0}
clean_balanced_contrast = {"noisy":0,"healthy":0}

with open("clean_data/clean_raw_data.csv", 'r') as f8:
  reader = csv.reader(f8)
  for row in reader:
    if row[0] == "unknown":
      clean_contrast["noisy"] += 1
    else:
      clean_contrast["healthy"] += 1

with open("clean_data/clean_raw_balanced_data.csv", 'r') as f9:
  reader = csv.reader(f9)
  for row in reader:
    if row[0] == "unknown":
      clean_balanced_contrast["noisy"] += 1
    else:
      clean_balanced_contrast["healthy"] += 1

print(clean_contrast)
print(clean_balanced_contrast)
print(nf_analyze)
print(nbf_analyze)
print(open_raw_mark.values())
print(close_raw_mark.values())

def clean_contrast_pie() -> Pie:
  c = (
    Pie(init_opts=opts.InitOpts(width="50%",
                                # height="800px",
                                theme=ThemeType.VINTAGE))
      .add(
      series_name="MATCH",
      radius=["25%", "65%"],
      data_pair=[list(z) for z in
                 zip(clean_contrast.keys(), clean_contrast.values())],
      label_opts=opts.LabelOpts(is_show=True,
                                # position="center"),
                                formatter="{b} : {c} ({d}%)",
                                font_size=24
                                )
    )
      .set_global_opts(
      legend_opts=opts.LegendOpts(pos_bottom="0%",
                                  orient="horizontal",
                                  is_show=True,
                                  item_height=25,
                                  item_width=45,
                                  item_gap=45,
                                  textstyle_opts=opts.TextStyleOpts(
                                    font_size=16)
                                  ),
      title_opts=opts.TitleOpts(title="置信学习噪声数据标记情况", pos_right="center")
    )
      .set_series_opts(
      tooltip_opts=opts.TooltipOpts(
        trigger="item", formatter="{b} : {c} ({d}%)"
      )
    )
  )
  return c

def clean_balanced_contrast_pie() -> Pie:
  c = (
    Pie(init_opts=opts.InitOpts(width="50%",
                                # height="800px",
                                theme=ThemeType.VINTAGE))
      .add(
      series_name="MATCH",
      radius=["25%", "65%"],
      data_pair=[list(z) for z in
                 zip(clean_balanced_contrast.keys(), clean_balanced_contrast.values())],
      label_opts=opts.LabelOpts(is_show=True,
                                # position="center"),
                                formatter="{b} : {c} ({d}%)",
                                font_size=24
                                )
    )
      .set_global_opts(
      legend_opts=opts.LegendOpts(pos_bottom="0%",
                                  orient="horizontal",
                                  is_show=True,
                                  item_height=25,
                                  item_width=45,
                                  item_gap=45,
                                  textstyle_opts=opts.TextStyleOpts(
                                    font_size=16)
                                  ),
      title_opts=opts.TitleOpts(title="置信学习噪声数据标记情况(数据规模平衡处理过）", pos_right="center")
    )
      .set_series_opts(
      tooltip_opts=opts.TooltipOpts(
        trigger="item", formatter="{b} : {c}"
      )
    )
  )
  return c


def nf_match_pie() -> Pie:
  c = (
    Pie(init_opts=opts.InitOpts(width="50%",
                                # height="800px",
                                theme=ThemeType.ROMA))
      .add(
      series_name="MATCH",
      radius=["25%", "65%"],
      data_pair=[list(z) for z in
                 zip(nf_analyze.keys(), nf_analyze.values())],
      label_opts=opts.LabelOpts(is_show=True,
                                # position="center"),
                                formatter="{b} : {c} ({d}%)",
                                font_size=24
                                )
    )
      .set_global_opts(
      legend_opts=opts.LegendOpts(pos_bottom="0%",
                                  orient="horizontal",
                                  is_show=True,
                                  item_height=25,
                                  item_width=45,
                                  item_gap=45,
                                  textstyle_opts=opts.TextStyleOpts(
                                    font_size=16)
                                  ),
      title_opts=opts.TitleOpts(title="置信学习噪声数据和人工标注数据对比情况", pos_right="center")
    )
      .set_series_opts(
      tooltip_opts=opts.TooltipOpts(
        trigger="item", formatter="{b} : {c}"
      )
    )
  )
  return c

def nbf_match_pie() -> Pie:
  c = (
    Pie(init_opts=opts.InitOpts(width="50%",
                                # height="800px",
                                theme=ThemeType.ROMA))
      .add(
      series_name="MATCH",
      radius=["25%", "65%"],
      data_pair=[list(z) for z in
                 zip(nbf_analyze.keys(), nbf_analyze.values())],
      label_opts=opts.LabelOpts(is_show=True,
                                # position="center"),
                                formatter="{b} : {c} ({d}%)",
                                font_size=24
                                )
    )
      .set_global_opts(
      legend_opts=opts.LegendOpts(pos_bottom="0%",
                                  orient="horizontal",
                                  is_show=True,
                                  item_height=25,
                                  item_width=45,
                                  item_gap=45,
                                  textstyle_opts=opts.TextStyleOpts(
                                    font_size=16)
                                  ),
      title_opts=opts.TitleOpts(title="置信学习噪声数据(数据规模平衡处理过)和人工标注数据对比情况", pos_right="center")
    )
      .set_series_opts(
      tooltip_opts=opts.TooltipOpts(
        trigger="item", formatter="{b} : {c}"
      )
    )
  )
  return c

def close_mark_bar() -> Bar:
  b = (
    Bar(init_opts=opts.InitOpts(width="1600px",
                                height="1000px",
                                theme=ThemeType.LIGHT
                                ))
    .add_xaxis(type)
    .add_yaxis("工具标注",[x for x in close_raw_mark.values()])
    .add_yaxis("人工标注第一组",[x for x in close_marked_first.values()])
    .add_yaxis("人工标注第二组",[x for x in close_marked_second.values()])
    .set_global_opts(
      xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size = 26)),
      yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size = 20)),
      legend_opts=opts.LegendOpts(orient="horizontal",
                                  is_show=True,
                                  item_gap = 50,
                                  item_height=25,
                                  item_width=45,
                                  textstyle_opts=opts.TextStyleOpts(
                                    font_size=16)
                                  ),
      title_opts=opts.TitleOpts(title="正报标记对比图",
                                pos_left="50px",
                                )

    )
    .set_series_opts(label_opts=opts.LabelOpts(font_size=26))
  )
  return b

def open_mark_bar() -> Bar:
  b = (
    Bar(init_opts=opts.InitOpts(width="1600px",
                                height="1000px",
                                theme=ThemeType.LIGHT
                                ))
    .add_xaxis(type)
    .add_yaxis("工具标注",[x for x in open_raw_mark.values()])
    .add_yaxis("人工标注第一组",[x for x in open_marked_first.values()])
    .add_yaxis("人工标注第二组",[x for x in open_marked_second.values()])
    .set_global_opts(
      xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=26)),
      yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=20)),
      legend_opts=opts.LegendOpts(orient="horizontal",
                                  is_show=True,
                                  item_gap=50,
                                  item_height=25,
                                  item_width=45,
                                  textstyle_opts=opts.TextStyleOpts(font_size=16)
                                  ),

      title_opts=opts.TitleOpts(title="误报标记对比图", pos_left="50px"),

    )
    .set_series_opts(label_opts=opts.LabelOpts(font_size=26))

  )

  return b



open_type_pie().render("../html/open_warning_pie.html")
close_type_pie().render("../html/close_warning_pie.html")

close_mark_bar().render("../html/close_mark_bar.html")
open_mark_bar().render("../html/open_mark_bar.html")

page1 = Page()
page1.add(nf_match_pie(),nbf_match_pie())
page1.render("../html/clean_match_pie.html")

page2 = Page()
page2.add(clean_contrast_pie(),clean_balanced_contrast_pie())
page2.render("../html/clean_contrast_pie.html")
