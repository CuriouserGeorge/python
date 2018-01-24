import pprint

#hardcoded suduko
field = [[5,1,7,6,0,0,0,3,4],
         [2,8,9,0,0,4,0,0,0],
         [3,4,6,2,0,5,0,9,0],
         [6,0,2,0,0,0,0,1,0],
         [0,3,8,0,0,6,0,4,7],
         [0,0,0,0,0,0,0,0,0],
         [0,9,0,0,0,0,0,7,8],
         [7,0,3,4,0,0,5,6,0],
         [0,0,0,0,0,0,0,0,0]]
#potential values and known valuesof each suduko grid
n = 9
potent = [[set()for k in range(n)] for j in range(n)]
for a in range(1,10):
    for i in range(n):
        for j in range(n):
            if field[i][j] != 0:
                potent[i][j].add(field[i][j])

            if field[i][j] == 0:
                potent[i][j].add(a)

correct = 0
counter = 0
while correct < 81:
    correct = 0
#creating sets of numbers in rows, cols and squares
    rowSet= [set() for k in range(n)]
    colSet = [set() for k in range(n)]
    squareSet = [set() for k in range(n)]
    for i in range(n):
        for j in range(n):
            if len(potent[i][j]) == 1:
                correct +=1
                for num in potent[i][j]:
                    rowSet[i].add(num)
            if len(potent[j][i]) == 1:
                for num in potent[j][i]:
                    colSet[i].add(num)
            x = int(i/3)
            y = int(j/3)
            z = (y +3*x) %9
            w = (j%3 + 3*i) %9
            if len(potent[z][w]) == 1:
                for num in potent[z][w]:
                    squareSet[i].add(num)
    #Removing sets from potential values
    for i in range(n):
        for j in range(n):
            if not len(potent[j][i]) == 1:
                potent[j][i] = potent[j][i] - rowSet[j]
            if not len(potent[i][j]) == 1:
                potent[i][j] = potent[i][j] - colSet[j]
                
            x, y = int(i/3), int(j/3)
            z = (y +3*x) %9
            w = (j%3 + 3*i) %9
            if not len(potent[z][w]) == 1:
                potent[z][w] = potent[z][w] - squareSet[i]
    counter += 1
#prints suduko in readable format
print(correct)
print(counter)
def print_table(setx):
    """returns a grid of a list of lists of numbers

    list of list -> grid"""
    for sets in setx:
        for i in sets:
            for x in i:
             print(x,end=' ')
        print()

print_table(potent)

        
        
    










