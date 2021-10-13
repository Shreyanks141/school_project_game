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

#Game 3.
def game():
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
#Brains.
print("Welcome to the game bar,Here you will find different games you can play:")
print()
print("The games includes \n1)Rock,Paper,Scisssor\n2)Guess the number\n3)Tic-Tac-Toe\ 4)Connect Four")
print()
print("The detailed discribtion will be given of how to play a game with you choose it:")
print()
di = {1:"Rock,Paper,Scisssor",2:"Guess the number",3:"Tic-Tac-Toe",4:"Connect Four"}
print(di)
inp1  = int(input("Enter the number for which game you want to play of:"))
print(("-")*40)
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
    print("Bro ashraf send me the code for connet four daaaaaaaaaa")


