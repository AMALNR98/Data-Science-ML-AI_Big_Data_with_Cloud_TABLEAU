"""
Calculate electricity bill
Unit
First 100 unit [Free]
101-200 [Unit = 5
Above 200 [unit = 10]

Example:
350 units
100 free
100 * 5 = 500
150*10 = 1500
"""
units = int(input('Enter the consumed units: '))
if units <= 100:
    print('No need to pay')
elif units > 100 >= units:
    after_free = units - 100
    print('The payable amount= ', after_free*5)
else:
    bill = (units - 200) * 10 + 500
    print('Amount payable', bill)

