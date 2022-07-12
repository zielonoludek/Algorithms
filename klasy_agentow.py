plik = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\szkola\\Informatyka\\python\\programy\\agent.txt", "r").read()
lista = plik.split("\n")
print(lista)

class Agent:
    def __init__(self, wers):
        dane = wers
        self.lp = wers[0]
        self.pseudonim = wers[1]
        self.nazwisko = wers[2]
        self.imie = wers[3]
        self.adres = wers[4]
        self.miasto = wers[5]
        self.stan = wers[6]
        self.kod = wers[7]
        self.region = wers[8]
        self.kraj = wers[9]
        self.firma = wers[10]
        self.stanowisko = wers[11]
        self.tel = wers[12]
        self.ostatni_kontakt = wers[13]





for wers in lista:
    agent = wers.split("; ")
    print(agent)
