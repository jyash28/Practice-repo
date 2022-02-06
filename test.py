# i=0
# while i<11:
#     print("hello")
#     i=i+1

# x=["navin",62,2.5]
# for i in x:
#     print(i)

# x="yash"
# for i in x:
#     print(i)

# for i in range(11,20,1):
#     print(i)

# for i in range(10):
#     if i==5:
#         break
#     print(i)

# for i in range(10):
#     if i==5:
#         continue
#     print(i)

# for i in range(4):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# num=7
# for i in range(2,num):
#     if num%i==0:
#         print(" not prime")
#         break
# else:
#     print(" prime")  

# from array import *
# vals = array('i',[5,9,-8,4,2])

# for e in vals:
#     print(e)

# user input array
# from array import *
# arr = array('i',[])
# n= int(input("enter the length of the array"))

# for i in range(n):
#     x=int(input("enter the next value"))
#     arr.append(x)
# print(arr)

# from numpy import * 
# arr1 = array([1,2,3,4,5])
# arr2 = array([6,7,8,9,10])

# arr3 = arr1 + arr2
# print(arr3)

# matrix
# from numpy import *
# m= matrix("1 2 ; 3 4 ; 5 6 ; 7 8")
# print(m)
# print(diagonal(m))
# print(m.min())
# print(m.max())

# def add_sub(x,y):
#     c= x+y
#     d= x-y
#     return c,d
# result1,result2=add_sub(4,5)
# print(result1,result2)

# def person(name,**data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)
# person("navin",age='28',city = "mumbai",mob="9549824740")

# def fib(n):
#     a=0
#     b=1

#     if n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)

#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
# fib(2)

# lambda expression

# f = lambda a : a*a
# result= f(5)
# print(result)

# from functools import reduce
# nums=[3,4,1,8.9,10,4]
# evens=list(filter(lambda n: n%2==0 ,nums))

# doubles= list(map(lambda n:n+2,evens ))
# sum = reduce(lambda a,b : a+b,doubles)

# print(evens)
# print(doubles)
# print(sum)



# decorators in python
# def div(a,b):
#     print(a/b)

# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b= b,a
#             return func(a,b)
#     return inner
# div= smart_div(div)
# div(2,4)


# class concepts

# class computer:
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#     def config(self):
#         print("config is",self.cpu,self.ram)

# comp1= computer("i5",16)
# comp2 = computer("ryzen3",8)
# comp1.config()
# comp2.config()

# class computer:
#     def __init__(self):
#         self.name="navin"
#         self.age=28
#     def update(self):
#         self.age=30
# c1=computer()
# c2=computer()

# c1.name="Rashi"
# c1.age=12

# print(c1.name)
# print(c2.name)

# class car:
#     wheels=4
#     def __init__(self):
#         self.mil=10
#         self.com="bmw"

# c1=car()
# c2=car()

# c1.mil=8

# print(c1.com,c1.mil,c1.wheels)
# print(c2.com,c2.mil,c2.wheels)

# inheritance concepts

# class A:
#     def feature1(self):
#         print("feature 1 is working")
#     def feature2(self):
#         print("feature 2 is working")
# class B(A):
#     def feature3(self):
#         print("feature 3 is working")
#     def feature4(self):
#         print("feature 4 is working")

# a1= A()
# a1.feature1()
# a1.feature2()
# b1= B()
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()


# class A:
#     def show(self):
#         print("in A show")
# class B:
#     def show(self):
#         print("in B show")
# a1 = B()
# a1.show()
        
# try statement
# a=5
# b=0
# try:
#     print(a/b)
# except Exception:
#     print("you cannot number divided ny zero")

# finally:
#     print("resoures closed")

# raise statement

# age = int(input("enter your age"))

# if age >= 18:
#     print("you can take luiquor")
# else:
#     raise Exception('you are not old enough')


# join and split
  
# def split_string(string):
  
#     list_string = string.split(' ')
      
#     return list_string
  
# def join_string(list_string):
  
#     string = '-'.join(list_string)
      
#     return string
  
# if __name__ == '__main__':
#     string = input()
      
    
#     list_string = split_string(string)
#     print(list_string)
  
    
#     new_string = join_string(list_string)
#     print(new_string)

# dictionary problem hacker rank

# test_dict = {"yash":20,"jitender":30,"vinay":40}
# print("The  dictionary is : " + str(test_dict))
# values=test_dict.values()
# total = sum(values)
# print(total)
# res = total/len(test_dict)
# print(res)

# liner search
# pos = -1
# def search(list,n):
#     i=0

#     while i<len(list):
#         if list[i] == n:
#             globals()['pos'] = i
#             return True
#         i = i + 1

#     return False

# list= [4,7,8,12,45,99]
# n= 45

# if search(list,n):
#     print("found at",pos)
# else:
#     print("not found")

# binary search
# pos = -1
# def search(list,n):
#     l = 0
#     u = len(list)-1

#     while l <= u:
#         mid = (l+u) // 2

#         if list[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list[mid] < n :
#                 l = mid+1
#             else:
#                 u = mid-1
#     return False

# list= [4,7,8,12,45,99]

# n= 45

# if search(list,n):
#     print("found at",pos)
# else:
#     print("not found")

# zip function

# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# x = zip(a, b)
# print(list(x))


# bubble sort

# def sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp

# nums = [5,3,8,6,7,2]
# sort(nums)
# print(nums)


# selection sort
# def sort(nums):
#     for i in range(5):
#         minpos = i 
#         for j in range(i,6):
#             if nums[j] < nums[minpos]:
#                 minpos = j
#         temp = nums[i]
#         nums[i] = nums[minpos]
#         nums[minpos] = temp       
                               
# nums = [5,3,8,6,9,1]      
# sort(nums)            
# # print(nums)   

# bubble sort using list comprihension

# def bubblesort(nums):
#     [[nums.insert(j+1, nums.pop(j)) for j in range(i) if nums[j] > nums[j+1]] for i in range(len(nums)-1,0,-1)]
#     return nums
# print(bubblesort([1,5,-5,0,10,100,105,110]))

# string swap case in python 
# str1="YasH JangiR";  
# new_str = ""  
   
# for i in range(0, len(str1)):   
#     if str1[i].islower():    
#         new_str += str1[i].upper()   
#     elif str1[i].isupper():   
#         new_str += str1[i].lower()   
#     else:  
#         new_str += str1[i];          
# print(new_str) 

# string concate in python
# str_1 = input("enter first string")
# str_2 = input("enter secons string")
# print(("Hello" + str_1 +str_2)+"!You just developed in python")



# str_1 = input()
# print(str_1.capitalize())

# def printRoman(number):
    # num = [1, 4, 5, 9, 10, 40, 50, 90,
    #        100, 400, 500, 900, 1000]
    # sym = ["I", "IV", "V", "IX", "X", "XL",
    #        "L", "XC", "C", "CD", "D", "CM", "M"]
#     i = 12
#     while number:
#         div = number // num[i]
#         number %= num[i]
 
#         while div:
#             print(sym[i], end = "")
#             div -= 1
#         i -= 1
 
# if __name__ == "__main__":
#     number = 3549
#     print("Roman numeral is:", end = " ")
#     printRoman(number)

# def nums_points(x,y,z):
#     return x+y+z
# a = int(input("enter the wiining matches"))
# b = int(input("enter the draws matches"))
# c = int(input("enter the losses matches "))

# wins = a * 3
# draws = b * 1
# loses = c * 0

# total = nums_points(wins, draws,loses)
# print(total)


# def int_roman(num):
#     result = ""
#     dict1 = {1000 : "M",900 : "CM", 500 : " D",400 : "CD", 100 : "C",90 : "XC", 50 : "L",40 :"XL", 10 : "X",9: 'IX', 5 : "V",4: 'IV', 1 :"I"}

#     while num != 0:
#         for k,v in dict1.items():
#             if num >= k:
#                 divi = int(num/k)
#                 num = num % k
#                 result = result + (divi*v)
#     return result
# print(int_roman(999)) 

# 4 : "VI"
# 9 : "IX"
# 40 :"XL"
# 90 : "XC"
# 400 : "CD"
# 900 : "CM"


# def convert(s, numRows):    
#     if numRows == 1 or numRows >= len(s):
#         return s
#     L = [''] * numRows
#     index = 0
#     step = 1
#     for x in s:
#         L[index] += x
#         if index == 0:
#             step = 1
#         elif index == numRows -1:
#             step = -1
#         index += step
#     return ''.join(L)
# total=convert("PAYPALISHIRING",4)
# print(total)


# while True:
#     amount=int(input("enter the amount you want to widraw"))
#     if (amount%100)==0:
#         print("you can easily withdraw the money")
#     else:
#         if amount >= 100 and amount <= 25000:
#             print("you cam witdraw the money between 100 to 25000")
#         else:
#             # print("please enter the amount between 100 to 25000")
#             note_want=
#             notes100 = amount/100
#             notes500 = amount/500
#             notes2000 = amount/2000


# ATM Machine program
# while True:
#     print("welcome to atm")
#     amount = int(input("enter the amount you want to widhraw"))
#     if (amount%100) != 0:
#         print("you can only widraw the the amount which is multiple of 100")
#     else:
#         if amount < 100 or amount > 25000:
#             print("you can widraw the money between 100 to 25000")
#         else:
#             print("enter")
#             notes2000 = 0
#             notes500 = 0
#             notes100 = 0
#             if amount >= 2000:
#                 # print("2000 > ", int(amount/2000))
#                 notes2000 = int(amount/2000)
#                 amount = amount % 2000
#                 print("amount", amount)
#             if amount >= 500:
#                 # print("500 > ", int(amount / 500))
#                 notes500 = int(amount/500)
#                 amount = amount % 500
#             if amount >= 100:
#                 # print("100 > ", int(amount / 100))
#                 notes100 = int(amount/100)
#                 amount = amount % 100

#             print("you can widraw" ,notes2000)
#             print("you can widraw" ,notes500)
#             print("you can widraw" ,notes100)

# notes = [2000,500,200,100,50,10] 
# amount = int(input("enter the amount"))
# for i in range(0,len(notes)):
#     print("rupees",int(amount/notes[i]))
#     amount = amount % notes[i]



# sys module in python
# 1. In order to start using the sys module and its various functions, you need to import it. => import sys

# 2.If you want to force quit the application or stop it from executing at any point, we can use the exit() function within the sys module.

# import sys
# print(“Hello there!”)
# sys.exit()
# print(“This line is not even executed because the program exited in the last line”)
# output: Hello there!

# 3.Obtaining the current version of Python

# import sys
# print (sys.version)

# output: 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)]

# 4. Getting locations of all the Python modules installed

# import sys
# sys.path

# 5. Reading values from the user
# import sys
# data = sys.stdin.readline()
# print(""+ data)

# 6.more about sys module
# from collections import defaultdict
# from functools import lru_cache
# import sys
# from typing import OrderedDict
# print(sys.copyright)
# print(sys.dllhandle)
# print(sys.executable)
# print(sys.getrecursionlimit())
# print(sys.getcheckinterval())
# print(sys.getwindowsversion())
# print(sys.platform)
# print(sys.api_version)
# print(sys.winver)
# sys.stdout.write("Hey") this is perform as print function
# sys.stderr.write("Hi") this is perform as print function but in red color
# data = sys.stdin.readlines()
# print(data,len(data))
# print(sys.argv[1],"Yash")

# collection module in python counter,named tuple,Orderdict,defaultdict

# counter
from collections import Counter
a = "aaaabbbcccc"
my_counter = Counter(a)
print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common(2))
# print(my_counter.most_common(1)[0][0])
# print(list(my_counter.elements()))

# # named tuple
# from collections import namedtuple
# Point = namedtuple('Points','x,y')
# pt = Point(1,-4)
# print(pt)
# print(pt.x,pt.y)

# OrderedDict
# from collections import OrderedDict
# ordered_dict ={}
# ordered_dict['a'] = 1
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# ordered_dict['a'] = 1
# ordered_dict['a'] = 1
# print(ordered_dict)

# # defaultdict
# from collections import defaultdict
# d = defaultdict(int)
# d['a'] =  1
# d['b'] =  2
# print(d)
# print(d['a'])

# # deque
# from collections import deque
# queue = deque(['name','age','dob'])
# queue.append(1)
# queue.appendleft(3)
# print(queue)
# d = deque()
# d.append(1)
# d.append(2)
# d.appendleft(3)
# print(d)
# d.pop()
# print(d)
# d.popleft()
# print(d)
# d.clear()
# print(d)
# d.extend([4,5,6])
# d.extendleft([1,2,3])
# print(d)
# d.rotate(1)
# print(d)

# funtools module in python
# 1.reduce
# from functools import reduce

# import functools
# result=reduce(lambda x,y:x+y,[1,2,3,4,5])
# print(result)
# result=reduce(lambda x,y:max(x,y),[1,2,3,4,5])
# print(result)
# result=reduce(lambda x,y:x+y,[1,2,3,4,5],10)
# print(result)

# another example of the reduce
# lis=[1,3,5,6,2,]
# print("the sum of the list is :",end="")
# print(functools.reduce(lambda a,b: a+b,lis))

# print("the max. is :",end="")
# print(functools.reduce(lambda a,b:a if a>b else b,lis))

# 2.total_ordering
# from functools import total_ordering
# class Car:
#     def __init__(self,model,mileage):
#         self.model = model
#         self.mileage = mileage
#     def __eq__(self,other):
#         return self.mileage == other.mileage 
#     def __lt__(self,other):
#         return self.mileage < other.mileage
# c1 = Car("Audi",700)
# c2 = Car("BMW",800)
# result1 =   c1 == c2
# print(result1)
# result2 =   c1 < c2
# print(result2)

# 3. lru_cache => this is used as a decorators
# from functools import lru_cache
# @lru_cache(maxsize=128)
# def fib(n):
#     if n < 2 :
#         return n 
#     print(f"calculating fib  {n}")
#     return fib(n-1) + fib(n-2)
# result =[ fib(x) for x in range(11)]
# print(result)

# 4. partial
# from functools import partial
# def add(a,b):
#     return a + b
# add_one = partial(add,1)
# print(add_one(4))


# import collections

# n = int(input())
# scol = (input().split())
# Student = collections.namedtuple('Student',scol)

# sum = 0
# for i in range(n):
#     row = input().split()
#     student = Student(*row)
#     sum += int(student.MARKS)

# print(sum/n)

# itertools in python : product,permutation,combination,accumulate
# # 1.product
# from itertools import  product
# a = [1,2]
# b = [3,4]
# prod = product(a,b)
# print(list(prod))

# # 2. permutations
# from itertools import permutations
# a = [1,2,3]
# perm = permutations(a)
# print(list(perm))
# perm = permutations(a,2)
# print(list(perm))

# 3. combination
# from itertools import combinations
# a = [2,1,2,1]

# comb = combinations(a,2)
# print(list(comb))

# 4. accumulate
# from itertools import accumulate
# a =[1,2,3,4]
# acc = accumulate(a)
# print(a)
# print(list(acc))



# word = 'incredible'
# length =len(list(word))
# actual =list(word)
# print(actual)
# l1 = actual[:5]
# l2 = actual[5:]
# demo =l1 + actual + l2
# print(demo)
# new_str = "".join(demo)
# print(new_str)

# second = new_str
# length1=len(list(new_str))
# print(length1)
# l3 = new_str[:7]
# print(l3)
# l4 = new_str[7:]
# print(l4)
# demo1 = l3 + word+ l4
# print(demo1)
# new_str1 = "".join(demo1)
# print(new_str1)

# third = new_str1
# length2 = len(list(new_str1))
# print(length2)
# l5 = new_str1[:11]
# print(l5)
# l6 = new_str1[11:]
# print(l6)
# demo2 = l5 + word + l6
# print(demo2)
# new_str2 = "".join(demo2)
# print(new_str2)


# word = "incredible"


# length = len(list(word))

# blank = [word for i in word[:5]]
# print(blank)

# import textwrap
# string = input()
# print(textwrap.wrap(string,2))
# print(textwrap.fill(string,3))


# import time;

# localtime = time.localtime(time.time())  
 
# print ("Local current time" , localtime)



# localtime = time.asctime( time.localtime(time.time()) )

# print ("Local current time ", localtime)  # getting formatted time


# import calendar

# cal = calendar.month(2021, 8)


# print ("Here is the calendar:")

# print (cal)


# import datetime

# import calendar
 
# def findDay(date):
    


#     data = datetime.datetime.strptime(date, '%m %d %Y').weekday()
#     user = calendar.day_name[data]
#     return (user.upper())



# date = "08 04 2021"     

# print(findDay(date))




# string = "225424272163254474441338664823"
# string = "594127169973391692147228678476"
# string = "721449827599186159274227324466"
    
# print(len(string))

# length = 0
# new_string = ''

# for i in range(len(string)):
#     # print(i)

#     temp = string[i]
#     # print(temp)

#     for j in range(i+1,len(string)):

#         if int(string[j])%2 !=  int(string[j-1])%2:

#             temp = temp + string[j]
            # print(temp)
            
        # else:
        #     break

#         if len(temp) > length:

#             length = len(temp)

#             new_string = temp


# print(new_string)



# str2=input("enter your string")
# length= len(str2)

# for i in str2:
#     print(i)
#     for


# def pattern(string):

#     for i in string:
#         print(i)
#         if string

# string = "ABC"
# print(pattern(string))




# row = int(input("enter the rows"))

# col = int(input("enter the coloums"))

# mat = []


# for i in range(row):
#     a = []

#     for j in range(col):

#         a.append(input())

#     mat.append(a)
    # print(a)


# for i in range(row):

#     for j in range(col):
        # print(mat[i][j],end="")
    #     print(mat[i][j])
    # print()

        # for k  in range(len(mat)):
        #     for l in range(len(a)):
        # if mat[0] == mat[1] == mat[2]:
        #     print("match")
        # print(mat[:,2])
        

# def unique(str):
     
#     for i in range(len(str)):
#         for j in range(i + 1,len(str)):
#             if(str[i] == str[j]):
#                 return
#     return True

# str = "qwertyuiopasdfghjklzxcvbnmq"
 
# if(unique(str)):
#     print("unique")
# else:
#     print("duplicate")








    
    


        

            


    



    







                    



















    



        