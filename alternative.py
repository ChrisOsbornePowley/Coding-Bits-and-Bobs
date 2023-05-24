string = "this will alternate capital letters"
#Create the variables ready to write the converted string to:
alternate_letters = ""
alternate_words = ""

####################################################
#ALTERNATE LETTERS:
#Grab the length of the string and loop through that many times
for i in range(len(string)):
    
    #If the current index is an even number, convert it to upper and add to new string
    if i % 2 == 0:
        alternate_letters += string[i].upper()
    #If it's an odd number, convert it to lower and add to new string
    else:
        alternate_letters += string[i].lower()

print(f"Alternate letters: {alternate_letters}")

####################################################
#ALTERNATE WORDS:
#Creates a list by splitting the string into each word
string_list = string.split()

#Grabs the number of items in the list and loops through that many times
for i in range(len(string_list)):

    #If the current word index is an even number, convert it to all upper case and add it to the new string with a space afterwards
    if i % 2 == 0:
        alternate_words += string_list[i].upper() + " "
    #Else, convert it to lower and add it to the new string with a space afterwards
    else:
        alternate_words += string_list[i].lower() + " "

print(f"Alternate words: {alternate_words}")