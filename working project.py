import mysql.connector as sql
mycon = sql.connect(host= "localhost",user="root",passwd="")
my = mycon.cursor()

#Game 1.
import random
count_rock = 0
count_paper= 0
count_scissors = 0
player_score = 0
computer_score = 0 
predict = 0
def prediction():
 global predict
 if count_rock > count_paper and count_rock > count_scissors:
   predict = 0
 elif count_paper > count_rock and count_paper > count_scissors:
   predict = 1
 elif count_scissors > count_rock and count_scissors > count_paper :
   predict = 2
 return predict
def update_counts(player_input):
  global count_rock, count_paper, count_scissors
  if player_input == 0:
    count_rock = count_rock + 1
  elif player_input == 1:
    count_paper = count_paper + 1
  else:
    count_scissors = count_scissors + 1
def update_scores(predicted, player_input):
  global player_score, computer_score
  if player_input == 0:
    if predicted == 0: 
     print("\nYou played ROCK, computer played ROCK.") 
     print("\nComputer Score:",computer_score, "\nPlayer score:", player_score)
    elif predicted == 1: 
     print("\nYou played ROCK, computer played PAPER.") 
     computer_score += 1 
     print("\nComputer Score:",computer_score, "\nPlayer score:", player_score) 
    else: 
     print("\nYou played ROCK, computer played SCISSORS.") 
     player_score += 1 
     print("\nComputer Score:",computer_score, "\nPlayer score:", player_score)
  elif player_input == 1:
    if predicted == 0:
      print("\nYou played PAPER, computer played ROCK.") 
      player_score += 1 
      print("\nComputer Score:",computer_score, "\nPlayer score:", player_score)
    elif predicted == 1:
      print("\nYou played PAPER, computer played PAPER.")
      print("\nComputer Score:",computer_score, "\nPlayer score:", player_score)
    else:
      print("\nYou played PAPER, computer played SCISSORS.")
      computer_score += 1 
      print("\nComputer Score:",computer_score, "\nPlayer score:", player_score)
  else:
    if predicted == 0:
      print("\nYou played SCISSORS, computer played ROCK.")
      computer_score += 1 
      print("\nComputer Score:",computer_score, "\nPlayer score:", player_score)
    elif predicted == 1:
      print("\nYou played SCISSORS, computer played PAPER.")
      player_score += 1 
      print("\nComputer Score:",computer_score, "\nPlayer score:", player_score)
    else:
      print("\nYou played SCISSORS, computer played SCISSORS.")
      print("\nComputer Score:",computer_score, "\nPlayer score:", player_score)
def gameplay():
  valid_entries = ['0', '1', "2"]
  while True:
    predicted = prediction()
    player_input = input("Enter either 0 for ROCK, 1 for PAPER, 2 for SCISSORS:")
    while player_input not in valid_entries:
          print("Invalid Input!")
          player_input = input("Enter either 0 for ROCK, 1 for PAPER, 2 for SCISSORS:")
    player_input = int(player_input)
    update_counts(player_input)
    update_scores(predicted, player_input)
    if player_score == 5:
      print("Congrats, You Won!")
      break
    elif computer_score == 5:
      print("Bad Luck, You Lost!")
      break
    ins = "insert into history values(%s,%s)"
    val = (zzz,"Rock,Paper,Scisssor")
    my.execute(ins,val)

#Game 2.
def gameplay2():
    cards = [[],[],[],[],[],[]]
    power_of_2 = [1,2,4,8,16,32]
    for num in range(1,64):
      b_eq = bin(num)
      bin_list = []
      for j in range(2, len(b_eq)):
        bin_list.append(int(b_eq[j])) 
      n = len(bin_list)
      for i in range(n):
        prod = bin_list[i]*2**(n-i-1)
        if prod  in power_of_2:
          cards[n-i-1].append(num)
    i = 0
    num = 0
    valid_entries = ["yes" ,"no" , "Yes" ,"No" ]
    print("Choose a number between 1 and 63 and see that the AI predicting your number")
    print("The game workes like this the number you have thought about as predicted by the AI \nBy just the AI showing you 6 cards and you answering yes or no if the number you have thought is there in the card showen or no")
    player_input = input("Please type yes or No in the input block for starting the game:\n")
    if player_input == "yes":
      while i < 6:
        print(cards[i],sep = "\n")
        desision = input("Is your num present in this card , if yes type yes or type no \n")
        while desision not in valid_entries:
          print("Invalid input")
          desision = input("Is your num present in this card , if yes type yes or type no \n")
        if desision == "yes":
          num = num + cards[i][0]
          i = i+1
        elif desision == "no":
          i = i +1
    print("The number that u have choosed is : ",num)
    ins = "insert into history values(%s,%s)"
    val = (zzz,"Guess the number")
    my.execute(ins,val)

#Game 3.
def game():
    ins = "insert into history values(%s,%s)"
    val = (zzz,"Tic-Tac-Toe")
    my.execute(ins,val)
    theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                '4': ' ' , '5': ' ' , '6': ' ' ,
                '1': ' ' , '2': ' ' , '3': ' ' }
    board_keys = []
    for key in theBoard:
        board_keys.append(key)
    def printBoard(board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")
        move = input()        
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'
#Game 4.
def game4():
    ins = "insert into history values(%s,%s)"
    val = (zzz,"Connect four")
    my.execute(ins,val)
    import numpy as np
    row_count=int(input("Enter the number of rows of the board , (>5 is preffered) :"))
    col_count=int(input("Enter the number of columns of the board, (>5 is preffered) :"))
    def create_board():
         board=np.zeros((row_count,col_count))
         return board                         
    def display_board(board):
      board=np.flip(board,0)
      dict={}
      for i in range(0,row_count):
        for j in range(0,col_count):
          if board[i][j]==0:
            dict[(i,j)]="   "
          if board[i][j]==1:
            dict[(i,j)]=" O "
          if board[i][j]==2:
            dict[(i,j)]=" X "
      for i in range(0,row_count):
        print('|',end="")
        for j in range(0,col_count):
          print(str(dict[(i,j)])+' |' , end="")
        print("\n",'-','----+'*(col_count-1) +"----+" ,sep="")
      for i in range(1,col_count+1):
        print("  " ,i,"  ",end="",sep="") 
    def drop_piece(board,row,col,piece):
      board[row][col]=piece
      pass
    def is_valid_location(board , col):
      return board[row_count-1][col]==0 
    def get_next_row(board,col):
      for r in range(row_count):
        if board[r][col]==0:
          return r 
      pass      
    def winning_move(board,piece):
      for c in range(col_count-3):
        for r in range(row_count): 
          if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
            return True
      for c in range(col_count):
        for r in range(row_count-3): 
          if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
            return True
      for c in range(col_count-3):
        for r in range(row_count-3): 
          if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
            return True
      for c in range(col_count-3):
        for r in range(row_count): 
          if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
            return True 
    turn=0
    board=create_board()
    display_board(board)
    game_over=False
    while not game_over:
      if turn==0:
          col=(int(input("Player 1 make your column selection from (1-"+str(col_count)+") :"))) - 1
          if is_valid_location(board,col):
            row=get_next_row(board,col)
            drop_piece(board,row,col,1)
            display_board(board)
            if winning_move(board,1):
              print("Player 1 WINS!!!Congrats!!")
              game_over=True 
      else:
          col=(int(input("Player 2 make your column selection from (1-"+str(col_count)+") :"))) -1
          if is_valid_location(board,col):
            row=get_next_row(board,col)
            drop_piece(board,row,col,2)
            display_board(board)
          if winning_move(board,2):
              print("Player 2 WINS!!!Congrats!!")
              game_over=True
      turn+=1
      turn=turn%2
      
#system setup:
my.execute("create database if not exists test;")
my.execute("use test;")
my.execute("create table if not exists cross_check(id varchar(25) primary key,psw varchar(25));")
my.execute("create table if not exists history(id varchar(25) primary key,games_played varchar(25));")
#Brains:
zzz = ""
ddd = 0
ppp = 0
d = 0
pp = 0 
def login_in():
    global ppp,ddd,zzz,d
    while (d == 0):
        print("To login in please enter your user id and psw:")
        inp111 = input("Enter user id:")
        inp222 = input("Enter the psw you want to set:")
        my.execute("select * from cross_check;")
        data1 = my.fetchall()
        data1 = list(data1)
        for i in data1:
            if (i[0] == inp111) and (i[1] == inp222):
                zzz = i
                print("Login in succesfull:")
                print()
                break
        if (zzz != ""):
            break
            print("User ID not found or psw entered is wrong pls")
            ttt = input("Would you like to try again:type 1:,if you want to sign in:type2:")
            if (ttt == 2):
                d = 1
                pp = 1
        my.execute("commit")
    
def sign_in():
    global pp,d,zzz,ddd
    while (ddd == 0):
        print("To sign in please enter a user id and psw:")
        inp111 = input("Enter user id:")
        inp222 = input("Enter the psw you want to set:")
        inp2222 = input("Reenter the psw you want to set :")
        if inp222 == inp2222:
            my.execute("select * from cross_check group by id;")
            data1 = my.fetchall()
            data1 = list(data1)
            if inp111 in data1:
                print("User id already exist,Pls continue to login page:")
                ppp = 1
                ddd = 1
            elif inp111 not in data1:
                ins = "insert into cross_check values(%s,%s)"
                val = (inp111,inp222)
                my.execute(ins,val)
                zzz = inp111
                ddd = 1
                ppp = 1
                print("Sign in succesfull:")
                print()
        elif (ddd == 1):
                break
        else:
            print("Both psw entered are not the same,pld try again:")
        my.execute("commit")
dd = 0
while (dd == 0):
   print("Welcome to the game bar,but first you need to sign in/login in")
   print("type 1:for sign in,type 2:for login in")
   inppp = input("Enter your choice:")
   if (inppp == "1"):
       sign_in()
       if (ppp == 0):
           dd = 1
   elif (inppp == "2"):
       login_in()
       if (pp == 0):
           dd = 1
#Actual Work:
print("Welcome to the game bar,Here you will find different games you can play:")
print()
print("The games includes\n1)Rock,Paper,Scisssor\n2)Guess the number\n3)Tic-Tac-Toe\n4)Connect Four")
print()
print("The detailed discribtion will be given of how to play a game with you choose it:")
print()
di = {1:"Rock,Paper,Scisssor",2:"Guess the number",3:"Tic-Tac-Toe",4:"Connect Four"}
print(di)
inp1  = int(input("Enter the number for which game you want to play of:"))
print(("-")*40)
las = 0
while (las == 0):
    if (inp1 == 1):
        print("You are playing Rock,Paper,Scisssor with the AI")
        print("The wining point/score is 5")
        print("You just need to give input as 0,1,2 which are representing Rock,Paper,Scisssor")
        print("!!!!Best of Luck!!!!")
        gameplay()
    elif (inp1 == 2):
        print("You are playing Guess the number with the AI")
        print("!!!!Best of Luck!!!!")
        gameplay2()
    elif (inp1 == 3):
        print("You are playing Tic-Tac-Toe")
        print("You need two players for this game")
        print("The instructions are simple,like how the keypad of phone is of \n7,8,9\n4,5,6\n1,2,3")
        print("The input of either X or O will be inputed using the numbers from 1 - 9")
        print("The number you enter is the place of your X or O")
        print("!!!!Best of Luck!!!!")
        game()
    elif (inp1 == 4):
        print("You are playing Connect Four:")
        print("You can only decide the shape of the board:")
        Print("This game is between Two players:")
        print("!!!!Best of Luck!!!!")
    inp2  = input("Do you want to play a game again ,pls enter yes or no:")
    inp2 = inp2.lower()
    if (inp2 == "yes"):
        print(("-")*40)
        print("Welcome to the game bar,Here you will find different games you can play:")
        print()
        print("The games includes \n1)Rock,Paper,Scisssor\n2)Guess the number\n3)Tic-Tac-Toe\ 4)Connect Four")
        print()
        print("The detailed discribtion will be given of how to play a game with you choose it:")
        print()
        di = {1:"Rock,Paper,Scisssor",2:"Guess the number",3:"Tic-Tac-Toe",4:"Connect Four"}
        print(di)
        inp1  = int(input("Enter the number for which game you want to play of:"))
    elif (inp2 == "no"):
        las = 1
        print("THANKS FOR PLAYING :)")
        print("History of games played are:")
        my.execute("select * from history where id == zzz;")
        data = my.fetchall()
        for i in data:
            print(data)
        my.close()
        mycon.close()
