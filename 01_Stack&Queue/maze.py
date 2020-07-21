class Offsets:
    def __init__(self, vert, horiz, name):
        self.vert = vert
        self.horiz = horiz
        self.name = name

move = [ 
    Offsets(-1,0, "N"), Offsets(-1,1, "NE"), 
    Offsets(0, 1, "E"), Offsets(1, 1, "SE"),
    Offsets(1, 1, "S"), Offsets(1, -1, "SW"),
    Offsets(0,-1, "W"), Offsets(-1,-1, "NW")
]
maze = [ [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
         [1, 1, 0, 1, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
w = len(maze)
h = len(maze[0])
# [ print(w) for w in maze ]
mark = [ [0] * h ] * w
# [ print(x) for x in mark ]
exitRow = w-1
exitCol = h-1

stack = []
found = False

mark[1][1] = 1
stack.append([1, 1, 2]) #row, col, dir

while len(stack) > 0 and found == False :
    position = stack.pop()
    print("pop stack : ", position)
    row = position[0]
    col = position[1]
    dirt = position[2]

    while dirt < 8 and found == False :
        # move dirt
        nextRow = row + move[dirt].vert
        nextCol = col + move[dirt].horiz
        print("   next : ", nextRow, nextCol)

        if nextRow == exitRow and nextCol == exitCol : 
            found = True
            print("Found!!!")
        elif maze[nextRow][nextCol] == 0 and mark[nextRow][nextCol] == 0 :
            #길이 있으면서 이전에 가지 않은 길
            mark[nextRow][nextCol] = 1
            stack.append([row, col, dirt+1])
            print("      find path : ", row, col, move[dirt].name)
            
        else : 
            dirt += 1
            print("      no path")

if found == True :
    print("The path is :")
    print( "row  col")
    for n in range(len(stack)) : 
        print( stack[n] )
    