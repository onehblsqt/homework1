from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Grid

years = [str(year) for year in range(2022, 2014, -1)]
y1 = [681.86, 762.70, 812.60, 922.39, 1009.11, 1059.04, 1138.61, 1220.59, 1302.04]  # 内地居民登记结婚(万对)
y2 = [1.64, 1.60, 1.74, 4.94, 4.84, 4.05, 4.22, 4.12, 4.70]  # 涉外及港澳台居民登记结婚(万对)
y3 = [287.92, 283.93, 433.90, 470.06, 446.08, 437.40, 415.82, 384.14, 363.68]  # 离婚登记(万对)
y4 = [2.04, 2.01, 3.09, 3.36, 3.20, 3.15, 3.02, 2.79, 2.67]  # 粗离婚率(‰)

bar = (
    Bar()
    .add_xaxis(years)
    .add_yaxis("内地居民登记结婚(万对)", y1, stack="stack1", color="#d14a61")
    .add_yaxis("涉外及港澳台居民登记结婚(万对)", y2, stack="stack1", color="#5793f3")
    .add_yaxis("离婚登记(万对)", y3, stack="stack2", color="#87CEFA")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="粗离婚率",
            type_="value",
            min_=0,
            max_=5,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#800080")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ‰"),
        )
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="婚姻服务状况柱状图"))
)

line = (
    Line()
    .add_xaxis(years)
    .add_yaxis("粗离婚率(‰)", y4, yaxis_index=1, color="#800080", label_opts=opts.LabelOpts(is_show=False))
)

bar.overlap(line)

grid = Grid()
grid.add(bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True)
grid.render('婚姻服务状况.html')
