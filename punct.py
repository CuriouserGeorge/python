def findShortestWords(txt):
    import string
    txt = txt.lower()
    txt = txt.split()
    txt.sort()
    
    #print (txt)

    minlength = min(len(s) for s in txt)
    
    lst = []
    
    for i in range(len(txt)):
        if len(txt[i]) == minlength and txt[i].isalpha():
            lst.append(txt[i])
        
        
    return lst

txt = input("please write a sentence")

word = findShortestWords(txt)

print(word)
























