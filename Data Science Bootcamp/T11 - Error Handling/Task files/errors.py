# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print ("Welcome to the error program") #syntax error: missing parentheses ()
print ("\n") #compilation/syntax error: incorrect indentation + missing parentheses ()

ageStr = "24" #I'm 24 years old.
# compilation error: incorrect indentation 
# runtime error: remove the extra = and ageStr cannot be cast into int so the string needs to be removed "years old"
age = (ageStr)
#runtime error: remove int casting as its no longer needed
print("I'm " + str(age) + " years old.") 
#runtime error: age needs to be cast into string 
three = "3"

answerYears = int(age) + int(three) # compilation error: incorrect indentation 
# logical/compilation error: need to cast age and three into int for calculations

print ("The total number of years: " + str(answerYears)) 
#syntax/compilation error: missing () and need to remove () from the variable answerYears
#runtime error: answerYears needs to be cast into str  
answerMonths = answerYears * 12
#compilation/ general error: wrong variable name answer needs to be answerYears
print ("In 3 years and 6 months, I'll be " + str(answerMonths+6) + " months old") #syntax error: missing ()
#runtime/logical error: answerMonths needs to be cast into string and answerMonths needs to add 6 months to total 330 months

#HINT, 330 months is the correct answer

