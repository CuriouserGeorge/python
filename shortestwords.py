def findShortestWords(txt):
    import string
    txt = txt.lower()
    table = str.maketrans('', '', string.punctuation)
    txt.translate(table)
    txt = txt.split()
    txt.sort()
    print (txt)

    minlength = min(len(s) for s in txt)
    
    lst = []
    
    for i in range(len(txt)):
        if len(txt[i]) == minlength and not txt[i].isdigit():
            lst.append(txt[i])
        
        
    return lst

















