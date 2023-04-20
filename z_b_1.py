#Банкомат видає суму максимально можливими купюрами
s=int(input('suma='))
bill=[1000, 500,200,100,50,20,10]
if s<bill[len(bill)-1] or s%bill[len(bill)-1]>0:
    print('not possible')
else:
    for b in bill:
        #print(b)
        kil=0
        while s>=b:
            kil+=1
            s-=b
        if kil:
            print(b,' -',kil, end=' ')
        
        