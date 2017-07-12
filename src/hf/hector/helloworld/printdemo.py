import datetime

__author__ = 'xudazhou'


'''
print "a",

print "gg", ""

print("b")

print "%s" % "abc",

print("ef")
'''
a = 80
print a,

# k1-v1 | END
print "%s-%s" % ("k1", "v1"), '|', 'END',

print("============ 1 ===============")

print "this is {food}".format(food="bread")  # this is bread

# 2016-12-22 15:38:42
print "%s | %s" % (datetime.datetime.fromtimestamp(1482392322),
                 "haha")
