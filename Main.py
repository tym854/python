import random
import time
import os
import shutil
from itertools import repeat
from sys import exception
import functools
import threading
from multiprocessing import Process, cpu_count
from tkinter import *

from helper import Car

first_name = 'Tymur'
last_name = 'Buriachok'
full_name = first_name + last_name
#age = 17
#age += 1

#print(type(age))
#print('My age is: ' +str(age))

#print(type(name))
#print(full_name + ' loves pizza')

#Human = False
#print('I am a human: ' + str(Human))

#name, age, atrractive = 'tymur', 21, True
#print(name)
#print(age)
#print(atrractive)

#print(first_name.find('r'))
#print(first_name.capitalize())
#print(first_name.upper())
#print(first_name.isdigit())
#print(first_name.isalpha())

#name = input('What is your name? Type it right hear: ')
#print('Hello ' +name)
#age = int(input('What is your age? Type hear: ' ))
#age = age + 1
#if age >= 18:
    #print('Yooooo, you are ' + str(age) + ' years old. Lets go for bear')
#else:
    #print('Nah bro, another time')

#name = 'Tymur Buriachok'

#first_name = name[0:5]
#last_name = name[6:]
#funky_name = name[::2]

#print(first_name)
#print(last_name)
#print(funky_name)

#website = 'https://www.youtube.com/watch?v=XKHEtdqhLK8&list=WL&index=8'
#slice = slice(12,19)
#print(website[slice])

#temp = int(input('What is the temperature is today?: '))

#if temp >= 0 and temp <= 30: also(if, elif, else, not)
    #print('The temperature is good today!')

#while 1==1:
    #print('Help! Im stuck in the loop!')



#name = ''
#while len(name) == 0:
    #name = input('Enter your name: ')

#print('Hello ' +name)

#for seconds in range(10,0,-1):
    #print(seconds)
    #time.sleep(1)
#print('Happy New Year!')

#rows = int(input('How many rows?: '))
#colums = int(input('How many colums?: '))
#symbol = input('Which symbol to use?: ')

#for high in range(rows):
    #for lengh in range(colums):
        #print(symbol, end='')
    #print()

#while True:
    #name = input('Enter your name: ')
    #if name != '':
        #break

#phone_number = input('Enter your phone number: ')


#if True:
      #if len(phone_number) <= 8:
         #print("Your phone number is incorrect!")
         #print(input('Enter your phone number: '))

      #for i in phone_number:
         #if i == "-":
            #continue
         #print(i, end=" ")


      #print("Congrats! You finished your registration!")


#breakfast = ['eggs', 'orange juice', 'toast']
#meal = ['hamburger', 'sandwich']
#dinner = ['Turkey', 'salad']

#food = [breakfast, meal, dinner]

#print(food[0] [0])

#student = ('Tymur', '17', '123-123-123')

#print(student.count('Bro'))
#print(student.index('123-123-123'))

#for i in student:
    #print(i)

#utensils = {'spoon', 'fork', 'knife'}
#dishes = {'plate', 'cup', 'bowl', 'knife'}

#utensils.add('napkin')
#print(utensils.intersection(dishes))
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)
#if True:
    #utensils.difference(dishes) != 1
    #utensils.remove("knife")
    #print(utensils)
#!!!!

#capitals = {'USA': 'Washington DC',
            #'India': 'New Dahli',
            #'China': 'Beijing',
            #'Ukraine': 'Kyiv'}

#capitals.update({'Germany': 'Berlin'})

#print(capitals['Ukraine'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

#for key, values in capitals.items():
    #print(key, values)

#functions

#def hello(first_name, last_name, age):
    #print('Hello '+first_name+' '+last_name)
    #print('Probably you are '+str(age)+' years old')
    #print('Have a nice day')

#hello('Tymur', 'Buriachok', 21)

#def multiply(number1, number2):
    #return number1 * number2

#x = multiply(6,6)

#print(x)

#def add(*args):
 #  sum = 0
    #args = list(args)
    #args.insert(0, 5)
    #for i in args:
        #sum += i
    #return sum

#print(add(1,3,8,10))



def hello(**kwargs):
    print('Hello ',end='')
    for key,value in kwargs.items():
        print(value, end=' ')

#hello(title='Mr.',first='Tymur',middle='Buriachok',last='Maximovich')


#animal = 'cow'
#item = 'moon'

#print('The {2} jumped over the {1}'.format(animal,item,'dog'))

#list = {'animal': 'cow',
        #'item': 'moon'}

##text = 'The {} jumped over the {}'



#for values in list.items():
    #print(text.format(list['animal','item']))

#print('The {:10} jumped over the {:^10}'.format('cow', 'moon'))

#x = random.randint(0,38)
#y = random.random()

#MyList = ['rock', 'paper', 'scissors']
#z = random.choice(MyList)

#cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']

#random.shuffle(cards)

#print(cards)

Errormassage = 'Invalid operation'

#number1 = int(input('Write a numerator: '))
#number2 = int(input('Write a denominator: '))

#if int(number2) == 0:
    #print(Errormassage)
    #number2 = int(input('Write a denominator: '))
#result = number1/number2
#print(result)
#one of the ways to do this operation

#try:
    #def division():
       #number1 = int(input('Write a numerator: '))
       #number2 = int(input('Write a denominator: '))
       #result = number1/number2
    #print(division())
#except ZeroDivisionError:
    #print('You cant divide by zero! Try again: ')
    #print(division())
#except ValueError:
    #print('You can write only numbers! Try again: ')
    #print(division())
#except Exception:
    #print(Errormassage)
#else:
    #print(result)
#finally:
    #print('Try later plz!')

#as two errors something bad happens

#path ='C:\\Users\\ёрсше\\Desktop\\PrScr\\Jopa.png'


#if os.path.exists(path):
    #print('This location exists')
    #if os.path.isfile(path):
        #print('This is a file!')
    #elif os.path.isdir(path):
        #print('This is a directory')
#else:
    #print('This location does not exist')
#try:
    #with open('pth.tx') as file: serves to open files
        #print(file.read())
#except FileNotFoundError:
    #print('File was not found')

#text = 'Yooooo\nHere you have some text\nHave a good one!\n'

#with open('pth.txt','a') as file:
    #file.write(text)

#shutil.copyfile('pth.txt','copy.file')

#source = 'pth.txt'
#destination = 'C:\\Users\\ёрсше\\Desktop\\pth.txt'

#try:
    #if os.path.exists(destination):
        #print('There alredy exists such a file')
    #else:
        #os.replace(source,destination) #cho i kuda
        #print('The source file was moved')
#except FileNotFoundError: #----------------------------------------------------------------------------------------------------------------------------------------------------------------
    #print('This file does not exist')

#os.remove(path) = do delete the file
#os.rmdir(path) = to delete the directory
#os.rmtree(path) =  to delete the directory with file within

#import helper as pth one way to import info from other source
#from helper import hello,Bye #* - all

#hello()
#Bye()

                                                                                        #Rock paper scissors game

#while True:

    #choices = ['rock', 'paper', 'scissors']

    #computer = random.choice(choices)
    #player = None

    #player = input('Rock, Paper or Scissors?: ').lower()

    #while player not in choices:
        #print('You can pick only proposed ones!')
        #player = input('Rock, Paper or Scissors?: ').lower()

    #print('computer: ', computer)
    #print('You: ', player)

    #if player == computer:
        #print('Tie!')
    #elif player == 'rock':
        #if computer == 'scissors':
            #print('You win!')
        #if computer == 'paper':
            #print('You lose!')
    #elif player == 'paper':
        #if computer == 'scissors':
            #print('You lose!')
        #if computer == 'rock':
            #print('You win!')
    #elif player == 'scissors':
        #if computer == 'paper':
            #print('You win!')
        #if computer == 'rock':
            #print('You lose!')

    #play_again = input('Would you like to play ones more? (yes/no): ').lower()

    #answer = ['yes', 'no']

    #while play_again not in answer:
        #print('Answer this question again plz!')
        #play_again = input('Would you like to play ones more? (yes/no): ').lower()
    #if play_again != 'yes':
        #break

#print('Bye!')

#Quiz game

#from PIL import Image

#def new_game(): #would like to intruduce the on which question you are now
    #guesses = []
    #correct_guesses = 0
    #question_num = 1

    #for key in questions:
        #print('----------------')
        #print(key)
        #for i in options[question_num - 1]:
            #print(i)
        #guess = input('Enter (A, B, C or D): ')
        #guess = guess.upper()
        #guesses.append(guess)

        #correct_guesses += check_answer(questions.get(key), guess)
        #question_num += 1
    #display_score(correct_guesses, guesses)


# ------------------
#def check_answer(answer, guess):
    #if guess not in options_to_answer:
        #print('You can only choose between A, B, C or D')
    #if answer == guess:
        #print('CORRECT')
        #return 1
    #else:
        #print('INCORRECT')
        #return 0


# ------------------
#def display_score(correct_guesses, given_guesses):
    #print('----------------')
    #print('RESULTS: ')
    #print('ANSWERS: ',end="")
    #for i in questions:
        #print(questions.get(i),end=" ")
    #print() #why so?
    #print('GUESSES: ', end="")
    #for i in given_guesses:
        #print((i), end=" ")
    #print() #why so?
    #score = int((correct_guesses/len(questions))*100) #why so?
    #print('Your score is: '+str(score)+'%')
# ------------------
#def play_again():
   #play_again = input('Would you like to play ones more? (yes/no): ').lower()

   #answer = ['yes', 'no']

   #while play_again not in answer:
      #print('Answer this question again plz!')
      #play_again = input('Would you like to play ones more? (yes/no): ').lower()
   #if play_again == 'yes':
       #return True
   #if play_again == 'no':
       #return False
# ------------------

#questions = {
#"Who created Python?: ": "A",
#"What year was Python created?: ": "B",
#"Python is tributed to which comedy group?: ": "C",
#"Is the Earth round?: ": "A"}
#2D list
#options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
#["A. 1989", "В. 1991", "C. 2000", "D. 2016"],
#["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

#options_to_answer = ['A','B','C','D']

#new_game()
#while play_again():
    #new_game()
#print('Bye!')


#car_1 = Car('Chevy', 'Corvette', '2021', 'blue')
#car_2 = Car('four-wheel drive ', 'Mustang', '2022', 'black')
#print(car_2.make)
#print(car_2.model)
#print(car_2.year)
#print(car_2.color)
#car_2.drive()
#car_2.stop()

#car_1.wheels = 2

#print(Car.wheels)

#print(car_1.wheels)

#class Organism:

    #alive = True
    #def breath(self):
        #print('All units of this type can breath')

#class Animals(Organism):

    #def eat(self):
        #print('This animal is eating')
    #def sleep(self):
        #print('This animal is sleeping')

#class Rabbit(Animals):
    #def eat(self):
        #print('This rabbit is eating carrot') #method overwriting
    #def run(self):
        #print('This rabbit can run')
#class Fish(Animals):
    #def swim(self):
        #print('This fish can swim')
#class Hawk(Animals):
    #def fly(self):
        #print('This hawk can fly')
#rabbit = Rabbit()
#fish = Fish()
#hawk = Hawk()

#print(Rabbit.alive)
#fish.swim()
#hawk.fly()
#fish.breath()
#rabbit.eat()

#class Car:
   #def turn_on(self):
      #print("You start the engine")
      #return self
   #def drive(self):
      #print("You drive the car")
      #return self
   #def brake(self):
      #print("You step on the brakes")
      #return self
   #def turn_off(self):
      #print("You turn off the engine")
      #return self

#car = Car()
#car.turn_on().drive()

#class Rectangle:

    #def __init__(self, length, width):

        #self.length = length
        #self.width = width

#class Square (Rectangle):

   #def __init__(self, length, width):
       #super().__init__(length,width)

   #def area(self):
       #return self.length*self.width

#class Cube (Rectangle):

   #def __init__(self, length, width, height):
      #super().__init__(length,width)
      #self.height = height

   #def volume(self):
      #return self.length*self.width*self.height

#square = Square(3,3)
#cube = Cube(3,3,3)

#print(square.area())
#print(cube.volume())

#from abc import ABC, abstractmethod

#class Vehicle (ABC):
   #@abstractmethod
   #def go(self):
      #pass
#class Car (Vehicle):
   #def go(self):
      #print("You drive the car")
#class Motorcycle (Vehicle):
    #def go(self):
        #print('You drive the motocycle')

#vehicle = Vehicle()
#car = Car()
#motocycle = Motorcycle()

#vehicle.go()

class Car:

    color = None

def change_color(car,color):

    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

change_color(car_1,'red')
change_color(car_2,'blue')
change_color(car_3,'pink')

#print(car_1.color)
#print(car_2.color)
#print(car_3.color)

#class Duck:
    #def walk(self):
        #print("This duck is walking")
    #def talk(self):
        #print("This duck is gwuacking")
#class Chicken:
    #def walk (self):
        #print("This chicken is walking")
    #def talk(self):
        #print("This chicken is clucking")
#class Person:
    #def catch(self, duck):
        #duck.walk()
        #duck.talk()
        #print('You caught the critter')

#duck = Duck()
#chicken = Chicken()
#person = Person()

#person.catch(chicken)

#foods = list()
#while food := input('What food do you like?:') != 'quit':
    #food.appends(food)

#while True:
    #food = input('What food do you like?:')
    #if food == 'quit':
        #print('Your favorite foods are: ',foods)
        #break
    #foods.append(food)

#                              Higher Order Function

#def loud(text):
    #return text.upper()
#def quiet(text):
    #return text.lower()
#def hello(func):
    #text = func('Hello')
    #print(text)

#hello(loud)
#hello(quiet)

#-------------Higher order function-------------#

#def divisor(x):
    #def dividend(y):
        #return x / y
    #return dividend

#divide = divisor(2)
#print(divide(10))

#-------------Lambda functions-------------#

#double = lambda x:x * 2
#print(double(5))
#multiply = lambda x,y:x * y
#print(multiply(5,6))
#age_check = lambda age:True if age >= 18 else False
#print(age_check(12))

#-------------Sort method-------------#

#students = ['Sandy', 'Partick', 'Spongebob', 'Mr.Crabs', 'Squidward'] #works only with LISTS

#students.sort(reverse=True)

#for i in students:
    #print(i)

#students = ('Sandy', 'Partick', 'Spongebob', 'Mr.Crabs', 'Squidward') #works for EVERYTHING

#sorted_students = sorted(students)

#for i in sorted(students):
    #print(i)

#students = [('Sandy', 'F', 60),
            #('Partick', 'A', 33),
            #('Spongebob', 'D', 36),
            #('Mr.Crabs', 'B', 20),
            #('Squidward', 'C', 78)]

#grade = lambda grades:grades[1]
#age = lambda age:age[2]
#name = lambda name:name[0]

#students.sort(key=grade)

#for i in students:
#    print(i)

#-------------Map function-------------#

#store = [('shirt', 20.00),('pants', 25.00),('jaket', 50.00),('socks', 10.00)]

#to_euros = lambda data: (data[0], data[1]*0.82)
#to_dollars = lambda data: (data[0], data[1]/0.82)

#store_euros = list(map(to_euros, store)) #--------- Apllies function to a list ----------#
#store_dollars = list(map(to_dollars, store)) #--------- Apllies function to a list ----------#

#for i in store_euros:
#    print(i)

#-------------Filter function-------------#

#friends = [("Rachel", 19),
#("Monica", 18),
#("Phoebe", 17),
#("Joey", 16),
#("Chandler", 21),
#("Ross",20)]

#age = lambda date:date[1] >= 18

#drinking_age = list(filter(age, friends))

#for i in drinking_age:
 #   print(i)

#-------------Filter function-------------#

#letters = ["H", "E","L","L","0"]
#word = functools.reduce (lambda x, y,:x + y,letters)

#print(word)

#factorial = [5,4,3,2,1]
#result = functools.reduce (lambda x, y,:x * y, factorial)
#print(result)

#-------------List comprehention -------------#

#squares = []
#for i in range(1, 11):
#    squares.append(i * i)
#print(squares)

#squares = [i * i for i in range(1,11)]
#print(squares)

#students = [100, 20, 30, 63, 70, 50, 48]

#students_passed = list(filter(lambda x: x >=60, students))
#print(students_passed)

#students_passed = [i for i in students if i >= 60]
#print(students_passed)

#students_passed = [i if i >= 60 else "Failed" for i in students]
#print(students_passed)

#-------------Dictionary comprehention -------------#

#dictionary = (key: expression for (key, value) in iterable}
#dictionary = {key: expression for (key, value) in iterable if conditional]
#dictionary = {key: (if/else) for (key, value) in iterable}
#dictionary = {key: function (value) for (key, value) in iterable]

#----------------------------------------------------#

#cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#cities_in_C = {key: round((value - 32) * (5/9)) for (key,value) in cities_in_F.items()}
#print(cities_in_C)


#weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'storming', 'Chicago': 'sunny'}

#sunny_weather = {key: value for (key,value) in weather.items() if value == 'sunny'}
#print(sunny_weather)

#cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#weather = {key: ('Warm' if value >= 40 else 'Cold') for (key, value) in cities_in_F.items()}
#print(weather)

#cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

#def weather(value):
#    if value >= 40:
#        return 'Warm'
#    else:
#        return 'Cold'

#weather = {key: weather(value) for (key, value) in cities_in_F.items()}
#print(weather)

#-------------Zip function -------------#

#usernames = ["Dude", "Bro", "Mister"]
#passwords = ("p@ssword", "abc123", "guest")
#login_date = ['1/1/2023', '3/12/2048', '31/8/2012']

#users = list(zip(usernames, passwords, login_date))

#print(type(users))

#for i in users:
#   print(i)

#----------------------------------------------------#

#usernames = ["Dude", "Bro", "Mister"]
#passwords = ("p@ssword", "abc123", "guest")

#users = dict(zip(usernames, passwords))

#print(type(users))

#for key, value in users.items(): #.items is required as it's dictionary
#   print(key,value)

#-------------if __name__ == '__main__' -------------#

#if __name__ == '__main__':
#    print('This is a main module')
#else:
#    print('This a other module')

#-------------Time module-------------#

#print(time.ctime(0))

#time_object = time.localtime() # local time
#time_object = time.gmtime() # UTC time
#local_time time.strftime("%B %d %Y %H:%M:%S", time_object)
#print(local_time)
#time_string = "20 April, 2020"
#time_object = time.strptime(time_string, "%d %B, %Y")
#print(time_object)
#(year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
#time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
#time_string = time.asctime (time_tuple)
#print(time_string)

#-------------Treading (like multiprocessing)-------------#

#def eat_breakfast():
#    time.sleep(3)
#    print('Finished to eat breakfast')

#def coffee():
#    time.sleep(5)
#    print('Finished to drink coffee')

#def study():
#    time.sleep(4)
#    print('Finished to study')


#x = threading.Thread(target=eat_breakfast, args='')
#x.start()

#y = threading.Thread(target=coffee, args='')
#y.start()

#z = threading.Thread(target=study, args='')
#z.start()

#x.join()
#y.join()
#z.join()

#print(threading.active_count())
#print(threading.enumerate())
#print(time.perf_counter())

#-------------Treading deamon(like multiprocessing)-------------#

#answer = input('Would you like to quit?: ')


#def timer():
#        if answer == ('yes', 'yeah', 'ok'):
#            breakpoint
#        else:
#            count = 0
#            print()
#            print()
#            while True:
#                time.sleep(1)
#                count += 1
#                print('current time running programm: ', count, 'seconds')
    

#x = threading.Thread(target=timer, daemon=False)
#x.start()

#answer = input('Would you like to quit?: ')

#if answer == ('yes', 'yeah', 'ok'):
    #pass

#-------------Python multiprocessing-------------#

#def counter(num):
#    count = 0 
#    while count < num:
#        count += 1


#def main():
#    print(cpu_count())
#    
#    a = Process(target=counter, args=(500000000, ))
#    b = Process(target=counter, args=(500000000, ))
#
#    b.start()
#    b.join()
#    a.start()
#    a.join()

#    print('finished in: ', time.perf_counter(), 'seconds')

#if __name__ == '__main__':
#    main()

#-------------Tkinter GUI-------------#

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets


#-----------------------#
window = Tk()
window.geometry('420x420')
window.title('Snake_game')
#-----------------------#


#def click(self):
#    print('You subscribed')

#def submit():
#    username = str(entry.get())
#    print('Your password is: ' + username)
#    entry.delete(0,END)
#    entry.config(state=DISABLED)

#def delete():
#    entry.delete(0,END)

#def backspace():
#    entry.delete(len(entry.get())-1, END)
    

icon = PhotoImage(file='he`ll give us what we need but it may not be what we want.png')
window.iconphoto(True, icon)
#window.config(background='black')

#lable = Label(window, text='I love Kanny West', font=('Arial', 40, 'bold'), fg='green', bg='black', relief=RAISED, bd=10, padx=10, pady=10, image=icon, compound='bottom')
#button = Button(window, text='Subscribe!', command=click, activeforeground='green', activebackground='black', state=ACTIVE)

#submit_text = Label(window, text='Enter your password plz=>')

#entry = Entry(window, show='*')

#entry.insert(0, 'Spongbob')

#submit_button = Button(window, text='submit', command=submit)
#delete_button = Button(window, text='delete', command=delete)
#backspace_button = Button(window, text='backspace', command=backspace)

#submit_text.pack(side=LEFT)
#entry.pack(side=LEFT)
#submit_button.pack(side=RIGHT)
#delete_button.pack(side=RIGHT)
#backspace_button.pack(side=RIGHT)


#lable.pack()
#button.pack()
#lable.place(x=0, y=0)

#-------------Tkinter GUI(checkbox)-------------#

#def display():
#    if (x.get()==1):
#        print('You agree!')
#    else:
#        print('You dont agree:(')

#x = IntVar()

#check_button = Checkbutton(window, text='i agree to smth', variable=x, onvalue= 1, offvalue= 0, command=display)

#check_button.pack()

#-------------Tkinter GUI(checkbox)-------------#

food = ["hotdog", "hamburger", "pizza"]

for index in range(len(food)): #Creating radio button for each item in the list
     radio_button = Radiobutton(window, text=food[index])

radio_button.pack()

window.mainloop()




