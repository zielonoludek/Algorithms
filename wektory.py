import random
A=[]
B=[]
skalar=0
wektor=[]
tab=[]
for i in range(6):
    tab.append(random.randint(0,40)-20)

#składowe wektorów
ax, ay, az, bx, by, bz = tab[0],tab[1],tab[2],tab[3],tab[4],tab[5]

#wektory jednostkowe
xi,yj,zk = 1,1,1
# A =  ax*xi + ay*yj + az*zk , B analogicznie

# współrzędne wektora
A=[ax*xi, ay*yj, az*zk]
B=[bx*xi, by*yj, bz*zk]
print("\nWspółrzędne: \nwektora A = ", A,"\nwektora B = ",B)

#długość wektorów
dla= round((ax**2 + ay**2)**0.5,2)
dlb= round((bx**2 + by**2)**0.5,2)
print("\nDługości : \n|A| = ", dla,"\n|B| = ", dlb)

#dodawanie i odejmowanie wektorów
#dodawaie :  (ax+bx)*xi + (ay+by)*yj + (az+bz)*zk
#odejmowanie : (ax-bx)*xi + (ay-by)*yj + (az-bz)*zk
suma = [ax + bx, ay+by, az+bz]
roznica = [ax - bx, ay-by, az-bz]
print("\nA + B =  ", suma,"\nA - B =  ",roznica)

# a1 przesunięcie wektora A wzdłuż osi X,
# a2 analogicznie wzdłuż osi Y 
print("\nZ1 = a1 + b1 = ", ax + bx)
print("Z2 = a1 - b1 = ", ax - bx)
print("Z1 + Z2 = ", (ax + bx)+(ax - bx) )
print("Z1 - Z2 = ", (ax + bx)-(ax - bx))

#iloczyn skalarny
skalar= ax*bx + ay*by + az*bz
print('\nIloczyn skalarny  :   \nA * B = ', skalar)

#iloczyn wektorowy
# wektorowy : (ay*bz - az*by)*xi + (az*bz - ax*bz)*yj + (ax*by - ay*bx)*zk
wektor= [(ay*bz - az*by), (az*bz - ax*bz), (ax*by - ay*bx)]
print("\nIloczyn wektorowy:   \nA x B = ", wektor)
