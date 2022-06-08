# program to print "*" of two pyramid in a single pattern.

rows = 5

for row in range(rows):
    for coloumn in range(row+ 1):
        print("*", end=" ")
    print()    

for row in range(rows, -1, -1):
    for coloumn in range(row+ 1):
        print("*",  end=" ")   
    print()    