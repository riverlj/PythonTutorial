#!/usr/bin/python3
# dic = {'lan':'python', 'version': '3.0'}
# print('dic=', dic)

# dic = {'lan':'python', 3.14: '3.0', (1,2,4): [1,2,4]}
# print('dic=', dic)


# for x in dic:
#     print('key=', x, 'value=', dic[x])

'''
dic = {'name': 'riverli', 'age': 18}
print('dic[name]=', dic['name'])
print('dic[age]=', dic['age'])
# print('dic[sex]=', dic['sex']) #KeyError: 'sex'

dic['sex'] = '男'
print('dic[sex]=', dic['sex'])
dic['age'] = 20
print('dic[age]=', dic['age'])


# del dic['age']
# print('dic[age]=', dic['age']) #KeyError: 'age'


dic.clear()
print('dic=', dic)
del dic 
print('dic=', dic) # NameError: name 'dic' is not defined
'''

dic = {'name': 'riverli', 'age': 18, 'name': 'pete'}
print('dic[name]=', dic['name'])

# dic2 = {'name': 'pete', 28: 28, (1, 2): 12}
# dic3 = {'name': 'pete', 28: 28,[1, 2]: 12} # TypeError: unhashable type: 'list'


print('dic的长度：', len(dic))
print('dic to string：', str(dic))
