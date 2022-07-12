plik=open('C:\\Users\\marty\\OneDrive\\Dokumenty\\Informatyka\\python\\programy\\pliki\\dwie_kolumny.txt','r').read()
linie = plik.split('\n')
print(linie,'\n')
x=[]
y=[]

for linia in linie:
    print(linia.split())
    x.append(int(linia.split()[0]))
    y.append(int(linia.split()[1]))
             
