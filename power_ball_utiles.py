import random
from random import randint

#create variable in list ,function and class
class lottery():
     def __init__(self):
         self.user_numbers = []
         self.user_powerball = []
 #enter five numbers in the list we want a choice numbers between 1 upto 20 to append inside self.user_numbers = []
 # only five numbers generate in user _numbers

     def genrerate(self):

         for num in range(0, 5):
             user_num = random.randint(1,20)
             self.user_numbers.append(user_num)

 ##enter a number in the list what we choose between 0 upto 10 to append self.user_powerball = []

         ball = random.randint(1,10)
         self.user_powerball.append(ball)

 #When you initialize a child class in Python, you can call the super().__init__() method.
 # This initializes the parent class object into the child class.
class lottery_1(lottery):
     def __init__(self):
         super().__init__()
         self.list_numbers = []
         self.game_powerball = []

 # enter a number in the list what we choose between 0 up to 10 to append self.game_powerball = []
     def atanaw(self):
         for num in range(0, 5):
             user_num = randint(1, 20)
             self.list_numbers.append(user_num)
         pball = randint(1, 10)
         self.game_powerball.append(pball)
class lottery_2(lottery_1):
 #to select common numbers from self.user_numbers and self.list_numbers after that print what we have self.correct_numbers
     def checked(self):
         self.correct_numbers = len(set(self.user_numbers).intersection(set(self.list_numbers)))
         return self.correct_numbers