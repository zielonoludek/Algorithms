print('plik.mode') #sprawdzamy typ w jakim został otwarty plik
print('plik.name') #ścieżka dostępu

#“r” –   plik otwarty do odczytu (read)

#“w” –   plik otwarty do zapisu (write)
#        przed zapisem zawartość pliku jest usuwana

#“a” –   plik otwarty do zapisu, dodaje nową treść na końcu pliku,
#        nie usuwa starej (append)

plik =open('C:\\Users\\marty\\OneDrive\\Dokumenty\\Informatyka\\python\\programy\\pliki\\aaa.txt','w')
for i in range(1,11):
    plik.write(str(i)+'\n')

plik.close()

tab=[]
file = open('C:\\Users\\marty\\OneDrive\\Dokumenty\\Informatyka\\python\\programy\\pliki\\aaa.txt','r').read()
x = (file.split())
for i in range(len(x)):
    tab.append(int(x[i]))

print(tab)
