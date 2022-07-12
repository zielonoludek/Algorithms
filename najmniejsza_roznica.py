import random


def roznica(tab):
    mini = 10*20
    x, y = 0, 0
    for i in range(len(tab)):
        for j in range(len(tab)):
            if abs(tab[i] - tab[j]) < mini and j != i:
                mini = abs(tab[i] - tab[j])
                x, y = i, j

    return f"{x,y,tab[x],tab[y], mini}"


tab = []
for i in range(random.randint(1, 50)):
    tab.append(random.randint(-300, 300))

print(roznica(tab))
