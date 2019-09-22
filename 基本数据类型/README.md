### 基本数据类型

Python中的变量是不需要声明的，每个变量在使用之前都必须赋值，变量赋值以后该变量才会被创建。变量没有具体的类型，我们所说的类型是变量所指的内存中对象的类型。

使用`=`来个变量赋值，等号左边是变量名，等号右边是存储在变量中的值。

```python
numberInt = 64 # Int 整型
numberFloat = 3.14 # float 浮点数
numberBool = False # 布尔值
string = 'hello world' # 字符串
```

#### 多变量赋值

```python
a = b = c = 5
m, n, k = 5, 6, 'hellow'
print ('a=', a, 'b=', b, 'c=', c)
print ('m=', m, 'n=', n, 'k=', k)
```

#### 变量的声明与删除：

```python
var1 = 10
var2 = 20
print(var1)
print(var2)

del var1
print(var1)
print(var2)
```

### Number

- int
- float
- bool
- complex



#### 数据类型转换

```python
var1 = 10
var2 = 3.14
var3 = True
var4 = complex(10,12)
var5 = 12+7j

print(var1, var2, var3, var4, var5)

var1 = float(var1)
var2 = int(var2)
var6 = complex(3)
print(var1, var2, var3, var4, var5, var6)
```

#### 进制表示

```python
var = 0xA #十六进制  10
var1 = 0o13 #八进制 11
print(var)
print(var1)
```

#### 数学运算

```python
print(2+2)
print(2-2)
print(2*2)
print(2/2)  # 1.0 总是返回一个浮点数
print(2//2)  # 1
print(2//2.0)  # 1.0
print(5-3*2) # -1
```

1. `/` 总是返回浮点数
2. `//` 会丢弃小数部分，但是如果参与计算的数字为浮点数，返回结果也是浮点数。
3. 不同类型的数混合运算时会将整数转换为浮点数。

#### 数学函数

```python
import math

print(abs(-10)) #取绝对值, 返回整数
print(math.fabs(-10)) #取绝对值, 返回浮点数
print(math.ceil(3.14)) # 向上取整
print(math.floor(3.14)) # 向下取整
print(max(1, 2, 3)) # 返回最大值
print(min(1, 2, 3)) # 返回最小值
print(math.modf(3.14)) # 返回参数的小数部分和整数部分，符号与参数的符号一样，整数部分以浮点数的形式返回
print(round(3.254, 1)) # 四舍五入
print(round(3.254, 2))
```

**随机数**

```python
result = random.choice([1,2,3,4,5,6])
print(result)

result = random.randrange(0, 100, 2) # 第一个参数和最后一个参数可选，默认值为0 和 1 范围[1, 100)
print(result)

result = random.randrange(100)
print(result)

result = random.random() #[0, 1)
print(result)

list = [1,2,3,4,5]
random.shuffle(list) 
print(list)

result = random.uniform(1, 10) #[1, 10) 实数
print(result)

random.seed()
print (random.random())

random.seed('你好')
print (random.random())
random.seed('你好')
print (random.random())

random.seed(4)
print (random.random())
```



### String

使用 `'` 或者 `"`  框起来 表示字符串。

```python
var = "Hello World"
var1 = 'Hello RiverLi'
```

#### 常见操作

```python
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
```

#### 转义字符

![转义字符表](https://riverli.oss-cn-beijing.aliyuncs.com/PythonTutorial/python%E8%BD%AC%E4%B9%89%E5%AD%97%E7%AC%A6.jpg)

```python
print('我是RiverLi\
我在写Python')
print('\\')
print('昨天看到一本书叫做\"python大全\"')
print('昨天看到一本书叫做\'21天入门python\'')
print('\a') #响了一下换了一行
print('Python真的很好学\n，三天我就入门了，\000\000\000而且\f')
```

#### 运算

```python
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
```

#### 格式化输出

```python
print("姓名：%s, 年龄： %d, 成绩：%.1f" % ('RiverLi', 28, 93.24))
```

![字符串格式化输出](https://riverli.oss-cn-beijing.aliyuncs.com/PythonTutorial/%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%A0%BC%E5%BC%8F%E5%8C%96%E8%BE%93%E5%87%BA.png)

**在Python3中，所有的字符串都是Unicode字符串。Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集**

#### 常见函数

```python
print('hello'.capitalize())
print('hello'.center(12,'-'))
print('hello'.count('l', 0, 5))

str = "你好";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))

print('hello'.islower())
print('12'.isdigit())
print('12.45'.isnumeric())
print('hello'.endswith('o'))
print('hello'.upper())
print('HellO'.swapcase())
```

### List 

```python
list = ['hello', 'python', '!', 'I', 'Love', 'you']
```

类似于其他语言中的数组。

```python
list = ['hello', 'python', 2019, 10]

print('查询：')
print(list[0], list[1])
print(list[0:3])

print('遍历：')
for li in list:
    print(li)

print('增加：')
list.append('good')
print(list)

print('修改：')
list[1] = 'RiverLi'
print(list)

print('删除：')
del list[0]
print(list[0])
```

#### 函数操作

```python
list = [4, 3, 5, 6, 4, 5, 4]
list.append(8)
print(list)
print(list.count(4))
list.extend([1,2,3])
print(list)
print(list.index(2))
list.insert(0,0)
print(list)
print(list.pop())
print(list)
list.remove(4)
print(list)
list.reverse()
print(list)
list.sort()
print(list)
newList = list.copy()
print(newList)
list.clear()
print(list)
```

### Tuple

### Set

### Dictionary

