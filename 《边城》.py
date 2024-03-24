import jieba
import jieba.posseg as pseg

txt_filename = '边城.txt'
result_filename = '边城_形容词统计.csv'

# 从文件读取文本
txt_file = open(txt_filename, 'r', encoding='utf-8')
content = txt_file.read()
txt_file.close()
# 分词
words = pseg.cut(content) # peseg.cut返回生成器
# 用字典统计每个形容词的出现次数
word_dict = {}
count = 0
for one in words: 
    w = one.word 
    f = one.flag 
    if 'a' in f: 
        if w in word_dict.keys(): 
            if w == '老' or w == '大':
                continue
            else: 
                word_dict[w] = word_dict[w] + 1
        else:
            word_dict[w] = 1    
items_list = list(word_dict.items())
items_list.sort(key=lambda x:x[1], reverse=True)
total_num = len(items_list)
print('共有' + str(total_num) + '个可能的形容词。')
num = input('您想查看前多少个形容词？')
if not num.isdigit() or num == '':
    num = 20
else:
    num = int(num)
if num > total_num:
    num = total_num
result_file = open(result_filename, 'w')   
result_file.write('形容词,出现次数\n')
for i in range(num):
    word, cnt = items_list[i]
    message = str(i+1) + '. ' + word + '\t' + str(cnt)
    print(message)
    result_file.write(word + ',' + str(cnt) + '\n')
result_file.close()

print('已写入文件：' + result_filename)
from pyecharts.charts import WordCloud
from pyecharts import options as opts
cloud = WordCloud()
cloud.add('', 
          items_list[0:num], 
          shape='diamond', 
          is_draw_out_of_bound=False, 
          word_size_range=[10, 100],
          textstyle_opts=opts.TextStyleOpts(font_family="宋体"),
          )

cloud.set_global_opts(title_opts=opts.TitleOpts(title="《边城》形容词词云"))
out_filename = '《边城》形容词词云.html'
cloud.render(out_filename)

