pesel=input("Jaki masz pesel?: ")
len(pesel)
waga=[]
for i in range(5):
    w=2*i+1
    if w != 5:
        waga.append(w)
suma = 0
il = 0
mn = 0
for i in range (10):
    il+=1
    suma += int(pesel[i])*waga[i-4*mn]
    if il % 4 == 0 :
        mn += 1
    suma_kntr = (10 - suma%10) % 10
    
if int(pesel[10]) == suma_kntr:
    print("\nPesel jest prawdziwy\n")
else : print("\nPesel jest fałszywy\n")

dzien=pesel[4:6]

if int(pesel[2]) == 0 or int(pesel[2]) == 1:
    rok = "19"+ pesel[:2]
elif int(pesel[2]) == 2 or int(pesel[2]) == 3:
    rok = "20"+ pesel[:2]

mies_slownie = [0, 'Stycznia', 'Lutego', 'Marca', 'Kwietnia', 'Maja', 'Czerwca'
                , 'Lipca', 'Sierpnia', 'Września', 'Października', 'Listopada', 'Grudnia']

miesiac = pesel[2:4]

if int(miesiac)>12:
    mies= int(miesiac)-20
else:
    mies= miesiac
    
miesiac = mies_slownie[mies]
print(dzien," ",miesiac," ",rok)

if int(pesel[9])%2 == 0:
    print("\nkobieta")
else : print("\nmężczyzna")
