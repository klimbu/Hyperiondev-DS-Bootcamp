'''
Create list:
	Menu = [Tea, Cakes, Food, Drinks]
Create Dictionary for stock value of each menu item:
	stock = {
     '24',
     '34',
     '63',
     '54'
     }
Create Dictionary for price of each menu item:
	price = {
     '3',
     '5',
     '4',
     '2,
     }
Calculate total stock worth of the cafe.
for i in range(len(Stock))
	totalstock = stock[i] * price[i]
	total = total + totalstock
 
Print result of calculation "Total Stock Worth of the Cafe is £{total}"

'''

menu = ['Tea', 'Cakes', 'Food', 'Drinks']
     
stock = { #stock for each menu item
     menu[0]:24, #*2 = 48
     menu[1]:34, #*3 = 102
     menu[2]:63, #*4 = 378
     menu[3]:54  #*5 = 270 = 798
     }
price = { #price for each menu item
	menu[0]:2, # Had problems with price calculation when dictionary was based on pseudocode
	menu[1]:3, # Realised I had to remove the quotation marks or asterisks as it would mistake it for string
	menu[2]:6,
	menu[3]:5
	}

total = 0 #counter for total worth

for i in stock: 
	totalstock = stock[i] * price[i] #calculated stock items * price
	total = total + totalstock #adds everything up to calculate total

print(f"Total Stock Worth of the Cafe is £{total}")

