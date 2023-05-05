#Write the conditions to check if anyone has won the game. This function will be called from the placeCharacter function. 
# r : In which row the current character was placed
# c : In which column the current character was placed
#returned value: True if anyone has won;Otherwise Flase
print("Welcome to TikTakToe")

while True:

    char_check = {}
    def checkBoard():
        #Write your code here
        global char_check
        
        win_check = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]]

        for k,v in char_check.items():
            for i in range(len(win_check)):
                win_step = 0
                for j in win_check[i]:
                    if j in v:
                        win_step += 1
                if win_step == 3:
                    return True
                    
    # This another way look if any of this arg is true then there will be a winner.. 
    #def checkBoard_1(r,c):
        # r_1 = board[0] == board[1] == board[2]
        # r_2 = board[3] == board[4] == board[5]
        # r_3 = board[6] == board[7] == board[8]

        # c_2 = board[1] == board[4] == board[7]
        # c_3 = board[2] == board[5] == board[8]

        # d_1 = board[0] == board[4] == board[8]
        # d_2 = board[6] == board[4] == board[2]

        
        
    #Write the necessary code to put the "char" in proper position of the board and check if anyone has won.
    #pos : The position that has been given by the player as input.
    #char : The character representing the player. It can be X or O.
    #count: It represents the number of turns. It can be from 0 to 8.
    #returned value: True if anyone has won;Otherwise Flase 
    def placeCharacter(pos,char,count):
        global char_check
        pos = int(pos)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == pos:
                    row = i
                    col = j 
                    board[i][j] = char
                    exe = [row,col]
                    if char not in char_check:
                        char_check[char] = [exe]
                    else:
                        char_check[char].append(exe)
        if count >= 4:
            checkBoard()
            if checkBoard() == True:
                return True
        
    
    def gameInitialization():
        global player1,player2
        player1 = input("Enter player 1's name: ")
        player2 = input("Enter player 2's name: ")
        print()
        print(f"{player1}, your character is X")
        print(f"{player2}, your character is O")
        
    def runGame():
        counter = 0
        f=False
        p_name=None
        while counter<9:
            printBoard()
            if counter%2==0:
                print()
                if (placeCharacter(input(f"{player1}, where do you want to place 'X':"),'X',counter)):
                    p_name = player1
                    f = True
                    break
            else:
                print()
                if (placeCharacter(input(f"{player2}, where do you want to place 'O':"),'O',counter)):
                    p_name = player2
                    f = True
                    break
            counter+=1
        printBoard()
        if f == False:
            print("The game ends in a draw.")
            
        else:
            print(f"{p_name} has won the game!!!!")
            

    board = [[1,2,3],[4,5,6],[7,8,9]]
    def printBoard():
        print()
        print("----","---","----")
        print("| "+str(board[0][0]) , "|" , str(board[0][1]) , "|" , str(board[0][2])+" |")
        print("----","---","----")
        print("| "+str(board[1][0]) , "|" , str(board[1][1]) , "|" , str(board[1][2])+" |")
        print("----","---","----")
        print("| "+str(board[2][0]) , "|" , str(board[2][1]) , "|" , str(board[2][2])+" |")
        print("----","---","----")

    player1 = player2 = None #Take input of player names in these 2 variables
    print()
    print("To start the game ----> Type 'start'")
    print("To exit the game ----> Type 'exit'")
    print()
    user_input = input()
    if user_input == "start": 

        gameInitialization()
        runGame()
    if user_input == "exit":
        break
    else:
        print()
        print("wrong input")
