'''
sequence[:end]    # elements from start to end-1
sequence[start:]  # elements from start to the last element
sequence[:]       # the full copy of the sequence
sequence[::step]  # every element with a given step
'''

import random

set = []
computer_pieces = []
player_pieces = []
domino_snake = []
status = ""



def snake(domino_snake, player_pieces, computer_pieces):
    # *********DOMINO SNAKE LIST AND PLAYER PIECES**********
    if(len(domino_snake) > 6):    
        for i in range(len(domino_snake))[:3]:
            print(f"{domino_snake[i]}", end= '')
        print("...", end = '')
        for i in range(len(domino_snake))[-3:]:
            print(f"{domino_snake[i]}", end= '')
    else:
        for i in range(len(domino_snake)):
            print(f"{domino_snake[i]}", end= '')
    print("\n\nYour pieces: ")
    
    for i in range(len(player_pieces)):
        print(f"{i+1}:{player_pieces[i]}")

    '''    
    print("\n\nComputer pieces: ")
    for i in range(len(computer_pieces)):
        print(f"{i+1}:{computer_pieces[i]}", end= ' ')
    '''
def bubbleSort(comp, con_):
    # ************SORT THE COMPUTER PIECES******************
  for i in range(len(comp)):
    swapped = False
    
    for j in range(0, len(comp) - i - 1):

        if (con_[comp[j][0]] + con_[comp[j][1]]) < (con_[comp[j + 1][0]] + con_[comp[j + 1][1]]):
            temp = comp[j]
            comp[j] = comp[j+1]
            comp[j+1] = temp
            swapped = True
          
    if not swapped:
      break



def countt(com_pieces, dom_pieces, con_):
    # ************COUNTS 1s, 2s...6s************
        # con_ = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for i in range(7):
            for j in com_pieces:
                for k in range(2):
                    if(j[k] == i):
                        con_[i] += 1
            for j in dom_pieces:
                for k in range(2):
                    if(j[k] == i):
                        con_[i] += 1    
        


def INPUT(player_pieces, empty, left_s, right_s):
    # ************TAKING INPUT (from user) AND INPUT VALIDITY***************
    while True:
        x = input() 
        if(len(x) == 0):
            break
        elif(int(x) in range(-len(player_pieces), len(player_pieces)+1)):
            if(int(x) == 0):
                if(empty):
                    print("Invalid input. Please try again.")
                else:
                    break   
            else:
                int_x = int(x)
                if(int_x < 0):
                    int_x *= -1
                    check = player_pieces[int_x - 1]
                    if(left_s not in check):
                        print("Illegal move. Please try again.")
                    else:
                        break
                elif(int_x > 0):
                    check = player_pieces[int_x - 1]
                    if(right_s not in check):
                        print("Illegal move. Please try again.")
                    else:
                        break
        else:
            print("Invalid input. Please try again.")
    return x

# Generates complete set
for i in range(7):
    for j in range(7):
        pair = [i, j]
        if(pair[::-1] not in set):
            set.append([i, j])
random.shuffle(set)

# Generates computer set and player set. Rest will be stock pieces
index = 27
for i in range(7):
    g = random.randint(0, index)
    computer_pieces.append(set[g])
    set.pop(g)
    index -= 1

    h = random.randint(0, index)
    player_pieces.append(set[h])
    set.pop(h)
    index -= 1

# picks the domino snake randomly and decides status and set starting value for x (input)
s = [6, 5, 4, 3, 2, 1]
for i in s:
    if([i, i] in computer_pieces):
        domino_snake.append([i, i])
        left_s = domino_snake[0][0]
        right_s = domino_snake[-1][-1]
        start_piece = computer_pieces.index([i, i])
        computer_pieces.remove([i, i])
        status = "It's your turn to make a move. Enter your command."
  
    if([i, i] in player_pieces):
        domino_snake.append([i, i])
        left_s = domino_snake[0][0]
        right_s = domino_snake[-1][-1]
        start_piece = player_pieces.index([i, i])
        player_pieces.remove([i, i])
        status = "Computer is about to make a move. Press Enter to continue..."
    
    if(domino_snake != []):
        break


# ************GAME LOOP***************
empty = False
y = 1
while True:
    
    print("=" * 70)
    print("Stock size: {}".format(len(set)))
    print("Computer pieces: {}\n".format(len(computer_pieces)))


    # ***************A.I (kind of)***************
    
    # COUNT
    con = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    countt(computer_pieces, domino_snake, con)

    # SORTING COMPUTER LIST
    bubbleSort(computer_pieces, con)

    # SNAKE LIST
    snake(domino_snake, player_pieces, computer_pieces)

    # CHECK WHO WINS
    if(len(player_pieces) == 0):
        status = "The game is over. You won!"
        print(f"\nStatus: {status}")
        break 
    elif(len(computer_pieces) == 0):
        status = "The game is over. The computer won!"
        print(f"\nStatus: {status}")
        break
    elif(left_s == right_s):
        count = 0
        for i in domino_snake:
            for j in range(0, 2):
                if(i[j] == left_s):
                    count += 1
        if(count == 8):
            print("Status: The game is over. It's a draw!")  
            break  

    # ASSIGNS STATUS AFTER FIRST ITERATION
    if((status == "It's your turn to make a move. Enter your command.") and (y != 1)):
        status = "Computer is about to make a move. Press Enter to continue..."
    elif((status == "Computer is about to make a move. Press Enter to continue...") and (y != 1)):
        status = "It's your turn to make a move. Enter your command."
    elif((status == '') and (y != 1)):
        status = "It's your turn to make a move. Enter your command."
    elif((status == ' ') and (y != 1)):
        status = "Computer is about to make a move. Press Enter to continue..."

    print(f"\nStatus: {status}")
    

    # USER INPUT
    x = INPUT(player_pieces, empty, left_s, right_s)
    
    # PROCESSES USERS INPUT
    if(len(x) >= 1):        
        # checks whether input is positive. If +ve appends at the last else if -ve appends at first
        int_x = int(x)
        if(int_x >= 1):
            check = player_pieces[int_x-1]
            if(right_s == check[-1]):
                domino_snake.append(player_pieces[int_x-1][::-1])
                player_pieces.pop(int_x-1)
            elif(right_s == check[0]):
                domino_snake.append(player_pieces[int_x-1])
                player_pieces.pop(int_x-1)
        elif(int_x <= -1):
            int_x *= -1
            check = player_pieces[int_x-1]
            if(left_s == check[0]):
                domino_snake.insert(0, player_pieces[int_x-1][::-1])
                player_pieces.pop(int_x-1)
            elif(left_s == check[-1]):
                domino_snake.insert(0, player_pieces[int_x - 1])
                player_pieces.pop(int_x - 1)
        elif(int_x == 0):
            skip = random.randint(0, len(set) - 1)
            player_pieces.append(set[skip])
            set.pop(skip)
            if(len(set) == 0):
                empty = True
            status = ' ' # if player enters 0 then 1 length space

    # PROCESSES COMPUTERS CHOICE AND VERIFIES IT
    elif(len(x) == 0):      
        # checks whether input is positive. If +ve appends at the last else if -ve appends at first
        
        i = 1
        c = -8
        
        while (i < (len(computer_pieces)+1)):
            check = computer_pieces[i-1]
            if(left_s in check):
                c = i * -1
                break
            
            if(right_s in check):
                c = i * 1
                break  
            
            i += 1
        
        if(c == -8):
            c = 0

        if(c >= 1):
            check = computer_pieces[c-1]
            if(right_s == check[-1]):
                domino_snake.append(computer_pieces[c-1][::-1])
                computer_pieces.pop(c-1)
            elif(right_s == check[0]):
                domino_snake.append(computer_pieces[c-1])
                computer_pieces.pop(c-1)
        elif(c <= -1):
            z = c * -1
            check = computer_pieces[z-1]
            if(left_s == check[0]):
                domino_snake.insert(0, computer_pieces[z-1][::-1])
                computer_pieces.pop(z-1)
            elif(left_s == check[-1]):
                domino_snake.insert(0, computer_pieces[z-1])
                computer_pieces.pop(z-1)
        elif(c == 0):
            if(empty == False):
                skip = random.randint(0, len(set) - 1)
                computer_pieces.append(set[skip])
                set.pop(skip)   
                if(len(set) == 0):
                    empty = True
                status = '' # if computer enters 0 then 0 length space
            else:
                pass
            
            
            

    left_s = domino_snake[0][0]
    right_s = domino_snake[-1][-1]
    
    y += 1        
