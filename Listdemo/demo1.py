# #列表的创建
# lst=[30,'你好',3.33,'hello']
# lst1=list([90,423,513,873,90])
# print(lst)
# #列表的索引
# print(lst[1])#查询
# print(lst1[-2])
# print(lst1.index(90))#如果列表中存在两个相同的元素，只索引第一个
# #print(lst.index(000000000000000)) 如果索引的元素在列表中不存在，则会抛出ValueError
# print(lst.index('hello',0,4))#在指定的start和stop之间索引
#列表元素的增加
lst=list([40,15,646,3434,113])
lst.append(10)#在列表末尾添加一个元素
lst1=['QQ','WW']
lst.extend(lst1)#在列表末尾至少添加一个元素
lst.insert(3,'车')#在列表的指定位置添加一个元素
#在任意位置上添加多个元素   切片
lst2=[True,False,True,11,22,33]
lst[2:]=lst2 #在索引2位置开始切片，把lst2添加进lst列表，类似于覆盖
print(lst)
#列表元素的删除
lst.remove(True) #一次删除一个元素，重复元素只删除第一个列表
lst.pop(2) #删除一个指定索引位置的元素，若不指定则删除最后一个元素
print(lst)
# 列表排序
lst = [5, 6, 2, 6, 77, 2]
lst.sort()
print(lst)
lst[2:4:1]=[] #使用切片删除列表元素
print(lst)
lst.clear() #清空列表
# del lst 删除列表
# #获取列表中的元素    切片
# print(lst[1:3:1])
# print(lst1[0::2])
# print(lst1[::-1])
# print(lst1[4:1:-1])
# #判断指定元素在列表中是否存在
# print(3 in lst)
# print(90 in lst1)
# #遍历列表元素
# for i in lst:
#     print(i,end='\t')
# print()
