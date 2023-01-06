'''
Create dictionary with 6 abbreviations and their meanings
	abbv = {
		'gg':'good game',
		'lol':'laughing out loud',	
		'smh':'shaking my head',
		'API':'Application Programming Interface',
		'dc':'disconnected',
		'SSH':'Secure Shell'
	}
format = keys(abbreviations), values(meanings)

ask user input for abbreviations
	if its in the dictionary 
		print abbreviations and its meanings
	else
		print "Not Found"

'''
abbv = { #dictionary of abbreviations
		'gg':'good game',
		'lol':'laughing out loud',	
		'smh':'shaking my head',
		'API':'Application Programming Interface',
		'dc':'disconnected',
		'SSH':'Secure Shell'
	}

user_input = input("Enter an abbreviation: ") #asking user input
if user_input in abbv: #if input is in dictionary
    print(user_input +":" +abbv.get(user_input)) #uses keys to get abbreviations
    #tried using meanings to see if program still worked - it went to else statement as expected
else:
    print("Abbreviation Not Found.")