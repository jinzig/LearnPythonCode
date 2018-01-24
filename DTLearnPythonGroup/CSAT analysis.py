import csv
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
from collections import Counter
import jieba.analyse

# CsvFile = csv.reader(open('/Users/sallyfan/desktop/csat2017.csv'))
# contents = []
# # for i in CsvFile:
# #     contents1  = contents.append(i)
# print(type(CsvFile))
# for i in CsvFile:
#     print(i)


openfile = open('/Users/sallyfan/desktop/cusfeedbacks.txt')
# for i in file:
#     print(i)
file = []
for i in openfile:
    file.append(i)
# print(file)
finalfile = "".join(file)
# print(type((finalfile))

# cutwords =  jieba.cut_for_search(finalfile)
cipin = jieba.analyse.textrank(finalfile, topK=20)
print(cipin)
cipin2 = jieba.analyse.extract_tags(finalfile, topK=20)
print(cipin2)

# for word in cutwords:
#     print(word)
# count  = Counter(cutwords)
# print(count)