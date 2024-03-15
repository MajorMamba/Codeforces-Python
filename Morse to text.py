import os
# Dictionary to map characters to Morse code
TEXT_to_MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    ' ': ' '  # To handle spaces between words
}

MORSE_TO_TEXT_CODE_DICT ={
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9','/': ' ',
    '': ' '  # To handle empty spaces between words
}


def text_to_morse(text):
    morse_code = ' '.join(TEXT_to_MORSE_CODE_DICT[char.upper()] if char.upper() in TEXT_to_MORSE_CODE_DICT else '?' for char in text)
    return morse_code

def morse_to_text(morse_code):
    # Split Morse code into words
    words = morse_code.strip().split('   ')  # Three spaces to represent a space between words
    text = ''
    for word in words:
        # Split each word into characters
        chars = word.split(' ')
        for char in chars:
            # Lookup the character in the reverse dictionary to get the text
            if char in MORSE_TO_TEXT_CODE_DICT:
                text += MORSE_TO_TEXT_CODE_DICT[char]
            else:
                # If the Morse code character is not found, append a question mark
                text += '?'
        # Add a space between words
        text += ' '
    return text.strip()

def main():
    
    while True:
        
        print("Menu:")
        print("Enter T to input text and convert it to Morse code")
        print("Enter M to input Morse code and convert it to text")
        print("Enter Q to quit")

        choice = input("Enter your choice: ").upper()

        if choice == 'T':
            text_input = input("Enter the text: ")
            morse_code = text_to_morse(text_input)
            print(f"Morse code: {morse_code}")
        elif choice == 'M':
            morse_input = input("Enter the Morse code: ")
            text = morse_to_text(morse_input)
            print(f"Text: {text}")
        elif choice == 'Q':
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
