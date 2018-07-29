'''Table of contents. Write a table of contents program here. Start the program with a list 
holding all of the information for your table of contents (chapter names, page numbers, and so on). 
Then print out the information from the list in a beautifully formatted table of contents. 
Use string formatting such as left align, right align, center.'''

babyBook = ("Baby-bit: ", "page 12", "while (food())", "page 62", "play(dad)", 
	"page 98", "mom = 'code_and_cola'", "page 133", "no_sleep == true", "page 250")
print("-" * 40)
print("\n " +  "Baby and code".center(40) + "\n")
print("-" * 40 + "\n")
width = 30
i = 0
while (i < len(babyBook)):
	print(babyBook[i].ljust(width), babyBook[i+1].ljust(width))
	i+=2
