
a=11111
print(type(a))
print(a)

b="rui"
print(type(b))
print(b)

c = [1,2,3,4]
print(type(c))
print(c)

d = (1,3,5,76)
print(type(d))
print(d)

e = {"姓名":"海豚","手机号":"13627546515","性别":"女"}
print(type(e))
print(e)
# 小明有20块钱，红双喜10块钱，玉溪25块钱，大前门5块钱   求出小明可以买那种烟
w = 1
if(w>=30):
    print(w, "小明能买玉溪25")
if(w>=10):
    print(w, "小明能红双喜买10")
if(w>=5):
    print(w, "小明能买大前门10")
if(w>0):
    print(w,"洗洗睡吧")
    for i in range(100):
        if (i % 2):
            print(i)

for i in range(1,10):
    for j in range(1,i+1):
        print(str(j) + str("*") + str(i)+"=" + str(i*j),end="\t")
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d\t"%(j,i,i*j),end='')
    print()
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(i, '*', j, '=', i * j, '   ', end='')
        print()

for i in [1,60,30,90,100,20,70.59,6,971,80,84]:
    c = 80
    b = 59
    a = 60
    if (i>=c):
        print(i,'优秀')
    elif(i<=b):
        print(i,'不及格')
    else:
        print(i,'及格')


o = 1
for i  in [81,90,81,90,99,5]:
    if(i<80):
        o = 2
if (o==1):
            print("优秀")
else:
            print("不优秀")

            # "01010010001110001001001010101010010101" 计算下几个0 几个1
            b = "01010010001110001001001010101010010101"
            a = 0
            s = 1
            for i in b:
                if (i == "0"):
                    a = a + 1
                else:
                    s = s + 1
            print("有", a, "个0", s, "个1")
#求1+2+3+4...+100
a = 0
for i in range(1,101):
        a = a + i
print(a)


a = 'http://qa.yansl.com/#/home'
qw = a.split('://')[0]
a = a.split('://')[1]
print(qw)

wq = a[:a.find('/')]
print(wq)

qa = a[a.find('/'):]
print(qa)
a = []
a.append('张')
a.append('艳艳')
a.append(55)
a.append(898)
b = ['是猪','020','9856']
print(a+b)
a.append(b)
print(a)
# a.pop(0)
# print(a)
# a.clear()
# print(a)
a [0]= '就是猪'
print(a)
for i in a:
    print(i)
print(a[1:4])
print(a[::2])
print(a[::-1])
if('艳艳' in a):
    print('存在')
else:
    print('不存在')


#=
#a="lkfldf张艳艳lkdlkdfljd是猪"
#按照扑克牌的规则，现在有6张牌，只要5张
#黑桃（S）红桃（H）方块（D）梅花（C）
#牌：2.3.4.5.6.7.8.9.10.J.Q.K.A
#数据库存的是下面格式的数据，写脚本验证满足3带2的牌型
#[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']
#["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]
#["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]
# a = '''["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]'''
# a = a[1:-1]
# a_li = a.split(',')
# print(a_li)
a = '''["C9" , "D6" , "D9" , "H13" , "H9" , "S7"]'''
a = a.replace("''",'"')
a=a[2:-2]
a_li = a.split('" , "')
s = {}
for i in a_li:
    j = i [1:]
    print(j)
    if(j not in s):
        s[j]=1
    else:
        s[j]+=1
print(s)
q1 = 0
q2 = 0
for m in s:
    if  (s[m] == 3):
        q1 = 1
    if (s[m]==2):
        q2 = 1
if(q1==1  and q2 ==1):
       print("3带2")
else:
       print("没有")



