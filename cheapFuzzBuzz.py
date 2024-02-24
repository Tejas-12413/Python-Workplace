import math
from time import sleep
import os

def divisible_by_5():
      userN1=int(input("Number 1 : ")); userN2=int(input("Number 2 : "))
      if userN1 >= userN2:
          n1=userN2; n2=userN1
      elif userN2>userN1:
          n1=userN1; n2=userN2
      for i in range(n1, n2+1):
          if i % 3 == 0:
              print(f'{i} Divisible by 3')
          elif i % 5 == 0:
              print(f'{i} Divisible by 5')

def factorial():
      n=int(input("Your number : "))
      f = 1
      for i in range(1, n+1):
            f=f*i
      print(f"The factorial of {n} is {f}")

def oddOrEvenList():
      a=eval(input("Your list : "))
      o=e=0
      for i in range(len(a)):
            if a[i] % 2 == 0:
                  print(f"{a[i]} is even.")
                  e=e+1
            elif a[i] % 2 != 0:
                  print(f"{a[i]} is odd.")
                  o=o+1
      print(f"(Odd, Even) : ({o}, {e})")

def circleArea():
      pi = math.pi
      r=eval(input("Radius of circle : "))
      area = round(pi*r*r, 2)
      circumferance = round(2*pi*r, 2)
      print(f"Area of the circle with radius {r} units is : {area} units\nCircumferance of the circle with radius {r} units is : {circumferance} units")
      
#---------------------------------------------------------------------------------------------------------------------#
      
functionChoices = ['DivisibleBy5', 'Factorial', 'OddOrEvenList', 'CircleArea']
userChoice = int(input("{}\nYour Choice : ".format(functionChoices)))

if userChoice == 1:
      os.system('cls')
      sleep(0.5)
      divisible_by_5()
elif userChoice == 2:
      os.system('cls')
      sleep(0.5)
      factorial()
elif userChoice == 3:
      os.system('cls')
      sleep(0.5)
      oddOrEvenList()      
elif userChoice == 4:
      os.system('cls')
      sleep(0.5)
      circleArea()      
