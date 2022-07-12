import random 

N = int(input( "n =  "))
    #  ilość pomiarów
    
X = []
    #  tabela z xami
    
epsilone = []
    #  tabela elipsonów dla każdego x
    
avg = 0
    #  średnia
    
sdev = 0
    #  odchylenie standeardowe
    
dev = 0
    #  ostateczny błąd pomiaru
    
alpha = 0
    #  współczynnik studenta
    #  tutaj używamy 70% ufności
    #  pełni role takiego wyrównania szans w błędzie  odchylenia standardowego 
    #  są 4 poziomy ufności, uznajemy że tylko x% pomiarów jest 
    #  wartch ogarniania a reszta jest błędna albo zaburzona
    #  na przykład :  50% -  najmniejszy błąd, 70%, 90%, 99% - najwiekszy błąd 
    
if N == 2: 
    alpha = 1.4 
elif 3 <= N <= 4:
    alpha = 1.3 
elif 5 <= N <= 6: 
    alpha = 1.2 
elif 7 <= N <= 40: 
    alpha = 1.1 
elif N > 40: 
    alpha = 1 
else:
    print('Error') 
    exit() 

for i in range(N): 
    X.append(random.randint(1, N)) 
    avg += X[i]/N
    
for i in range(N): 
    epsilone.append(X[i] - avg) 
    sdev += epsilone[i]**2 

sdev = (sdev/(N - 1))**0.5 
dev = alpha*sdev 
errorp = round((dev/avg)*100, 2)
    #  błąd procentowy
 
print("pomiary :  ",X) 
print("średnia  :  ", avg, ' +- ', dev) 
print("błąd procentowy  :  ",errorp, '%') 
