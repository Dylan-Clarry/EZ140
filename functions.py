'''
-----------------------------
|    functions.py           |
|    Dylan Clarry           |
|    external functions     |
|    January 28 2018        |
-----------------------------
'''
#read file
def read_file(var_file, path):
        #try to open file
        try:
            path += var_file
            file = open(path, 'r')
            for line in file:
                yield (line)
            file.close()
            print("file initialized.")
        #File not found
        except FileNotFoundError:
            print("error. file '{}' not found in path.".format(var_file))

#read_me
def read_me():
    file = open('readme.txt', 'r')
    line = file.readline()
    for c in range(13):
        line = file.readline()
    try:
        for c in range (6):
            while line[0] != '#':
                print(line)
                line = file.readline()
            print()
            cont = input("press enter to continue.")
            line = file.readline()
            print()
    except IndexError:
        print()
        
#print_title
def print_title():
    print()
    print("  /$$$$$$$$$$  /$$$$$$$$$$    /$$   /$$  /$$   /$$$$$$" )
    print("   $$_______/          /$$  /$$$$    $$   $$  /$$$_ /$$")
    print("   $$                /$$      /$$    $$  /$$   $$$$  $$")
    print("   $$$$$$          /$$         $$   /$$$$$$$$  $$ $$ $$")
    print("   $$___/        /$$           $$    ____$$_/  $$  $$$$")
    print("   $$          /$$             $$        $$    $$  /$$$")
    print("  /$$$$$$$$$$  /$$$$$$$$$$  /$$$$$$      $$    /$$$$$$/")
    print("   _________/   _________/  /_____/     /_/    ______/" )
    print("  By Dylan Clarry                                 V 0.2")
    print("  March 5th 2017")
    print()

#print_menu
def print_menu():
    print ("1. file select")
    print ("2. initialize")
    print ("3. start quiz")
    print ("4. instructions")
    print ("5. exit")