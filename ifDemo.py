#!/usr/bin/python3


score = float(input("请输入考试成绩:"))
if score < 60:
    print('差：不及格')
elif score <= 80:
    print('良：考的不错')
elif score <= 100:
    print('优秀：再接再厉')
else:
    print('无法识别')


index = 0
while(index <= 10):
    print('index=', index)
    index += 1