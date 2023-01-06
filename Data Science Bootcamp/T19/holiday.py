''' 
hotel_cost 
	- ask input number of nights
	- multiply by cost per night
	- return total cost of hotel stay

plane_cost
	- ask input for flight destination
	- using if statements for each destination
	- return plane cost

cat_rental
	- ask number of days car will be hired
	- multiply by cost per day
	- return total cost of rental

holiday_cost
	- call the three functions above to calculate holiday cost

display results 
'''
def hotel_cost(nights): #costs 90 per night
    cost_per_night = nights*90
    return cost_per_night

def plane_cost(city): #5 choices of cities with varying prices
    plane_cost = 0
    if city=='london':
        plane_cost = 120
    elif city=='berlin':
        plane_cost = 140
    elif city=='edinburgh':
        plane_cost = 110
    elif city=='dublin':
        plane_cost = 130
    elif city=='paris':
        plane_cost = 110
    return plane_cost

def car_rental(days): #costs 30 per day
    car_cost = days*30
    return car_cost

def holiday_cost(): #calculates total costs
    holiday_cost = hotel_cost(nights) + plane_cost(city) + car_rental(days)
    return holiday_cost

#variables used for calculations 
nights = int(input("How many nights will you be staying at the hotel?\n"))
city = input("Enter the destination city (London, Berlin, Edinburgh, Dublin, Paris):\n").lower()
days = int(input("How many days will you be renting the car for?\n"))

#output - tested for various cities and just did a little optimization for plane_cost using lower() 
print(f'''
The cost of the hotel is £{hotel_cost(nights)}.
The cost of the flight is £{plane_cost(city)}.
The cost of the car rental is £{car_rental(days)}'. 
The total cost of the holiday is £{holiday_cost()}      
''')
