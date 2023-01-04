import os
import random
from src.core.tobcore import *
from pystyle import *
import time
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
        print(Colorate.DiagonalBackwards(Colors.red_to_yellow, "{}".format(menu_banner), 2))
        print("\n\033[1;34m[---]    Text-Object Basic Cript ({}\033[1;34m).   [---]".format(tname)+bcolors.RESET)
        print("\033[1;34m[---]          Created by: {}\033[1;34m          [---]".format(cname)+bcolors.RESET)
        print("\033[1;34m[---]            Version: \033[1;31m {} \033[0;0m \033[1;34m          [---] \n".format(version))
        print(Colors.green,"Welcome to The Text Object Basic Crypt (TOB).\n"+bcolors.RESET)
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
                    l = len(text)
                    i = 0
                    loading_bar(i, l, prefix='a', suffix='', length=50)
                    for char in text:
                        char_code = ord(char) # get ascii value
                        key = key % 10000
                        encrypt_code = char_code + key
                        encrypted_char = chr(encrypt_code) # covert back to char
                        result += encrypted_char
                        i += 1
                        if i == l:
                            loading_bar(i, l, prefix='', suffix='Complete', length=50)
                        else:
                            loading_bar(i, l, prefix='', suffix='', length=50)
                    return result

                print(Colorate.Vertical(Colors.purple_to_red,(cript_banner),2))
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
                encrypted_text = encrypt(text, key)
                time.sleep(1)
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
                    l = len(text)
                    i = 0
                    loading_bar(i, l, prefix='a', suffix='', length=50)
                    for char in text:
                        char_code = ord(char) #get ascii value
                        key = key % 10000
                        decrypted_code = char_code - key 
                        decrypted_char = chr(decrypted_code) #covert back to char
                        result += decrypted_char
                        i += 1
                        if i == l:
                            loading_bar(i, l, prefix='', suffix='Complete', length=50)
                        else:
                            loading_bar(i, l, prefix='', suffix='', length=50)
                    return result
                print(Colorate.Vertical(Colors.purple_to_red,(decript_banner),2))
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
                print(Colorate.Horizontal(Colors.black_to_red,key_banner,1))
                display_key_box(key)
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