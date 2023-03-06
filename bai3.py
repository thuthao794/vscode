import math
print('Nhap hai canh ke')
a = int(input())
b = int(input())
canhhuyen = round(math.sqrt(a**2+b**2),2)
print('Canh ke thu nhat la:',a,end=', ')
print('Canh ke thu hai la:',b,end=', ')
print('co canh huyen =',canhhuyen,end='')

