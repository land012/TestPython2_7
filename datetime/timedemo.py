# coding: utf-8

import unittest
import time


class TimeDemo(unittest.TestCase):

    @staticmethod
    def test1():
        print(time.time())  # 1551758983.41

    @staticmethod
    def test2():
        st = time.strptime("2019-09-10 03:04:00", "%Y-%m-%d %H:%M:%S")
        """
        time.struct_time(tm_year=2019, tm_mon=9, tm_mday=10, tm_hour=3,
            tm_min=4, tm_sec=0, tm_wday=1, tm_yday=253, tm_isdst=-1)
        """
        print st
        # <type 'time.struct_time'>
        print type(st)
        print st.tm_year  # 2019
        print st.tm_mon  # 9
        print st.tm_mday  # 10
        print st.tm_hour  # 3
        print st.tm_min  # 4
        print type(st.tm_min)  # <type 'int'>
        print st.tm_sec  # 0

        day_min = st.tm_hour * 60 + st.tm_min
        print day_min  # 184
