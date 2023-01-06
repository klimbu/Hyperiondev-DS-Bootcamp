'''
Create dictionary with key/value pairs:	
	countryMap = {
		'United Kingdom': 'London',
		'Sweden': 'Stockholm',
		'Canada': 'Ottawa',
		'Japan': 'Tokyo',
		'Nepal': 'Kathmandu'
	} 
print countryMap('Sweden')

'''
countryMap = { #Dictionary of country and its capital city
		'United Kingdom': 'London',
		'Sweden': 'Stockholm',
		'Canada': 'Ottawa',
		'Japan': 'Tokyo',
		'Nepal': 'Kathmandu'
	} 
# print (countryMap('Sweden')) returns TypeError: 'dict' object is not callable
# Correct method to do this is to use .get() like shown below

print(countryMap.get('Sweden'))
