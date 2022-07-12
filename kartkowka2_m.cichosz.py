import random
tab=[[],[],[],[],[],[],[],[],[],[]]
for i in range(10) :
    for j in range(10):
        tab[i].append(random.randint(0,45)-10)
il=0
suma_elementow=0
y=0
print(tab)
for i in range(10) :
    for j in range(10):
        if (i+j)%3 == 0:
            suma_elementow += tab[i][j]
                                   
        if (i*j)%2==0:
            y +=j*tab[i][j]
                            
        if ((j+i)>4) and (tab[i][j]<0):
            il+=1

print("\nJeżeli suma indeksów tablicy jest podzielna przez trzy, suma elementów = ",suma_elementow )

print("\nJeżeli iloczyn indeksow tablice jest podzielny przez dwa, suma wartości = ",y)

print("\nilość elementów tablicy, których wartość jest mniejsza od zera dla sumy indeksów tablicy większej niż 4 = ",il)

