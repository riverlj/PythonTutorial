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