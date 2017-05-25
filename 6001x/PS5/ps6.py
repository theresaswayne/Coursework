import string
import copy

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        
        '''
        
        # initialize a new empty dictionary 
        self.shift_dict = {}
        shifted_index = 0
        letter_key = 0
        
        # get the  letters
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        
        # shift the lowercase letters
        for index in range(0,26):
            letter_key = lowercase_letters[index]
            shifted_index = index + shift
            if shifted_index <= 25:
                cipher_value = lowercase_letters[shifted_index]
            else:
                cipher_value = lowercase_letters[shifted_index-26]
            self.shift_dict[letter_key] = cipher_value
            
        # shift the uppercase letters
        for index in range(0,26):
            letter_key = uppercase_letters[index]
            shifted_index = index + shift
            if shifted_index <= 25:
                cipher_value = uppercase_letters[shifted_index]
            else:
                cipher_value = uppercase_letters[shifted_index-26]
            self.shift_dict[letter_key] = cipher_value
            
        return self.shift_dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        # get the message text
        plaintext = self.get_message_text()
        
        # initialize the output string
        ciphertext = ""
        
        # get the encryption dictionary
        shift_dict = self.build_shift_dict(shift)
        
        # loop through the text
        for char in plaintext:
            if char in string.ascii_letters: # it's a letter that should be encrypted
                ciphertext += shift_dict[char]
            elif (char in string.punctuation) or (char in string.digits) or (char == ' '):
                ciphertext += char
            else:
                ciphertext += "*"
        
        return ciphertext
        
        

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)  # construct a Message with text and valid words
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift
        

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()


    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted


    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)  # construct a Message with text and valid words
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        final_decrypt = ""
        trial_decrypt = ""
        trial_words = []
        answer = () # return values
        valid_word_count = {} # count valid words for each shift
        best_shift = 0
        
        #get a list of valid words
        word_list = self.get_valid_words()
                
        # loop through all possible shifts (0-25)
        for shift in range(0,26):
            
            trial_decrypt = self.apply_shift(shift)
            
            # split the trial decryption into a list of words using trial.split(' ')
            trial_words = trial_decrypt.split(" ")
            valid_word_count[shift] = 0 # initialize shift entry in dict

            # loop through words
            for word in trial_words:
                if is_word(word_list, word):
                    valid_word_count[shift] += 1
            
            # if counter = number of words in message then stop
            if valid_word_count[shift] == len(trial_words):
                answer = (shift, trial_decrypt)
                return answer
                        
        best_shift = max(valid_word_count, key=lambda k: valid_word_count[k])
        final_decrypt = self.apply_shift(best_shift)
        answer = (best_shift, final_decrypt)
        return answer
        

def decrypt_story():
    ''' 
    string = encrypted story retrieved by get_story_string()
    creates ciphertext message and decodes optimally
    returns tuple of best shift value and the unencrypted story
    '''
    
    # get the encrypted story string using get_story_string()
    story = get_story_string()
    
    # create a CiphertextMessage
    cipher = CiphertextMessage(story)
    
    # decrypt it optimally
    decode = cipher.decrypt_message()    
    
    # return answer
    return decode
    
#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())

#cipher = "Mnmrdmrd vnqcr: vghsd ansskd ldzrtqd aqnvm ehkl gdzk onkhshbhzm ghkk xdrsdqczx ldqqx okzsd dmsdq sgzmj bzqd rnkhc"
#
#ciphertext = CiphertextMessage(cipher)
#print("Cipher: ", ciphertext.get_message_text())
#print("Decoded: ", ciphertext.decrypt_message())
