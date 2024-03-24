import xlrd
def read_xls_to_dict(file_path, row1, row2):
    # 打开xls文件
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)
    # 读取指定的两行
    keys = sheet.row_values(row1)[1:]
    values = sheet.row_values(row2)[1:]
    # 将两行转换为字典
    data_dict = dict(zip(keys, values))
    return data_dict
file_paths = ['国际数据主要国家(地区)年度数据_亚洲.xls', '国际数据主要国家(地区)年度数据_非洲.xls', '国际数据主要国家(地区)年度数据_拉丁美洲.xls','国际数据主要国家(地区)年度数据_欧洲.xls' , '国际数据主要国家(地区)年度数据_北美洲.xls', '国际数据主要国家(地区)年度数据_大洋洲.xls']
# 读取每个文件并生成字典
dict_list = []
for file_path in file_paths:
    data_dict = read_xls_to_dict(file_path, 2, 6)
    dict_list.append(data_dict)

from pyecharts import options as opts
from pyecharts.charts import Map

map_data=[]
# 遍历字典列表
for data_dict in dict_list:
    # 遍历字典中的每个对
    for country,value in data_dict.items():
        try:
            # 尝试将值转换为浮点数
            value = float(value)
            map_data.append((country, value))
        except ValueError:
            # 如果转换失败，说明这个值不是数字，跳过这个项
            print(f"跳过非数字值: {country}: {value}")

c = (
    Map()
    .add("2020年平均预期寿命（单位：岁）", 
         map_data,
         maptype="world",
         is_map_symbol_show=False,  # 不描点
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="世界主要国家平均预期寿命地图"),
        visualmap_opts=opts.VisualMapOpts(min_=min(value for _, value in map_data), max_=max(value for _, value in map_data), is_piecewise=True),
    )
)

c.render('./世界主要国家平均预期寿命地图.html')