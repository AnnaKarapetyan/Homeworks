def towords(a:str):
    '''տեքստից բառերի ցուցակ ստանալու համար'''
    b=',:.?!;\n'
    c=''
    for i in a:
        if i in b:
            c+=' '
        else:
            c+=i
    c=c.split(' ')
    while('' in c):
        c.remove('')
    return c
#-----------book file exersices--------------

#--------------ex149grel enq---------------- 

#--------------ex150----------------
def tail(f):
    try:
        with open(f,'r') as file:
            a=file.readlines()
            b=''
            if(len(a)<=10):
                k=0
            else:
                k=len(a)-10
            for i in a[k:]:
                b+=i
            return b
    except FileNotFoundError:
        return 'File not found'
# print(tail('t.txt'))
#___________________________________

#-----------ex151,152grel enq-------

#--------------ex153----------------
def longest_words(a):
    try:
        with open(a,'r') as file:
            file=file.read()
            file=towords(file)
            dic={}
            mmax=0
            for i in file:
                dic[i]=len(i)
                if(len(i)>mmax):
                    mmax=len(i)
            p=[]
            for i in dic:
                if(dic[i]==mmax):
                    p.append(i)
            return p
    except FileNotFoundError:
        return 'File not found'
# print('longest words are',longest_words('t.txt'))
#___________________________________

#--------------ex154----------------
def frequency(a):
    try:
        with open(a,'r') as file:
            file=file.read()
            dic={}
            for i in file:
                if(i.isalpha()):
                    dic[i.lower()]=file.count(i.lower())+file.count(i.upper())
            return dic
    except FileNotFoundError:
            return 'File not found'
# print(frequency('t.txt'))
#___________________________________

#--------------ex155----------------
def most_common_word(a):
    try:
        with open(a,'r') as file:
            file=file.read()
            file=towords(file)
            dic={}
            for i in file:
                dic[i]=file.count(i)
            key=sorted(dic,key=dic.get,reverse=True)
            return key[0]
    except FileNotFoundError:
        return 'File not found'
# print(most_common_word('t.txt'))
#___________________________________

#--------------ex156----------------
# ssum=0
# while True:
#     a=input('input the number ')
#     if(a==''):
#         break
#     try:
#         ssum+=int(a)
#         print('sum =',ssum)
#     except:
#         print('you should input a number!')  
#         print('sum =',ssum)
#___________________________________

#--------------ex157----------------
def grade_to_num(a):
    dic={
    'A+':4.0,
    'A': 4.0,
    'A-':3.7,
    'B+':3.3,
    'B':3.0 ,
    'B': 2.7,
    'C+': 2.3,
    'C':2.0,
    'C-':1.7,
    'D+':1.3,
    'D':1.0,
    'F':0
    }
    return dic[a]
def num_to_grade(a):
    a=int(a)
    dic={
    4.0:'A+',
    4.0:'A',
    3.7:'A-',
    3.3:'B+',
    3.0:'B' ,
    2.7:'B',
    2.3:'C+',
    2.0:'C',
    1.7:'C-',
    1.3:'D+',
    1.0:'D',
    0:'F'
    }
    if(a>4):
        return 'A+'
    k=a
    ind='F'
    for i in dic:
        if(((i-a)*(i-a))**0.5<k):
            k=i-a
            ind=dic[i]
    return ind
def convert(a):
    dic={}
    for i in a:
        try:
            dic[i]=num_to_grade(i)
        except:
            try:
                dic[i]=grade_to_num(i)
            except:
                dic[i]='Not possible'
    return dic
# a=[]
# while True:
#     b=input('input grade or number ')
#     if(b==''):
#         break
#     a.append(b)
# print(convert(a))
#___________________________________

#---------------ex158---------------
def comment(f1:str,f2:str):
    '''from f1 remove comments and save the information in f2'''
    try:
        b=''
        with open(f1,'r') as file:
            a=file.readlines()
            for i in a.copy():
                if(i[0]=='#'):
                    a.remove(i)
                else:
                    b+=i
        with open(f2,'w') as file:
            file=file.write(b)
            return 'Good!'
    except FileNotFoundError:
        return 'File not found'
# print(comment('t.txt','a.txt'))
#___________________________________

#---------------ex159---------------
import random
def parol(f1):
    b=''
    try:
        with open(f1,'r') as file:
           file=file.read()
           file=towords(file)
           t=0
           for i in file.copy():
               if len(i)<3:
                   file.remove(i)
               if(len(i)>7):
                   file.remove(i)
           file=sorted(file,key=len)
           if(len(file)>1 and len(file[0])+len(file[1])<=10 and len(file[-1])+len(file[-2])>=8):
               while True:
                   a1=random.choice(file)
                   h=file.copy()
                   h.remove(a1)
                   a2=random.choice(h)
                   c=a1.capitalize()+a2.capitalize()
                   if(7<len(c)<11):
                       return c
           else:
               return 'Not possible'    
    except FileNotFoundError:
        return 'File not found'
# print(parol('t.txt'))
#___________________________________

#--------------ex160----------------
def correct(k):
    a=k.lower()
    for i in range(len(a)-1):
        if(a[i]=='e' and a[i+1]=='i'):
            if(i==0 or a[i-1]!='c'):
                return False
    return True
def ei(f1:str):
    try:
        with open(f1,'r') as file:
            file=file.read()
            file=towords(file)
            t=[]
            f=[]
            for i in file:
                if('ei' in i.lower() or 'ie' in i.lower()):
                    if(correct(i)):
                        t.append(i)
                    else:
                        f.append(i)
            t=set(t)
            f=set(f)
            print("TRUE -",t)
            print("FALSE -",f,f'{len(f)} elements')
    except FileNotFoundError:
        return 'File not found'
# ei('t.txt')
#___________________________________

#---------------ex162---------------
def frequency2(a):
    try:
        with open(a,'r') as file:
            file=file.read()
            file=file.lower()
            file=towords(file)
            dic={
                'a':0,'b':0,'c':0,'e':0,'f':0,'g':0,'h':0,'i':0,'g':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0
            }
            l=len(file)
            for i in dic:
                for j in file:
                    if(i in j):
                        dic[i]+=1
                dic[i]=str(round((dic[i]/l)*100,2))+'%'
            return dic
    except FileNotFoundError:
            return 'File not found'
# print(frequency2('t.txt'))
#___________________________________

#--------------ex163----------------
def frequensy_names(lst):
    boys=set()
    try:
        for i in lst[::2]:
            with open(i,'r') as file:
                file=file.read()
                file=towords(file)
                boys.add(file[0])
        girls=set()
        for i in lst[1::2]:
            with open(i,'r') as file:
                file=file.read()
                file=towords(file)
                girls.add(file[0])
        print('boys -',boys)
        print('girls -',girls)
    except FileNotFoundError:
        print('file not found')
a=[]
# for i in range(1900,2013):
#     a.append(input(f'input the name of file with boys names of {i} year '))
#     a.append(input(f'input the name of file with girls names of {i} year '))
# frequensy_names(a)
#___________________________________

#--------------ex164----------------
def univesal_names(lst,y):
    try:
        b=lst[y-1900]
        g=lst[y-1900+1]
    except:
        print('no information of this year')
    try:
        bg=set()
        uni=['Parker','River','Rowan', 'Riley','Avery','Logan', 'Quinn', 'Jordan', 'Cameron', 'Angel','Carter','Ryan','Dylan','Noah', 'Ezra''Emery','Hunter','Kai','August', 'Nova']
        with open(b,'r') as file:
            file=file.read()
            file=towords(file)
            for i in file:
                if i in uni:
                    bg.add(i)
        with open(g,'r') as file:
            file=file.read()
            file=towords(file)
            for i in file:
                if i in uni:
                    bg.add(i)
            return bg
    except FileNotFoundError:
        print('File not found!')
# for i in range(1900,2013):
#     a.append(input(f'input the name of file with boys names of {i} year '))
#     a.append(input(f'input the name of file with girls names of {i} year '))
# year=int(input('input the year'))
# print(f'universal names of {year} are - {univesal_names(a,year)}')
#___________________________________

#--------------ex165-166 նման ձևով--------------

#--------------ex167----------------
def correct(file,dic='dictionary,txt'):
    try:
        with open(file) as file:
            file=file.read()
            file=towords(file)
            with open(dic) as f:
                f=f.read()
                f=f.split(',')
            di={}
            for i in f:
                di[i]=0
            notcorrect=[]
            for i in file:
                if di.get(i.lower())==None:
                    notcorrect.append(i)
            return notcorrect
    except FileNotFoundError:
        print('file not found')
# print(correct('a.txt','t.txt'))
#___________________________________
