import random
import numpy
import os
from msvcrt import getch
from colorama import Fore, Back, Style, init
from time import sleep

global game_board
global win_num

init() 

def clear():              #for clearing the screen after every output
    os.system('cls')


def new_game():
    choice=input("Do you want to play a default game ? y/n : ")  # default size=5 and default win_number=2048
    if choice.lower()=="n":
        size=int(input("Enter the size of board which you want the play : "))
        global win_num
        win_num=int(input("Enter the End number : "))
        if size==1 and win_num!=2:                               # checks the case of 1*1 game
            print("GAME OVER!!")
            new_game()
        else:    
            global game_board
            game_board=numpy.zeros([size,size],dtype=int)
    elif choice.lower()=="y":
        game_board=numpy.zeros([5,5],dtype=int)
        win_num=2048
    
    return game_board


def add_2(game_board):
    a=random.randint(0,len(game_board)-1)
    b=random.randint(0,len(game_board)-1)

    while game_board[a][b]!=0:
        a=random.randint(0,len(game_board)-1)
        b=random.randint(0,len(game_board)-1)
    game_board[a][b]=2
    colour(game_board)
    sleep(2)                                     #clears the screen after sleep time of 2 seconds
    clear()

    return game_board


def game_won(game_board):                       # checks if the win_number is present in the board
    
    for row in range(len(game_board)):
        for col in range(len(game_board)):
            if game_board[row][col]==win_num:
                print("CONGRATULATIONS !!! You Win.....")
                return True
                break
        
    if check_end(game_board):
        print("No moves left...GAME OVER")
        return True
    
    return False

def board_full(game_board):               #checks whether the board is full i.e. no space is left 
    
    for row in range(len(game_board)):
        for col in range(len(game_board)):
            if game_board[row][col]==0:
                return False
    return True 


def check_end(game_board):                # even when board is full it is not end of game.It can still be shifted is adjacent nos are same
    noMoves=True
    if board_full(game_board):
        for row in range(len(game_board)-1):
            for col in range(len(game_board)-1):
                if game_board[row][col]==game_board[row+1][col] and game_board[row][col]!=0:
                    return False
                if game_board[row][col]==game_board[row][col+1] and game_board[row][col]!=0:
                    return False

        if game_board[row+1][col+1]==game_board[row][col+1]:
            return False
        if game_board[row+1][col+1]==game_board[row+1][col]:
            return False

        return True           
    else:
        return False
    

def reverse_board(game_board):
    board_rev=numpy.flip (game_board,axis=1) 
    return board_rev


def transpose(game_board):
    temp=numpy.zeros([len(game_board),len(game_board)],dtype=int)
    for row in range(len(game_board)):
        for col in range(len(game_board)):
            temp[row][col]=game_board[col][row]
    return temp


def compress(game_board):     # brings all the tiles together (removes the spaces in between) 
    new_mat=numpy.zeros([len(game_board),len(game_board)],dtype=int)
    for row in range(len(game_board)):
        pos=0
        for col in range(len(game_board)):
            if game_board[row][col]!=0:
                new_mat[row][pos]=game_board[row][col]

                pos=pos+1
    
    return new_mat


def merge(game_board):       # merges all the adjacent numbers of same values
    for row in range(len(game_board)):
        for col in range(len(game_board)-1):
            if game_board[row][col]==game_board[row][col+1]:
                game_board[row][col]*=2
                game_board[row][col+1]=0
    
    return game_board


def left_shift(game_board):
    left_board=compress(merge(compress(game_board)))
    if numpy.allclose(left_board,game_board):      # checks for invalid move
        print("Invalid Move...please try another")
        return left_board
    else:
        game_board=add_2(left_board)
        return game_board
    

def right_shift(game_board):
    right_board=reverse_board(compress(merge(compress(reverse_board(game_board)))))
    if numpy.allclose(right_board,game_board):     # checks for invalid move
        print("Invalid Move...please try another") 
        return right_board
    else:
        game_board=add_2(right_board)
        return game_board
    

def up_shift(game_board):
    up_board=transpose(compress(merge(compress(transpose(game_board)))))
    if numpy.allclose(up_board,game_board):       # checks for invalid move
        print("Invalid Move...please try another")
        return up_board
    else:
        game_board=add_2(up_board)
        return game_board
        

def down_shift(game_board):          
    down_board=transpose(reverse_board(compress(merge(compress(reverse_board(transpose(game_board)))))))
    if numpy.allclose(down_board,game_board):    # checks for invalid move
        print("Invalid Move...please try another")
        return down_board
    else:
        game_board=add_2(down_board)
        return game_board
    

def colour(game_board):          #sets the number colours
    for row in range(len(game_board)):
        coloured_row=""
        for col in range(len(game_board)): 
                        
            if game_board[row][col]==0:
                coloured_row+="  0 |"
            elif game_board[row][col]==2:
                coloured_row+=Fore.GREEN + "  2 |" + Style.RESET_ALL
            elif game_board[row][col]==4:
                coloured_row+= Fore.BLUE + Style.BRIGHT + "  4 |" + Style.RESET_ALL
            elif game_board[row][col]==8:
                coloured_row+= Fore.YELLOW + "  8 |" + Style.RESET_ALL
            elif game_board[row][col]==16:
                coloured_row+= Fore.RED + " 16 |" + Style.RESET_ALL
            elif game_board[row][col]==32:
                coloured_row+= Fore.MAGENTA + " 32 |" + Style.RESET_ALL
            elif game_board[row][col]==64:
                coloured_row+= Fore.CYAN + " 64 |" + Style.RESET_ALL
            elif game_board[row][col]==128:
                coloured_row+= Fore.BLUE + Style.BRIGHT + " 128|" + Style.RESET_ALL
            elif game_board[row][col]==256:
                coloured_row+= Fore.MAGENTA + " 256|" + Style.RESET_ALL
            elif game_board[row][col]==512:
                coloured_row+= Fore.CYAN + " 512|" + Style.RESET_ALL
            elif game_board[row][col]==1024:
                coloured_row+= Fore.RED + " 1024|" + Style.RESET_ALL
            elif game_board[row][col]==2048:
                coloured_row+= Fore.YELLOW + " 2048|" + Style.RESET_ALL
                
        print(coloured_row)


def process_input(game_board):  #takes input from player in from of wasd keys and also as arrow keys
    while not game_won(game_board):
        dir=ord(getch())
        if dir==27 or dir==81 or dir==113: # Esc or Q or q
            print("Quitting Game")
            break
        elif dir==87 or dir==119:          # W or w
            game_board=up_shift(game_board)
            
        elif dir==65 or dir==97:           # A or a
            game_board=left_shift(game_board)
            
        elif dir==83 or dir==115:          # S or s
            game_board=down_shift(game_board)
            
        elif dir==68 or dir==100:          # D or d
            game_board=right_shift(game_board)
            
        if dir==224:
                               # Special keys( arrow key )     
            dir=ord(getch())
            if dir==80:                    # DOWN Key
                game_board=down_shift(game_board)
            elif dir==72:                  # UP Key
                game_board=up_shift(game_board)
            elif dir==75:                  # LEFT Key
                game_board=left_shift(game_board)
            elif dir==77:                  # RIGHT Key
                game_board=right_shift(game_board)

    while game_won(game_board):
        again=input("Do you want to play again?  y/n  : ")
        if again.lower()=="n":
            print("Quitting")
            break

        elif again.lower()=="y":
            game_board=new_game()
            game_board=add_2(game_board)
            process_input(game_board)
   

game_board=new_game()
game_board=add_2(game_board)
process_input(game_board)