import random
tab=[[],[],[],[],[],[],[],[],[],[]]

for i in range(10) :
    for j in range(10):
        if i<j :
            x= ((random.randint(0,20)-5)%2) #podzielne przez 2
            if x==0:
                x=-20
                tab[i].append(x)
            else : tab[i].append(" ")  
        elif i>j :
            x= ((random.randint(0,20)-5)) #mniejsze od 0
            if x > 0 :
                x=-100
                tab[i].append(x)
            else : tab[i].append(" ")
        elif i==j : tab[i].append((random.randint(0,20)-5)**2)
print(tab)
