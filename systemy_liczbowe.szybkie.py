print('Program zamienia liczbę zapisaną w systemie dziesiętnym na notację w systemie  dwójkowym i szesnastkowym.') 
print('\n') 
n = int(input('Podaj liczbe      n = ')) 
print('\n')

dwojkowy = [] 
n_pom = n 
reszta = n_pom % 2 
il = 0

while (n_pom >= 1): 
    dwojkowy.append(reszta) 
    n_pom = n_pom // 2 
    reszta = n_pom % 2 
    il += 1 
print(il)
print(dwojkowy)
tab=[]
for i in range(il): 
    tab.append(dwojkowy[il - i - 1])

print(tab)
heksa = [] 
suma = 0 
k = 0 
licz = 0 
ilosc_przeb = 0 

for i in range(il): 
    suma = suma + dwojkowy[i]*(2**(i-4*k)) 
    licz +=1 
    ilosc_przeb += 1 
# print(i,' ',licz,' ',i-4*k,' ',suma) 
    if (licz % 4) == 0:
        k += 1 
        heksa.append(suma) 
        suma = 0 
        licz = 0 

if ((ilosc_przeb % 4) != 0): 
    heksa.append(suma) 
    k += 1 

lista_heks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F'] 
heksa_num = [] 

for i in range(k): 
    for j in range(16): 
        if heksa[i] == j: 
            heksa_num.append(lista_heks[j]) 

print('\nw systemie szesnastkowym', heksa) 

for i in range(k):
    print(heksa_num[k - i - 1], end="")
