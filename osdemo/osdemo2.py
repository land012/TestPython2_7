# coding:utf-8
"""
__author__ = 'xudazhou'
"""
import os


if __name__ == "__main__":
    f = open("parts.txt")
    for line in f:
        line = line.strip()
        line2 = line[:line.rindex(".")]
        print line
        os.system("/home/work/local/hadoop-client-1.6.2/hadoop/bin/hadoop fs -conf /home/work/local/hadoop-client-1.6.2/hadoop/conf/hadoop-site-fmflow.xml -mv %s %s" % (line, line2))
