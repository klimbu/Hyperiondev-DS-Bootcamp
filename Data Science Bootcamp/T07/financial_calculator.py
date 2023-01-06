'''
P = present value
i = monthly interest rate (if i = 8 : i =(8/100)/12 annual rate)
Pseudo code
	Display Menu showing investment calculation options for user
	Request user input for which calculation should be used
		Display error, should incorrect input be detected
	if user selects investment: 	
		request integers for investment calculation
		request input for simple or compound interest rate calculation
	else:
		selected calculation is bond
		request integers for bond repayment calculation
	Calculate final value for either investment 
 		{A = P(1 * r x t) simple interest}
		{A = P(1 * r)^t compound interest}
    Bond repayment
	     {R = (i x P)/(1 - (1 + i) ^ (-n))}
    Display final result
    End

'''
# importing math module for use
import math

calc_selection = input(f''' 
investment - to calculate the amount of interest you'l earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan

Please select either bond or investment calculation to proceed                       
''').lower() # lower function handles all types of input

if calc_selection == 'investment':
    
    personal_deposit = int(input("Please enter the amount you'd like to invest : $"))
    
    interest_rate = int(input("Enter the interest rate (do not include the % symbol): "))
    interest_rate = interest_rate/100
    
    time_invested = int(input("Please enter the years you'd like to invest : "))
    
    invest = input("Please select simple or compound interest : ").lower()
   
    # had some object not callable errors: discovered I had to put * before ()
    if invest == 'simple':
        # {A = P(1 * r x t) simple interest}
        simple = personal_deposit*(1*interest_rate*time_invested)
        print(f"The simple interest you'll earn on your investment is ${round(simple, 2)}")
    elif invest == 'compound':
		# {A = P(1 * r)^t compound interest}
        compound = personal_deposit*math.pow((1+interest_rate), time_invested)
        print(f"The compound interest you'll earn on your investment is ${round(compound, 2)}")
    else:
        print("Please enter valid input. Try again.")
        
# 		Comments
#       results of simple interest with values $10000, 8%, 20 years
#       = $16000.0
#       results of simple interest with values $10000, 8%, 20 years
#       = $46609.57
#       almost $30,000 in difference
#       Note:
#       Compound interest calculator in internet generates different values so the formula may need a rework 

elif calc_selection == 'bond':

# bond calculation {R = (i x P)/(1 - (1 + i) ^ (-n))}

    present_value = int(input("Please enter present value of the house : "))
    interest_rate = int(input("Please enter the interest rate : "))
    interest_rate = interest_rate/12

# I am assuming we have to do i/12 as it says that to ask for interest rate but doesn't 
# specify if its monthly or annual and most usually default to giving annual interest rate 

    month_number = int(input("Please enter the number of months to repay the bond : "))
    
    bond = (interest_rate*present_value)/(1-(1+interest_rate)**(-month_number))
    
    monthly_repayment = (present_value+bond)/month_number
    
    print(f'''The interest you'll have to pay on the home loan is ${round(bond, 2)}. 
    The monthly repayment amount is ${round(monthly_repayment, 2)}.''')    
    

#    Testing: 
#    testing using values: 240000, 8%, 120 months
#    answer = $160000
#    monthly_repayment = $3333.33
#    
#    My Comments:
#    this was different from what I got from using online websites to check if it was right or not
#    the interest amount = 109,000 roughly and roughly 2,900 for monthly repayments
#    
#    Through testing I found out that doing interest_rate/18 leads to the answer closest to the real one    
#    Maybe I need to use a different formula 

else:
    print("Invalid input .... terminating.")
            
# was getting invalid space and indentation error and I looked up how to fix it in youtube 
# couldn't believe the solution was to delete the indent and replace it with blank space 
