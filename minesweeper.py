#I struggled with this task for a long time, but have finally got a solution that works even if it is not the most efficient!
#I haven't used the enumerate function that was suggested in the task briefing as I struggled to understand it very well.
#Would love to get a suggestion for it if possible please!

#Makes the grid in a 2D list. # represents mines. - represents safe space.
grid = [["-","-","-","#","-"],
        ["-","-","-","-","#"],
        ["-","#","#","#","-"],
        ["-","#","-","#","-"],
        ["-","#","#","#","-"]]

#Function to print the grid correctly
def show_grid():
    for i in grid:
        for j in i:
            print(j, end="\t")
        print()

#Print the original grid before any changes
print("The original grid:")
show_grid()

#Function for checking for mines, then printing the revealed grid
def reveal_mines():
    for i in range(len(grid)):       #Loop through each list
        for j in range(len(grid[i])):   #Loop through each item in the current list
            mines = 0 #Holds the number of mines. Sets it to 0 at the start of each loop.
            
            if grid[i][j] == "#":   #If the value is #, skip it and start the next loop
                continue

            #If the above statement isn't triggered, check for mines in adjacent cells:
            #Each statement starts with an if to check if the adjacent cell would be out of bounds
            #I recognise this isn't very efficient - may come back to improve later on if I find another solution.
            else:
                if j+1 < len(grid[i]):                    
                    if grid[i][j+1] == "#":     #Check EAST
                        mines += 1
                
                if j-1 >= 0:
                    if grid[i][j-1] == "#":     #Check WEST
                        mines += 1
                
                if i-1 >= 0:
                    if grid[i-1][j] == "#":     #Check NORTH
                        mines += 1
                
                if i+1 < len(grid):
                    if grid[i+1][j] == "#":     #Check SOUTH
                        mines += 1
            
                if i-1 >= 0 and j+1 < len(grid[i]):
                    if grid[i-1][j+1] == "#":   #Check NORTH-EAST
                        mines += 1

                if i-1 >= 0 and j-1 >= 0:
                    if grid[i-1][j-1] == "#":   #Check NORTH-WEST
                        mines += 1

                if i+1 < len(grid) and j+1 < len(grid[i]):
                    if grid[i+1][j+1] == "#":   #Check SOUTH-EAST
                        mines += 1
            
                if i+1 < len(grid) and j-1 >= 0:
                    if grid[i+1][j-1] == "#":   #Check SOUTH-WEST
                        mines += 1
                
                grid[i][j] = mines  #Sets the cell value to the current value of mines, before it is reset for the next loop.
                

    show_grid()

#Print the revealed grid using the function to convert the values:
print("The revealed grid:")
reveal_mines()