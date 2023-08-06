#A madlib story generator made by following TechWithTim tutorial: https://youtu.be/21FnnGKSRZo 

#Read in the text file (must be located in same directory)
with open("Madlib_story.txt", "r") as f:
    story = f.read()

#Create a set to store the words found later so there are no duplicates like there would be in a list
words = set()
start_of_word = -1  #Starts at -1 to mean no word is being tracked

#Store the characters for the start and end characters of target words
target_start = "<"  
target_end = ">"

#Loop through every character in the story, using the enumerate function to get the index and the character of each position
for i, char in enumerate(story):
    #Check if the current character is a < and if it is, mark it by updating the start of word variable to the current index
    if char == target_start:
        start_of_word = i
    
    #Check if the current char is > and if we have also already found the start of a word
    if char == target_end and start_of_word != -1:
        #Extracts the word from the story by slicing it using the index stored in start_of_word and the i+1 for the end of it
        word = story[start_of_word: i + 1] 
        #Add the word to the words set
        words.add(word)
        #Reset the start_of_word variable to -1 to show we aren't currently tracking a word
        start_of_word = -1

#Create a dictionary for the answers
answers = {}

#Loop through every word stored in the words set, and ask for a corresponding input. 
for word in words:
    answer = input(f"Enter a word for {word}: ")
    #Store the answer in the dictionary with the word as the key and answer as the value
    answers[word] = answer

#Replace each word from the set in the story and update the story variable with the new story
for word in words:
    story = story.replace(word, answers[word])

print("\nHERE IS YOUR STORY:\n")
print(story)