import win32api
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
import pandas as pd
from pyecharts.globals import ThemeType
import win32gui

# 获取分辨率
hDC = win32gui.GetDC(0)
w = win32api.GetSystemMetrics(0)
h = win32api.GetSystemMetrics(1)
# 缩放系数
w, h = w * 0.85, h * 0.85
w = str(w)
h = str(h)

# 读取数据
df = pd.read_csv("Book1.csv")
label = ["Time", "Out_clear", "In_clear", "Out_PV", "In_PV", "Out_RRC", "In_RRC", "A_T"]
i = 0
data = []
# 处理数据
for each in label:
    each = df.iloc[:, i]
    each = each.tolist()
    data.append(each)
    i += 1
# 创建柱状图表
bar = (
    Bar(init_opts=opts.InitOpts(width=f"{w}px", height=f"{h}px", theme=ThemeType.DARK))
        .add_xaxis(data[0])
        .add_yaxis(label[1], data[1])
        .add_yaxis(label[2], data[2])
        .add_yaxis(label[3], data[3])
        .add_yaxis(label[4], data[4])
        .add_yaxis(label[5], data[5])
        .add_yaxis(label[6], data[6])
        # 设置额外纵坐标轴
        .extend_axis(
        yaxis=opts.AxisOpts(
            name="Ambient Temperature",
            type_="value",
            min_=10,
            max_=35,
            interval=5,
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
        )
    )
        # 不显示数值
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        # 设置标题及左侧纵坐标轴
        .set_global_opts(title_opts=opts.TitleOpts(title="Temperature"),
                         datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
                         yaxis_opts=opts.AxisOpts(
                             name="Temperature",
                             type_="value",
                             min_=21,
                             max_=55,
                             interval=5,
                             axislabel_opts=opts.LabelOpts(formatter="{value} ℃"),
                             axistick_opts=opts.AxisTickOpts(is_show=True),
                             splitline_opts=opts.SplitLineOpts(is_show=True),
                         ),
                         # 增加显示盒
                         tooltip_opts=opts.TooltipOpts(
                             is_show=True, trigger="axis", axis_pointer_type="cross"
                         ),
                         toolbox_opts=opts.ToolboxOpts(is_show=True, feature=opts.ToolBoxFeatureOpts(save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(is_show=True, title="保存为图片", type_="png")))
                         )
)
# 增加折线图
line = (
    Line()
        .add_xaxis(xaxis_data=data[0])
        .add_yaxis(
        series_name="Ambient Temperature",
        yaxis_index=1,
        y_axis=data[7],
        label_opts=opts.LabelOpts(is_show=False),
    )
)
# 合并图表
bar.overlap(line).render("bar_data_zoom_slider.html")
