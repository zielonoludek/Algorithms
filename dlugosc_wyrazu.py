anagram = open('C:\\Users\\marty\\OneDrive\\Dokumenty\\szkola\\Informatyka\\python\\programy\\anagram.txt', 'r').read()
sort = open('C:\\Users\\marty\\OneDrive\\Pulpit\\wynik.txt', 'w')


def sortowanie(tab):
    for i in range(len(tab)):
        for j in range(i, len(tab)):
            if len(tab[j]) < len(tab[i]):
                tab[i], tab[j] = tab[j], tab[i]


tab = []
linie = anagram.split()
for linia in linie:
    tab.append(linia)

print(tab)
sortowanie(tab)
