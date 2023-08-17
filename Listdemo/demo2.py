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
lst.remove(True) #一次删除一个元素，重复元素只删除第一个
lst.pop(2) #删除一个指定索引位置的元素，若不指定则删除最后一个元素
print(lst)
lst[2:4:1]=[] #使用切片删除列表元素
print(lst)
lst.clear() #清空列表
# del lst 删除列表