import random

def sortowanie_wybor(tab):
    lenght = len(tab)
    for i in range(lenght):
        for j in range(i, lenght):
            if tab[j] < tab[i]:
                tab[j], tab[i] = tab[i], tab[j]
    return tab


tab = []
ile = random.randint(1, 20)
for i in range(ile):
    tab.append(random.randint(1, 100))
print(tab)
print(sortowanie_wybor(tab))
