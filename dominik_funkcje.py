import random 
tab=random.randint(100,999999999999999)

print(tab)

def suma(tab):
    s=0
    while tab>0:
        s+=tab%10
        tab/=10 
        return s 

print(suma(tab))

def is_integer(suma):
    if type(suma) in (int, long):
        return True
    elif type(suma) is float:
        return number.is_integer()
    else:
        return False

print(is_integer(suma))
