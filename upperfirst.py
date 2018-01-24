def capitalize(sntce):
    s = list(sntce)
    s[0] = s[0].upper()
    for i in range(1,len(sntce)):
        if s[i].istitle:
            s[i] = s[i].lower()
        if s[i] == ' ':
            s[i+1] = s[i+1].upper()
        
    return ''.join(s)
    


x = capitalize('hello this is a test')
print(x)

