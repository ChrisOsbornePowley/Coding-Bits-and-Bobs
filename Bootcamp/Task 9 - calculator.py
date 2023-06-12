#Starts in a while loop so the user can choose to go through the program again at the end.
while True:
    #Explains the choices to the user then asks them to choose the function they wish to use:
    print("Calculator allows you to input 2 numbers and an operator to calculate an answer.")
    print("Print allows you to read all the equations from a text file and print them out here.")
    calculator_or_print = input("Choose either 'calculator' or 'print': ")

    #CALCULATOR CHOICE:
    if calculator_or_print.lower() == "calculator":

        #Ask the user for a number and only accept integer values. Loops back if int value is not entered.
        while True:
            try: 
                first_number = int(input("Enter your first number: "))
                break
            except ValueError:
                print("That is not a valid number. Please try again.")

        #Ask the user for a second number and only accept integer values. Loops back if int value is not entered.
        while True:
            try: 
                second_number = int(input("Enter your second number: "))
                break
            except ValueError:
                print("That is not a valid number. Please try again.")

        #Asks the user for an operation. Only accepts +, -, x or / from the user, else repeats the loop around again.
        while True:
            user_operation = input("Please enter +, -, x or / to perform on the numbers: ")
            if user_operation == "+":       
                answer = first_number + second_number       #Add their numbers together then break out of the loop
                break
            elif user_operation == "-":             
                answer = first_number - second_number       #Subtract second number from first number then break out the loop
                break
            elif user_operation == "x":
                answer = first_number * second_number       #Multiply their numbers together then break out the loop
                break
            elif user_operation == "/":                     #Divide first number by second number
                #NEW CODE added 11/4/23: Thanks for the feedback! I've added a Try Except block to catch a zero division error and tell the user it's not possible.
                try:                            
                    answer = first_number / second_number
                    break                   #Breaks the loop if division is possible possible
                except ZeroDivisionError:   #Stops the user from breaking the program by trying to divide by 0. Asks them for a new operator instead
                    print("Sorry, you can't divide by 0. Try something else.") 
                #End of new code 11/4/23
            else:                                           #If none of the above choices are entered, start the loop again to ask for a new input.
                print("Input not recognised. Please try again.")
        

        #Saves the calculation as a new variable then prints it out to the user.
        calculation = f"{first_number} {user_operation} {second_number} = {answer}"
        print(calculation)

        #Opens the file completedcalculations.txt (or create it if it doesn't exist)
        #Writes the finished calculation by appending it to the bottom of any current content
        f = open("completedcalculations.txt", "a")
        f.write(calculation + "\n")  #Starts a new line after the calculation
        f.close()   #Closes the file after writing to it

    #PRINT CHOICE:
    elif calculator_or_print.lower() == "print":
        f = None        
        while True:
            try:
                #Asks the user for a file name, opens and prints it if possible. Breaks out the loop if successful
                file_choice = input("Please enter the file name you wish to print from: ")
                f = open(file_choice)
                print(f.read())
                break
            except FileNotFoundError:
                #If the file name entered does not exist, ask the user to try again
                print("File not found. Please try again.")

    #NEITHER CALCULATOR OR PRINT ENTERERED, restarts the loop from the beginning
    else: 
        print("Invalid input. Please try again")
        continue
    
    #After completing a function, ask the user if they want to start again and either begin from the start or stop the program.
    #Exits the program for any input other than y, but gives a nice message if they enter n instead of mashing the keyboard!    
    restart = input("Would you like to perform a new task? y/n : ")
    if restart.lower() == "y":
        continue
    elif restart.lower() == "n":
        print("Thank you. Ending program.")
        break
    else:
        print("Invalid entry. Please restart the program if you wish to begin again.")
        break
