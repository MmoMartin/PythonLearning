#key的判断
cathouse={'白猫':5,'橘猫':13,'黑猫':3,'玩具猫':21}
print('红猫'in cathouse)
print('哈士奇'not in cathouse)
#字典元素的删除
del cathouse['玩具猫']
print(cathouse)
#cathouse.clear()
#字典元素的添加
cathouse['黑白相间猫']=1
print(cathouse)
#字典元素的修改
cathouse['黑白相间猫']=2
print(cathouse)
#获取字典视图
print(cathouse.keys()) #获取字典中所有key
print(cathouse.values()) #获取字典中所有value
print(cathouse.items()) #获取字典中所有key，value对
#字典元素的遍历
for catcate in cathouse:
    print(catcate)
for c in cathouse:
    print(c,cathouse[c])