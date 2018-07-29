
'''
- Old-school Roman numerals. In the early days of Roman numerals, the Romans didn’t bother with any 
of this new-fangled subtraction “IX” nonsense. 

No Mylady, it was straight addition, biggest to littlest—so 9 was written “VIIII,” and so on. 

Write a method that when passed an integer between 1 and 3000 (or so) returns a string containing 
the proper old-school Roman numeral. In other words, old_roman_numeral 4 should return 'IIII'. 
Make sure to test your method on a bunch of different numbers. 

Hint: Use the integer division and modulus methods. 
“Modern” Roman numerals. Eventually, someone thought it would be terribly clever 
if putting a smaller number before a larger one meant you had to subtract the smaller one. 
As a result of this development, you must now suffer. 
Rewrite your previous method to return the new-style Roman numerals 
so when someone calls roman_numeral 4, it should return 'IV', 90 should be 'XC' etc.'''


import math

print("Please insert a number between 0 and 3000.")
decimal = (1000, 500, 100, 50, 10, 5, 1)
roman = ("M", "D", "C", "L", "X", "V", "I")


def write_roman_letters(number):
	roman_letter = ""
	if number < 0 or number > 3000:
		print("Please insert a number between 0 and 3000.")
	i = 0
	for d in decimal:
		if number == 9:
			roman_letter = roman_letter + "IX"
			break
		elif number == 4:
			roman_letter = roman_letter + "IV"
			break

		q = math.floor(number / d) 
		rest = number % d 
	

		roman_letter = roman_letter + (q * roman[i])
		number = rest
		i+=1
	
	print(roman_letter)
write_roman_letters(int(input())) 

# 

