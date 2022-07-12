#sortowanie bąbelkowe
import random
tab,pom = [],[]
for i in range(10):
    tab.append(random.randint(-100,100))
print("Tablica przed sortowaniem bąbelkowym :   \n",tab)

for i in range(len(tab)-1):
    for i in range(len(tab)-1):
        if tab[i] >= tab[i+1]:
            tab[i], tab[i + 1] = tab[i + 1],tab[i]

print("\nPosortowana tablica rosnąco\n",tab)

for i in range(len(tab)):
    pom.append(tab[len(tab) -1 -i])
print("\nPosortowana tablica malejąco\n",pom)
