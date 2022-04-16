# Write your code here

from itertools import product
import time

def drawboard(matrix, dim__y, dim__x):    
    spaces = len(str(dim__x * dim__y))
    for i in range(dim__y):
        col = []
        for j in range(dim__x):
            col.append("_" * spaces)
        matrix.append(col)

def updateboard(matrix_, dim__y, dim__x):
    spaces = len(str(dim__x * dim__y))
    a = 0
    gap = dim__x * (spaces + 1) + 3
    print(" ", "-" * gap)
    for i in range(dim__y, 0, -1):
        if(i < 10):
            print(f" {i}|", end=" ")
        else:
            print(f"{i}|", end=" ")
        b = 0
        for j in range(dim__x, 0, -1):
            print(matrix_[a][b], end=' ')
            b += 1
        a += 1
        print("|")
    print(" ", "-" * gap)
    print(" " * spaces, end="  ")
    for i in range(1, dim__x+1):
        print(i, end=" " * spaces)


def plot(move, dim_y, space, matrix__, count = "O"):

    new_x, new_y = move  
    shift_x = new_x - 1             # column 5
    shift_y = dim_y - new_y         # row  1
    if space == 1:
        matrix__[shift_y][shift_x] = str(count)
    elif space == 2:
        matrix__[shift_y][shift_x] = " " + str(count)
    elif space == 3:
        matrix__[shift_y][shift_x] = "  " + str(count)
    elif space == -1:
        matrix__[shift_y][shift_x] = "_"
    elif space == -2:
        matrix__[shift_y][shift_x] = "__"
    elif space == -3:
        matrix__[shift_y][shift_x] = "___"


def plotnum(move, dim_y, space, matrix__, count):

    new_x, new_y = move  
    shift_x = new_x - 1             # column 5
    shift_y = dim_y - new_y         # row  1
    if space == 1:
        matrix__[shift_y][shift_x] = str(count)
    elif space == 2 and len(count) == 1:
        matrix__[shift_y][shift_x] = " " + str(count)
    elif space == 2 and len(count) == 2:
        matrix__[shift_y][shift_x] = str(count)
    elif space == 3 and len(count) == 1:
        matrix__[shift_y][shift_x] = "  " + str(count)
    elif space == 3 and len(count) == 2:
        matrix__[shift_y][shift_x] = " " + str(count)
    elif space == 3 and len(count) == 3:
        matrix__[shift_y][shift_x] = str(count)


def plot_x(matrix, x, y, dim_y, space):
    shift_x_ = x - 1             
    shift_y_ = dim_y - y         

    if space == 1:
        matrix[shift_y_][shift_x_] = "X"
    elif space == 2:
        matrix[shift_y_][shift_x_] = " X"
    elif space == 3:
        matrix[shift_y_][shift_x_] = "  X"
    elif space == -1:
        matrix[shift_y_][shift_x_] = "*"
    elif space == -2:
        matrix[shift_y_][shift_x_] = " *"
    elif space == -3:
        matrix[shift_y_][shift_x_] = "  *"


def knight_moves(position, dim_x, dim_y):
    x, y = position
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if x > 0 and y > 0 and x <= dim_x and y <= dim_y]
    return moves


def validateMove(bo, row, col, dim_y, dim_x):
    shift_x_ = row - 1             
    shift_y_ = dim_y - col
    if bo[shift_y_][shift_x_] == "__" or bo[shift_y_][shift_x_] == "_" or bo[shift_y_][shift_x_] == "___":
        return True


def solve (bo, row, col, dimy, dimx, counter, space):
    moves = knight_moves((row, col), dimx, dimy)
    for i in moves:
        if counter >= (dimx*dimy+1):
            return True
        new_x, new_y = i
        if validateMove(bo, new_x, new_y, dimy, dimx):
            plotnum(i, dimy, space, bo, str(counter))
            if solve(bo, new_x, new_y, dimy, dimx, counter+1, space):
                return True
            plot(i, dimy, -space, bo)
    return False

def main():
    while True:
        try:
            dim = input("Enter your board dimensions: ")

            dim_x = int(dim.split()[0])
            dim_y = int(dim.split()[-1])

            assert dim_x > 0 and dim_y > 0 and len(dim.split()) == 2
            break
        except (ValueError, AssertionError):
            print("Invalid dimensions!")

    while True:
        try:
            pos = input("Enter the knight's starting position: ")

            x = int(pos.split()[0])
            y = int(pos.split()[-1])

            assert 1 <= x <= dim_x and 1 <= y <= dim_y and len(pos.split()) == 2
            break
        except (ValueError, AssertionError):
            print("Invalid position!")


    used = []
    spaces = len(str(dim_x * dim_y))


    while True:
        try:
            choice = input("Do you want to try the puzzle? (y/n): ")
            assert (choice == 'y') or (choice == 'n')
            
            if dim_x == dim_y and dim_x <= 4:
                print("No solution exists!")
                break
            
            if (dim_x < 4 and dim_y < 3) or ((dim_y < 4 and dim_x < 3)):
                print("No solution exists!")
                break

            if choice == "y":
                while True:
                    matrix = []
                    drawboard(matrix, dim_y, dim_x)
                    
                    for i in used:
                        w, z = i
                        plot_x(matrix, w, z, dim_y, -spaces)

                    plot_x(matrix, x, y, dim_y, spaces)

                    move = knight_moves((x, y), dim_x, dim_y)
                    move = [e for e in move if e not in used]
                    

                    for i in move:
                        next_move = knight_moves(i, dim_x, dim_y)
                        next_move = [j for j in next_move if j not in used]
                        c = str(len(next_move) - 1)
                        plot(i, dim_y, spaces, matrix, c)

                    updateboard(matrix, dim_y, dim_x)
                    
                    used.append((x, y))
                    plot_x(matrix, x, y, dim_y, -spaces)
                    
                    print()

                    if len(used) == dim_x * dim_y:
                        print("What a great tour! Congratulations!")
                        break
                    elif len(move) == 0:
                        print(f'''
                No more possible moves!
                Your knight visited {len(used)} squares!''')
                        break
                    
                    while True:
                        try:
                            pos = input("Enter your next move: ")

                            x = int(pos.split()[0])
                            y = int(pos.split()[-1])

                            assert 1 <= x <= dim_x and 1 <= y <= dim_y and len(pos.split()) == 2 and ((x, y) not in used) and ((x, y) in move)
                            break
                        except (ValueError, AssertionError):
                            print("Invalid move!", end=' ')
                break
            elif choice == "n":
                print()
                print("Here's the solution!")
                matrix = []
                drawboard(matrix, dim_y, dim_x)

                plot((x, y), dim_y, spaces, matrix, "1")
                start = time.perf_counter()
                solve(matrix, x, y, dim_y, dim_x, 2, spaces)
                end = time.perf_counter()
                print(end - start)
                updateboard(matrix, dim_y, dim_x)
                break

        except (ValueError, AssertionError):
            print("Invalid input!")

if __name__ == "__main__":
    main()