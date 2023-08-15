#----------------from the book--------------

#-------------ex85------------
def pyutagoras(a,b):
    return (a**2+b**2)**(0.5)
# a=int(input('input a '))
# b=int(input('input b '))
# print('c =',pyutagoras(a,b))
#_____________________________

#------------ex86-------------
def Taxi(n):
    return 4+(n//140)*0.25
# a=int(input('input the lenghth of the road in meters '))
# print('you should pay',Taxi(a),'$')
#_____________________________

#------------ex87-------------
def order(m):
    return 10.95+(m-1)*2.95
# a=int(input('input the count of orders '))
# print('you should pay',round(order(a),2),'$')
#_____________________________

#-----------ex88--------------
def med(a,b,c):
    return((a+b+c)-(max(a,b,c)+min(a,b,c)))
# a=int(input('input a '))
# b=int(input('input b '))
# c=int(input('input c '))
# print('the median is',med(a,b,c))
#_____________________________

#-----------ex89-------------
def num(n):
    nums={ 1:'First',2:'Second',3:'Tird',4:'Fourth',5:'Fifth',6:'Sixth',7:'Seventh',8:'Eight',9:'Ninth',10:'Tenth',11:'Eleventh',12:'Twelfth'}
    return(nums.get(n))
# for i in range(1,13):
#     print(num(i))
#_____________________________ 

#-----------ex90--------------
def Csong(n):
    a=['12 Drummers Drumming','11 Pipers Piping','10 Lords a Leaping','9 Ladies Dancing','8 Maids a Milking','7 Swans a Swimming','6 Geese a Laying','5 Golden Rings','4 Calling Birds','3 French Hens','2 Turtle Doves','and a Partridge in a Pear Tree']
    a.reverse()
    print('On the',num(n),'day of Christmas')
    print('my true love sent to me:')
    t=''
    if(n==1):
        print('A Partridge in a Pear Tree')
    else:
        for i in range(n-1,-1,-1):
            t+=a[i]+'\n'
    return t
# for i in range(1,13):
#     print(Csong(i))
#_____________________________

#------------ex91-------------
def ordinalDate(d,m,y):
    a=[31,28,31,30,31,30,31,30,31,31,30,31]
    if(y%4==0):
        a[1]=29
    ind=0
    for i in range(m-1):
        ind+=a[i]
    ind+=d
    return ind
# y=int(input('Input the year '))
# m=int(input('Input the month index '))
# d=int(input('Input the day '))
# print('it is the',ordinalDate(d,m,y),'- th day of year')
#_____________________________

#------------ex91-------------
def Date(ind,y):
    if(y%4==0):
        if(ind>366):
            y+=1
            ind=ind-366
    elif(ind>365):
        y+=1
        ind-=365
    a=[31,28,31,30,31,30,31,30,31,31,30,31]
    if(y%4==0):
        a[1]=29
    m=0
    while(ind>a[m]):
        ind-=a[m]
        m+=1
    b='%.2d'%ind
    c='%.2d'%(m+1)
    r=str(b)+' '+str(c)+' '+str(y)
    return r
# ind=int(input('input the index of the day '))
# y=int(input('Input the year '))
# print('The date -',Date(ind,y))
#_____________________________

#------------ex93-------------
def Center(s,w):
    if(len(s)>=w):
        return s
    else:
        return(' '*((w-len(s))//2)+s)
# s=input('input the text ')
# w=int(input('input the size of window '))
# print(Center(s,w))
#_____________________________

#------------ex94-------------
def IsTriangle(a,b,c):
    return((a==0 or b==0 or c==0 or a>=b+c or b>=a+c or c>=b+a)==False)
# a=int(input('input a '))
# b=int(input('input b '))
# c=int(input('input c '))
# print(IsTriangle(a,b,c))
#_____________________________

#------------ex95-------------
def Text(t):
    t=t.capitalize()
    a='.?!'
    tp=''
    for i in range(len(t)):
            if(t[i]=='i' and i!=0 and (t[i-1]==' ' or (t[i-1] in a)) and ((i==len(t)-1) or ((t[i+1] in a) or t[i+1]==' '))):
                g=t[i].capitalize()
                tp+=g
            elif((t[i] not in a) and t[i]!=' ' and i!=0):
                k=i
                while(k>=0):
                    k-=1
                    if(t[k]!=' '):
                        break
                if(t[k] in a):
                    g=t[i].capitalize()
                    tp+=g
                else:
                    tp+=t[i]
            else:
                tp+=t[i]
    return tp 
# while True:
#     a=input('input the text ')  
#     print(Text(a))
#_____________________________

#------------ex95'urish'-------------
# def Text(t1):
#     t1=t1.capitalize()
#     a='.?!'
#     tp=''
#     t=''
#     t1=t1.split(' ')
#     while('' in t1):
#         t1.remove('')
#     for i in range(len(t1)):
#         if(t1[i] not in a and i!=len(t1)-1 and (t1[i+1] not in a)):
#             t+=t1[i]+' '
#         else:
#             t+=t1[i]
#     for i in range(len(t)):
#             if(t[i]=='i' and i!=0 and (t[i-1]==' ' or (t[i-1] in a)) and i!=len(t)-1 and ((t[i+1] in a) or t[i+1]==' ')):
#                 g=t[i].capitalize()
#                 tp+=g
#             elif(i!=0 and (t[i-1] in a)):
#                 g=t[i].capitalize()
#                 tp+=g
#             else:
#                 tp+=t[i]
#     return tp   
# while True:
#     a=input('input the text ')
#     print(Text(a))   
#_____________________________


#------------ex96--------------
def IsInt(n):
    n=n.strip()
    if(len(n)<1):
        return False
    for i in n:
        if(n.isdigit()==False):
            return  False
    return True
# a=input('input the nnumber ')
# print(IsInt(a))
#______________________________

#-------------ex97-------------
def prioritet(char):
    pr={
        1:['+','-'],
        2:['*','/'],
        3:['^']
    }
    for i in pr:
        if(char in pr[i]):
            return i
    return None
# print(prioritet('^'))
#______________________________

#-------------ex98,99 grel enq---------

#---------------ex100--------------
import random
def parol():
    a=[7,8,9,10]
    l=random.choice(a)
    b=''
    for i in range(l):
        k=random.randint(33,126)
        b+=chr(k)
    return b
# print(parol())
#__________________________________

#---------------ex101--------------
def autonum():
    b=''
    for i in range(4):
        b+=str(random.randint(0,9))
    for i in range(3):
        b+=chr(random.randint(65,90))
    return b
# print(autonum())
#__________________________________

#----------=---ex102---------------
def IsParol(n):
    a=b=d=1
    if(len(n)>7):
        for i in n:
            if i.isdigit():
                d=0
            if 96<ord(i)<123:
                a=0
            if 64<ord(i)<91:
                b=0
    return (a==0 and b==0 and d==0)
# i=input('input your parol ')
# print(IsParol(i))
#__________________________________

#--------------ex103---------------
def goodparol():
    a=parol()
    count=1
    while(IsParol(a)==False):
        a=parol()
        count+=1
    print('After',count,'times')
    return a
# print(goodparol())
#__________________________________

#--------------ex104---------------
def dechex(n):
    nums={
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F',
    }
    temp=n
    num=''
    while(temp!=0):
        if(temp%16<10):
            num+=str(temp%16)
        else:
            num+=nums[temp%16]
        temp//=16
    return num[::-1]
def hexdec(n):
    a=0
    b='ABCDEF'
    nums={
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15
    }
    for i in range(len(n)-1,-1,-1):
        if(n[len(n)-i-1] in b):
            a+=16**(i)*nums[n[len(n)-i-1]]
        else:
            a+=(16**i)*int(n[len(n)-i-1])
    return a
# a=input('Input the number in hex ')
# print(a,'in dec wil be',hexdec(a))
#__________________________________

#---------------ex105--------------
def decx(n,x):
    if(x>15):
        return None
    nums={
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F',
    }
    temp=n
    num=''
    while(temp!=0):
        if(temp%x<10):
            num+=str(temp%x)
        else:
            num+=nums[temp%x]
        temp//=x
    return num[::-1]
def xdec(n,x):
    if(x>15):
        return None
    a=0
    b='ABCDEF'
    nums={
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15
    }
    for i in range(len(n)-1,-1,-1):
        if(n[len(n)-i-1] in b):
            a+=x**(i)*nums[n[len(n)-i-1]]
        else:
            a+=(x**i)*int(n[len(n)-i-1])
    return a
def convert(n,f,t):
    n=xdec(n,f)
    n=int(n)
    n=decx(n,t)
    return n
# f=int(input('From - '))
# n=input('input the number ')
# t=int(input('To - '))
# print(convert(n,f,t))
#__________________________________

#--------------ex106---------------
def month(m,y):
    a=[31,28,31,30,31,30,31,30,31,31,30,31]
    if(y%4==0):
        a[1]=29
    return a[m-1]
# m=int(input('input the month '))
# y=int(input('input the year '))
# print(month(m,y),'days')
#__________________________________