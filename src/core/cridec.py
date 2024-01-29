#!/usr/bin/env python3

from src.core.tobcore import *

#cript function
def encrypt(text, key):
    result= ""
    l = len(text)
    i = 0
    for char in text:
        char_code = ord(char) # get ascii value
        key = key % 10000
        encrypt_code = (char_code + key) % 0x110000 #range(0x110000) unicode
        encrypted_char = chr(encrypt_code) # covert back to char
        result += encrypted_char
        i += 1
        if i == l:
            loading_bar(i, l, prefix='', suffix='Complete', length=50)
        else:
            loading_bar(i, l, prefix='', suffix='', length=50)
        #result += hashcript(result)
    return result

#decrypt function
def decrypt(text, key):
    result = ""
    l = len(text)
    i = 0
    for char in text:
        char_code = ord(char)
        key = key % 10000
        decrypted_code = (char_code - key) % 0x110000 #range(0x110000) unicode
        decrypted_char = chr(decrypted_code) #covert back to char
        result += decrypted_char
        i += 1
        if i == l:
            loading_bar(i, l, prefix='', suffix='Complete', length=50)
        else:
            loading_bar(i, l, prefix='', suffix='', length=50)
    return result

#Author JMCG