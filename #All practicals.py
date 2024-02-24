#All practicals done.
#@Digitron :)

#MODULES
import math
import os

#GLOBAL VARIABLES
spacer = '______________________________________________________'
dict = "1) Calculate final velocity based on initial velocity, acceleration, and time.\n2) Find the total surface area and volume of a cylinder given its radius and height.\n3) Determine if an integer is odd or even.\n4) Check if three given sides can form a triangle and calculate its perimeter and area.\n5) Determine if a given year is a leap year.\n6) Display the sum of natural numbers up to a given number.\n7) Find the factorial of a positive integer.\n8) Display a series of numbers increasing by 3 starting from 1 up to a given number.\n9) Find the sum of digits in a positive integer.\n10) Display numbers within a given range divisible by 3 or 5.\n11) Convert a string to lowercase if it's in uppercase.\n12) Check if concatenating two strings in different orders results in the same string.\n13) Count odd and even numbers in a given list.\n14) Find the sum of all numerical values in a given list.\n15) Modify a list of integers: divide even numbers by 2, multiply odd numbers by 2."

#______________________________________________________________#
def prac1():
	u = float(input("Enter initial velocity : "))
	f = float(input("Enter acceleration : "))
	t = float(input("Enter time period : "))
	v = u + f * t
	print("The final velocity is = ", v) 
def prac2():
	r = float(input("Enter radius : "))
	h = float(input("Enter height : "))
	sa = 2*math.pi*r*(r+h)
	v = math.pi*r**2*h
	print("Surface area of the cylinder = ", sa)
	print("Volume of the cylinder = ", v)
def prac3():
	n = int(input("Enter an integer : "))
	if n % 2 == 0:
		print(n, "is even")
	else:
		print(n, "is odd") 
def prac4():
	a = float(input("Enter 1st side : "))
	b = float(input("Enter 2nd side : "))
	c = float(input("Enter 3rd side : "))
	if a + b > c and b + c > a and c + a > b:
		print("Triangle can be formed")
		p = a + b + c
		s = p / 2
		sa = math.sqrt(s * (s - a) * (s - b) * (s - c))
		print("Perimeter of triangle = ", p)
		print("Surface area of triangle = ", sa)
	else:
		print("Triangle cannot be formed")
def prac5():
	y = int(input("Enter a year : "))
	if y%400==0:
		print(y,"is leap year")
	elif y%100==0:
		print(y,"is not leap year")
	elif y%4==0:
		print(y,"is leap year")
	else:
		print(y,"is not leap year")
def prac6():
	n=int(input("Enter a number : "))
	a = []
	for i in range(1, n+1):
		a.append(i)
	print(f"Sum of first {n} natural numbers is : {sum(a)}")
def prac7():
	n=int(input("Your number : "))
	f = 1
	for i in range(1, n+1):
		f=f*i
	print(f"The factorial of {n} is {f}")
def prac8():
	#Input a positive integer and display all the series: 1, 4, 7, 10, ….., n.abs
	num = int(input("Enter a positive integer : "))
	for i in range(1, num+1, 3):
		print(f"The AP is : {i}")
def prac9():
	#input a positive integer and find the sum of all its digits.
	num = int(input("Enter a positive integer : "))
	digit_sum = 0
	while num>0:
		digit = num % 10
		digit_sum += digit
		num //= 10
	print("The sum of all the digits is :", digit_sum)
def prac10():

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
def prac11():
	s=str(input("Your string : "))
	if s.islower():
		print(f"{s} : lowercase")
	else:
		print(f"{s.lower()} : converted to lowercase")
def prac12():
	s1=str(input("String 1 : ")); s2=str(input("String 2 : "))
	if s1+s2==s2+s1:
		print("Same")
	else:
		print("Different")
def prac13():
	arr = eval(input("Your list : "))
	odd = even = 0
	for i in arr:
		if i % 2 == 0:
			even = even+1
		else:
			odd=odd+1
	print(f"Number of odd : {odd}\nNumber of even : {even}")
def prac14():
	arr=eval(input("Your list : "))
	print(f"The sum of the list {arr} is : {sum(arr)}")
def prac15():
	arr = eval(input("Your list : "))
	for i in range(0, len(arr)):
		if arr[i]%2==0:
			arr[i]=arr[i]/2
		else:
			arr[i]=arr[i]*2
	print(f"Modified : {arr}")

#______________________________________________________________#

while True:
	print(f"{spacer}\n\n\n{dict}\n\n")
	scriptRunner = int(input(f"{spacer}\n\n\nSerial number of practical to run : "))
	if scriptRunner ==  1:
		os.system('cls')
		print("\n\nNow running : V=U/T.")
		prac1()
	elif scriptRunner == 2:
		os.system('cls')
		print("\n\nNow running : Cylinder=> Surface area, Volume.")
		prac2()
	elif scriptRunner == 3:
		os.system('cls')
		print("\n\nNow running : Odd/Even.")
		prac3()
	elif scriptRunner == 4:
		os.system('cls')
		print("\n\nNow running : 3 Sides = Triangle or not.")
		prac4()
	elif scriptRunner == 5:
		os.system('cls')
		print("\n\nNow running : Leap year or not.")
		prac5()
	elif scriptRunner == 6:
		os.system('cls')
		print("\n\nNow running : Sum of all numbers till n.")
		prac6()
	elif scriptRunner == 7:
		os.system('cls')
		print("\n\nNow running : Factorial.")
		prac7()
	elif scriptRunner == 8:
		os.system('cls')
		print("\n\nNow running : AP/Series.")
		prac8()
	elif scriptRunner == 9:
		os.system('cls')
		print("\n\nNow running : Sum of all its digits.")
		prac9()
	elif scriptRunner == 10:
		os.system('cls')
		print("\n\nNow running : Divisible by 3,5.")
		prac10()
	elif scriptRunner == 11:
		os.system('cls')
		print("\n\nNow running : uppercase/lowercase.")
		prac11()
	elif scriptRunner == 12:
		os.system('cls')
		print("\n\nNow running : s1+s2=s2+s1.")
		prac12()
	elif scriptRunner == 13:
		os.system('cls')
		print("\n\nNow running : Number of odd and even numbers [].")
		prac13()
	elif scriptRunner == 14:
		os.system('cls')
		print("\n\nNow running : sum of a list's elements.")
		prac14()
	elif scriptRunner == 15:
		os.system('cls')
		print("\n\nNow running : If odd => *2. If even => /2.")
		prac15()