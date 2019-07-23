
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
# def en_3(a):
#     # a = input("打牌：")
#     # a = '''[''D1'' , ''H1'' , ''H10'' , ''H7'' , ''S1'' , ''S7'']'''
#     a = a.replace("''",'"')
#     a=a[2:-2]
#     a_li = a.split('" , "')
#     s = {}
#     for i in a_li:
#         j = i [1:]
#         if(j not in s):
#             s[j]=1
#         else:
#             s[j]+=1
#     q1 = 0
#     q2 = 0
#     for m in s:
#         if  (s[m] == 3):
#             q1 = 1
#         if (s[m]==2):
#             q2 = 1
#     if(q1==1  and q2 ==1):
#            print("3带2")
#     else:
#            print("没有3带2")
#
# with open("D:\\softwaredata\\pycarm\\zhs_1\\shaz\\dma04\\rui_1.txt",'r') as f:
#     # lines = f.readlines()
#     qq = f.readlines()
#     for io in qq :
#         io = io.replace('\n','')
#         print(io)
#         en_3(io)


def a_1 (a,b):
     d = a+b
     print(a,'+',b,'=',d)
     return d
a_1(5,3)

def a_2 (q,w):
    f = q-w
    print(q,'-',w,'=',f)
a_2(556,985)

def a_3 (e,r):
    g = e*r
    print(e,'*',r,'=',g)
a_3(3,5)
def a_4(a,s):
    qq = a/s
    print(a,'/',s,'=',qq)
a_4 (10,5)

a_1(a_1(5,3),8)



def qq(q1,q2,q3,q4):
    return '{}和{}{}吧！不行在加一顿{}'.format(q1,q2,q3,q4)
print(qq('张艳艳','我去海南','吃生蚝','皮皮虾'))

def hai_xian(q1,q2):
print('来海鲜店')
h_x = q1
print('告诉大妈我要买',h_x,'海鲜')
dama = 30
dsq = q2
print('给钱',dsq)
dsql = dsq - dama*h_x
print('拿走',h_x,'海鲜,还剩下',dsql,'元钱')












