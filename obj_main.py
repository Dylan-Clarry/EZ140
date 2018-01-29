
'''
-----------------------------
|    obj_main.py            |
|    Dylan Clarry           |
|    Questions objects      |
|    January 28 2018        |
-----------------------------
'''
from copy import deepcopy

class List:
    #initialize
    def __init__(self):
        self._values = []
        self._count = 0
        return

    #append - adds new value to the list
    def append(self, value):
        self._values.append(deepcopy(value))
        return
    
    #gen_to_question
    def gen_to_question(self, gen):
        self._count = 0
        for i in gen:
            temp = []
            count = 0
            try:
                #Check if current line is the beginning of a question
                if (i[0:3].isnumeric() and i[3] == ')') or (i[0:2].isnumeric() and i[2] == ')') or (i[0].isnumeric() and i[1] == ')'):
                    temp.append(i)
                    self._count += 1
                    count += 1
                    print(i)
                    i = next(gen)
                    #For when question exceeds one line
                    while i[1] != ')' or i[0] == 'i' or i == '':
                        temp.append(i)
                        count += 1
                        print(i)
                        i = next(gen)
                    #Appemd each alternate
                    for c in range(5):
                        temp.append(i)
                        print(i)
                        i = next(gen)
                    #Append the correct answer
                    k = i[len(i) - 2]
                    temp.append(k)
                    self._values.append(Question(temp[0:count], temp[count:len(temp) - 1], temp[len(temp) - 1]))
            #End of questions list
            except StopIteration:
                print('itercmpl')
        return

    #quiz
    def quiz(self):
        answer = ''
        num_correct = 0
        for c in range (self._count):
            print()
            #If user enters 'q' to quit
            if answer == 'q':
                break
            else:
                #Print stem
                for i in range (len(self._values[c]._stem)):
                    print(self._values[c]._stem[i])
                print()
                #Print alternates
                for i in range (len(self._values[c]._alt)):
                    print(self._values[c]._alt[i])
                answer = input("answer: ").lower()
                print()
                #Invalid input
                while answer not in self._letters and answer.lower() != 'q':
                    print("invalid input.")
                    answer = input("answer: ").lower()
                    print()
                #Correct response
                if answer == self._values[c]._ans:
                    print()
                    print("correct.")
                    num_correct += 1
                #Incorrect response
                else:
                    print("\nincorrect.")
                    print("the correct answer is {}".format(self._values[c]._ans))
            print()
        print("you got {}/{} correct".format(num_correct, self._count))

    #print_question_list
    def print_question_list (self):
        for c in range (self._count):
            self._values[c].print_question()
        return

class Question:
    #initialize
    def __init__(self, stem, alt, ans):
        self._stem = []
        for c in range(len(stem)):
            self._stem.append(stem[c])
        self._alt = []
        for c in range(len(alt)):
            self._alt.append(alt[c])
        self._ans = ans.lower()
        return

    #print_question
    def print_question(self):
        for c in range(len(self._stem)):
            print(self._stem[c])
        for c in range(len(self._alt)):
            print(self._alt[c])
        return