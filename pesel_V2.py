            #x --> pesel liczba 
x=int(input("Podaj pesel "))
print(x)
            #pesel --> tekst
pesel =""

for i in range(8,11):
    if x // (10**i) == 0 :
        pesel+="0"
        
for i in range(0,8):
    y=(int(x //(10**(7-i))))
    pesel+= str(y%10**1)
print(pesel)

#if len(str(x))== 11 :
#    pesel = str(x)
#else :
#    y=11-len(str(x))
#    pesel="0"*y+str(x)
#print(pesel)
