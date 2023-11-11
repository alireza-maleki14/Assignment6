# print(Game_board)
def show():
    for row in Game_board:
       for col in row:
         print(col,end=" ")
       print()

def chec_game_1():
    if Game_board[0][0]=="o" and Game_board[0][1]=="o" and Game_board[0][2]=="o" or Game_board[1][0]=="o" and Game_board[1][1]=="o" and Game_board[1][2]=="o" or Game_board[2][0]=="o" and Game_board[2][1]=="o" and Game_board[2][2]=="o" or Game_board[0][0]=="o" and Game_board[1][1]=="o" and Game_board[2][2]=="o" or Game_board[0][2]=="o" and Game_board[1][1]=="o" and Game_board[2][0]=="o" :
        print("player 1 is win.")
        quit()

def chec_game_2():
    if Game_board[0][0]=="x" and Game_board[0][1]=="x" and Game_board[0][2]=="x" or Game_board[1][0]=="x" and Game_board[1][1]=="x" and Game_board[1][2]=="x" or Game_board[2][0]=="x" and Game_board[2][1]=="x" and Game_board[2][2]=="x" or Game_board[0][0]=="x" and Game_board[1][1]=="x" and Game_board[2][2]=="x" or Game_board[0][2]=="x" and Game_board[1][1]=="x" and Game_board[2][0]=="x" :
        print("player 2 is win.")
        quit()

def check_draw(): 
    if Game_board[0][0]!="-" and Game_board[0][1]!="-" and Game_board[0][2]!="-" and Game_board[1][0]!="-" and Game_board[1][1]!="-" and Game_board[1][2]!="-" and Game_board[2][0]!="-" and Game_board[2][1]!="-" and Game_board[2][2]!="-": 
        print("Draw") 
        quit() 
        

Game_board=[['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]
show()


while True:
    #player1 o
    print("player1")
    while True:
        row=int(input("Enter a row:"))
        col=int(input("Enter a col:"))
        if 0<= row <=2 and 0<= col <=2:
            if Game_board[row][col]=='-':
                Game_board[row][col]="o"
                show()
                chec_game_1()
                check_draw()
                break
            else:
                print("yek khone dige entekhab kon")
        else:
            print("bein 0 ta 2 entekhab kon")


    #player2 x
    print("player2")
    while True:
        row=int(input("Enter a row:"))
        col=int(input("Enter a col:"))
        if 0<= row <=2 and 0<= col <=2:
            if Game_board[row][col]=='-':
                Game_board[row][col]="x"
                show()
                chec_game_2()
                break
            else:
                print("yek khone dige entekhab kon")
        else:
            print("bein 0 ta 2 entekhab kon")

