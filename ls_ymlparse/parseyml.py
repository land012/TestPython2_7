# coding: utf-8
import re

__author__ = 'xudazhou'


def parseyml(p_ymlname):
    """
    解析 yml 文件，返回一个 dict
    output_dir 输出路径，目前只支持只有一个输出路径
    :param p_ymlname:
    :return:
    """
    res_dict = dict()
    ymlfile = open(p_ymlname)
    line = ymlfile.readline()
    while line:
        line = line.rstrip()
        if line.startswith("OUTPUT_DIRS"):
            line = ymlfile.readline()
            while line:
                line = line.rstrip()
                if re.match("^\S", line) and not line.startswith("#"):
                    break
                line = line.lstrip()
                if not line.startswith("#"):
                    res_dict["output_dir"] = line
                    break
                line = ymlfile.readline()
        line = ymlfile.readline()

    return res_dict


if __name__ == "__main__":
    print(parseyml("E:\\TDDOWNLOAD\\temp\\lishantao_train.yml"))
