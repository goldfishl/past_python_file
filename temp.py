# flag = True
# num = 2022
# while flag:
#     if str(bin(num))[:-6].count("0") == 6:
#         print(num)
#         flag = False
#     num += 1


# from datetime import datetime
# a = datetime(1949, 10, 1)
# b = datetime(2022, 1, 1)

# print(b-a)


# for in range(10):
# num=[]
# i=2
# for i in range(2,2022):
#    j=2
#    for j in range(2,i):
#       if(i%j==0):
#          break
#    else:
#       num.append(i)
# print(num)


# import math 
# def judge_prime(n):
#     if (n == 0 or n == 1): return False
#     if (n == 2): return True
#     if (n % 2 == 0): return False
#     # 判断
#     if 0 in [n % i for i in range(2, int(math.sqrt(n) + 1))]:
#         return False
#     return True

# def equal_prime(n):
#     '''n拆分成素数之和'''
#     plist = [i for i in range(n + 1) if judge_prime(i)]
#     DFS(n, 0, 0, plist, S=set())
    
# def DFS(n, index=0, sum_num=0, primes=[], L=[], S=set()):
#     if (sum_num > n):
#         return
#     if (sum_num == n):
#         if (tuple(L) not in S):  # 避免重复输出
#             print(len(L))
#             print(L)
#             S.add(tuple(L))
#             z = input()
            
#     # 只要index没有超过素数表primes的长度，就可以继续选择，超过了则不操作，迭代返回上一层
#     if (index < len(primes)):
#         # sum==n 找到了这样的一组数字
#         L.append(primes[index])
#         DFS(n, index + 1, sum_num + primes[index], primes, L, S)
#         L.pop()
#         DFS(n, index + 1, sum_num, primes, L, S)

# equal_prime(2022)

# # 第7题
# num = int(input())
# words = [input() for _ in range(num)]
# _words = []
# for w in words:
#     if w not in _words:
#         _words.append(w)
# print("\n".join(_words))

# # 第十题
# def bubbleSort(arr):
#     cost = 0
#     n = len(arr)
 
#     # 遍历所有数组元素
#     for i in range(n):
 
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
 
#             if arr[j] > arr[j+1] :
#                 cost += arr[j]
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
                
#     print(cost)

# _ = int(input())
# num = [int(i) for i in input().split(" ")]

# bubbleSort(num)

# # 第六题
# inputstr = input()
# input_num = [int(i) for i  in inputstr.split(" ")]

# a = (input_num[0] * input_num[2]) / input_num[1] - input_num[0]
# print(int(a))


# #第八题
# input_str = input()
# s_list = list(input_str)

# for i in range(len(s_list)):
#     temp_list = s_list[::-1]
#     o_list = s_list+ temp_list[-(i+1):]
#     # print(o_list)
#     if o_list == o_list[::-1]:
#         break
# print("".join(o_list))


#第三题
# for i in range(10,10000):
#     if eval("0x"+str(i)) % i == 0:
#         print(i)
#         z=input()


# # 第四题
# def maxPathSum(grid):
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if i == j == 0: 
#                 continue
#             elif i == 0:  
#                 grid[i][j] = grid[i][j - 1] + grid[i][j]
#             elif j == 0:  
#                 grid[i][j] = grid[i - 1][j] + grid[i][j]
#             else: 
#                 grid[i][j] = max(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
#     return grid[-1][-1]

# #%%
# import numpy as np


# input_num = "174094882455171152761423221685761892795431233411387427793198650286024865090061389344606618496378829135984076361542097372601657541200146071777733599818266038012509478351201640618984143988087783837107349651099683484992553337438088068198972282890781586124258626539246182119762952003918195325258677229419698255491250839396799769357665825441616335532825361862146291503649293440596342887581257444442930778730382520372975343211325351222640703400531067500454956482168314849207060705673849265774579830223671554026061117300483012903885770893074783710083450145620356667677191627276513995926532444279237315785832411595106453089134746365281031552217482363035280722591085079053410485925413958279617719034175332412908745680774313630190429314820559328748143552689295945058801322270313370955837837939182801848609300876356583948397645861551964542532682663945625356614462682551015176002433628234343684739800880514363921982340231989891351425389287014819359798014755509282450440511590838726938103384801541373585690893606978941566666714061214952341523168827712604946036245881214982452998386986623826275782780208928205527678781609589000725521486468983551558405472149903035076783644195574734088152324666290493119955560594634905391288186024902215444250421277955403412298227858394469856607272647132163832860126054679347881638761723785858733108109249157334220127702410373959720286708183036202841837581704881367895556630088230650972282944827258473951902831431040790814079538232104075905120989173307660289899942087873076421916033622143260549608274076012938515668898707915863945382394851328164677964192631597026176253407553188801750590935427267220117591817866992665840378311257621611574856498432538327068011953631534031790352912617015229051836886166704989498756486878095690013558017746707412183571476823027885971347137127534455141"
# input_num = [int(i) for i in input_num]
# len(input_num)
# test_matrix = np.array(input_num).reshape(30,60)
# print(maxPathSum(test_matrix))

# # %%


    

# n, m = [int(i) for i in input().split()]
# mat = [ [_s for _s in input()] for _ in range(n)]

# count = 0
# for i in range(1, n):
#     for j in range(1, m):
#         min_i = min(i, n-i-1)
#         min_j = min(j, m-j-1)
#         num = min(min_i,min_j)
#         center = mat[i][j]
#         for z in range(1,num+1):
#             if mat[i-z][j-z] == center and mat[i-z][j+z] == center and mat[i+z][j-z] == center and mat[i+z][j+z] == center:
#                 count +=1
# print(count)


from math import sqrt

# DFS
num = 2022

def prime(num):
    if num < 1:
        return False
    for i in range(2,int(sqrt(num)+1)):
        if num %i == 0:
            return False
    else:
        return True

prime_list = [i for i in range(num) if prime(i)][::-1]


temp = []
res = set()
def dfs_search(num, index, temp_sum):
    if temp_sum > num or index == len(prime_list):
        return
    if temp_sum == num:
        print(temp)
        return
    temp.append(prime_list[index])
    dfs_search(num, index+1, temp_sum+prime_list[index])
    temp.pop()
    dfs_search(num, index+1, temp_sum)

dfs_search(num, 0, 0)
print(res)