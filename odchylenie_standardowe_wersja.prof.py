import random 

n = int(input('Podaj ilość pomiarów     n = '))

x = [] 
y = [] 
xsr = 0 
    #średni x

ysr = 0 
    #średni y

sumy2 = 0 
    #suma (elipson) y do kwadratu
    
sumxepsy = 0 
    #elipson z x

sumxeps2 = 0 
    #elipson do kwadratu

# ustalam współczynnik studenta  
if n == 2: 
    alfa = 1.4 
elif n == 3 or n == 4: 
    alfa = 1.3 
elif n == 5 or n == 6: 
    alfa = 1.2 
elif n > 6 and n < 41: 
    alfa = 1.1 
else: 
    alfa = 1 

for i in range(n):
    # ustalam wartośći x i y
    x.append(random.randint(0,20)-10) 
    y.append(random.randint(0,20)-10)

    # obliczam średnie x i y
    xsr += x[i]/n 
    ysr += y[i]/n 
    sumy2 += y[i]**2

for i in range(n): 
    sumxepsy += (x[i]-xsr)*y[i] 
    sumxeps2 += (x[i]-xsr)**2 

# oblicznie śrdnich a i b 
asr = sumxepsy/sumxeps2 
bsr = ysr - asr * xsr 

print("x : \n",x)
print("\ny : \n",y)

print('\nśrednie a = ', asr) 
print('średnie b = ', bsr)

sumeps = sumy2 - asr*sumxepsy - n*ysr**2 

sa = (1/((n-2)*sumxeps2)*sumeps)**(1/2) 
sb = (1/(n*(n-2))*sumeps + sa**2 * xsr**2)**(1/2)  

# błędy obliczneń a i b 
deltaa = alfa*sa 
deltab = alfa*sb 

print('delta a = ', deltaa) 
print('delta b = ', deltab)
