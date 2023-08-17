#列表的修改
score=list([55,99,33,66,11])
score[1]=98 #为指定索引位置赋一个新值
score[0:3:1]=[61,100,60] #使用切片修改列表元素，类似于删减
#列表的排序
score.sort() #默认升序
print(score)
score.sort(reverse=True) #降序，如果reverse=True则升序
print(score)
print('----------使用内置函数sorted()将列表进行排序，将生产生一个新的列表对象--------------')
new_score=sorted(score)
print('原列表为：',score)
print('新列表为：',new_score)
#指定关键字参数，实现l列表元素降序排序
downorder=sorted(score,reverse=True)
print(downorder)