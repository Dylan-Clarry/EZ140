'''
-----------------------------
|    EZ140.py               |
|    Dylan Clarry           |
|    Main program           |
|    January 28 2018        |
-----------------------------
'''
import sys
import os
from obj_main import List
from functions import read_file, print_title, print_menu, read_me

print_title()
path = os.getcwd() + '\\question_bank\\'
loop = True
list_made = False

while loop:
    print_menu()
    choice = input()
    choice = choice.lower()

    #file select
    if choice == str(1):
        print()
        var_file = input("file name: ")
        if var_file.endswith('.txt') == False:
            var_file += '.txt'
    #initialize
    elif choice == str(2):
        print()
        try:
            gen = read_file(var_file, path)
            l = List()
            l.gen_to_question(gen)
            list_made = True
        except NameError:
                print("error. file name not given.")
    #start quiz
    elif choice == str(3):
        print()
        if list_made == True:
            print("enter 'q' to quit at any time")
            print()
            l.quiz()
        else:
            print("error. file not initialized.")
    #instructions
    elif choice == str(4):
        read_me()
    #quit
    elif choice == str(5):
        loop = False
    #cmd
    elif choice == 'cmd':
        print()
        x = input(">>>")
        try:
            if x != '':
                while x[0] == ' ':
                    x = x[1:len(x)]
                #list questions
                if x == 'list_questions':
                    l.print_question_list()
                #list count
                elif x == 'list_count':
                    try:
                        print("questions: {}".format(l._count))
                    except NameError:
                        print("error. list not initialized.")
                #show path
                elif x == 'show_path':
                    print()
                    print(path)
                #change directory
                elif x[0:2] == 'cd' and x[2] == ' ':
                    x = x[3:len(x)]
                    if x.startswith("C:\\"):
                        path = x
                        if path.endswith('\\') == False:
                            path += '\\'
                    else:
                        print("error. file must be on c-drive.")
                else:
                    print("error. input valid selection.")
        except TypeError:
            print("error. not valid selection.")
        except IndexError:
            print("error. not valid selection.")
    #invalid input
    else:
        print("error. not valid selection.")
    print()
sys.exit(0)