### Python教程

#### 条件控制

通过执行一条或者多条语句的执行结果(True 或 False)来决定执行哪一个代码块。

##### if语句

```python
if 条件1:
	#do A
elif 条件2:
	#do B
else:
	#do C
```

例1：

```python
if True:
    print('True block')
    
if False:
    print('True block')
else:
    print('False block')
```

例2：

```python
score = float(input("请输入考试成绩:"))
if score < 60:
    print('差：不及格')
elif score <= 80:
    print('良：考的不错')
elif score <= 100:
    print('优秀：再接再厉')
else:
    print('无法识别')
```

##### while

```python
index = 0
while(index <= 10):
    print('index=', index)
    index += 1
```



###### for

