#Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри
s=int(input('suma='))
bill=[200,100,50,20,10]
if s<bill[len(bill)-1] or s%bill[len(bill)-1]>0:
    print('not possible')
else:
    F=True
    k1=10
    while k1>=0 and F:
        k2=10
        while k2>=0 and F:
            k3=10
            while k3>=0 and F:
                k4=10
                while k4>=0 and F:
                    k5=10
                    while k5>=0 and F:
                        if k1*bill[-1]+k2*bill[-2]+k3*bill[-3]+k4*bill[-4]+k5*bill[-5]==s:
                            print(k1,'-',bill[-1],k2,'-',bill[-2],k3,'-',bill[-3],k4,'-',bill[-4],k5,'-',bill[-5])
                            F=False
                        k5-=1
                    k4-=1
                k3-=1
            k2-=1
        k1-=1
    if F:
        print('not possible,there are not enough bills')
        
        
        