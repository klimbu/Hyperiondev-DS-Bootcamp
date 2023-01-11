''' 
Using index[][] values check if adjacent indexes have # 
	if so replace - with the number of adjacent indexes with #
        if below, above, left, right
        if diagonally above right, left
        if diagonally below right, left,
'''
ms = [ 
["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"] ]

## Disclaimer: I did get some help/ inspiration from the discord group 

for row in range(len(ms)):
    for col in range(len(ms[row])):
        if ms[row][col] != '#':
            ms[row][col] = 0
            if row -1 >= 0:         
                if ms[row-1][col] == '#': # if # is above add 1
                    ms[row][col] += 1
            if row + 1 < len(ms):
                if ms[row+1][col] == "#": # if # is below add +1
                    ms[row][col] += 1
            if col -1 >= 0:         
                if ms[row][col-1] == '#': # if # is to the left add +1
                    ms[row][col] += 1
            if col +1 < len(ms):         
                if ms[row][col+1] == '#': # if # is to the right add +1
                    ms[row][col] += 1     
            if row + 1 < len(ms) and col-1 >= 0:     
                if ms[row+1][col-1] == "#": # if # is diagonally to the left (below) add +1
                    ms[row][col] += 1
            if row -1 >= 0 and col + 1 < len(ms) :
                if ms[row-1][col+1] == '#': # if # is diagonally to the right (above) add +1
                    ms[row][col] += 1
            if row + 1 < len(ms) and col + 1 < len(ms) :
                if ms[row+1][col+1] == "#": # if # is diagonally to the right (below)
                    ms[row][col] += 1
            if row -1 >= 0 and col-1 >= 0 :
                if ms[row-1][col-1] == '#': # if # is diagonally to the left (above) add +1
                    ms[row][col] += 1

for row in range(len(ms)):
    print(ms[row])