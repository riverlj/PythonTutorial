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

###### while else

```python
a = 1
while a < 4:
    print(a)
    a+=1
else:
    print('a 大于等于 4')
```

###### 死循环

```python
# 使用 CTRL+C 结束程序
while True:
    print('死循环')
```

例1：

```python
# 求 1 + 2 + 3 + ... + 100
sum = 1
result = 0
while sum <= 100:
    result += sum
    sum+=1
print('result = ', result)
```

##### for

```python
for var in sequence:
    # do something
else:
    # do something else
```

例1:

```python
list = ['a', 'b', 'c', 'd']
for li in list:
    print(li)
else:
    print("没有循环数据!")
```

##### break

例1: 猜数字

```python
a = 80
while True:
    number = int(input("请猜测:"))
    if number > a:
        print('大了')
    elif number < a:
        print('小了')
    else:
        print('中了')
        break
```

##### continue

例2: 打印偶数

```python
list = [1, 2, 3, 5, 6, 8, 10]
for li in list:
    if li%2!=0:
        continue
    print(li)
```

##### pass

Python pass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句，如下实例

```python
list = [1, 2, 3, 5, 6, 8, 10]
for li in list:
    if li%2!=0:
        continue
    pass
    print(li)
```