if not a1:
    # print("Variable is empty")
    c1='no value in database'

else:
    print('Variable has value')
    print('------------------------------')
    i=0
    c1=a1[i][0]

    print('c1=',c1,' c1 type=',type(c1))
    print('------------------------------')
    r=len(a1)
    print('length a1=',r)
    print('------------------------------')
    for i in range(len(a1)):
        print('i=',i)
        print('-----------')
        print('-----------')
        c1=a1[i][0]
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