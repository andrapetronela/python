'''Write a program that will display a table of contents so that it looks like this: '''

content = ["Chapter 1: Getting Started", "page 1", "Chapter 2: Numbers", "page 9", "Chapter 3: Letters", "page 13"]

width = 40
print("Table of Contents".center(width))
print("-" * 40)

col_width = 30

i = 0
while (i<len(content)):
	print(content[i].ljust(col_width), content[i+1].ljust(col_width))
	i+=2
