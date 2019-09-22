#!/usr/bin/python3

"""
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
"""

"""
list = ['hello', 'python', 2019, 10]
list1 = ['你好', 'coder', 2019, 10]
print(len(list))
print(list + list1)

print(2019 in list1)

print(list[-1])
print(list[-2])
print(list[-3])
print(list[-4])
"""

"""
list = [1, 3, 5]
print(len(list))
print(max(list))
print(min(list))
"""

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






