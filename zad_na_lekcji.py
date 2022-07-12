import random
b=0
tab=[]
okk=[]
suma=0

def sito(suma):
    tab = [1 for x in range(suma+1)]
    for i in range(2,suma+1):
        for j in range (i+1, suma+1):
            if j%i == 0 :
                tab[j] = 0
    pom = []
    for i in range(2,len(tab)):
        if tab[i] == 1:
            pom.append(i)
    if suma in pom :
        print("suma jest liczbą pierwszą")

for i in range(0,31):
    x = random.randint(100,1000000000000000)
    print("\nx = ",x)
    pom=x
    for j in range (0,len(str(x))):
        x=str(x)
        suma+=int(x[j])
        b+=1
        if b == len(str(pom)):
            b=0
            print( "suma = ",suma)
            sito(suma)     
            suma=0
        
        
    
