from tkinter import *
from tkinter import messagebox
import random

global root
root = Tk()
root.geometry('318x360')
root.title('Tic-Tac-Toe-Linh')
root.configure(bg="#141414")

# Human & Ai
ai = "O"
human = "X"
winner = 10
loose = -10

# Board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# disable all the buttons
def disable_all_buttons():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)

# Equal 3 X or 3 O
def equals3(a, b, c):
	return a == b and b == c and a != " "

# check - Winner - Check to see if someone won
def checkWinner_Board():
	global board, winner, loose, human, ai
	
	# horizontal
	for i in range(0, 3):
		if equals3(board[i][0], board[i][1], board[i][2]):
			if board[i][0] == human:
				return loose
			elif board[i][0] == ai:
				return winner
	# Vertical
	for i in range(0, 3):
		if equals3(board[0][i], board[1][i], board[2][i]):
			if board[0][i] == human:
				return loose
			elif board[0][i] == ai:
				return winner

	# Diagonal
	if equals3(board[0][0], board[1][1], board[2][2]):
		if board[0][0] == human:
			return loose
		elif board[0][0] == ai:
			return winner

	if equals3(board[0][2], board[1][1], board[2][0]):
		if board[0][2] == human:
			return loose
		elif board[0][2] == ai:
			return winner

# Tie
def checkTie_Board(board):
	# Tie
	openSpots = 0
	for i in range (0, 3):
		for j in range(0, 3):
			if board[i][j] == " ":
				openSpots += 1

	if openSpots == 0:
		return "tie"

# Minimax
def minimax(board, isMaximizing):
	global ai, human

	result = checkWinner_Board()
	if checkTie_Board(board) == "tie":
		return 0
	if result == 10:
		return result
	if result == -10:
		return result

	if(isMaximizing):
		bestScore = -1000
		for i in range(3):
			for j in range(3):
				# Is the spot avaible?
				if board[i][j] == " ":
					board[i][j] = ai
					score = minimax(board, False)
					bestScore = max(bestScore, score)
					board[i][j] = " "
		return bestScore
	else:
		bestScore = 1000
		for i in range(3):
			for j in range(3):
				# Is the spot avaible?
				if board[i][j] == " ":
					board[i][j] = human
					score = minimax(board, True)
					bestScore = min(bestScore, score)
					board[i][j] = " "
		return bestScore

# Best move
def bestMove(board):
	global human, ai
	bestScore = -1000
	score = -1
	movei = -1
	movej = -1

	# AI to make its turn
	for i in range(3):
		for j in range(3):
			# Is the spot avaible?	
			if board[i][j] == " ":
				board[i][j] = ai
				score = minimax(board, False)
				board[i][j] = " "
			if score > bestScore:
				bestScore = score
				movei = i
				movej = j

	return((3*movei)+(movej+1))

def checkForWin():
	if (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
          b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
          b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
          b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
          b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' or
          b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
          b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
          b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
		messagebox.showinfo("Tic-Tac-Toe", "Computer Wins")
		return True

	elif(b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
          b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
          b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' or
          b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
          b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' or
          b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
          b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
          b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
		messagebox.showinfo("Tic-Tac-Toe", "Player Wins")
		return True

	elif(checkTie_Board([[b1['text'],b2['text'],b3['text']],[b4['text'],b5['text'],b6['text']],[b7['text'],b8['text'],b9['text']]])== "tie"):
		messagebox.showinfo("Tic-Tac-Toe", "It's a draw") 
		return True
	return False

# Button clicked function
def b_click_Player_First(b):
	global board, human, ai

	if b["text"] == " ":
		b["text"] = human
		if checkForWin():
			return
		board = [[b1["text"], b2["text"], b3["text"]], [b4["text"], b5["text"], b6["text"]], [b7["text"], b8["text"], b9["text"]]]
		move = bestMove(board)
		if move == 1:
			b1["text"] = ai
			board[0][0] = ai
		if move == 2:
			b2["text"] = ai
			board[0][1] = ai
		if move == 3:
			b3["text"] = ai
			board[0][2] = ai
		if move == 4:
			b4["text"] = ai
			board[1][0] = ai
		if move == 5:
			b5["text"] = ai
			board[1][1] = ai
		if move == 6:
			b6["text"] = ai
			board[1][2] = ai
		if move == 7:
			b7["text"] = ai
			board[2][0] = ai
		if move == 8:
			b8["text"] = ai
			board[2][1] = ai
		if move == 9:
			b9["text"] = ai
			board[2][2] = ai
		if checkForWin():
			return	
	else:
		messagebox.showerror("Tic-Tac-Toe", "Button already Clicked!")
		
	#print(board)

def b_click_Computer_First(b):
	global board, human, ai

	if b["text"] == " ":
		b["text"] = human
		if checkForWin():
			return
		board = [[b1["text"], b2["text"], b3["text"]], [b4["text"], b5["text"], b6["text"]], [b7["text"], b8["text"], b9["text"]]]
		move = bestMove(board)
		if move == 1:
			b1["text"] = ai
			board[0][0] = ai
		if move == 2:
			b2["text"] = ai
			board[0][1] = ai
		if move == 3:
			b3["text"] = ai
			board[0][2] = ai
		if move == 4:
			b4["text"] = ai
			board[1][0] = ai
		if move == 5:
			b5["text"] = ai
			board[1][1] = ai
		if move == 6:
			b6["text"] = ai
			board[1][2] = ai
		if move == 7:
			b7["text"] = ai
			board[2][0] = ai
		if move == 8:
			b8["text"] = ai
			board[2][1] = ai
		if move == 9:
			b9["text"] = ai
			board[2][2] = ai
		if checkForWin():
			return	
	else:
		messagebox.showerror("Tic-Tac-Toe", "Button already Clicked!")
		
	#print(board)

# Start the game over!
def reset_Player_First():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9
	global board

	# Build our buttons
	b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Player_First(b1))
	b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Player_First(b2))
	b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Player_First(b3))

	b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Player_First(b4))
	b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Player_First(b5))
	b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Player_First(b6))

	b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Player_First(b7))
	b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Player_First(b8))
	b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Player_First(b9))

	# Grid our buttons to the screen
	b1.grid(row=0, column=0)
	b2.grid(row=0, column=1)
	b3.grid(row=0, column=2)

	b4.grid(row=1, column=0)
	b5.grid(row=1, column=1)
	b6.grid(row=1, column=2)

	b7.grid(row=2, column=0)
	b8.grid(row=2, column=1)
	b9.grid(row=2, column=2)

def reset_Computer_First():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9
	global board

	# Build our buttons
	b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Computer_First(b1))
	b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Computer_First(b2))
	b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Computer_First(b3))

	b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Computer_First(b4))
	b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Computer_First(b5))
	b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Computer_First(b6))

	b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Computer_First(b7))
	b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Computer_First(b8))
	b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click_Computer_First(b9))

	# Grid our buttons to the screen
	b1.grid(row=0, column=0)
	b2.grid(row=0, column=1)
	b3.grid(row=0, column=2)

	b4.grid(row=1, column=0)
	b5.grid(row=1, column=1)
	b6.grid(row=1, column=2)

	b7.grid(row=2, column=0)
	b8.grid(row=2, column=1)
	b9.grid(row=2, column=2)

	i = random.randint(0, 2)
	j = random.randint(0, 2)

	move = ((3*i)+(j+1))

	if move == 1:
		b1["text"] = ai
		board[0][0] = ai
	if move == 2:
		b2["text"] = ai
		board[0][1] = ai
	if move == 3:
		b3["text"] = ai
		board[0][2] = ai
	if move == 4:
		b4["text"] = ai
		board[1][0] = ai
	if move == 5:
		b5["text"] = ai
		board[1][1] = ai
	if move == 6:
		b6["text"] = ai
		board[1][2] = ai
	if move == 7:
		b7["text"] = ai
		board[2][0] = ai
	if move == 8:
		b8["text"] = ai
		board[2][1] = ai
	if move == 9:
		b9["text"] = ai
		board[2][2] = ai

def exit():
	global root
	root.destroy()

def game_Player_First():
	# Create menue
	my_menu = Menu(root)
	root.config(menu=my_menu)

	# Create Options Menu
	options_menu = Menu(my_menu, tearoff=False)
	my_menu.add_cascade(label="Options", menu=options_menu)
	options_menu.add_command(label="Reset Game", command=reset_Player_First)
	options_menu.add_command(label="Exit", command=exit)

	reset_Player_First()

def game_Computer_First():
	# Create menue
	my_menu = Menu(root)
	root.config(menu=my_menu)

	# Create Options Menu
	options_menu = Menu(my_menu, tearoff=False)
	my_menu.add_cascade(label="Options", menu=options_menu)
	options_menu.add_command(label="Reset Game", command=reset_Computer_First)
	options_menu.add_command(label="Exit", command=exit)

	reset_Computer_First()

def gui(x, y, text, bcolor, fcolor, cmd):
	global mybutton

	def on_enter(e):
		mybutton["background"]=bcolor
		mybutton["foreground"]=fcolor

	def on_leave(e):
		mybutton["background"]=bcolor
		mybutton["foreground"]=fcolor

	mybutton = Button(root, width=28,height=2, text=text, fg=bcolor, bg=fcolor,
                      border=0, activeforeground=fcolor, activebackground=bcolor,
                      font=(20), command=cmd)
	mybutton.bind("<Enter>", on_enter)
	mybutton.bind("<Leave>", on_leave)
	mybutton.place(x=x,y=y)

def title(x, y, text, bcolor, fcolor, font):
	
	def on_enter(e):
		myLabel["background"]=bcolor
		myLabel["foreground"]=fcolor

	def on_leave(e):
		myLabel["background"]=bcolor
		myLabel["foreground"]=fcolor

	myLabel = Label(root, width=30,height=2, text=text, fg=bcolor, bg=fcolor,
                      border=0, activeforeground=fcolor, activebackground=bcolor,
                      font=font)
	myLabel.bind("<Enter>", on_enter)
	myLabel.bind("<Leave>", on_leave)
	myLabel.place(x=x,y=y)

title(0,20, "TIC TAC TOE GAME", '#141414','darkolivegreen2', ("Helvetica",15))
gui(0,100,"Player first",'#ffcc66','#141414', game_Player_First)
gui(0,160,"Computer first",'#25dae9','#141414', game_Computer_First)
title(0,240, "By Nguyen Hoang Thao Linh", '#141414','darkolivegreen2', ("Helvetica",14))

root.mainloop()