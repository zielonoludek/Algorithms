print("Program przeliczający liczbę z systemu dziesiętnego na dwujkowy, ósemkowy i szesnastkowy\n\n")
dwujkowy=[]
dwujkowy2=[]
dwujkowy3=[]
osemkowy=[]
szesnastkowy=[]

end = 1
while end==1:
#
#
#DWOJKOWY
#
#
    x=0
    while x==0:
        n=int(input(("podaj liczbę naturalną ")))
        if (n < 0) or (type(n) != int):
            print("podaj inną liczbę")
            x=0
        elif (n > 0) and (type(n) == int) :         
            z=1
            while z==1 :
                if n >0 :
                    x = n%2
                    dwujkowy.append(x)
                    dwujkowy2.append(x)
                    dwujkowy3.append(x)
                    n = int((n-x)/2) 
                    z=1
                elif n==0:
                    z=0
                    x=1
    pombin=dwujkowy
    dwujkowy = dwujkowy[::-1]           
    dwujkowy2 = dwujkowy2[::-1]
    dwujkowy3 = dwujkowy3[::-1]
    print("\nw systemie binarnym : \n",dwujkowy)
#
#
#OSEMKOWY  
#
#
    suma = 0 
    y=0
    while y==0:
        dlugosc =len(dwujkowy)
        if dlugosc <= 3: pom = dwujkowy
        elif dlugosc > 3: pom = dwujkowy[-3:]
                                                    #jak odcinek jest równy 3
        if len(pom)==3:
            if pom[0] == 1:suma= suma + 4
            else:suma = suma
                
            if pom[1] == 1:suma= suma + 2
            else:suma = suma
            
            if pom[2] == 1:suma= suma + 1
            else:suma = suma
                                                    #jak odcinek jest równy 2        
        elif len(pom) == 2:
            if pom[0] == 1:suma= suma + 2
            else:suma = suma
        
            if pom[1] == 1:suma= suma + 1
            else:suma = suma
                                                    #jak odcinek jest równy 1
        elif len(pom) == 1:
            if pom[0] == 1:suma= suma + 1
            else:suma = suma
        
        osemkowy.append(suma)
    
        if len(dwujkowy) ==1:
            del dwujkowy[-1]
        elif len(dwujkowy) ==2:
            del dwujkowy[-1]
            del dwujkowy[-1]
      
        elif len(dwujkowy) >=3:
            del dwujkowy[-1]
            del dwujkowy[-1]
            del dwujkowy[-1]

        suma = 0
        
        if  dlugosc == 0 :
            osemkowy=osemkowy[::-1]
            if (osemkowy[0] == 0) :
                del osemkowy[0]
                print("\nw systemie osemkowym : \n",osemkowy)
                y=1
            else :
                print("\nw systemie osemkowym : \n",osemkowy)
                y=1
        elif dlugosc > 0 : y=0
#
#
#SZESNASTKOWY 
#
#
    suma = 0 
    y=0
    licz=0
    while y==0:
        dlugosc =len(dwujkowy2)
        if dlugosc <= 4: pom = dwujkowy2
        elif dlugosc > 4: pom = dwujkowy2[-4:]
                                                    #jak odcinek jest równy 4
        if len(pom)==4:
            if pom[0] == 1:     suma= suma + 8
            else:suma = suma
        
            if pom[1] == 1:     suma= suma + 4
            else:suma = suma
        
            if pom[2] == 1:     suma= suma + 2
            else:suma = suma
        
            if pom[3] == 1:     suma= suma + 1
            else:suma = suma
                                                    #jak odcinek jest równy 3
        elif len(pom)==3:
            if pom[0] == 1:     suma= suma + 4
            else:suma = suma
        
            if pom[1] == 1:     suma= suma + 2
            else:suma = suma
        
            if pom[2] == 1:     suma= suma + 1
            else:suma = suma
                                                    #jak odcinek jest równy 2        
        elif len(pom) == 2:
            if pom[0] == 1:     suma= suma + 2
            else:suma = suma
        
            if pom[1] == 1:     suma= suma + 1
            else:suma = suma

                                                    #jak odcinek jest równy 1
        elif len(pom) == 1:
            if pom[0] == 1:     suma= suma + 1
            else:suma = suma
        
        if suma == 10 :     szesnastkowy.append("A")
        elif suma == 11 :   szesnastkowy.append("B")
        elif suma == 12 :   szesnastkowy.append("C")
        elif suma == 13 :   szesnastkowy.append("D")
        elif suma == 14 :   szesnastkowy.append("E")
        elif suma == 15 :   szesnastkowy.append("F")
        else : szesnastkowy.append(suma)
    
        if len(dwujkowy2) ==1:
            del dwujkowy2[-1]
        elif len(dwujkowy2) ==2:
            del dwujkowy2[-1]
            del dwujkowy2[-1]
        elif len(dwujkowy2) ==3:
            del dwujkowy2[-1]
            del dwujkowy2[-1]
            del dwujkowy2[-1]
        elif len(dwujkowy2) >= 4:
            del dwujkowy2[-1]
            del dwujkowy2[-1]
            del dwujkowy2[-1]
            del dwujkowy2[-1]
        
        suma = 0

        if  dlugosc == 0:
            szesnastkowy=szesnastkowy[::-1]
            if (szesnastkowy[0] == 0) :
                dwujkowy = dwujkowy3
                del szesnastkowy[0]
                print("\n w systemie szesnastkowym : \n",szesnastkowy)
                y=1
            else :
                print("\n w systemie szesnastkowym : \n",szesnastkowy)
                y=1
        elif dlugosc > 0:   y=0

    o=input("\n\nCzy chcesz podać kolejną liczbę? ")
    if (o == "Tak") or (o == " Tak")or (o == "tak") or (o == " tak") or (o == "TAK") or (o == " TAK")  :
            end = 1
    else: break
dec2bin=0
#
#
#dec to bin
#
#
for a in range(len(pombin)):
    if pombin[a]==0:
        dec2bin+=0
    elif pombin[a]==1:
        dec2bin= dec2bin + 2**a
print(dec2bin)
