# list1=[]
# list1.insert(0,6)
# list1.insert(1,5)
# list1.insert(2,10)
# print(list1)
# list1.remove(6)
# list1.append(9)
# list1.append(1)
# list1.sort()
# print(list1)
# list1.pop()
# list1.reverse()
# print(list1)

# N=int(input())
# L=[]
# for i in range(0,N):
#     cmd=input().split()
#     if cmd[0]=="insert":
#         L.insert(int(cmd[1]),int(cmd[2]))
#     elif cmd[0]=="append":
#         L.append(int(cmd[1]))
#     elif cmd[0]=="pop":
#         L.pop()
#     elif cmd[0]== "print":
#         print(L)
#     elif cmd[0] == "remove":
#         L.remove(int(cmd[1]))
#     elif cmd[0] == "sort":
#         L.sort()
#     else:
#         L.reverse()

# cap=input("enter your name")

# print(cap.capitalize())

# reduce hacker rank problem

# from fractions import Fraction
# from functools import reduce
# def product(fracs):
#     t = Fraction(reduce(lambda x,y:x*y,fracs))
#     return t.numerator, t.denominator

# if __name__ == '__main__':
#     fracs = []
#     for _ in range(int(input())):
#         fracs.append(Fraction(*map(int, input().split())))
#     result = product(fracs)
#     print(*result)

# permutation hacker rank problem

# from itertools import permutations
# s,n=input().split()
# n1=int(n)
# vals=list(permutations(s,n1))
# res=[]
# for x in vals:
#     res.append(''.join(x))
# print('\n'.join(sorted(res)))

# combination hacker rank solution

# from itertools import combinations
# n = input().split()
# S = n[0]
# k = int(n[1])
# for i in range(1,k+1):
#     for j in combinations(sorted(S),i):
#         print("".join(j))



# combination with replacement hacker rank

# from itertools import combinations_with_replacement
# a = [1,2,3]
# comb = combinations_with_replacement(a,2)
# print(list(comb))


#product hacker rank solution

# from itertools import  product
# A = [1,2]
# B = [3,4]
# output = list(product(A,B))
# for i in output:
#     print(i,end="")

# collection deque hacker rank solution

# from collections import deque
# n = int(input())
# d = deque()
# for i in range(n):
#     lst = list(input().split())
#     if lst[0]=='append':
#         d.append(int(lst[1]))
#     elif lst[0]=='appendleft':
#         d.appendleft(int(lst[1]))
#     elif lst[0]=='popleft':
#         d.popleft()
#     elif lst[0]=='pop':
#         d.pop()
# for k in d:
#     print(k,end=" ")

# counter hacker rank problem
# from collections import Counter
# class my_dictionary(dict):
  
#     def __init__(self):
#         self = dict()
          
    
#     def add(self, key, value):
#         self[key] = value
  
# x = int(input())
# size = list(map(int,input().split()))
# n = int(input())
# my_counter = Counter(size)
# dict_1=my_dictionary()
# prize = 0
# for i in range(n):
#     sz = list(map(int,input().split()))
#     dict_1.add(sz[0],sz[1])
# print(dict_1)             
# for i in dict_1.keys():
#     if i in size:
#         prize += dict_1.get(i)   
# print(prize)        

# ip =[ [6, 55],
#       [6 ,45],
#       [6 ,45],
#       [4,50],
#       [4,50],
#       [4,40]]

# size = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]

# dicta = { 6 : [55, 45, 40, 38], 4 : [50, 40, 30, 28]}


# checked_dict = {}

# for i in size:
#     checked_dict[i] = size.count(i)

# print("checked_dict", checked_dict)

# total = 0
# available_count = 0
# var = {}
# for i in ip:
#     if i[0] in dicta.keys():
#         counter_size = checked_dict[i[0]]
#         if i[1] in dicta[i[0]]:
#             if i[0] not in var.keys() or i[1] not in var.values():
#                 total += i[1]
#                 var[i[0]] = i[1]


# print("final", total)

# hacker rank problem in named tuple
# from collections import namedtuple
# import collections
# n = int(input())
# s = input().split()
# # print(n)
# # print(s)
# sum = 0
# Student_data = collections.namedtuple('Student_data',s)

# for i in range(n):
#     data = input().split()
#     print(data)

#     print(i)
#     print(sum)

# def longest_substring(digits):
#     max_len = 0
#     ans = ''
    
#     for i in range(len(digits)):
#         temp = digits[i]
#         for x in range(i+1, len(digits)):
#             if int(digits[x])%2 != int(digits[x-1])%2:
#                 temp += digits[x]
#                 # print(temp)
#             else:
#                 break
#         if len(temp) > max_len:
#             max_len = len(temp)
#             print(max_len)
#             ans = temp
#             print(ans)
#     return ans
# # digits = "225424272163254474441338664823"
# digits = "594127169973391692147228678476"
# # digits = "721449827599186159274227324466"

# print(longest_substring(digits))
# x = [[1, 2, 3],[2, 3, 4],[3, 4, 1]]

# def rows(matrix):
#     list = [val for val in matrix]
#     list1 = [i for i in zip(*matrix)]
#     print (list)
#     print (list1)
#     if list == list1:
#         return True
#     else:
#         return False

# print(rows(x))
# from numpy import *
# from numpy.matrixlib.defmatrix import matrix
# m = matrix('1 2 ; 3 4 ; 5 6')
# print(m)
# print(diagonal(m))
# print(m.min())


# pytz module
# 1. all_timezones
# import pytz
# print("the time supported by the pytz module",pytz.all_timezones)
# print(pytz.all_timezones_set)
# print(pytz.common_timezones)
# print(pytz.common_timezones_set)


# get ans set method in python
# class prac:
#     def __init__(self,age=0):
#         self._age = age
#     def get_age(self):
#         return self._age
#     def set_age(self,x):
#         self._age = x

# yash = prac()
# yash.set_age(21)
# print(yash.get_age())

# class prac:
#     def __init__(self,age=0):
#         self._age = age
#     def get_age(self):
#         return self._age
#     def set_age(self,x):
#         self._age= x
# yash = prac()
# yash.set_age(21)
# print(yash.get_age())

# magic methods in python
# num = 10
# print(num.__add__(5))
# print(num.ceil())
# import math
# print(math.__ceil__(seld))
# print(int.__str__(num))

# Cmath module in python

# import cmath

# print the cos value of x 
# print(cmath.cos(45)) 


# hyper bolic value of x
# print(cmath.cosh(2 + 3j))  


# arc cos value
# print(cmath.acos(2+3j))  


# check value close or not
# print(cmath.isclose(10+5j, 10+5j))  
# print(cmath.isclose(10+5j, 10.01+5j))


# give the polar cordinates
# print (cmath.polar(2 + 3j)) 

# print(cmath.sqrt(4))


# polar coordinates to rectangular form
# print(cmath.rect(3.1622776601683795, 1.2490457723982544)) Convert 


# base-10 log value of complex numbers
# print (cmath.log10(2+ 3j)) 


# base-10 log value of complex numbers
# print (cmath.log10(1+ 2j))  


#find whether a complex number is finite or not
# print (cmath.isfinite(2 + 3j))
# print (cmath.isfinite(complex(5.0,float('inf'))))
# print (cmath.isfinite(float('inf')+ 5j))


#  oprator module in python
# import operator
# from typing import Type
# a= 20
# b= 5
# print(operator.add(a,b))

# print(operator.sub(a,b))

# print(operator.mul(a,b))

# gives the float division
# print(operator.truediv(a,b))

#  gives the int division
# print(operator.floordiv(a,b))

# gives the reminder
# print(operator.mod(a,b))

# gives the a^b
# print(operator.pow(a,b))

# check the number is less than
# print(operator.lt(a,b))

# check the number is less than or equal to 
# print(operator.le(a,b))

# check no. is equal or not
# print(operator.eq(a,b))

# check no. is greater than 
# print(operator.gt(a,b))

# check no. is greater than ,equal to 
# print(operator.ge(a,b))

# not equal
# print(operator.ne(a,b))

# decimal module in python

# from decimal import *
# a= 1.1
# d= Decimal('1.1')
# print(type(a))
# print(type(d))
# check = (a==d)
# print(check)

# Hacker rank polar cordinate 
# import cmath
# var1 = cmath.polar(1+2j)
# print(type(var1))
# ip =complex(input())
# a = complex(ip)
# print(type(ip))
# print(cmath.polar(ip)[0])
# print(cmath.polar(ip)[1])

# import cmath

# ip = complex(-1,-2)
# print(ip)
# print(cmath.polar(ip))
# ip1 = cmath.rect(2,cmath.pi)
# print(ip1)

# give_list = list()
# result_list = list()

# size = int(input(' size of list :'))


# for i in range(size):
#     give_list.append(int(input(' element add : ')))

# for i in range(len(give_list) + 1):
#     for j in range(i + 1, len(give_list) + 1):
#         result_list.append(give_list[i:j])

# print(give_list)
# print(sorted(result_list))

# zip function basic example
# tup1 = ("yash","vinay","utsav")

# tup2 = ("jangir","gupta","jain")

# x = zip(tup1,tup2)
# print(tuple(x))

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
marks = [ 40, 50, 60, 70 ]

x = zip(name,roll_no,marks)
x = list(x)
print(x)

namez,roll_num,mark = zip(*x)
print(namez)
print(roll_num)
print(mark)





