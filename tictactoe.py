'''
1 2 3	0 1 2 
4 5 6	3 4 5
7 8 9	6 7 8
'''
def printBoard(board):
	count=0
	s=""
	for ind,i in enumerate(board):
		print(i,end=" | ")
		count+=1
		if count%3==0:
			print()

def checkSuccess(board):
	if board[0]!='*':
		if (board[0]==board[1] and board[1]==board[2]) or (board[0]==board[3] and board[3]==board[6]) or (board[0]==board[4] and board[4]==board[8]):
			print("inside 0")
			return board[0]
	if board[8]!='*':
		if (board[8]==board[7] and board[7]==board[6]) or (board[8]==board[5] and board[5]==board[2]):
			return board[8]
	if board[2]!='*':
		if board[2]==board[4] and board[4]==board[6]:
			return board[2]
	if board[4]!='*':
		if (board[1]==board[4] and board[4]==board[7]) or (board[5]==board[4] and board[4]==board[5]):
			return board[4]
	return -1


#main program starts here
playAgain=True
while playAgain:
	player1=input("Do you want to play with 'X' or 'O' : ")
	player2="O"
	if player1=="O":
		player2="X"
	elif player1!="O" and player1!="X":
		print("Invalid input so assigning default values 'X' for player1 and 'O' for player2")
	board=['*','*','*','*','*','*','*','*','*']
	player=1
	gameOver=-1
	while gameOver==-1:
		index=int(input("Enter the number where you want to put your value : "))
		if board[index-1]=='*':
			if player==1:
				board[index-1]=player1;
				player=2
			else:
				board[index-1]=player2;
				player=1
			gameOver=checkSuccess(board)
		else:
			print("Value already exists in that index. So re-enter another index.")
		print('\n'*2)
		printBoard(board)
		if '*' not in board:
			break
	if gameOver==player1:
		print("Player1 won the match")
	elif gameOver==player2:
		print("Player2 won the match")
	else:
		print("Game tied")
	playAgain=(input("Do you want to play again? Press 'Y' for Yes : ")=="Y")
