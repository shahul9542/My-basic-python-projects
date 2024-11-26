#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output
def display_board(board):
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])
    


# In[ ]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[ ]:


test_board = [' ']*10
display_board(test_board)


# In[ ]:


from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])
    


# In[ ]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[ ]:


def player_input():
    marker = ''
    
    #Keep asking player1 choose X or O
    
    while marker != 'X' and marker != 'O':
        marker =input("Player1,Please choose X or O: ")
        
    #Assign player2 ,the opposite marker
    Player1 = marker
    
    if Player1 == 'X':
        Player2 = 'O'
    else:
        Player2 = 'X'
        
    return(Player1,Player2)
    
    
        


# In[ ]:


player_input()


# In[ ]:


player1_marker,player2_marker = player_input()


# In[ ]:


player2_marker


# In[ ]:


player1_marker


# In[ ]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)   #This is the first program
print('-----')
display_board(test_board)


# In[ ]:


test_board = ['#','X','O','X','O','X','O','X','O','X'] 
display_board(test_board)  #This is the second  progarm we use clear output that's execute one time only
print('-----')
display_board(test_board)


# now this table we maximimixe the size of the table...... 

# In[ ]:


from IPython.display import clear_output
def display_board(board):
    print('    |     |')
    print(board[7]+'   |  '+board[8]+'  |  '+board[9])
    print('    |     |')
    print('---------------')
    print('    |     |')
    print(board[4]+'   |  '+board[5]+'  |  '+board[6])
    print('    |     |')
    print('---------------')
    print('    |     |')
    print(board[1]+'   |  '+board[2]+'  |  '+board[3])
    print('    |     |')
    


# In[ ]:


display_board(test_board)


# In[ ]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[ ]:


player_input()


# STEP 2: write a function to make the select the symbol X or O until you choose correctly asiking continouslly

# In[ ]:


def player_input():
    '''
    OUTPUT : (Player1_marker,Player2_marker)
    
    '''
    
    marker = ''
    while marker != 'X' and marker != 'O':  #OR while not(marker = 'X' and marker = 'O')
        marker = input('Player1,Choose X or O: ').upper()
    if marker == 'X':
        
        return('X','O')
    else:
        return('O','X')
  


# In[ ]:


player_input()


# Test Step 2: Run the function to make sure it returns desired output

# In[ ]:


player1_marker,player2_marker = player_input()


# In[ ]:


player2_marker


# In[ ]:


test_board


# Step 3: write a function to check that the board list object ,a marker(X or O) desired the position (1-9) and assigned a position

# In[ ]:


def place_marker(board,marker,position):
    board[position] = marker


# Test step 3: run the palce marker function using test parameters in display the modified board!

# In[ ]:


place_marker(test_board,'$',8)
display_board(test_board)


# step 4: to check To check in Board X or O who is won?

# In[ ]:


def win_check(board,mark):
    # WIN TIC TAC TOE?
    
    #All rows and check if they all share the same marker?
    return ((board[1] == mark and board[2]== mark and board[3] == mark) or # bottom horizantal line
    
    (board[4] == board[5] == board[6] == mark) or # same logic
    
    (board[7] == mark and board[8]== mark and board[9] == mark) or
    #All coulums,check to see if marker matches
    (board[7] == mark and board[4]== mark and board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    #2 diagonals ,check to see match
    (board[1] == board[5] == board[9] == mark) or 
    (board[7] == board[5] == board[3] == mark))


# In[ ]:


win_check(test_board,'X')


# In[ ]:


display_board(test_board)
win_check(test_board,'X')


# Step 5: Write a function that uses the random module to randomly decide which player goes first.You may to lookup random.randint().Return a string of which player went first.

# In[ ]:


import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'


# Step6: Write a boolean function indicating a space board is freely avaliable

# In[ ]:


def space_check(board,position):
    
    return board[position] == ' '
    


# Step7: Write a boolean function if the board is full returns the boolean value,True if full otherwise False

# In[ ]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        #BOARD IS FULL IS WE RETURN TRUE
    return True


# Step8:Write a function that asks for a next palyer's position (as a number 1-9) and then use that function from step6 to check if the position is free if it is position return for later use

# In[ ]:


def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position here: (1-9)  "))
        
    return position
        
        


# Step9 :Write a function that asks if the player wants to play again and it returns a boolean True if they want to play again

# In[ ]:


def replay():
    
    choice = input('Play again? Enter Yes or No ')
    
    return choice == 'Yes'


# Step10 :Here comes the hard part! Use while loops and functions you've made to run the game

# In[ ]:


# WHILE LOOP KEEP RUNNING THE GAME
print("welcome to Tic TAC TOE!")

while True:
    
    # PLAY THE GAME HERE
    
    
    ## SET EVERYTHING UP(BOARD,CHOOSE FIRST, CHOOSE MARKERS(X or O) )
    the_board = [' ']*10
    Player1_marker,Player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to Play? y or n?')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    
    ## GAME PLAY
    while game_on:
        if turn == 'player1':
            # show the board
            display_board(the_board)
            #Choose a position
            position = player_choice(the_board)
            
            #place the marker on the position 
            place_marker(the_board,player1_marker,position)
            
            #Check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("THE GAME IS TIE!!")
                    game_on = False
                    break
                else:
                    turn = 'player2'
                        
        else:
            # show the board
            display_board(the_board)
            #Choose a position
            position = player_choice(the_board)
            
            #place the marker on the position 
            place_marker(the_board,player2_marker,position)
            
            #Check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("THE GAME IS TIE!!")
                    game_on = False
                    break
                else:
                    turn = 'player1'
    
  
    
    
    
    
    
    
    if not replay():
        break

     # Break out the while loop on replay()


# In[ ]:


def tic_tac_toe():
        # WHILE LOOP KEEP RUNNING THE GAME
    print("welcome to Tic TAC TOE!")

    while True:
    
    # PLAY THE GAME HERE
    
    
    ## SET EVERYTHING UP(BOARD,CHOOSE FIRST, CHOOSE MARKERS(X or O) )
        the_board = [' ']*10
        Player1_marker,Player2_marker = player_input()
    
        turn = choose_first()
        print(turn + ' will go first')
    
        play_game = input('Ready to Play? y or n?')
    
        if play_game == 'y':
            game_on = True
        else:
            game_on = False
    
    
        ## GAME PLAY
        while game_on:
            if turn == 'player1':
                # show the board
                display_board(the_board)
                #Choose a position
                position = player_choice(the_board)
            
                #place the marker on the position 
                place_marker(the_board,player1_marker,position)
            
                #Check if they won
                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print("PLAYER 1 HAS WON!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("THE GAME IS TIE!!")
                        game_on = False
                        break
                    else:
                        turn = 'player2'
                        
            else:
                # show the board
                display_board(the_board)
                #Choose a position
                position = player_choice(the_board)
            
                #place the marker on the position 
                place_marker(the_board,player2_marker,position)
            
                #Check if they won
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print("PLAYER 2 HAS WON!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("THE GAME IS TIE!!")
                        game_on = False
                        break
                    else:
                        turn = 'player1'
    
  
    
    
    
    
    
    
        if not replay():
            break

         # Break out the while loop on replay()
  


# In[ ]:


tic_tac_toe()


# In[ ]:




