import json

# opening the dictionary.json in read mode
fin = open("/Users/illiabohdan/Documents/kalicz/eng-dict/dictionary.json", "r")
# loading into python object 
cont = json.load(fin)

# function to display words that begin with a specific letter
def dispwords():
    letter = input("Enter the letter to display the words with which it begins with: ")
    for i in cont:
        if i.startswith(letter):
            print(i)

# function to find a word and display whether it is in dict or not
def findword():
    word = input("Enter the word to check in the dictionary: ").lower()
    found = False
    for i in cont:
        if i == word:
            found = True
    if found == False:
        print("No such word exists in the dictionary")
    else:
        print("It is there in the dictionary!")

# function to display the meaning
def dispm():
    word = input("Enter the word to check the meaning of: ").lower()
    found = False
    for key, value in cont.items():
        if key == word:
            found = True
            print("{} has meaning {}".format(key, value))
    if found == False:
        print("No such word exists in the dictionary")

# function to display the meanings for the specific word that is there in the meaning
def dispsm():
    word = input("Enter a word to be searched in the dictionary and to display the meaning of: ")
    found = False
    for key, value in cont.items():
        if key == word or word in value:
                found = True
                print ("Word {} - Meaning {}".format(key, value))
    if found == False:
        print("No such word exists in the dictionary")

# search words by the number of letters
def searchno():
    num = int(input("Enter number of letters of length of the word: "))
    found = False
    for key in cont:
        if len(key) == num:
            print(key)
            found == True
    if found == False:
        print("No words with this specific length")

# menu for interactive dictionary
while True:
    try:
        print("""
        I N T E R A C T I V E  D I C T I O N A R Y 
        ==========================================
        1. Display the words that began with a specific letter
        2. Find a specific word
        3. Display the meaning of the word
        4. Display the word-meanings for the specific word that is there
        5. Search and display words by the number of letters
        6. Exit
        """)
        choice = int(input("Enter your choice of opperation (1-6): "))
        if choice == 1:
            dispwords()
        elif choice == 2:
            findword()
        elif choice == 3:
            dispm()
        elif choice == 4:
            dispsm()
        elif choice == 5:
            searchno()
        elif choice == 6:
            break

    except:
        print("Invalid input")