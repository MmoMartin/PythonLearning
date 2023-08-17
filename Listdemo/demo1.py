#列表的创建
lst=[30,'你好',3.33,'hello']
lst1=list([90,423,513,873,90])
print(lst)
#列表的索引
print(lst[1])#查询
print(lst1[-2])
print(lst1.index(90))#如果列表中存在两个相同的元素，只索引第一个
#print(lst.index(000000000000000)) 如果索引的元素在列表中不存在，则会抛出ValueError
print(lst.index('hello',0,4))#在指定的start和stop之间索引
#获取列表中的元素    切片
print(lst[1:3:1])
print(lst1[0::2])
print(lst1[::-1])
print(lst1[4:1:-1])
#判断指定元素在列表中是否存在
print(3 in lst)
print(90 in lst1)
#遍历列表元素
for i in lst:
    print(i,end='\t')
print()
