userInput = input("input any positive integer")
try:
    x = int(userInput)
    total = x 
    for i in range(1,x):
        total = total*i
    print(total)
    
except ValueError:
    print( " that's not an integer")
