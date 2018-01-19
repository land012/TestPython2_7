# coding: utf-8
import re
"""
修改 yml
逐行读文件，然后拼接到 text，
替换需要修改的部分，
读取完整个文件
覆盖原文件
"""

__author__ = 'xudazhou'

ymlfile = open("E:\\TDDOWNLOAD\\feed_production_lishantao_train_user_model.yml", mode="r+")
text = ""
input_begin = False  # True 下一行进入 input_dir
input_end = False  # True 此行已离开 input_dir

for line in ymlfile:
    if line.startswith("INPUT_DIRS"):
        input_begin = True
        text += line
        text += "    - /rrrrr\n"
    elif input_begin and not input_end and not re.match("^\s|#", line):
        # 离开 input_dir
        input_end = True

    if input_begin and not input_end:
        # 原文件的 input dirs
        continue
    else:
        text += line

# print(text)
ymlfile.seek(0)
ymlfile.truncate()
ymlfile.write(text)
