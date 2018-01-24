import random
import string

goal = input("Please enter your text:")

spew = ''.join(random.choice(string.printable + string.digits) for _ in range(len(goal)))
print(spew)
spewlst = list(spew)
goallst = list(goal)
x = 0
while spewlst != goallst:
    x += 1
    for i in range(len(spewlst)):
        if spewlst[i] != goallst[i]:
            spewlst[i] = random.choice(string.printable + string.digits)
    print(''.join(spewlst))

print("this took only %d iterations!!!!" % x)




