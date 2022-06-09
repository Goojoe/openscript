import math
dict_bit={"b":0,"kb":0,"mb":0}#建立bit字典
dict_Byte={"B":0,"KB":0,"MB":0}#建立Byte字典
list_b2=["b","kb","mb"]#bit名称列表
list_B2=["B","KB","MB"]#Byte名称列表
'''
假设要转换的为：1MB
那么byte字典：
[MB:1,KB:1024,B:1024*1024]
由等比数列可得：
list[n]/list[n-1]=1024
显然此字典为等比数列
其中q为1024
MB=1024^0*a0
逆推得知a0=1
可用循环补全字典
'''
name=input()#获取已知量的名称
got_data=eval(input())#获取已知量
if name.isupper():#如果名称都是大写字母则判断为Byte字典内
    #dict_Byte[name]=got_data#放入字典对应位置
    #处理补全字典
    place=0
    for i in range(3):
        if name==list_B2[i]:
            place=2-i
            break
    a0=got_data*(math.pow(1024,i))
    for i in range(3):
        dict_Byte[list_B2[i]]=a0
        a0/=1024
    for i in range(3):
        dict_bit[list_b2[i]]=\
        dict_Byte[list_B2[i]]*8
else:
#不是大写就是小写，小写判断为bit字典内容
#下面处理情况同上
    place=0
    for i in range(3):
        if name==list_b2[i]:
            place=2-i
            break
    a0=got_data*(math.pow(1024,i))
    for i in range(3):
        dict_bit[list_b2[i]]=a0
        a0/=1024
    for i in range(3):
        dict_Byte[list_B2[i]]=\
        dict_bit[list_b2[i]]/8
print(dict_Byte)
print(dict_bit)