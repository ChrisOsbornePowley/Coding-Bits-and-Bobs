#A simple calculator app built following ClearCode's youtube video: https://youtu.be/kQ8DGP9p2LY 
#Allows the user to change themes by right clicking and to perform different calculations
#This uses the PySimpleGUI module

import PySimpleGUI as sg

#A function to create the app with a specific theme and layout:
def create_window(theme):
    #Set a theme for all objects coming after this line:
    sg.theme(theme)
    sg.set_options(font = "Franklin 14",        #Font = style size
                button_element_size = (6,3)) #Button element size for all - although will set it individually later anyway. 
    button_size = (6,3)   #Set a tuple as a variable to set individual button sizes with it

    #Layout:
    # expand_x = True stretches the x dimension of the element
    # size = button_size sets the size of the element to the button_size variable above
    layout = [
        [sg.Text("Output", key = "-TEXT-", font = "Franklin 26", justification = "center", expand_x = True, pad = (10,20),
                 right_click_menu = theme_menu)],
        [sg.Button("Clear", expand_x = True), sg.Button("Enter", expand_x = True)],
        [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button("*", size = button_size)],
        [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button("/", size = button_size)],
        [sg.Button(3, size = button_size), sg.Button(2, size = button_size), sg.Button(1, size = button_size), sg.Button("-", size = button_size)],
        [sg.Button(0, expand_x = True), sg.Button(".", size = button_size), sg.Button("+", size = button_size)]
        ]


    return sg.Window("Calculator", layout)

#A list of themes to choose from
theme_menu = ["menu", ["LightGrey1", "Dark", "DarkGray8", "Random"]]
window = create_window("dark")

current_num = []    #A list to use to store the numbers inputted
full_operation = []

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break

    #If the event is a theme_menu selection, close the current window and make a new one with the event as the new theme
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ["0","1","2","3","4","5","6","7","8","9","."]:
        current_num.append(event)   #Adds the event to the list
        num_string = "".join(current_num)   #Joins the current_num list items into a single string
        window["-TEXT-"].update(num_string) #Updates the text to show the string

    if event in ["*","/","-","+"]:
        full_operation.append("".join(current_num))     #Join the current_num list into a single string
        current_num = []    #Empty the current_num list ready for the second number
        full_operation.append(event)    #Add the operation to the string as a new item
        window["-TEXT-"].update(event) #Updates the text to show the operation event

    if event == "Enter":
        full_operation.append("".join(current_num)) #Join the new (number 2) current_num list into a single string, and add it to the operation variable (so it now has number 1, operation, number 2)
        result = eval(" ".join(full_operation)) #Joins all elements of the list into a single string separated by spaces, then sses python's eval function to calculate the answer and saves it as result
        window["-TEXT-"].update(result) #Updates the text to show the result variable
        full_operation = [] #Clears the lists
        current_num = []
    
    if event == "Clear":
        current_num = []    #Clears both lists and empties the text box
        full_operation = []
        window["-TEXT-"].update("")

window.close()