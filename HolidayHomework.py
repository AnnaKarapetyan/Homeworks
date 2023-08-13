#---------------from the book----------------

#--------------ex5------------
# n=int(input('input how many bottles are 1L or smaller '))
# n1=int(input('input how many bottles are bigger than 1L '))
# print(f'The sum is %.2f'%(n*0.1+n1*0.25))
#_____________________________

#--------------ex6------------
# n=int(input('input the sum '))
# nalog=round(n*32/100,2)
# chay=round(n*18/100,2)
# mnac=n-nalog-chay
# print(f'Nalog - {nalog}\nChayevoy - {chay}\nShahuyt - {mnac}')
#_____________________________

#--------------ex7------------
# n=int(input('input the number '))
# print("sum =",n*(n+1)/2)
#_____________________________

#--------------ex13------------
# n=int(input('input the sum of money '))
# b=[1,5,10,25,100,200]
# s=n
# for i in range(6):
#     c=s//b[5-i]
#     s%=b[5-i]
#     if(c!=0):
#         print(f'{c} - {b[5-i]}')
#______________________________

#-------------ex26-------------
# import time
# print(time.asctime())
#______________________________

#-------------ex32-------------
# n=int(input('input the number '))
# n=list(str(n))
# Sum=0
# for i in range(len(n)):
#     Sum+=int(n[i])
# print(Sum)
#______________________________

#-------------ex33-------------
# n=int(input('input the 1 number '))
# n1=int(input('input the 2 number '))
# n2=int(input('input the 3 number '))
# ssum=n+n1+n2
# print(min(n1,n,n2),ssum-min(n,n1,n2)-max(n1,n,n2),max(n,n1,n2))
#______________________________

#-------------ex34-------------
# old_b=round(3.49*2/5,2)
# new_b=3.49
# n=int(input('input the count of old bread '))
# print(f'new bread costs {new_b}$\nold bread costs {old_b}$\nyou should pay {n*old_b}$')
#______________________________

#-----------ex45---------------
# Mydict={
#    '1январь':'Новый год',
#     '1июль':'День Канады',
#     '25декабрь':'Рождество'
# }
# m=input('Input the month ')
# d=input("Input the day ")
# if(Mydict.get(d+m)!=None):
#     print(Mydict[d+m])
# else:
#     print('none')
#______________________________

#-----------ex46---------------
# c=input('input the coordinates ')
# x=c[0]
# y=int(c[1])
# a='abcdefgh'
# if((y%2==0 and a.index(x)%2==0)or(y%2==1 and a.index(x)%2==1)):
#     print('white')
# else:
#     print('black')
#______________________________

#-----------ex59---------------
# y=int(input("Input the year "))
# m=input("Input the month ")
# d=int(input("Input the day "))
# month=['January','February',' March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']
# day=[31,28,31,30,31,30,31,31,30,31,30,31]
# if(d==day[month.index(m)] and m=='December'):
#     print(f'The next day is- 1 January {y+1} year')
# elif(d==day[month.index(m)]):
#     print(f'The next day is- 1 {month[month.index(m)+1]} {y} year')
# else:
#     print(f'The next day is- {d+1} {m} {y} year')
#______________________________

#-----------ex63---------------
# a=[]
# n=int(input('input the number '))
# a.append(n)
# Sum=0
# if(n==0):
#     print('Error')
# else:
#     while True:
#         a.append(int(input('input the number ')))
#         if(a[-1]==0):
#             Sum=sum(a)
#             break
#     print(Sum/(len(a)-1))
#______________________________

#-----------ex67---------------
# x=float(input('input the point\'s x '))
# y=float(input('input the point\'s y '))
# x1=x
# y1=y
# p=0
# while True:
#     tx=x
#     ty=y
#     x=input('input the point\'s x ')
#     if(x==''):
#         p+=((x1-tx)**2+(y1-ty)**2)**(0.5)
#         break
#     x=int(x)
#     y=float(input('input the point\'s y '))
#     p+=((x-tx)**2+(y-ty)**2)**(0.5)
# print(f'P = {p}')
#______________________________

#-----------ex69---------------
# price=0
# while True:
#     age=input('input your age ')
#     if(age==''):
#         break
#     age=int(age)
#     if(2<age<12):
#         price+=14
#     elif(11<age<65):
#         price+=23
#     elif(age>64):
#         price+=18
# print(f'Price is - {price}$')
#______________________________

#-----------ex72---------------
# for i in range(1,101):
#     if(i%15==0):
#         print('Fizz-Buzz')
#     elif(i%3==0):
#         print('Fizz')
#     elif(i%5==0):
#         print('Buzz')
#     else:
#         print(i)
#______________________________

#-----------ex73---------------
# code='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# a=input('input the word ')
# n=int(input('input the count of steps '))
# b=''
# for i in a.upper():
#     b+=code[code.index(i)+n]
# print(b)
#______________________________

#-----------ex80---------------
# n=int(input('input the number '))
# factor=2
# a=[]
# while factor<=n:
#     if(n%factor ==0):
#         a.append(factor)
#         n=n//factor
#     else:
#         factor+=1
# print(a)
#______________________________

#-----------ex82---------------
# n=int(input('input the number '))
# temp=n
# t=[]
# if(temp==0):
#     print(0)
# else:
#     while(temp!=0):
#         t.append(temp%2)
#         temp//=2
#     print(t[::-1])
#______________________________

#-----------ex83---------------
# import random
# Max=random.randint(1,100)
# c=0
# print(Max)
# for i in range(99):
#     a=random.randint(1,100)
#     if(a>Max):
#         print(a,'-->new greatest')
#         c+=1
#         Max=a
#     else:
#         print(a)
# print(f'Max number is - {Max},count of changes of maximum is {c}')
#______________________________

#-----------ex84---------------
# import random
# a='PPP'
# b='OOO'
# c=['O','P']
# Sum=0
# for i in range(10):
#     k=''
#     co=0
#     while((a not in k)and(b not in k)):
#         k+=random.choice(c)
#         co+=1
#     print(k,'after',co,'times')
#     Sum+=co
# print('Avarage',Sum/10,'times')
#______________________________

#----------------------ex110-----------------------
#b=[]
#while True:
#    a=int(input("Input the number "))
#    if a==0:
#        break
#    b.append(a)
#b.sort()
#for i in b:
#    print(i)
#___________________________________________________

#----------------------ex113-----------------------
#b=[]
#while True:
#    a=input("Input the word ")
#    if a=="":
#        break
#    if(a not in b):
#        b.append(a)
#print(b)
#_________________________________________________

#------------------ex114---‐----------------------
#m=[]
#n=[]
#p=[]
#while True:
#    a=input("Input the number ")
#    if a=="":
#        break
#    a=int(a)
#    if(a>0):
#        p.append(a)
#    elif(a<0):
#        m.append(a)
#    else:
#        n.append(0)
#m.extend(n)
#m.extend(p)
#input(m)
#_________________________________________________

#-------------‐------ex115----------‐---‐-------
#n=int(input("Input the number "))
#a=[]
#for i in range(2,n//2+1):
#    if(n%i==0):
#        a.append(i)
#print(a)
#________________________________________________

#----------------------ex116--------------------
#for n in range(1,10000):
#    a=[]
#    for i in range(1,n//2+1):
#         if(n%i==0):
#            a.append(i)
#    Sum=sum(a)
#    if(Sum==n):
#        print(n)
#_______________________________________________

#---------------------ex117--‐‐-----------------
#a=input("input the sentence ")
#b=", .:;,"
#a=list(a)
#d=""
#for i in range(len(a)):
#    if(a[i] in b):
#        a[i]=' '
#    d+=a[i]
#c=d.split(' ')
#if(' ' in c):
#    c.remove(' ')
#print(c)
#'  ' ner chi hanum?????
#_______________________________________________

#---------------------ex121--‐‐-----------------
#import random
#a=[]
#for i in range(1,50):
#    a.append(i)
#random.shuffle(a)
#b=a[:6]
#k=True
#for i in range(6):
#    i=int(input(f'Imput the {i+1} number '))
#    if(i not in b):
#        print("You lose the wining ticket was ",b)
#        t=False
#        break
#if(t):
#    print("You won congratulations!!!!")
#_______________________________________________

#---------------------ex133--‐‐-----------------
#n=int(input("imput the count of elements in array "))
#arr=[]
#for i in range(n):
#    arr.append(int(input(f"input the {i+1} number ")))
#n1=int(input("imput the count of elements in second array "))
#arr1=[]
#for i in range(n1):
#    arr1.append(int(input(f"input the {i+1} number of small array ")))
#for i in range(n):
#    if(arr[i]==arr1[0] ):
#        if((i+len(arr1))>len(arr)):
#            print("False")
#            break
#        elif(arr1==arr[i:i+len(arr1)]):
#             print("True")
#             break
#_______________________________________________

#--------------------ex134--‐-----‐-----‐-------
#n=int(input("imput the count of elements in array "))
#arr=[]
#for i in range(n):
#    arr.append(int(input(f"input the {i+1} number ")))
#a2=[[],]
#for i in range(n):
#    # a1=[]
#    for j in range(i,n):
#         a1.append(arr[j])
#        a2.append(arr[i:j+1])
#print(a2)
#_______________________________________________

#--------------------ex137--‐-----‐-----‐-------
#import random
#mydict={
#2:0,
#3:0,
#4:0,
#5:0,
#6:0,
#7:0,
#8:0,
#9:0,
#10:0,
#11:0,
#12:0
#}
#for i in range(1000):
#    a=random.randint(1,6)
#    b=random.randint(1,6)
#    mydict[a+b]+=1
#for i in mydict:
#    print(i,mydict[i]/10,'%')
#_______________________________________________

#--------------------ex138--‐-----‐-----‐-------
#mylist={
#     1:".,?!:",
#     2:"ABC",
#     3:"DEF",
#     4:"GHI",
#     5:"JKL",
#     6:"MNO",
#     7:"PQRS",
#     8:"TUV",
#     9:"WXYZ",
#     0:" "
# }
#word=input("input the word ")
#for i in word.upper():
#    for j in mylist:
#        if(i in mylist[j]):
#               print((mylist[j].index(i)+1)*str(j),end=" ") 
#_______________________________________________

#--------------------ex139--‐-----‐-----‐-------
#MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
#                    'C':'-.-.', 'D':'-..', 'E':'.',
#                    'F':'..-.', 'G':'--.', 'H':'....',
#                    'I':'..', 'J':'.---', 'K':'-.-',
#                    'L':'.-..', 'M':'--', 'N':'-.',
#                    'O':'---', 'P':'.--.', 'Q':'--.-',
#                    'R':'.-.', 'S':'...', 'T':'-',
#                    'U':'..-', 'V':'...-', 'W':'.--',
#                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
#                    '1':'.----', '2':'..---', '3':'...--',
#                    '4':'....-', '5':'.....', '6':'-....',
#                    '7':'--...', '8':'---..', '9':'----.',
#                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
#                    '?':'..--..', '/':'-..-.', '-':'-....-',
#                    '(':'-.--.', ')':'-.--.-'}
#word=input("input the word ")
#for i in word.upper():
#           print(MORSE_CODE_DICT[i],end="  ")   
#_______________________________________________

#-------------------ex145-‐-------‐‐------‐---
#mydict={
#1:["A", "E", "I"," L", "N","O", "R", "S", "T","U"],
#2:["D","G"],
#3:["B", "C","M" ,"P"],
#4:["F","H", "V", "W","Y"],
#5 :"K",
#8:["J","X"],
#10:["Q","Z"]
#}
#word=input("input the word ")
#word=word.upper()
#Sum=0
#for i in word:
#    for j in mydict:
#        if i in mydict[j]:
#                  Sum+=j
#                  break
#print(Sum)               
#_______________________________________________









