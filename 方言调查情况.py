import xlrd
def read_two_columns_to_dict(file_path, col1_index, col2_index):
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)
    data_dict = {sheet.cell(row, col1_index).value: sheet.cell(row, col2_index).value for row in range(sheet.nrows)}
    return data_dict
file_path = '方言调查情况统计.xls'
column1_index = 0  # 第一列
column2_index = 1  # 第二列
data_dict = read_two_columns_to_dict(file_path, column1_index, column2_index)

from pyecharts import options as opts
from pyecharts.charts import Map
map_data = list(data_dict.items()) #画图时需要的数据格式为list
c = (
    Map()
    .add("各省方言调查点数量（单位：个）", 
         data_pair=map_data, 
         maptype="china",
         is_map_symbol_show=True, # 描点             
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各省语言资源保护概况"),
        visualmap_opts=opts.VisualMapOpts(min_=0, max_=106, is_piecewise=True,range_color=["#F5FFFA", "#1E90FF"],),
    )
)

c.render('各省语言资源保护概况.html')