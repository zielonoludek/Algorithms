import random

def szukanie(val, tab):
    lewy = 0
    prawy = len(tab)
    print(tab)
    warunek = True
    while warunek:
        srodek = ((lewy + prawy)//2)
        if tab[srodek] < val: lewy = srodek + 1 
        else: prawy = srodek
        print(tab[lewy : prawy+1])
        if tab[prawy] == val:
            return prawy
            warunek = False
    
tab=[]
for i in range(21):
    tab.append(i)
    
x = random.randint(0,20)
print(szukanie(x,tab))
