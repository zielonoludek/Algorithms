dwojkowy=[]
end = 1
pom=[]

#DWOJKOWY
n = int(input('Podaj liczbe     n = '))
x=0
dwojkowy = [] 
n_pom=n 
reszta = n_pom % 2 
il = 0

while (n_pom >= 1): 
    dwojkowy.append(reszta)
    pom.append(reszta)
    n_pom = n_pom // 2 
    reszta = n_pom % 2 
    il += 1

dobry=[]
for i in range(il): 
    dobry.append(dwojkowy[il - i - 1])
print(tab)

#dec to bin

dec2bin=0
for a in range(len(pom)):
    if pom[a]==0:
        dec2bin+=0
    elif pom[a]==1:
        dec2bin= dec2bin + 2**a
print(dec2bin)
