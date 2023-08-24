#------------Recursion------------

#-----------ex174----------
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
# print(gcd(int(input('input 1 number ')),int(input('input 2 number '))))
#--------------------------

#----------ex176-----------
def words(a):
    a=a.upper()
    dic={'A':'Alpha', 'J':'Juliet', 'S':'Sierra', 'B':'Bravo', 'K':'Kilo', 'T':'Tango', 'C':'Charlie', 'L':'Lima', 'U':'Uniform', 'D':'Delta', 'M':'Mike', 'V':'Victor', 'E':'Echo', 'N':'November', 'W':'Whiskey', 'F':'Foxtrot', 'O':'Oscar', 'X':'Xray', 'G':'Golf', 'P':'Papa', 'Y':'Yankee', 'H':'Hotel','Q':'Quebec','Z':'Zulu', 'I':'India', 'R':'Romeo'}
    if a=='':
        return ''
    if a[0] in dic:
       return dic[a[0]]+' '+words(a[1:])
    else:
        return a[0]+words(a[1:])
# print(words(input('input the sentence ')))
#_________________________

#----------ex177-----------
def rim(a):
    r=['M','D','C','L','X','V','I']
    ar=[1000,500,100,50,10,5,1]
    if a=='':
        return 0
    if len(a)>1 and 1<ar[r.index(a[1])]/ar[r.index(a[0])]<=10:
        return ar[r.index(a[1])]-ar[r.index(a[0])]+rim(a[2:])
    else:
        return ar[r.index(a[0])]+rim(a[1:])
# print(rim(input('input the rime number ')))
#__________________________

#-----------ex178----------
def polydrom(a):
    a=a.upper()
    if len(a)<=1:
        return True
    if a[0]!=a[-1]:
        return False
    return polydrom(a[1:-1])
# print(polydrom(input('input the word ')))
#___________________________

#----------ex179------------
def sqrt(n,guess=1):
    k=1/(10**12)
    if -k<=guess**2-n<=k:
        return guess
    guess=(guess+n/guess)/2
    return sqrt(n,guess)
# print(sqrt(float(input('input your number '))))
#___________________________

#------------ex180----------
def difference(s,t):
    if len(s)==0:
        return len(t)
    elif len(t)==0:
        return len(s)
    else:
        cost=0
        if s[-1]!=t[-1]:
            cost=1
        d1=difference(s[:-1],t)+1
        d2=difference(s,t[:-1])+1
        d3=difference(s[:-1],t[:-1])+cost
        return min(d1,d2,d3)
# a = input("input the 1 word ") 
# b = input("input the 2 word ")
# print(difference(a,b))
#___________________________

#-----------ex181-----------
def  razmen(c,s,n,i=-1,t=0):
        if s==0 and n==0:
            return True
        if s<0 or n==0 :
            i=-1
            return False
        i+=1
        if(len(c)>i):
            return razmen (c,s-c[i],n-1,i,t) or razmen(c[1:],s,n,t)
        else:
            print("False")
            exit()
n=int(input('input the number of coins '))
s=int(input('input the sum of money '))
l=[25,]*n+[10,]*n+[5,]*n+[1,]*n
print(razmen(l,s,n))
#___________________________ 
