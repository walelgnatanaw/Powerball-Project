
import colorama
from colorama import Fore
colorama.init(autoreset=True)


from power_ball_utiles import lottery_2
#to change the color in LIGHTMAGENTA_EX random numbers from the given self.user_numbers and self.list_numbers)
#sorted numbers lower to higher from the given self.user_numbers and self.list_numbers)
#to change the color in yellow random numbers from the given self.game_powerball and self.user_powerball
class lottery_3(lottery_2):
  def condtion(self, correct_numbers):
            print(f'Result user_numbers:' ,Fore.LIGHTMAGENTA_EX + f"{sorted(self.user_numbers)}",Fore.
                  YELLOW + f'{self.user_powerball}')
            print(f'Result Lucky_numbers:',Fore.LIGHTMAGENTA_EX + f"{sorted(self.list_numbers)}",
                  Fore.YELLOW +f' {self.game_powerball}')
            print(f'You got {self.correct_numbers} white ball',end=" ")
            if self.user_powerball == self.game_powerball:
                print("and the powerball")
            else:
                print("but no powerball")

            if self.user_powerball == self.game_powerball and correct_numbers == 0:
                print("you got 4$")
            elif self.user_powerball == self.game_powerball and correct_numbers == 1:
                print("you got 4$")
            elif self.user_powerball == self.game_powerball and correct_numbers == 2:
                print("you got 7$ ")
            elif self.user_powerball != self.game_powerball and correct_numbers == 3:
                print("you got 7$ ")
            elif self.user_powerball == self.game_powerball and correct_numbers == 3:
                print("you got 100$")
            elif self.user_powerball != self.game_powerball and correct_numbers == 4:
                print("you got 100$ ")
            elif self.user_powerball == self.game_powerball and correct_numbers == 4:
                print("you got 10000$")
            elif self.user_powerball != self.game_powerball and correct_numbers == 5:
                print("you got 1000000$")
            elif self.user_powerball == self.game_powerball and correct_numbers == 5:
                print("you got $324000000")
            else:
                print("Try again ")

#calling class from starter to end and calling function in the above
walelgn = lottery_3()
walelgn.genrerate()
walelgn.atanaw()
walelgn.condtion(walelgn.checked())