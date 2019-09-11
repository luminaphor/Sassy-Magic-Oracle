import random

#reads the list of responses from 'possibleresponses.txt'
#returns them in a list called responses
def getResponses():
	filename="possibleresponses.txt"
	openfile=open(filename,'r')

	lines=openfile.readlines()
	responses=[]

	for line in lines:
		if '\n' in line:
			line=line.replace('\n','')
		responses.append(line)
	
	return responses

#reads all responses from the file and copies them to prevent overwrites
#opens 'possibleresponses.txt' for writing, and enters all previously copied responses so the aren't overwritten
#begins a listener loop that prompts the user to enter a new response, writes the response, and stops when the keyword '/end' is used.	
def inputResponses():
	print("Type /stop to stop entering responses.")
	savedResponses=getResponses()


	
	filename="possibleresponses.txt"
	openfile=open(filename,'w')
	
	for response in savedResponses:
		openfile.write(response+'\n')
		

	
	run=True
	
	while run:		
			
		entry=input("Enter a New Response: ")
		
		if entry=='/stop':
			run==False
			return False
		else:
			openfile.write(entry+'\n')
	
		
#draws from the pool of responses obtained through getResponses()
#picks a random response from that list
def getAnswer():
	responses= getResponses()
		
	result=random.randint(0,len(responses)-1)
	result= responses[result]
	return result

#lists all keywords that can be entered by the user
def getOptions():
	options= {
		'/help':'                          Show a list of options.',
		'/new':'                           Input a new response.',
		'/list':'                          Lists all possible responses.',
		'/quit':'                          Exit the program.',
		'/stop':'                          Ends the sequence for entering new responses.'
		}

	for option in options:
		print(option,options[option])
	
def checkEntry(entry):
	if entry=='/help':
		getOptions()
		return True
		
	elif entry=='/new':
		 inputResponses()
		 return True
		 
	elif entry=='/list':
		print(getResponses())
		return True
		
	elif entry=='/quit':
		return False
		
	else:
		print(getAnswer())
		return True
		
	
#main loop of the program. Prompts user to ask a question and generates a random response.
#ends when the keyword /quit is used, and gives a list of options when /help is entered.	
def mainLoop():
	run=True
	
	while run:
		print("")
		entry=input("Please, ask me anything: ")
		print("")
		
		run=checkEntry(entry)
	
		
print("Welcome! Ask me your questions, or enter '/help' for a list of options.")
mainLoop()
