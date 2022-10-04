#Initialises the dictionary (key: ascii letter, value: morse code equivalent of the latter)
letter_to_morse = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----'}

#Swaps the key and values
morse_to_letter = {value:key for key,value in letter_to_morse.items()}

#Initialises a result array
result = []

#Prompts user for choice
choice = input("Morse to Text or Text to Morse?: ")

#Validates the input (presence check)
while choice.lower() != 'morse to text' and choice.lower() != 'text to morse':
    choice = input("Invalid choice. Morse to Text or Text to Morse?: ")
if choice.lower() == 'text to morse':
    #Asks user for a text
    text = input("Text: ")
    
    #Convert text into uppercase
    text = text.upper()
    
    #Iterates over each letter in the text to convert text into morse code
    for letter in text:
        if letter in letter_to_morse:
            result.append(letter_to_morse[letter] )
        elif letter == ' ':
            result.append('/')
    print(' '.join(result))
else:
    morse_text = input("Morse code: ")
    morse_text = morse_text.split(' ')
    for morse_code in morse_text:
        if morse_code in morse_to_letter:
            result.append(morse_to_letter[morse_code])
        #Check if there are spaces (to indicate ending)
        elif morse_code == '/' or morse_code == '|':
            result.append(' ')
    #Prints the result
    print(''.join(result))
    
