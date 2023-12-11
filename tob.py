#!/usr/bin/env python3

import secrets
from src.core.tobcore import *
from src.core.cridec import *
from pystyle import *

def main(i=0):
    try:
        invoption = i
        disp_clean()
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
            disp_clean()
            def cript(ik=0):
                invkey=ik
                print(Colorate.Vertical(Colors.purple_to_red,(cript_banner),2))
                if (invkey == 1):
                    print(invkey_text)
                text = (input("\nInput Text: "))
                while True: ## invalid key looping
                    try:
                        key = int(input("Input your KEY: "))
                        min_valid_key = secrets.randbelow(999999999999999999999999)

                        if len(str(key)) == len(str(min_valid_key)):
                            break
                        else:
                            disp_clean()
                            print(Colorate.Vertical(Colors.purple_to_red,(cript_banner),2))
                            print(invkey_text,"\n")
                    except Exception as e:
                        disp_clean()
                        cript(ik=1)            
                encrypted_text = encrypt(text, key)
                write(encrypted_text) #output in .txt
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
                disp_clean()
                invkey=ik
                print(Colorate.Vertical(Colors.purple_to_red,(decript_banner),2))
                if (invkey == 1):
                    print(invkey_text)
                text = (input("\nInput Text: "))
                while True: ## invalid key looping
                    try:
                        key = int(input("Input your KEY: "))
                        min_valid_key = secrets.randbelow(999999999999999999999999)

                        if len(str(key)) == len(str(min_valid_key)):
                            break
                        else:
                            disp_clean()
                            print(Colorate.Vertical(Colors.purple_to_red,(cript_banner),2))
                            print(invkey_text,"\n")
                    except Exception as e:
                        disp_clean()
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
                disp_clean()
                invoption = i
                key = secrets.randbelow(999999999999999999999999)
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

#Author JMCG