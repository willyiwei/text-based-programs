# Python text-based program for the Morse Code Translator

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '!': '-.-.--', '/': '-..-.',
                   '-': '-....-', '(': '-.--.', ')': '-.--.-',
                   '`': '.----.', }


def encode(plain_text: str) -> str:
    """
    Function to encode a string
    according to the morse code chart
    :param plain_text: string to be encoded
    :return: encoded morse code in str
    >>> encode("SOS")
    '... --- ... '
    """
    cipher = ''
    for letter in plain_text:
        if letter != ' ':
            letter = letter.upper()

            # lookup the dictionary and add a morse code to the cipher.
            # NOTE: need to add a space at the end of the code for certain padding,
            # otherwise it is hard to read the code.
            cipher += (MORSE_CODE_DICT[letter]) + ' '
        else:
            # add 1 more space (2 in total)
            # in order to indicate this is a separate for another word.
            cipher += ' '

    return cipher


def decode(morse_code: str) -> str:
    decrypt = ''
    cipher_letter = ''
    for code in morse_code:
        if code == '.' or code == '-':
            cipher_letter += code
        elif code == ' ':
            decrypt += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(cipher_letter)]
            cipher_letter = ''
        else:
            print(f"Error: '{code}' is not a valid morse code!")

    return decrypt


def test_encoding():
    # testcase1 - normal case
    test1 = "I use this sentence to test translation to Morse Code."
    print(encode(test1))

    # testcase2 - special characters only
    test2 = ",.?`!"
    print(encode(test2))

    # testcase3 - long string no space
    test3 = "aaaaaaaabbbbbbbbbbcccccccccdddddddddddeeeeeeeeeefffffffffffgggggggggghhhhhhhhhiiiiiiiiiiiiiiiiii"
    print(encode(test3))

    # testcase4 - interactive
    user_input = input("Enter the texts you would like translate into Morse Code: ")
    code = encode(user_input)
    print(f"The Morse Code for the texts {user_input} is as below:")
    print(f"{code}")


if __name__ == '__main__':
    test_code = 's'
    result_text = decode(test_code)
    print(result_text)
