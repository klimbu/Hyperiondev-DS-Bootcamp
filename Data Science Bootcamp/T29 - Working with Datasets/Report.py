''' 
Import pandas
create dataframe for 'balance.txt'
Produce a report on:
	comparison of average income based on ethnicity
	married vs single people - who has higher balance
	who has the highest income
	who has the lower income
	how many cards is recorded in the dataset (using sum())
'''

import pandas as pd

df = pd.read_csv('balance.txt', sep=' ')

# comparison of average income based on ethnicity
eth_comp = df.groupby('Ethnicity')['Income'].mean()
# Output
''' Ethnicity
African American    47.682101
Asian               44.187833
Caucasian           44.521945
Name: Income, dtype: float64 '''

print('''Report:
-----------------------------------------------------------------------------------------------------------------
The average income of African Americans (47.68) is the highest followed by Caucasians (44.52) then Asians(44.18).''')

# married vs single people - who has higher balance
relationship = df.groupby('Married')['Balance'].mean()
#Output
'''Married
No     13.493509
Yes    13.388473'''
print("People who are not married have a higher balance of 13.49 in comparison to married people who have a balance of 13.38.")

# who has the highest income
richest = df.sort_values(['Income'], ascending=[False]).iloc[0:1]
print("The person with the highest income is the one with the ID number 28 with an income of 186.634.")
#Output
'''      Balance   Income  Limit  Rating  Cards  Age  Education  Gender Student Married         Ethnicity
28  35.271011  186.634  13414     949      2   41         14  Female      No     Yes  African American     '''

# who has the lower income
poorest = df.sort_values(['Income'], ascending=[True]).iloc[0:1]
print("The person with the lowest income is the one with the ID number 58 with an income of 9.18.")
#Output
''' Balance  Income  Limit  Rating  Cards  Age  Education Gender Student Married  Ethnicity
58  9.180797  10.354   3480     281      2   70         17   Male      No     Yes  Caucasian'''

# how many cards is recorded in the dataset (using sum())
cards_total = df['Cards'].sum()
# Output = 1183
print(f"The total amount of cards recorded in the dataset is {cards_total}.")