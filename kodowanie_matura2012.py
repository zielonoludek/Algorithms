print("Koder z maturki 2012")
text = input("Podaj wyraz   ") 
text = text.upper() 
key = input("Podaj wyraz kodujący  ") 
key = key.upper() 
output = '' 
for i in range(len(text)): 
    c = ord(text[i]) + ord(key[i % len(key)]) - 64 
    if c > 90: 
        c -= 26 
    output += chr(c) 
print(output)
