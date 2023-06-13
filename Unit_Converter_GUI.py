#A simple converter app built following ClearCode's youtube video: https://youtu.be/kQ8DGP9p2LY 
#This uses the PySimpleGUI module

import PySimpleGUI as sg

#Layout: Layout has list of lists. Each list is a row in the GUI, with the elements you want to include on that row
#Arguments are name, then key
#Key = a unique identifier for that element
layout = [
    [sg.Input(key = "-INPUT-"), 
     sg.Spin(["km to mile", "kg to pound", "sec to min"], key = "-UNITS-"), 
     sg.Button("Convert", key = "-CONVERT-")],
    [sg.Text("Output", key = "-OUTPUT-")]]

#sg.Window creates a Window with title, layout arguments
window = sg.Window("Converter",layout)

#Loop to run the GUI
while True:
    event, values = window.read()   #.read() shows the window.

    if event == sg.WIN_CLOSED:  #Breaks the while loop if the event is closing the window
        break  

    if event == "-CONVERT-":                #If the Convert button is pressed:
        input_value = values["-INPUT-"]     #Set input_value variable to whatever is written in the input text box
        if input_value.isnumeric():         #Check if it's a number, and if it is:
            match values["-UNITS-"]:        #Compare it to the current value of the unit selector
                
                case "km to mile":                                  #If the unit selector is on "km to mile":
                    output = round(float(input_value) * 0.6214, 2)  #Convert the input_value to a float, then multiply, then round to 2 dp
                    output_string = f"{input_value} km are {output} miles." #Set the output string ready to update the output element
                
                case "kg to pound":                                 #Same for kg to pound
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f"{input_value} kg are {output} pounds."
                
                case "sec to min":                                  #Same for sec to min
                    output = round(float(input_value) / 60, 2)
                    output_string = f"{input_value} seconds are {output} minutes."
            
            window["-OUTPUT-"].update(output_string)   #Update the window output element to show the output_string
       
        else:   #If anything other than a number is entered, update the output element to say enter only numbers
            window["-OUTPUT-"].update("Please enter only numbers.")
            
             
window.close()

