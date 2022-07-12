moje = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\Informatyka\\python\\programy\\pliki\\moje.txt","r")
prof = open("C:\\Users\\marty\\OneDrive\\Dokumenty\\Informatyka\\python\\programy\\pliki\\prof.txt","r")

krok = 0
for pole in range(501):
    m = moje.readline()[:-1]
    p = prof.readline()[:-1]
    krok +=1
    
    print('krok ', krok,'   moja', m,'   pana', p)
