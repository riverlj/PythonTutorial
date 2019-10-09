#!/usr/bin/python3

'''
set1 = set()
dict1 = {}

print(type(set1))
print(type(dict1))

# <class 'set'>
# <class 'dict'>

set2 = {'hello', 'python', 'learn'}
set3 = set('nihao')
print(set2)
print(set3)
# {'python', 'learn', 'hello'}
# {'a', 'h', 'i', 'n', 'o'}


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
'''

'''
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
'''

'''
set1 = {'hello', 'python', '2019'}
set1.remove('hello')
print(set1) # {'2019', 'python'}
# set1.remove('riverli') #KeyError: 'riverli'
set1.discard('riverli') # 如果元素不存在，不会发生错
print(set1) # {'2019', 'python'}
set1.pop() # 随机删除集合中的一个元素
print(set1)
'''

set1 = {'hello', 'python', '2019'}
print(len(set1))
print('hello' in set1)
set1.clear()
print(set1)