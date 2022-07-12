#sito Eratostenesa
n = int(input("Podaj liczbę : "))
def sito(n):
    tab = [1 for x in range(n+1)]
    for i in range(2,n+1):
        for j in range (i+1, n+1):
            if j%i == 0 :
                tab[j] = 0
    pom = []
    for i in range(2,len(tab)):
        if tab[i] == 1:
            pom.append(i)
    return pom
print(sito(n))
