#Challenge from https://exercism.org/tracks/python/exercises/little-sisters-vocab

#Note: For all of these functions, I have chosen to just "print" the result rather than using "return".
#I think this is more straight forward for a little sister use the function this way! 
#And there is no need to save the value to recall it later, like would be useful in a return method.


#Function to add "un" to start of word
def add_prefix_un(word):
    result = "un" + word    #Adds un to the start of the word  
    print(result)    #Prints completed word.

add_prefix_un("happy")
add_prefix_un("manageable")


#Function to make words by taking in a prefix then a list of words
def make_word_groups(vocab_words):
    prefix = vocab_words[0] #Identifies the prefix as the first word
    words = vocab_words[1:] #Identifies the words to be every word after the first word

    results = prefix    #Makes the finanl string with the prefix at the front

    #Go through each word, adding prefix to it and then adding the result to the results string:
    for word in words:
        result = prefix + word
        results += " :: " + result  
    
    print(results)

make_word_groups(["en", "close", "joy", "lighten"])
make_word_groups(['pre', 'serve', 'dispose', 'position'])
make_word_groups(['pre', 'serve', 'dispose', 'position'])
make_word_groups(['inter', 'twine', 'connected', 'dependent'])


#Function to remove ness from the end of a word
def remove_suffix_ness(word):
    word = word.rstrip("ness")   #Removes "ness" from the end of the word   
    #If the last letter of the word is i, then return the word without the last letter then add y to it:
    if word[-1] == "i":     
        word = word[:-1] + "y"
    print(word)

remove_suffix_ness("heaviness")
remove_suffix_ness("sadness")


#Function to turn a specific word into a verb by adding en:
def adjective_to_verb(sentence,index):
    sentence = sentence.split() #Split the sentence by whitespace into individual words
    word = sentence[index]  #Identify the needed word using the index input
    word = word.strip(".")  #Strip a full stop from the end if it exists
    word = word + "en"  #Add "en" to the word
    print(word)

adjective_to_verb('I need to make that bright.', -1 )
adjective_to_verb('It got dark as the sun set.', 2)