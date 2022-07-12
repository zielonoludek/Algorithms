a, b, n = 400, 36000, 500

def y(x):
    g = 6.67e-11
    m1 = 5.97e+24
    m2 = 2e+04
    return (g*m1*m2)/x*2

x, sila, pom = a, 0, (b-a)/n

while x <= b:
    sila += pom*y(x)
    x += (b-a)/n

print(sila)
        
