# 1 - masala

# togri = '/\ : * ? " < > | '
# check = bool
s = 'example.txt'
# for i in togri :
#     if i in s :
#         check = False
#         break
# if check :
#     file = open(s,'a')
#     file.write("bemalol yozish mumkin")
#     file.close()

# 2 - masala


# m = 'butun_sonlar.txt'
# n = int(input())
# x = list(range(1,n+1))
# print(x)
# satr = ''
# for i in x :
#     satr += str(i)+''
# f = open(m,'w')
# f.write(satr)
# f.close()

# 3 - masala

# s = "file3.text"
# a,d =int(input()),int(input())
# x = list(range(a,a+9*d,d))
# satr = ""
# for i in x :
#     satr+=str(i)+' '
# f = open(s,'w')
# f.write(satr)
# f.close()

# 4 - masala

# import os
# f1,f2,f3,f4 = 'file3.text','salom.text','example.txt','zaribjon'
# m = 0
# if os.path.exists(f1) :
#     m+=1
# if os.path.exists(f2) :
#     m+=1
# if os.path.exists(f3) :
#     m+=1
# if os.path.exists(f4) :
#     m+=1
# print(m)

# 5 - masala

# file = open('file3.text','r')
# print(len(file.read().split()))
# file.close()

# 6 - masala

# file = open('file3.text','r')
# x = file.read().split()
# file.close()
# print(x)

# 7 - masala

# m = 'file7.txt'
# x = list(range(1,9))
# satr = ''
# for i in x:
#     satr +=str(i)+""
# print(satr[0],satr[1],satr[-1],satr[-2])
# file = open(m,'w')
# file.write(satr[0])
# file.write(satr[1])
# file.write(satr[-2])
# file.write(satr[-1])
# file.close()

# 8 - masala

# f1, f2 = 'file3.txt', 'file8.txt'
# file = open('file3.text','r')
# x = file.read().split()
# file.close()
# satr,satr1 = str(x[-1]),str(x[0])
# print(satr)
# file = open(f2,'w')
# file.write(satr)
# file.write(satr1)
# file.close()

# 9 - masala

# f1, f2 = 'file3.txt', 'file9.txt'
# file = open('file3.text','r')
# x = file.read().split()
# file.close()
# satr,satr1 = str(x[-1]),str(x[0])
# print(satr)
# file = open(f2,'w')
# file.write(satr)
# file.close()

# 10 - masala

# m = 'file10.text'
# file = open('file3.text','r')
# x = file.read().split()
# file.close()
# x.reverse()
# print(x)
# satr = ''
# for i in x :
#     satr+=str(i)+' '
# file = open(m,'w')
# file.write(satr)
# file.close()

# 11 - masala

# f1,f2 = 'file11_1.txt', 'file11_2.txt'
# x = list(range(1,15,3))
# satr1 = ''
# satr2 = ""
# print(x)
# for i in range(len(x)):
#     if i%2==0 :
#         satr1 +=str(x[i])+' '
#     else:
#         satr2 += str(x[i])+' '
# print(satr1,satr2)
# file = open(f1,'w')
# file.write(satr1)
# file.close()
# file = open(f2,'w')
# file.write(satr2)
# file.close()


# 12 - masala

# f1,f2 = 'file12_1.txt', 'file12_2.txt'
# x = list(range(1,15,3))
# satr1 = ''
# satr2 = ""
# print(x)
# for i in range(len(x)):
#     if i%2==0 :
#         satr2 +=str(x[i])+' '
#     else:
#         satr1 += str(x[i])+' '
# print(satr1,satr2)
# file = open(f1,'w')
# file.write(satr1)
# file.close()
# file = open(f2,'w')
# file.write(satr2)
# file.close()

# 13 - masala

# f1,f2 = 'file13_1.txt','file13_2.txt'
# x = [1,2,-3,-6,4,-12,8,-10]
# satr1 = ''
# satr2 = ''
# for i in range(len(x)):
#     if x[i]==abs(x[i]) :
#         satr1+=str(x[i])+" "
#     else:
#         satr2+= str(x[i])+" "
# print(satr2)
# print(satr1)
# file = open(f1,'w')
# file.write(satr1)
# file.close()
# file = open(f2,'w')
# file.write(satr2)
# file.close()

# 14 - masala

# file = open('file3.text','r')
# x = file.read().split()
# file.close()
# for i in range(len(x)) :
#     x[i] = int(x[i])
# print(sum(x)/len(x))

# 15 - masala

# file = open('file3.text','r')
# x = file.read().split()
# file.close()
# print(x)
# for i in range(len(x)) :
#     x[i] = int(x[i])
# s = 0
# for i in range(0,len(x),2):
#     s+=x[i]
# print(s)

# 16 - masala

# file = open('file3.text','r')
# print(len(file.read().split()))
# file.close()

# 18 - masala

# f = 'file18.txt'
# x = [1,2,3,4,5,3,12,6,9]
# satr = ''
# for i in x:
#     satr += str(i)+' '
# file = open(f,'w')
# file.write(satr)
# file.close()
# file = open(f,'r')
# y = file.read().split()
# file.close()
# for i in range(len(y)) :
#     y[i] = int(y[i])
# for i in range(1,len(y)-1) :
#     if y[i-1] < y[i] >y[i+1] :
#         print(y[i])
#         break

# 19 - masala

# f = 'file18.txt'
# x = [1,2,3,4,5,3,12,6,9]
# satr = ''
# for i in x:
#     satr += str(i)+' '
# file = open(f,'w')
# file.write(satr)
# file.close()
# file = open(f,'r')
# y = file.read().split()
# file.close()
# max = 0
# for i in range(len(y)) :
#     y[i] = int(y[i])
# for i in range(1,len(y)-1) :
#     if y[i-1] < y[i] >y[i+1] :
#         max = y[i]

# 20 - masala

# f = 'file18.txt'
# x = [1,2,3,4,5,3,12,6,9]
# satr = ''
# for i in x:
#     satr += str(i)+' '
# file = open(f,'w')
# file.write(satr)
# file.close()
# file = open(f,'r')
# y = file.read().split()
# file.close()
# for i in range(len(y)) :
#     y[i] = int(y[i])
# for i in range(1,len(y)-1) :
#     if y[i-1] < y[i] >y[i+1]  or y[i-1] > y[i] <y[i+1] :
#         print(y[i])

# 21 - masala

# f = 'file21.txt'
# x = [2,3,4,7,9,4,2,6,8,12,5]
# satr = ''
# for i in range(1,len(x)-1) :
#     if x[i-1]<x[i]>x[i+1] :
#         satr+=str(i)+' '
# print(satr)
# file = open(f,'w')
# file.write(satr)
# file.close()

# 22 - masala

# f = 'file22.txt'
# x = [2,3,4,7,9,4,2,6,8,12,5]
# satr = ''
# for i in range(1,len(x)-1) :
#     if x[i-1]<x[i]>x[i+1] or x[i-1]>x[i] <x[i+1] :
#         satr+=str(i)+' '
# print(satr)
# file = open(f,'w')
# file.write(satr)
# file.close()

# 23 - masala

# f = 'file23.txt'
# a = [1,2,3,5,4,3,7,5,3,8,7,5,3,2,9,8,6]
# s = 0
# for i in range(len(a)-1) :
#     m = 0
#     if a[i] >a[i+1] :
#         for j in range(i+1,len(a),1) :
#             if a[i] < a[j] :
#                 m += 1
#                 i = j
#     s += m
# print(s)

# 25 - masala

# f = 'file25.txt'
# file = open('file3.text','r')
# x = file.read().split()
# file.close()
# for i in range(len(x)) :
#     x[i] = int(x[i])
#
# y = []
# for i in range(len(x)) :
#     y.append(x[i]*x[i])
# print(y)
# satr = ''
# for i in y :
#     satr+=str(i)+" "
# file = open(f,'w')
# file.write(satr)
# file.close()

# 26 - masala

# f = 'file26.txt'
# file = open('file25.txt','r')
# x = file.read().split()
# file.close()
# for i in range(len(x)) :
#     x[i] = int(x[i])
# x.sort()
# x[0],x[-1] = x[-1],x[0]
# satr = str(x[0])+" "+str(x[-1])
# file = open(f,'w')
# file.write(satr)
# file.close()

# 27 - masala

# f = 'file27.txt'
# file = open('file25.txt','r')
# x = file.read().split()
# file.close()
# for i in range(len(x)) :
#     x[i] = int(x[i])
# y = []
# for i in x :
#     y.append(x[0])
#     y.append(x[-1])
#     x.pop(0)
#     x.pop(-1)
# print(y)
# satr = ' '
# for i in y :
#     satr += str(i)+' '
# file = open(f,'w')
# file.write(satr)
# file.close()

# 28 - masala

# f = 'file28.txt'
# file = open('file25.txt','r')
# x = file.read().split()
# file.close()
# for i in range(len(x)) :
#     x[i] = int(x[i])
# print(x)
# satr = ''
# y  = []
# for i in range(2,len(x)-2) :
#     y.append((x[i-1]+x[i]+x[i+1])//3)
# for i in y :
#     satr += str(i)+' '
# file = open(f,'w')
# file.write(satr)
# file.close()

# 29 - masala

# f = 'file29.txt'
# file = open('file25.txt','r')
# x = file.read().split()
# file.close()
# print(x)
# for i in range(len(x)) :
#     x[i] = int(x[i])
# del x[5:]
# print(x)
# satr = ''
# for i in x :
#     satr += str(i)+' '
# file = open(f,'w')
# file.write(satr)
# file.close()

# 30 - masala

# f = 'file30.text'
# x = list(range(0,20,2))
# print(x)
# satr = ''
# for i in x :
#     satr += str(i)+' '
# file = open(f,'w')
# file.write(satr)
# file.close()
#
# file = open('file30.text','r')
# y = file.read().split()
# file.close()
# for i in range(len(y)) :
#     y[i] = int(y[i])
# del y[len(y)//2 :]
# print(y)
# satr1 = ' '
# for i in y :
#     satr1 += str(i)+' '
# file = open('file30_1.txt','w')
# file.write(satr1)
# file.close()

# 31 - masala 29- bn bir xil yolda ishlanadi

# 32 - masala

# f = 'file32.text'
# x = list(range(0,20,2))
# print(x)
# satr = ''
# for i in x :
#     satr += str(i)+' '
# file = open(f,'w')
# file.write(satr)
# file.close()
#
# file = open('file32.text','r')
# y = file.read().split()
# file.close()
# for i in range(len(y)) :
#     y[i] = int(y[i])
# del y[ :len(y)//2]
# print(y)
# satr1 = ' '
# for i in y :
#     satr1 += str(i)+' '
# file = open('file32_1.txt','w')
# file.write(satr1)
# file.close()

# 33 - masala

# y = []
# file = open('file25.txt','r')
# x = file.read().split()
# file.close()
# print(x)
# for i in range(len(x)):
#     x[i] = int(x[i])
# for i in range(0,len(x),2) :
#     y.append(x[i])
# print(y)
# satr = ''
# for i in y :
#     satr += str(i)+' '
# file = open('file25.txt','w')
# file.write(satr)
# file.close()

# 34 - masala

# f = 'file34.txt'
# x = [2,3,4,-5,6,-6,8,-23,13,-18,-14]
# satr = ''
# for i in x :
#     satr += str(i)+' '
# file = open(f,'w')
# file.write(satr)
# file.close()
# file = open('file34.txt','r')
# y = file.read().split()
# file.close()
# for i in range(len(y)) :
#     y[i] = int(y[i])
# m = []
# for i in range(len(y)):
#     if  y[i] > 0 :
#         m.append(y[i])
# print(m)
# satr1 = ''
# for i in m :
#     satr1 += str(i)+' '
# file = open('file34.txt','w')
# file.write(satr1)
# file.close()

# 35 - masala

# x = list(range(1,51,2))
# y =[]
# for i in range(len(x)) :
#     y.append(x[i])
#     y.append(0)
# satr = ' '
# for i in y :
#     satr += str(i)+' '
# file = open('file35.txt','w')
# file.write(satr)
# file.close()

# 36 - masala

# file = open('file25.txt','r')
# x = file.read().split()
# file.close()
# x +=x
# satr = ''
# for i in x :
#     satr += i+' '
# file = open('file36.txt','w')
# file.write(satr)
# file.close()

# 37 - masala

# file = open('file25.txt','r')
# x = file.read().split()
# file.close()
# x.reverse()
# x +=x
# satr = ''
# for i in x :
#     satr += i+' '
# file = open('file36.txt','w')
# file.write(satr)
# file.close()

# 38 - masala

# x = list(range(15))
# y = []
# for i in range(1,len(x),2) :
#     y.append(x[i])
#     y.append(x[i])
# satr = ''
# for i in y :
#     satr += str(i)+' '
# file = open('file38.txt','w')
# file.write(satr)
# file.close()
