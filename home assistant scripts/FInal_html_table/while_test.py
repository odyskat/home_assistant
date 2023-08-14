

c=[('unknown',),('unknown',),(20,),(55,),(23,)]
print('c=',c, ' type=', type(c))
print('------------------------------')
i=0
c1=c[i][0]

print('c1=',c1,' c1 type=',type(c1))
print('------------------------------')
r=len(c)
print('length c=',r)
print('------------------------------')
for i in range(len(c)):
    print('i=',i)
    print('-----------')
    print('-----------')
    c1=c[i][0]
    print('c1=',c1,'type=',type(c1))
    print('------------------------------')
    print('------------------------------')
    if str(c1)>="unknown" :
            pass
    else:
            break

print('****************************************at the end*****************')
print('i=',i)
print('-----------')
print('c1=',c1)