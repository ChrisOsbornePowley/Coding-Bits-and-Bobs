""" Edabit challenge "Deadly Virus": https://edabit.com/challenge/sARz4TDdxCuqK6pja
Mubashir needs your help to identify the spread of a deadly virus. He can provide you with the following parameters:

A two-dimensional array persons, containing affected persons 'V' and unaffected persons 'P'.
Number of hours n, each infected person is spreading the virus to one person up, down, left and right each hour.
Your function should return the updated array containing affected and unaffected persons after n hours."""

#Function starts by creating rows and cols variables to count the length of the array:
def deadly_virus(persons, n):
	rows = len(persons)
	cols = len(persons[0])

	#Helper function to check if the left, right, top or bottom adjacent cell exists
	def is_valid(row, col):
		return 0 <= row < rows and 0 <= col < cols
		
	#Helper function to check if the cell exists, then spreads the virus by changing P to virus
	#note: I changed it to "virus" not "V" here so that I can continue iterating over the rest of the list without it picking up more "V"s
	def spread(row, col):
		if is_valid(row, col) and persons[row][col] == "P":
			persons[row][col] = "virus"
	
	#Loop the number of times given in the function parameters
	for hour in range(n):
		
		#Loop through each row, and each column in each row. If it is a "V", call the spread function to change all valid adjacent cells
		for i in range(rows):
			for j in range(cols):
				if persons[i][j] == "V":
					spread(i-1, j)
					spread(i+1, j)
					spread(i, j-1)
					spread(i, j+1)
		
		#After looping through each item once, loop through again to change any "virus" entries to "V". 
		#Whilst this isn't very efficient as it means it takes a whole new loop the array through to complete, I found it a straight forward
		# solution to stop the first loop from messing up when it encounters a "V" created by spreading in the same iteration
		for i in range(rows):
			for j in range(cols):
				if persons[i][j] == "virus":
					persons[i][j] = "V"
	
	#Returns the now updated array back to the function
	return(persons)

persons=[
["P","P","P","P","P"],
["V","P","P","P","P"],
["P","P","P","P","P"],
["P","P","P","P","P"],
["P","P","P","P","P"]
]

print(deadly_virus(persons, 4))
