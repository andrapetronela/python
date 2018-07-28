'''Leap years. Write a program that asks for a starting year and an ending year 
and then puts all the leap years between them (and including them, if they are also leap years). 
Leap years are years divisible by 4 (like 1984 and 2004). 
However, years divisible by 100 are not leap years (such as 1800 and 1900) unless 
they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess! '''


firstYear = int(input())
secondYear = int(input())


for x in range(firstYear, secondYear + 1):
	if x % 400 == 0: 
		print(x)
	elif x % 4 == 0 and x % 100 != 0:
		print(x)
	
