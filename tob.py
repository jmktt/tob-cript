#!/usr/bin/env python3

import secrets
import string
from src.core.tobcore import *
from src.core.cridec import *
from pystyle import *
import random


def main(i=0):
    try:
        invoption = i
        disp_clean()
        selected_banner = random.choice(banners)
        print(Colorate.DiagonalBackwards(Colors.yellow_to_red, "{}".format(selected_banner), 2))
        print("\n\033[1;34m[---]    Text-Object Basic Cript ({}\033[1;34m).   [---]".format(tname)+bcolors.RESET)
        print("\033[1;34m[---]          Created by: {}\033[1;34m          [---]".format(cname)+bcolors.RESET)
        print("\033[1;34m[---]            Version: \033[1;31m {} \033[0;0m \033[1;34m          [---] \n".format(version))
        print(Colors.green,"Welcome to The Text Object Basic Crypt (TOB).\n"+bcolors.RESET)
        print("Select from menu:\n")

        print("1) CRYPT")
        print("2) DECRYPT")
        print("3) GEN KEY")
        print("4) BTC")
        print("\n99) EXIT\n")
        if (invoption == 1):
            print(invoption_text)
        option = (input("\n\033[4mtob\033[0m> "))
        if (option == '1'):
        # option 1 - CRIPT
# option 1 - CRIPT
            def cript(ik=0):
                disp_clean()
                invkey = ik
                print(Colorate.Vertical(Colors.purple_to_red, cript_banner, 2))
                
                if invkey == 1:
                    print(invkey_text)
                if invkey == 2:
                    print(invoption_text)
                if invkey == 3:
                    print(invfile_text)
            
                print("\nOptions:")
                print("1) Input text manually")
                print("2) Read text from file")
                print("\n99) Back")
            
                choice = (input("\n\033[4mtob\033[0m> "))
            
                if choice == '1':
                    text = input("\nInput Text: ")
                elif choice == '2':
                    try:
                        filename = input("Enter the filename: ")
                        if filename == "tob.py" or filename == "tob":
                            print(Colorate.Vertical(Colors.green_to_yellow, funny, 2))
                            print("\n[!] Did you think I wouldn't see this coming?...")
                            wait = input("Press Enter to back.")
                            cript()
                            return 0;
                        else:   
                            with open(filename, 'r', encoding='utf-8') as file:
                                text = file.read()
                    except FileNotFoundError:
                        disp_clean()
                        cript(ik=3)
                elif choice == '99':
                    main()
                    return
                else:
                    disp_clean()
                    cript(ik=2)
                    return
            
                while True:  # looping de chave inválida
                    try:
                        key = input("Input your KEY: ")

                        if len(key) == 24 and all(char in string.ascii_letters + string.digits for char in key):
                            break
                        else:
                            disp_clean()
                            print(Colorate.Vertical(Colors.purple_to_red, cript_banner, 2))
                            print(invkey_text, "\n")
                    except Exception as e:
                        disp_clean()
                        cript(ik=1)
            
                encrypted_text = encrypt(text, key)
                #write(encrypted_text)  # output in .txt
                print("\nEncrypted text: {0}".format(encrypted_text))
            
                # CRIPT SUB MENU
                def cript_menu(i=0):
                    invoption=i
                    print("\n1) Back")
                    print("\n99) Exit\n")
                    if (invoption == 1):
                        print(invoption_text)
                    option = (input("\n\033[4mtob\033[0m> "))
                    if (option == '1'):
                        main()
                    elif option == '99'or option == 'exit' or option == 'quit':
                        print(bye_message)
                    else:
                        cript_menu(i=1)
                cript_menu()
            cript()
        elif (option == '2'):
            # option 2 - DECRYPT
            def decript(ik=0):
                disp_clean()
                invkey = ik
                print(Colorate.Vertical(Colors.purple_to_red, decript_banner, 2))
                
                if invkey == 1:
                    print(invkey_text)
                if invkey == 2:
                    print(invoption_text)
                if invkey == 3:
                    print(invfile_text)
                
                print("\nOptions:")
                print("1) Input text manually")
                print("2) Read text from file")
                print("\n99) Back")
                
                choice = (input("\n\033[4mtob\033[0m> "))
                
                if choice == '1':
                    text = input("\nInput Text: ")
                elif choice == '2':
                    try:
                        filename = input("Enter the filename: ")
                        if filename == "tob.py" or filename == "tob":
                            print(Colorate.Vertical(Colors.green_to_yellow, funny, 2))
                            print("\n[!] Did you think I wouldn't see this coming?...")
                            wait = input("Press Enter to back.")
                            decript()
                            return 0;
                        else:   
                            with open(filename, 'r', encoding='utf-8') as file:
                                text = file.read()
                    except FileNotFoundError:
                        disp_clean()
                        decript(ik=3)
                elif choice == '99':
                    main()
                    return
                else:
                    disp_clean()
                    decript(ik=2)
                    return
                
                while True:  # looping de chave inválida
                    try:
                        key = input("Input your KEY: ")

                        if len(key) == 24 and all(char in string.ascii_letters + string.digits for char in key):
                            break
                        else:
                            disp_clean()
                            print(Colorate.Vertical(Colors.purple_to_red, cript_banner, 2))
                            print(invkey_text, "\n")
                    except Exception as e:
                        disp_clean()
                        cript(ik=1)
                
                decrypted_text = decrypt(text, key)
                print("\nDecrypted text: {0}".format(decrypted_text))
            
                # DECRIPT SUB MENU
                def decript_menu(i=0):
                    invoption=i
                    print("\n1) Back")
                    print("\n99) Exit\n")
                    if (invoption == 1):
                        print(invoption_text)
                    option = (input("\n\033[4mtob\033[0m> "))
                    if (option == '1'):
                        main()
                    elif option == '99'or option == 'exit' or option == 'quit':
                        print(bye_message)
                    else:
                        decript_menu(i=1)
                decript_menu()
            decript()
        elif (option =='3'):
        # option 3 - GENERATE KEY
            def gen_key(i=0):
                disp_clean()
                invoption = i
                ##################################
                if (invoption == 3):
                    key_length = 24
                    key = str(secrets.randbelow(10**key_length)).zfill(key_length)### zero fill
                else:
                    key_length = 24 ### KEY SIZE
                    characters = string.ascii_letters + string.digits
                    key = ''.join(secrets.choice(characters) for _ in range(key_length))  ## increase possibility of keys
                print(Colorate.Horizontal(Colors.black_to_red,key_banner,1))
                display_key_box(key)
                print("\n1) Back")
                print("2) ReGen")
                print("3) ReGen (only numbers)")
                print("\n99) Exit\n")
                #keygen sub menu
                if (invoption == 1):
                    print(invoption_text)
                option = (input("\n\033[4mtob\033[0m> "))
                if (option == '1'):
                    main()
                elif (option == '2'):
                    gen_key(i=0)
                elif (option == '3'):
                    gen_key(i=3)
                elif option == '99'or option == 'exit' or option == 'quit':
                    print("\033[1;36m"+bye_message+bcolors.RESET)
                else:
                    gen_key(i=1) 
            gen_key()
################### bip39 
        elif option == '4':
            def bip(ik=0):
                disp_clean()
                invkey = ik
                print(Colorate.Horizontal(Colors.black_to_white,bit_logo,2))  
                
                if invkey == 1:
                    print(invoption_text)
            
                print("\nOptions:")
                print("1) Generate BIP39 Keys")
                print("\n99) Back")
            
                choice = (input("\n\033[4mtob\033[0m> "))
                
                if (choice == '1'):
                    def bip_menu(i=0): #gen bip submenu
                        disp_clean()
                        print(Colorate.Horizontal(Colors.white_to_blue,bit_logo,2))  
                        print("")
                        keys()
                        invoption=i
                        print("\nOptions:")
                        print("\n1) Back")
                        print("2) ReGen")
                        print("\n99) Exit")

                        if (invoption == 1):
                            print(invoption_text)
                        option = (input("\n\033[4mtob\033[0m> "))
                        if (option == '1'):
                            bip()
                            return
                        if (option == "2"):
                            bip_menu()
                        elif option == '99'or option == 'exit' or option == 'quit':
                            print(bye_message)
                        else:
                            bip_menu(i=1)
                    bip_menu()
                elif choice == '99':
                    main()
                else:
                    bip(ik=1) 
            bip(ik=0)
##########################         
        elif option == '99'or option == 'exit' or option == 'quit':
            print(bye_message)
        elif option == "john" or option == "jm":
            print(Colorate.Vertical(Colors.red_to_black, john, 2))
            credit_text()
            wait = input("\nPress Enter to back to main menu.")
            main()
        else:
            main(i=1)
    except KeyboardInterrupt:
        print("\n[!] Control-C detected. Exiting TOB.")
        print(bye_message)
        quit

    except Exception as e:
        print("\n[!] Something went wrong. Printing the error: {0}".format(e))
        print("[!] Looks like our code decided to pause for a joke!")
#---------------------# start
check_status()
main() 

#Author JMCG