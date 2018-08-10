import string
ALPHABET = set(string.ascii_letters[:26])

def is_pangram(sentence):
    '''Given a sentence, determine if it is a pangram'''
    return set(str_to_alpha(sentence)) == ALPHABET

def str_to_alpha(string):
    '''Given a string, return a string containing only the aphabetic characters (in lowcase)'''
    return (''.join(char for char in string if char.isalpha())).lower()