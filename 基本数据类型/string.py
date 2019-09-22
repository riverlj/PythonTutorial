#!/usr/bin/python3

'''
var = "hello world"
print(var[0], var[1]) # 访问 
print(var[0:5]) # 截取
print(var[0:5] + ' RiverLi') # 拼接

# 遍历字符串
for i in var:
    print (i)

# 遍历字符串
for i in range(0, len(var)):
    print (var[i])
'''

'''
print('我是RiverLi\
我在写Python')
print('\\')
print('昨天看到一本书叫做\"python大全\"')
print('昨天看到一本书叫做\'21天入门python\'')
print('\a') #响了一下换了一行
print('Python真的很好学\n，三天我就入门了，\000\000\000而且\f')
'''

'''
name = 'RiverLi'
age = '28'

userInfo = name + " " + age
print(userInfo)
print(userInfo*2)
print(userInfo[0])
print(userInfo[0:7])
print('RiverLi' in userInfo)
print('RiverLi' not in userInfo)
print(r"\n")
print(R"\n")
'''

'''
print("姓名：%s, 年龄： %d, 成绩：%.1f" % ('RiverLi', 28, 93.24))

var = """其实我也是一个Python初学者
遇到了很多问题(\t)。
还在努力中[\n]。
"""
print(var)

'''

"""
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''

print(errHTML)
"""

# print('hello'.capitalize())
# print('hello'.center(12,'-'))
# print('hello'.count('l', 0, 5))

# str = "你好";
# str_utf8 = str.encode("UTF-8")
# str_gbk = str.encode("GBK")
# print(str)
# print("UTF-8 编码：", str_utf8)
# print("GBK 编码：", str_gbk)
# print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
# print("GBK 解码：", str_gbk.decode('GBK','strict'))

# print('hello'.islower())
# print('12'.isdigit())
# print('12.45'.isnumeric())
# print('hello'.endswith('o'))
# print('hello'.upper())
# print('HellO'.swapcase())