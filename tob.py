import os
import random
import time
invoption_text = ("\n\033[;1m\x1b[31m There is no such option...\033[0;0m\n")

def main(i=0):
    invoption = i
    print("\033[1;33m\n   ooooooooooooo   .oooooo.   oooooooooo. ")
    print("\033[1;33m   8'   888   `8  d8P'  `Y8b  `888'   `Y8b ")
    print("\033[1;33m        888      888      888  888     888 ")
    print("\033[1;33m        888      888      888  888oooo888' ")
    print("\033[1;33m        888      888      888  888    `88b ")
    print("\033[1;33m        888      `88b    d88'  888    .88P ")
    print("\033[1;33m       o888o      `Y8bood8P'  o888bood8P'  \033[0;0m")
    print("\n\033[1;34m[---]    Text-Object Basic Cript (\033[1;33mTOB\033[1;34m).   [---]\033[0;0m")
    print("\033[1;34m[---]          Created by: \033[1;31mJMKTT\033[1;34m          [---]\033[0;0m")
    print("\033[1;34m[---]            Version: \033[1;31m 1.2 \033[0;0m \033[1;34m          [---] \n")
    print("\033[1;92m  Welcome to The Text Object Basic Crypt (TOB).\033[0;0m\n")
    print("\nSelect from menu:\n")
    print("1) CRYPT")
    print("2) DECRYPT")
    print("3) GEN KEY")
    print("\n99) EXIT\n")
    if (invoption == 1):
        print(invoption_text)
    option = int(input("\nSelect: "))
    if (option == 1):
        print("IN PROGRESS\n")
    elif (option == 2):
        print("IN PROGRESS\n")
    elif (option ==3):
        def gen_key(i=0): #------------# gen key
            os.system("clear")
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
            if (invoption == 1):
                print(invoption_text)
            option = int(input("\nSelect: "))
            if (option == 1):
                main()
            elif (option == 2):
                gen_key(i=0)
            elif (option == 99):
                print("\033[1;36mBye...\033[0;0m\n")
            else:
                gen_key(i=1) 
        gen_key()
    elif (option == 99):
        print("\033[1;36mBye...\033[0;0m\n")
    else:
        main(i=1)
#---------------------# start
main() 