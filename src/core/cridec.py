#!/usr/bin/env python3

from src.core.tobcore import *
import bip32utils
from mnemonic import Mnemonic




def encrypt(text, key):
    result = ""
    if key.isdigit():  ## check if the key is made up of digits only
        key_as_int = int(key)  ## convert key for int number
        key_as_digits = key_as_int % 10000  # 10000
    else: #numbers and letters key
        key_as_digits = ''.join(str(ord(char)).zfill(3) for char in key)  # key characters to numbers and ensuring each number has 3 digits
        key_as_digits = int(key_as_digits[:24])  # first 24 digits of the converted key
        key_as_digits = key_as_digits % 10000  # 10000
    l = len(text)
    i = 0
    for char in text:
        char_code = ord(char)  # get ascii of char
        encrypt_code = (char_code + key_as_digits) % 0x110000  # cript with key in numbers
        encrypted_char = chr(encrypt_code)  # back to char
        result += encrypted_char
        i += 1
        if i == l:
            loading_bar(i, l, prefix='', suffix='Complete', length=50)
        else:
            loading_bar(i, l, prefix='', suffix='', length=50)
    return result



#decrypt function
def decrypt(text, key):
    result = ""
    if key.isdigit():  # check if the key is made up of digits only
        key_as_int = int(key)  # convert key for int number
        key_as_digits = key_as_int % 10000  # Reduzir o valor para um número gerenciável
    else: # numbers and letters key
        key_as_digits = ''.join(str(ord(char)).zfill(3) for char in key)  # key characters to numbers and ensuring each number has 3 digits
        key_as_digits = int(key_as_digits[:24])  # first 24 digits of the converted key
        key_as_digits = key_as_digits % 10000  # 10000
    l = len(text)
    i = 0
    for char in text:
        char_code = ord(char)  # get ascii of char
        decrypted_code = (char_code - key_as_digits) % 0x110000  # decript with key in numbers
        decrypted_char = chr(decrypted_code)  # back to char
        result += decrypted_char
        i += 1
        if i == l:
            loading_bar(i, l, prefix='', suffix='Complete', length=50)
        else:
            loading_bar(i, l, prefix='', suffix='', length=50)
    return result

def keys():
    try:
        mnemo = Mnemonic("english")
        ### 32 bytes entropy
        entropy = os.urandom(32)
        #### bip 39
        seed_words = mnemo.to_mnemonic(entropy)
        #### gen seed
        seed = mnemo.to_seed(seed_words)
        master_key = bip32utils.BIP32Key.fromEntropy(seed)
        xprv = master_key.ExtendedKey()
        
        print("\033[1;90mSeed Words (BIP39):\033[0m")
        print("\033[1;97m%s\033[0m" % seed_words)
        
        print("\n\033[1;90mBIP32 Root Key (xprv):\033[0m")
        print("\033[1;97m%s\033[0m" % xprv)
    
    except Exception as e:
        print(f"An error occurred: {e}")

#Author JMCG