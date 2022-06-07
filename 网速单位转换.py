dict_bit={"b":0,"kb":0,"mb":0}#建立bit字典
dict_Byte={"B":0,"KB":0,"MB":0}#建立Byte字典
list_b2=["b","kb","mb"]#bit名称列表
list_B2=["B","KB","MB"]#Byte名称列表
name=input()#获取已知量的名称
got_data=eval(input())#获取已知量
if name.isupper():#如果名称都是大写字母则判断为Byte字典内
    dict_Byte[name]=got_data#放入字典对应位置
    #处理补全字典
    if name=="B":
        dict_Byte["KB"]=dict_Byte["B"]/1024
        dict_Byte["MB"]=dict_Byte["KB"]/1024
    elif name=="KB":
        dict_Byte["B"]=dict_Byte["KB"]*1024
        dict_Byte["MB"]=dict_Byte["KB"]/1024
    elif name=="MB":
        dict_Byte["KB"]=dict_Byte["MB"]*1024
        dict_Byte["B"]=dict_Byte["MB"]*1024
    #根据Byte字典处理bit处理字典
    for i in range(3):
        dict_bit[list_b2[i]]=dict_Byte[list_B2[i]]*8
else:
#不是大写就是小写，小写判断为bit字典内容
#下面处理情况同上
    dict_bit[name]=got_data
    if name=="b":
        dict_bit["kb"]=dict_bit["b"]/1024
        dict_bit["mb"]=dict_bit["kb"]/1024
    elif name=="kb":
        dict_bit["b"]=dict_bit["kb"]*1024
        dict_bit["mb"]=dict_bit["kb"]/1024
    elif name=="mb":
        dict_bit["kb"]=dict_bit["mb"]*1024
        dict_bit["b"]=dict_bit["mb"]*1024
    for i in range(3):
        dict_Byte[list_B2[i]]=dict_bit[list_b2[i]]/8
print(dict_Byte)
print(dict_bit)