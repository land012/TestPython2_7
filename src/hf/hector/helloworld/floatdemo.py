__author__ = 'xudazhou'

str1 = "12345678901234567890"
f1 = float(str1)
if f1 > 1000:
    print("1-1")
else:
    print(float(str1))

try:
    str2 = "123:12"
    print(float(str2))
except ValueError:
    print("error")

str3 = "-5"
print(float(str3))
