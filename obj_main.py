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
                if (i[0:3].isnumeric() and i[3] == ')') or (i[0:2].isnumeric() and i[2] == ')') or (i[0].isnumeric() and i[1] == ')'):
                    temp.append(i)
                    self._count += 1
                    count += 1
                    print(i)
                    i = next(gen)
                    while i[1] != ')' or i[0] == 'i' or i == '':
                        temp.append(i)
                        count += 1
                        print(i)
                        i = next(gen)
                    for c in range(5):
                        temp.append(i)
                        print(i)
                        i = next(gen)
                    k = i[len(i) - 2]
                    temp.append(k)
                    self._values.append(Question(temp[0:count], temp[count:len(temp) - 1], temp[len(temp) - 1]))
                    
            except StopIteration:
                print('itercmpl')
        return

    #quiz
    def quiz(self):
        answer = ''
        num_correct = 0
        for c in range (self._count):
            print()
            if answer == 'q':
                break
            else:
                for i in range (len(self._values[c]._stem)):
                    print(self._values[c]._stem[i])
                print()
                for i in range (len(self._values[c]._alt)):
                    print(self._values[c]._alt[i])
                answer = input("answer: ")
                answer = answer.lower()
                print()
                while answer not in self._letters and answer.lower() != 'q':
                    print("invalid input.")
                    answer = input("answer: ")
                    answer = answer.lower()
                    print()
                if answer == self._values[c]._ans:
                    print()
                    print("correct.")
                    num_correct += 1
                else:
                    print()
                    print("incorrect.")
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
