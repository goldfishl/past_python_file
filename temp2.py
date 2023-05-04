# ctrl + n : 新建文件
# ctrl + s : 保存文件

# from turtle import *


# color('red', 'red')
# begin_fill()
# for i in range(5):
#     fd(200)
#     rt(144)
# end_fill()
# done()

# NCRE要求的第三方库：jieba, pyinstaller, numpy
# pip install <库名>




# import turtle
# import turtle as t
# from turtle import begin_fill, end_fill, fd, rt, done
# from turtle import *


# [自定义变量名]  =  [值]
# ‘=’ 赋值运算


# var == varibale



# 数值类型：int(整数,integater), float(浮点数), complex(复数)
# var1 = 1
# var2 = 2.1
# var3 = 1.1 + 2j  # (实数，虚数)
# print(type(var1))
# print(type(var2))
# print(type(var3))

# 字符串类型: str(字符串,string)
# var4 = "Hello World"
# var5 = 'Hello World'

# print(var4[0])


# 布尔类型:bool(boolean)
# var1 = True
# var2 = False


# # 整数数据类型int，浮点数据类型float
# # 字符串类型str
# # 布尔类型bool
# var1 = int(input("输入第一个数："))
# var2 = int(input("输入第二个数："))

# print("var1的数据类型是：", type(var1))
# print("var2的数据类型是：", type(var2))
# print(var1 + var2)




# 通过input输入 12, 23
# var1 = "12"
# var2 = "23"

# 通过input输入 hello1, hello2
# var1 = "hello1"
# var2 = "hello2"

# 执行类型转换，通过input输入 12, 23
# var1 = int("12")
# var1 = int("23")

# 加了eval后，通过input输入 12, 23
# var1 = 12
# var2 = 23


# var1 = eval(input("输入第一个数据："))
# var2 = eval(input("输入第二个数据："))

# print("var1的数据类型是：", type(var1))
# print("var2的数据类型是：", type(var2))



# 考生文件夹下存在一个文件PY102.py，请写代码替换横线，键盘输入一段文本，保存在一个字符串变量s中，分别用Python内置函数及jieba库中已有函数计算字符串s的中文字符个数及中文词语个数。注意：中文字符包含中文标点符号。
# 例如，键盘输入：
# 俄罗斯举办世界杯


# 屏幕输出：
# 中文字符数为8，中文词语数为3。
# 提示：建议使用本机提供的Python集成开发环境IDLE编写、调试及验证程序。


# 俄罗斯举办世界杯 -> 俄罗斯 举办 世界杯

# import jieba
# s=input("请输入一个字符串")
# n=len(s)
# m=len(jieba.lcut(s))

# python string format
# # print("中文字符数为{}，中文词语数为{}。".format(n, m))

# print("dsad", "dsa")

# import jieba
# jieba.lcut("俄罗斯举办世界杯")

# # 
# "中文字符数为{}，中文词语数为{}。".format(n, m)

# # 计算表达式：左边运算数  操作符号  右边运算数
# var1 = 19 ** 4
# var2 = 2.1
# var3 = var1 + var2

# print("var1的数据类型为", type(var1))
# print("var2的数据类型为", type(var2))
# print("var3的数据类型为", type(var3))



# bool: True or False





# # print(var1 > 60)
# if var1 < 60:
#     print("D")

# else:
#     print("C or higher")

# var1 = eval(input("输入成绩："))

# if type(var1) != type(1) or var1 < 0 or var1 > 100:
#     print("输入内容不是整数类型，不符合要求")
#     exit()
# else:
#     if var1 < 60: #[0-59]
#         print("D")
#     elif var1 < 80: #[60-79]
#         print("C")
#     elif var1 < 90: #[80-89]
#         print("B")
#     else: # [90-100]
#         print("A")


# and 与运算
# or 或运算
# not 非运算  



# var1 = "dsadsa"
# var2 = 1232
# var3 = 1 + 8j
# list 列表数据类型
# var = [34, 56, 67, 89, 67, 45]

# index索引
# 计算机是从0开始数数
# 
# print(var[1])


# slice切片
# 起始索引号:结束索引号
# 切片结果不包含结束索引号对应的元素
# print(var[2:5])


# for i in var:
#     # 第一循环 i = var[0]
#     # 第二循环 i = var[1] 
# var = [98, 56, 67, 89, 67, 45]

# for i in var:
#     if i < 60: #[0-59]
#         print("D")
#     elif i < 80: #[60-79]
#         print("C")
#     elif i < 90: #[80-89]
#         print("B")
#     else: # [90-100]
#         print("A")
    

# 求1-50的累加和
# result = 0
# i = 1
# while i < 51:
#     result = result + i
#     i = i + 1 
# print(result)


# try:
#     n = eval(input("输入一个数字:"))
#     print(n ** 2 / 5 + 1)
# except:   
#     print("输入的不是一个数字")



# from turtle import *


# def draw(size, angle):
#     begin_fill()
#     for i in range(5):
#         fd(size)
#         rt(angle)
#     end_fill()
#     done()


# draw(200, 144)


# print(list(range(7)))

# 1-50的累加和
# sum = 0
# for i in range(51):
#     sum = sum + i
# print(sum)

# for i in range(4):
#     print("hello")

# print(min([56, 100, 90]))



# var2 = [101, 101, 90, 200]
# var3 = set(var2)
# print(len(var3))
# print(var2)


# x = [90, 67, 87, 22, 93]

# x.append(80)

# print(x)


# dictionary
# dict
# key-value

# var = {"龙金雨":173, "安德鲁":177}

# print(var["龙金雨"])
# result = 0
# for name in var.keys():
#    result = result + var[name]
# print(result / len(var)) 

# print(var.items())



# # PY103.py
# #请在...处使用一行或多行代码替换
# #注意：请不要修改其他已给出代码

# n=eval(input("请输入数量："))
# cost = 0
# if n > 0:
#     cost = cost + 160
# if n > 1:
#     if n < 5: # 买了2-4双鞋
#         cost = cost + (n-1) * 0.9 * 160
#     else:
#         cost = cost + 3 * 0.9 * 160
# if n > 4:
#     if n < 10: # 买了2-4双鞋
#         cost = cost + (n-4) * 0.8 * 160
#     else:
#         cost = cost + 5 * 0.8 * 160    
# if n > 10:
#     cost = cost + (n-10) * 0.7 * 160
# print("总额为：",cost)


var = open("/Users/longjinyu/Desktop/Code/Shell/the_missing_semester/ex2/q3.sh", "r")
print(var.read())