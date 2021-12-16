# Import difflid to compare words.
import difflib


# Function checks if given sentence contains misspelled words, and then gives improvement suggestions. 
# Function checks if the given word is in wordlist.txt that contains 109 583 words.
def spellchecker():
    with open('wordlist.txt') as textfile:  # Opens a wordlist file. 
        wordlist = [line.replace('\n','') for line in textfile]  # Creates a new list from a file. 
    
    # Asks user input and and creates a list that contains single words from input sentence. 
    text = input('write text: ')
    line = text.split(' ')

    # Adds correct words to a new list as they appear and incorrect words are added like *this*.
    word = [f'*{w}*' if w.lower() not in wordlist else f'{w}' for w in line]

    # Adds incorrect words to a new list. 
    wrong_words = [w for w in line if w not in wordlist]

    # Prints user input sentence with * * marks on incorrect words. 
    print(' '.join(word))

    # Prints modification suggestions using for loop and compares words using difflib.
    print('Improvement suggestions:')
    for w in wrong_words:
        print(f'{w}: ', end='')
        correct_words = difflib.get_close_matches(w, wordlist)
        print(', '.join(correct_words))

if __name__ == '__main__':
    pass
spellchecker()
