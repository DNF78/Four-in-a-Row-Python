import os        #import os for file handling
import random    # import random module for random number generating
import datetime #import datetime module for gathering time stamps, not used in end

###########################################################################################################

class Cell:					#  Cell is to have attributes row, column and status 

	def __init__(self, row,column, status):

		self.row = row
		self.column = column	
		self.status = status

	def getRow(self):					#accessor for Row

		return self.row 

	def getColum(self):					#accessor for Colum

		return self.column

	def getStatus(self):				# accessor for Status

		return self.status

	def setRow (self, newRow):			# mutator for Row

		self.row = newRow

	def setColumn (self, newColumn):	# mutator for Colum

		self.column = newColumn

	def setStatus (self, newStatus):	# mutator for Status

		self.status = newStatus


##########################################################################

# ***************************FUNCTIONS************************************

##########################################################################

# ***************************Blank Grid **********************************

# Generates a new blank grid of, I hard coded x,y values as variable in case I can change the sizes
# For now I have l left the print function in to show how the grid builds from this list

def BlankGrid():	

	global gameList

	x = 6 
	y = 7					

	initalCell = Cell(0,0,"Blank")
	
	gameList = []

	for i in range(x):
		for j in range(y):
			initalCell.row = i 
			initalCell.column = j
			initalCell.status = "Blank"
			gameList.append(Cell(initalCell.row, initalCell.column, initalCell.status))
	

# ***************************Print Grid **********************************
# this prints a grid using a list of cell objects for user, I have hard coded this part to be 6x7 grid

def PrintGrid(self):
	
	templist = self
	x = len(templist)
	y = len(templist) - 7
	z = 6

	for i in range(z):

		for i in templist[y:x]:				#this is reversing from length of list to build grid for user interface, bottom to top
			if i.getStatus() == "Blank":
				print ("[ ],", end = "\t ")
			elif i.getStatus() == "Player1":
				print ("[X],", end = "\t ")
			elif i.getStatus() == "Opponent":
				print ("[O],", end = "\t ")
			else:
				print("Error in Print Grid Loop") # was used for exception handling
				print("Error", i.getStatus(), i.getRow(), i.getColum())

		x -= 7
		y -= 7
		print("")
	print()
	print ("Row1,\t Row2,\t Row3,\t Row4,\t Row5,\t Row6,\t Row7,")

		
#*******************************************************************************
#the next four functions are checks across Colums, Rowsm, Forward Diagnol & Backward Diagnols

# ***************************Column Check**************************************
# this checks for rows for 4 in a row, it iterates over each of the columns combinations for matches with nested for loops
def CheckColumFor4(self, person):  
	global gametype
	global winner	

	n = 7  # columns are seven in fixed game size, but in case I can amend later TODO

	w = 0
	x = n 
	y = 2*n
	z = 3*n

	for no in range(n):

		for i in range(3):
			if self[w].getStatus() == person and self[x].getStatus() == person and self[y].getStatus() == person and self[z].getStatus() == person:

				print ("4 in a Row found in column, cells :",  (w+1), (x+1), (y+1),(z+1),"\n")
				PrintGrid(self)
				winner = person
				break 

			w +=7
			x +=7
			y +=7
			z +=7

		w -= 20
		x -= 20
		y -= 20
		z -= 20

		

# ***************************Row Check**************************************
# this checks for for 4 in a row, it iterates over each of the row combinations for matches with nested for loops
def CheckRowFor4(self, person):  
	global gametype
	#checkrowlist = self
	# toCheck = person
	global winner	

	n = 6 # TODO , game size is fixed with grid 6*7, TODO if we can make any grid size
	
	w = 0
	x = 1 
	y = 2
	z = 3

	for no in range(n):

		for i in range(4):
			
			if self[w].getStatus() == person and self[x].getStatus() == person and self[y].getStatus() == person and self[z].getStatus() == person:

				print ("4 in a Row found at row, cells :", (w+1), (x+1), (y+1),(z+1),"\n")
				PrintGrid(self)
				winner = person				
				break 

			w +=1
			x +=1
			y +=1
			z +=1

		w +=3
		x +=3
		y +=3
		z +=3



# ***************************Downward Diagnol Check**************************************
# this function checks all the downward diagnol combinations, hard coded mostly
def CheckUpwardDiagnolFor4(self, person):   
	global gametype
	global winner

	#TODO really needs to be tidied up, hard coding for 6*7 grid

	n = 6 # TODO , game size is fixed with grid 6*7, TODO if we can make any grid size
	
	#the two if checks below check the downward diagnol in the two rows of with a single 4 in a row combo
	

	w = 3
	x = 11 
	y = 19
	z = 27

	if self[w].getStatus() == person and self[x].getStatus() == person and self[y].getStatus() == person and self[z].getStatus() == person:

				print ("Upward diagnol 4-in-a-row was found, cells :", (w+1), (x+1), (y+1),(z+1),"\n")
				PrintGrid(self)
				winner = person
								 
	w += 11
	x += 11
	y += 11
	z += 11

	if self[w].getStatus() == person and self[x].getStatus() == person and self[y].getStatus() == person and self[z].getStatus() == person:

				winner = person
				PrintGrid(self)
				print ("Upward diagnol 4-in-a-row was found, cells :", (w+1), (x+1), (y+1),(z+1),"\n")
				 
	# this reinitates the starting points and the two nested loops below check the two forward diagnols that have two possible
	# 4 in a row combinsations
	w = 2
	x = 10
	y = 18
	z = 26

	for no in range(2):

		for number in range(2):
			#print(w,x,y,z)
			if self[w].getStatus() == person and self[x].getStatus() == person and self[y].getStatus() == person and self[z].getStatus() == person:

					winner = person
					PrintGrid(self)
					print ("Upward diagnol 4-in-a-row was found, cells :", (w+1), (x+1), (y+1),(z+1),"\n")
					break 

			w += 8
			x += 8
			y += 8
			z += 8

		w = 7
		x = 15
		y = 23
		z = 31

	# this reinitates the starting points and the two nested loops below check the two forward diagnols that have 3 possible
	# 4 in a row combinsations

	w = 0
	x = 8
	y = 16
	z = 24

	for no in range(2):

		for number in range(3):
			#print(w,x,y,z)
			if self[w].getStatus() == person and self[x].getStatus() == person and self[y].getStatus() == person and self[z].getStatus() == person:

					winner = person
					PrintGrid(self)
					print ("Upward diagnol 4-in-a-row was found, cells :", (w+1), (x+1), (y+1),(z+1),"\n")
					break 

			w += 8
			x += 8
			y += 8
			z += 8

		w = 1
		x = 9
		y = 17
		z = 25



# ***************************Downward Diagnol Check**************************************
# this function checks all the downward diagnol combinations
def CheckDownDiagnolFor4(self, person):  

	global gametype
	global winner	

	n = 6 # TODO , game size is fixed with grid 6*7, if updated to variable size this would need adjusted, hard codedd

	#the two if checks below check the downward diagnol in the two rows of with a single 4 in a row combo

	w = 3
	x = 9 
	y = 15
	z = 21

	if self[w].getStatus() == person and self[x].getStatus() == person and self[y].getStatus() == person and self[z].getStatus() == person:

				print ("Downward diagnol 4-in-a-row was found, cells :",(w+1), (x+1), (y+1),(z+1),"\n")
				PrintGrid(self)
				winner = person
				return
				 
	w += 17
	x += 17
	y += 17
	z += 17

	if self[w].getStatus() == person and self[x].getStatus() == person and self[y].getStatus() == person and self[z].getStatus() == person:

				print ("Downward diagnol 4-in-a-row was found, cells :",(w+1), (x+1), (y+1),(z+1),"\n")
				PrintGrid(self)
				winner = person
				return 
				 
	# reiniate starting point for checks, the two nested for loops below check the two rows where there are 2 possible 
	#4 in a row combos in each section

	w = 4
	x = 10
	y = 16
	z = 22

	for no in range(2):  # this picks up and interates the two rows 

		for number in range(2):
			if self[w].getStatus() == person and self[x].getStatus() == person and self[y].getStatus() == person and self[z].getStatus() == person:

					print ("Downward diagnol 4-in-a-row was found, cells :",(w+1), (x+1), (y+1),(z+1),"\n")
					PrintGrid(self)
					winner = person
					break 

			w += 6
			x += 6
			y += 6
			z += 6

		w = 13
		x = 19
		y = 25
		z = 31

	#reinitates the starting points, the two nested for loops below check the two rows where there are three posssible
	#4 in row combos in each section
	w = 5
	x = 11
	y = 17
	z = 23

	for no in range(2):

		for number in range(3):
			if self[w].getStatus() == person and self[x].getStatus() == person and self[y].getStatus() == person and self[z].getStatus() == person:

					print ("Downward diagnol 4-in-a-row was found, cells :",(w+1), (x+1), (y+1),(z+1),"\n")
					PrintGrid(self)
					winner = person
					break 

			w += 6
			x += 6
			y += 6
			z += 6

		w = 6
		x = 12
		y = 18
		z = 24

#****************************************************
# ***************************All 4 combination checks **************************************
#this consolidates the four checking functions and checks against list as self and person as called
def CheckAllFor4(self, person):  
	global winner
	global gameList

	CheckColumFor4(self, person)
	CheckRowFor4(self, person)
	CheckUpwardDiagnolFor4(self, person)
	CheckDownDiagnolFor4(self, person)


# ***************************Make a Move**************************************
# ****************************** this function takes list, choice(colum) and player and tries to place it in once of the colums
def MakeAMove(self, choice, player):

	if choice >= 8:										#asssumes choice is valid, for a now an addtional check in case varying sie of game grid is coded
		print("not a valid choice in MakeAMove")
		return

		#this is hard coded for grid of 42 TODO if varying size can be updated
		
	for i in range(choice-1,42,7):  #indexing issue of 0 in list and item choice subtract 1
		
		if self[i].getStatus() == "Blank":
			self[i].setStatus(player)
			return

		else:
			pass 


# ***************************Oppponent Move**************************************
	#TODO below is a quick attempt at opponent move with intelligence, this only 
	#checks columns and rows for possible move, if there are any suggestions it 
	# adds to a list which is randomly selected at end, a check is also made to 
	# see if the move is valid if there are no suggestions a random no is picked.  
	#I have included a print line to show if any are being considered but this can be 
	#removed from user interface as appropriate.

def OpponentMove(self):

	
	#global n 

	global gameList
	global winner 
	global gametype

	OpponentMoveTempList =[]  #temp list for possible moves


	suggestedMove = 1 #initiates the suggestedMove variable

	x=0  # variables x,y,z will be used to check for three in a rows
	y=1
	z=2
	
	#  below I attempt to find three in a row option in each of the six rows, any found are appended to the temp list

	for n in range(1,7):   # this iteration is for no of rows

		for i in range (1,5): # this iteration is across a row

			if self[x].getStatus() == "Player1" and self[y].getStatus() == "Player1" and self[z].getStatus()== "Player1":
		
					suggestedMove = (i+3)
					if self[z+1].getStatus() == "Blank": #checks the move is not taken
						OpponentMoveTempList.append(suggestedMove)
						print("Attempt to block player winning row", "suggestedMove :", suggestedMove)
						print(x,y,z)


			if self[x].getStatus() == "Opponent" and self[y].getStatus() == "Opponent" and self[z].getStatus() == "Opponent":
			
					suggestedMove = (i+3)
					if self[z+1].getStatus() == "Blank": #checks the move is not taken
						OpponentMoveTempList.append(suggestedMove)
						print("Attempt to win for pc in row", "suggestedMove :", suggestedMove)
						print(x,y,z)
				
			x+=1
			y+=1
			z+=1
			
		x +=3
		y +=3
		z +=3
	
	#reset the x,y and z variables	
				
	x=0
	y=7
	z=14					

	# below I attempt to find three in a column in each of the 7 columns, any found are appended to temp list		

	for n in range (1,8): #iteration of rows

		for i in range (1,4): #iteration of columns

			if self[x].getStatus() == "Player1" and self[y].getStatus() == "Player1" and self[z].getStatus() == "Player1":

					#			this I hope to catch block columns

					suggestedMove = n
					if self[z+7].getStatus() == "Blank": #checks the move is not taken
						OpponentMoveTempList.append(suggestedMove)
						print("Attempt to block PLAYER colum", "suggestedMove :", suggestedMove)
						
			
			if self[x].getStatus() == "Opponent" and self[y].getStatus () == "Opponent" and self[z].getStatus() == "Opponent":
					suggestedMove = n
					if self[z+7].getStatus() == "Blank": #checks the move is not taken
						print("Attempt for PC to win in Colum", "suggestedMove :", suggestedMove)
						OpponentMoveTempList.append(suggestedMove)
			
			x += 7
			y += 7
			z += 7

		x = n
		y = x+7
		z = y+7
			
	#the three if checks below are to determine to use a random guess if there are none suggested from above
	# or a suggested move from above, if there are multiples a random choice from them is generated
	if len(OpponentMoveTempList) == 0:
			suggestedMove = random.randint(1,7)
			print("************ No sugggested move for Opponent ************")

	elif len(OpponentMoveTempList) == 1:
			suggestedMove = OpponentMoveTempList[0]
			print("************ Single suggested move for Opponent ************")


	else:
			suggestedMove = OpponentMoveTempList[random.randint(0, len(OpponentMoveTempList)-1)]
			print("************ 2+ suggested moves for Opponent************")

	x = suggestedMove
	
	# this checks if the suggested move is playable, hard coded for full columns, regenerates a random no

	while self[34+x].getStatus() != "Blank":
		x = random.randint(1,7)
		print(x, "Random move was regeneated")

	
	print("*********** Opponent has Chosen Colum :", x," ***********\n")
	MakeAMove(self,x,"Opponent")							# calls the make a move function for choice
	CheckAllFor4(self, "Opponent")						# checks the grid for 4-in-a-Row

#************************************************************************************************************

# ***************************Main Menu Function**************************************
# this is the main menu fuction, with options for PvE, PVP, and continuing saved games


def menu():

	global gameList
	#global n #no of turns
	global winner
	global gametype

	# initates the winner and gameList variable

	winner ="no one"
	gameList=[]

	#main menu display
	
	print ("\n******************Main Menu******************\n")
	print("1 - Play Game V's Computer")
	print("2 - Computer V's Player")
	print("3 - PvP")
	print("4 - Load Saved Game Single Player Game")
	print("5 - Load Saved Game PVP")
	print("6 - How to play 4-in-a-row")
	print("7 - Quit\n")
	menuOption = input ("Please select an option!\n")

	if menuOption == "1":		# starts a new Plaver v PC match
		gameList=[]
		BlankGrid()
		gametype = "Single"
		while winner == "no one":
			SinglePlayerGame(gameList)	
			if winner != "no one":
				break
			OpponentMove(gameList)	

		print ("\nCongratualtions to winner in PVE match: ", winner)
		menu()								
		

	elif menuOption == "2":				#starts a new PC v Player match

		gameList=[]
		BlankGrid()
		gametype = "Single"
		while winner == "no one":
			OpponentMove(gameList)	
			if winner != "no one":
				break
			SinglePlayerGame(gameList)	
				

		print ("\nCongratualtions to winner in the PVE match ", winner)
		menu()


	elif menuOption == "3":				#starts a new PVP match
		gameList=[]
		BlankGrid()
		gametype = "PvP"
		while winner == "no one":
			SinglePlayerGame(gameList)	
			if winner != "no one":
				break
			TwoPlayerGame(gameList)	
				

		print ("\nCongratualtions to winner in the PVP match : ", winner)
		menu()
		

	elif menuOption == "4":				#loads up the saved single player match, as player can pause, player has to start
		gametype = "Single"
		LoadSavedGame()
		while winner == "no one":
			
			SinglePlayerGame(gameList)
			if winner != "no one":
				break
			OpponentMove(gameList)	

		print ("\nCongratualtions to winner in the saved PvE match: ", winner)
		menu()


	elif menuOption == "5":			#loads the pvp match, checks which player is to resume
		gametype = "PvP"
		LoadSavedGame()
		count = 0

		for item in gameList:
			if item.getStatus() == "Blank":
				count +=1

		if (count%2) == 1:

			print ("Second player is to resume")

			while winner == "no one":
				TwoPlayerGame(gameList)	
				SinglePlayerGame(gameList)

			print ("\nCongratualtions to winner of the saved PVP match: ", winner)
			menu()

		elif (count%2) == 0:

			print ("First player is to resume")

			while winner == "no one":
				SinglePlayerGame(gameList)	
				TwoPlayerGame(gameList)						

			print ("\nCongratualtions to winner in saved PvP Match : ", winner)
			menu()

	elif menuOption == "6":			#basic help file with instructions
		print("The connect 4 game rules are pretty straightforward.")
		print("The game name says it, what you have to do is connect four to win the game.") 
		print("After choosing to play versus the computer or versus a second player you have to make a row of four checkers of your own.") 
		print("The rows can be done vertically, horizontally or diagonally.")
		print("The game is over if one player connects 4 and wins or the grid is full and game is drawn")
		print("The standard grid is 7x6 with 7 colums to choose from")
		print("Pick a free row to drop your counter to the bottom, try to connect 4 in the grid")

		menu()
				
	elif menuOption == "7":		
		print("Goodbye")			
		
	else:
		print("Invalid selction")			
		menu()


#************************************************
# ***************************Player v Computer Main, player Move**************************************
#this function prompts the user for a choice, checks its vadility and makes a move, can be paused


def SinglePlayerGame(self):

	#global n 

	#TODO LOAD EXISTING GAME

	global gameList
	global winner 
	global gametype

	#winner = "no one"

	if any(item for item in self if item.getStatus() == "Blank"):	 #check for full grid

		PrintGrid(self)
		print("\nPlayer 1 to pick")

		choice = input("\nPlease select a column: 1 for Row1, 2 for Row2...., P or p will pause the game\n")

		if choice == "1":
					
			if (self[35].getStatus()) != "Blank":
				print ("*********************************************COLUMN 1 FULL TRY AGIAN **********************************************************************************\n")
				SinglePlayerGame(self)		

			else:
				MakeAMove(self,1,"Player1")	
				CheckAllFor4(self, "Player1")  
			
		elif choice == "2":
			if (self[36].getStatus()) != "Blank":
				print ("*********************************************COLUMN 2 FULL TRY AGIAN **********************************************************************************\n")
				SinglePlayerGame(self)		

			else:
				MakeAMove(self,2,"Player1")	
				CheckAllFor4(self, "Player1")  
						
		elif choice == "3":
			if (self[37].getStatus()) != "Blank":
				print ("*********************************************COLUMN 3 FULL TRY AGIAN **********************************************************************************\n")
				SinglePlayerGame(self)		

			else:
				MakeAMove(self,3,"Player1")	
				CheckAllFor4(self, "Player1")  
						
		elif choice == "4":
			if (self[38].getStatus()) != "Blank":
				print ("*********************************************COLUMN 4 FULL TRY AGIAN **********************************************************************************\n")
				SinglePlayerGame(self)		

			else:
				MakeAMove(self,4,"Player1")
				CheckAllFor4(self, "Player1") 

		elif choice == "5":		 
			if (self[39].getStatus()) != "Blank":
				print ("*********************************************COLUMN 5 FULL TRY AGIAN **********************************************************************************\n")
				SinglePlayerGame(self)		

			else:
				MakeAMove(self,5,"Player1")	
				CheckAllFor4(self, "Player1")  

		elif choice == "6":					
			if (self[40].getStatus()) != "Blank":
				print ("********************************************* COLUMN 6 FULL TRY AGIAN **********************************************************************************\n")
				SinglePlayerGame(self)		

			else:
				MakeAMove(self,6,"Player1")
				CheckAllFor4(self, "Player1")  	

		elif choice == "7":					
			if (self[41].getStatus()) != "Blank":
				print ("*********************************************COLUMN 7 FULL TRY AGIAN **********************************************************************************\n")
				SinglePlayerGame(self)		

			else:
				MakeAMove(self,7,"Player1")	
				CheckAllFor4(self, "Player1")  

		elif choice =="p" or choice == "P":
				PauseGame(self)
				menu()

		else:
			print("Invalid selction")			
			SinglePlayerGame(self)

	else:
			print("Grid Filled, No More Moves, This is a drawn game")
			menu()
			return

#***********************************************************************************************************

# ***************************Pause Game Function **************************************
#this function will pause a game and write cell details to a list, it checks if it is PVE or PVP, saves the details to a file
#the file ending is an isssue I had when loading the file so the exta "end" is to assist this
def PauseGame(self):

	global gametype

	#check which file, PvE or PVP

	if gametype == "Single":
		filename = "4inaRowfile.txt"

	elif gametype == "PvP":
		filename = "PVP4inaRow.txt"

	#context file manager depending on file, will create a cell and append to list

	try:
		with open(filename, "w") as file:
			for item in self:
				x= item.getColum() 
				y= item.getRow() 
				z = item.getStatus()
				celldetails = str(x)+" "+str(y)+" "+z+" "+"end"
				file.write(celldetails + "\n")
				
	except:
		print("There does not appear to be a valid save file") # exception catching

	print("\nGame Saved : returning to menu\n")

# ***************************Load  Game Function **************************************
#the load saved game function below checks which file is being loaded, PVE or PVP, it strips the end of the file 
# and loads the first three values into a cell and iterates to form the game list.  

def LoadSavedGame():
	global gametype
	global winner
	global gameList

	BlankGrid()						#initiates a blank grid, to be used if no saved game exits
	myloadtemplist = gameList
	winner ="no one"

	#check which file, PvE or PVP

	if gametype == "Single":
		filename = "4inaRowfile.txt"

	elif gametype == "PvP":
		filename = "PVP4inaRow.txt"

	#context file manager depending on file, will create a cell and append to list

	try:
		with open(filename, "r") as file:
				for line in file:
					Row,Colum,Status,End = line.split(" ", 3)
					Loadupcell = Cell(int(Row),int(Colum),Status)
					myloadtemplist.append(Loadupcell)

	except:
			print("There appears to be no saved game") # exception catching

	gameList = myloadtemplist.copy()
	
# ***************************Load  Game Function **************************************	
# this is similar to the single player function but adapted so opponent is second player
# user is presented with grid, and prompted for choice, can also pause

def TwoPlayerGame(self):

	global gameList
	global winner
	global gametype 

	winner = "no one"

	if any(item for item in gameList if item.getStatus() == "Blank"):	 #check for valid saved file status

		PrintGrid(gameList)

		print ("\nPlayer 2 to pick")

		choice = input("\nPlease select a column: 1 for Row1, 2 for Row2....(P or p will pause the game)\n") # prompt for column no

		if choice == "1":
					
			if (self[35].getStatus()) != "Blank":
				print ("*********************************************COLUMN 1 FULL TRY AGIAN **********************************************************************************\n")
				TwoPlayerGame(self)		

			else:
				MakeAMove(self,1,"Opponent")	
				CheckAllFor4(self, "Opponent")  
							
		elif choice == "2":
			if (self[36].getStatus()) != "Blank":
				print ("*********************************************COLUMN 2 FULL TRY AGIAN **********************************************************************************\n")
				TwoPlayerGame(self)		

			else:
				MakeAMove(self,2,"Opponent")	
				CheckAllFor4(self, "Opponent")  
						
		elif choice == "3":
			if (self[37].getStatus()) != "Blank":
				print ("*********************************************COLUMN 3 FULL TRY AGIAN **********************************************************************************\n")
				TwoPlayerGame(self)		

			else:
				MakeAMove(self,3,"Opponent")
				CheckAllFor4(self, "Opponent")  	

		elif choice == "4":
			if (self[38].getStatus()) != "Blank":
				print ("*********************************************COLUMN 4 FULL TRY AGIAN **********************************************************************************\n")
				TwoPlayerGame(self)		

			else:
				MakeAMove(self,4,"Opponent")
				CheckAllFor4(self, "Opponent")		

		elif choice == "5":		 
			if (self[39].getStatus()) != "Blank":
				print ("*********************************************COLUMN 5 FULL TRY AGIAN **********************************************************************************\n")
				TwoPlayerGame(self)		

			else:
				MakeAMove(self,5,"Opponent")
				CheckAllFor4(self, "Opponent")  	

		elif choice == "6":					
			if (self[40].getStatus()) != "Blank":
				print ("*********************************************COLUMN 6 FULL TRY AGIAN **********************************************************************************\n")
				TwoPlayerGame(self)		

			else:
				MakeAMove(self,6,"Opponent")
				CheckAllFor4(self, "Opponent") 	

		elif choice == "7":					
			if (self[41].getStatus()) != "Blank":
				print ("*********************************************COLUMN 7 FULL TRY AGIAN **********************************************************************************\n")
				TwoPlayerGame(self)		

			else:
				MakeAMove(self,7,"Opponent")
				CheckAllFor4(self, "Opponent")  

		elif choice =="p" or choice == "P": #option to pause game
				PauseGame(self)
				menu()

		else:
			print("Invalid selction")			
			TwoPlayerGame(self)

	else:
			print("Grid Filled, No More Moves, This is a drawn game")
			menu()
			return

# ***************************Functions over **************************************

#call the main menu fuction to start

menu()

