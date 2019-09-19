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

### List

### Tuple

### Set

### Dictionary

