import random

tab=[]

for i in range(20):
    tab.append(int(random.randint(1,80)))

print(tab)

wart_max = tab[0]
wart_min = tab[0]

for i in range(20):
    if tab[i] >= wart_max : wart_max = tab[i]
    if tab[i] <= wart_min : wart_min = tab[i]

print("Największe ",wart_max)
print("Najmniejsze ",wart_min)
