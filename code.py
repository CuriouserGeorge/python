import urllib.request 
from urllib.request import urlopen
import re


index = "8022"
for i in range (400):
    html = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + index)

    str =html.read()
    print(str)

    nothing = re.search(b'(?<=next nothing is )\w+', str)
    print(nothing.group(0))

    index = (nothing.group(0)).decode("utf-8") 
    
