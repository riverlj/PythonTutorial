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
var2 = 20	基本数据类型
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

例子

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
元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号表示，列表使用中(方)括号表示。
```python
#!/usr/bin/python3

tuple1= ('riverli', 1992, "01-06", 28)
tuple2 = ('python', "learn", 1)

# tuple1[0] = 12 非法
tuple3 = tuple1 + tuple2
print('tuple3=', tuple3) # tuple3= ('riverli', 1992, '01-06', 28, 'python', 'learn', 1)

del tuple3
print ("删除后的元组 tuple3 : ")
# print('tuple3=', tuple3) # NameError: name 'tuple3' is not defined

print("元组tuple1的长度为: ", len(tuple1))
print("元组tuple1的复制4次: ", tuple1 * 4)
print('\'riverli\' 在tuple1中：', 'riverli' in tuple1)

for x in tuple1:
    print('x =', x)

list1 = [1, 2, 3, 4]
print('list to tuple:', tuple(list1))

print('tuple1[2]=', tuple1[2])
print('tuple1[-1]=', tuple1[-1])
print('tuple1[1:]=', tuple1[1:])
```

### Set

集合是一个无序的不重复的元素序列。

创建空的集合要使用`set()`，不能使用`{}`。

```python
set1 = set()
dict1 = {}

print(type(set1))
print(type(dict1))

# <class 'set'>
# <class 'dict'>
```

创建集合

```python
set2 = {'hello', 'python', 'learn'}
set3 = set('nihao')
print(set2)
print(set3)
# {'python', 'learn', 'hello'}
# {'a', 'h', 'i', 'n', 'o'}
```

集合运算

```python
a = set('abcd')
b = set('cdef')
print(a-b) # 集合a中包含而集合b中不包含的元素
print(a|b) # 集合a或b中包含的所有元素
print(a&b) # 集合a和b中都包含了的元素
print(a^b) # 不同时包含于a和b的元素
# {'b', 'a'}
# {'d', 'e', 'a', 'f', 'c', 'b'}
# {'c', 'd'}
# {'e', 'a', 'f', 'b'}
```

增加元素

```python
set1 = {'ni', 'hao'}
set1.add('2019')
print(set1)
set1.add('ni')
print(set1)
# {'hao', '2019', 'ni'}
# {'hao', '2019', 'ni'}

set1.update('10')
set1.update({1,4})
set1.update((2,5))
print(set1)
# {1, 2, '2019', 4, 5, 'ni', '1', '0', 'hao'}
```

移除元素

```python
set1 = {'hello', 'python', '2019'}
set1.remove('hello')
print(set1) # {'2019', 'python'}
# set1.remove('riverli') #KeyError: 'riverli'
set1.discard('riverli') # 如果元素不存在，不会发生错
print(set1) # {'2019', 'python'}
set1.pop() # 随机删除集合中的一个元素
print(set1)
```

其他

```python
set1 = {'hello', 'python', '2019'}
print(len(set1))
print('hello' in set1)
set1.clear()
print(set1)
# 3
# True
# set()
```



### Dictionary
字典是可变容器，可以存储任意类型的对象。对象以键值对(key=>value)的方式存储，键与值之间以及冒号分割，对象之间以逗号分割，字典使用大括号表示。
```python
dic = {'lan':'python', 'version': '3.0'}
print('dic=', dic)
```

**键必须是唯一的且不可变，如字符串、数字、元组，值可以取任何数据类型**
```python
dic = {'lan':'python', 3.14: '3.0', (1,2,4): [1,2,4]}
print('dic=', dic)
```
增删改查
``` python
dic = {'name': 'riverli', 'age': 18}
print('dic[name]=', dic['name'])
print('dic[age]=', dic['age'])
# print('dic[sex]=', dic['sex']) #KeyError: 'sex'

dic['sex'] = '男'
print('dic[sex]=', dic['sex'])
dic['age'] = 20
print('dic[age]=', dic['age'])

'''
del dic['age']
print('dic[age]=', dic['age']) #KeyError: 'age'
'''

dic.clear()
print('dic=', dic)
del dic 
print('dic=', dic) # NameError: name 'dic' is not defined

 for x in dic:
    print('key=', x, 'value=', dic[x])
```

特性解释
1. 不允许同一个键出现两次，如果出现以最后的值为准。
2. 键必须是不可变的。所以可以用 数字 字符串 或者 元组。
```python
dic = {'name': 'riverli', 'age': 18, 'name': 'pete'}
print('dic[name]=', dic['name'])

# dic2 = {'name': 'pete', 28: 28, (1, 2): 12}
# dic3 = {'name': 'pete', 28: 28,[1, 2]: 12} # TypeError: unhashable type: 'list'
```
相关函数



