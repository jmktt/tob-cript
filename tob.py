import os
import random
from src.core.tobcore import *
from pystyle import Colors, Colorate, Write,Add
operating_system = check_os()

def main(i=0):
    try:
        invoption = i
        if (operating_system == "1"):
            os.system("clear")
        elif (operating_system == "0"):
            os.system("cls")
        else:
            print("[!]UNIDENTIFIED OS")
        print(Colorate.Vertical(Colors.yellow_to_red, "{}".format(menu_banner), 1))
        print("\n\033[1;34m[---]    Text-Object Basic Cript (\033[1;33mTOB\033[1;34m).   [---]"+bcolors.RESET)
        print("\033[1;34m[---]          Created by: {}\033[1;34m          [---]".format(cname)+bcolors.RESET)
        print("\033[1;34m[---]            Version: \033[1;31m {} \033[0;0m \033[1;34m          [---] \n".format(version))
        print("\033[1;92m  Welcome to The Text Object Basic Crypt (TOB).\n"+bcolors.RESET)
        print("Select from menu:\n")
        print("1) CRYPT")
        print("2) DECRYPT")
        print("3) GEN KEY")
        print("\n99) EXIT\n")
        if (invoption == 1):
            print(invoption_text)
        option = (input("\nSelect: "))
        if (option == '1'):
        # option 1 - CRIPT
            if (operating_system == "1"):
                os.system("clear")
            elif (operating_system == "0"):
                os.system("cls")
            else:
                print("[!]UNIDENTIFIED OS")
            def cript(ik=0):
                invkey=ik
                def encrypt(text, key):
                    result= ""
                    for char in text:
                        char_code = ord(char) # get ascii value
                        key = key % 10000
                        encrypt_code = char_code + key
                        encrypted_char = chr(encrypt_code) # covert back to char
                        result += encrypted_char
                    return result

                print(cript_banner)
                if (invkey == 1):
                    print(invkey_text)
                text = (input("\nInput Text: "))
                try:
                    key = int(input("Input your KEY: "))
                except Exception as e:
                    if (operating_system == "1"):
                        os.system("clear")
                    elif (operating_system == "0"):
                        os.system("cls")
                    else:
                        print("[!]UNIDENTIFIED OS")
                    cript(ik=1)        
                print(key)        
                encrypted_text = encrypt(text, key)
                #write(encrypted_text) #output in .txt
                print("\nEncrypted text:{0}".format(encrypted_text))
                # CRIPT SUB MENU
                def cript_menu(i=0):
                    invoption=i
                    print("\n1) Back")
                    print("\n99) Exit\n")
                    if (invoption == 1):
                        print(invoption_text)
                    option = (input("\nSelect: "))
                    if (option == '1'):
                        main()
                    elif option == '99'or option == 'exit' or option == 'quit':
                        print("\033[1;36mBye...\n"+bcolors.RESET)
                    else:
                        cript_menu(i=1)
                cript_menu()
            cript()
        elif (option == '2'):
        # option 2 - DECRIPT
            def decript(ik=0):
                if (operating_system == "1"):
                    os.system("clear")
                elif (operating_system == "0"):
                    os.system("cls")
                else:
                    print("[!]UNIDENTIFIED OS")
                invkey=ik
                def decrypt(text, key):
                    result = ""
                    for char in text:
                        char_code = ord(char) #get ascii value
                        key = key % 10000
                        decrypted_code = char_code - key 
                        decrypted_char = chr(decrypted_code) #covert back to char
                        result += decrypted_char
                    return result
                print(decript_banner)
                if (invkey == 1):
                    print(invkey_text)
                text = (input("\nInput Text: "))
                try:
                    key = int(input("Input your KEY: "))
                except Exception as e:
                    if (operating_system == "1"):
                        os.system("clear")
                    elif (operating_system == "0"):
                        os.system("cls")
                    else:
                        print("[!]UNIDENTIFIED OS")
                    decript(ik=1)                           
                decrypted_text = decrypt(text, key)
                print("\nDecrypted text:{0}".format(decrypted_text))
                # DECRIPT SUB MENU
                def decript_menu(i=0):
                    invoption=i
                    print("\n1) Back")
                    print("\n99) Exit\n")
                    if (invoption == 1):
                        print(invoption_text)
                    option = (input("\nSelect: "))
                    if (option == '1'):
                        main()
                    elif option == '99'or option == 'exit' or option == 'quit':
                        print("\033[1;36mBye...\n"+bcolors.RESET)
                    else:
                        decript_menu(i=1)
                decript_menu()
            decript()
        elif (option =='3'):
        # option 3 - GENERATE KEY
            def gen_key(i=0):
                if (operating_system == "1"):
                    os.system("clear")
                elif (operating_system == "0"):
                    os.system("cls")
                else:
                    print("[!]UNIDENTIFIED OS")
                invoption = i
                random.seed()
                key = random.randrange(000000000000000000000000, 999999999999999999999999)
                print("\033[1;97m\n\n              8 8 8 8                     ,ooo.     ")
                print("              8a8 8a8                    oP   ?b    ")
                print("             d888a888zzzzzzzzzzzzzzzzzzzz8     8b   ")
                print("              `ii^ii'                    ?o___oP'   \033[0;0m")
                print("\033[1;32m\n       +--------------------------------------------+")
                print(" \033[1;32m\n       |\033[0;0m  YOUR KEY IS : {}    \033[1;32m|\n".format(key))
                print("       +--------------------------------------------+\033[0;0m\n")
                print("\n1) Back")
                print("2) ReGen")
                print("\n99) Exit\n")
                #keygen sub menu
                if (invoption == 1):
                    print(invoption_text)
                option = (input("\nSelect: "))
                if (option == '1'):
                    main()
                elif (option == '2'):
                    gen_key(i=0)
                elif option == '99'or option == 'exit' or option == 'quit':
                    print("\033[1;36mBye...\n"+bcolors.RESET)
                else:
                    gen_key(i=1) 
            gen_key()
        elif option == '99'or option == 'exit' or option == 'quit':
            print("\033[1;36mBye...\n"+bcolors.RESET)
        else:
            main(i=1)
    except KeyboardInterrupt:
        print("\n[!] Control-C detected. Exiting TOB.")
    except Exception as e:
        print("\n[!] Something went wrong. Printing the error: {0}".format(e))

#---------------------# start
main() 