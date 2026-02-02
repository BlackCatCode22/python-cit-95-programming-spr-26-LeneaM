#Exercise 2: Write a program that uses input to prompt a user for their name
# and then welcomes them.
#Enter your name: Chuck
#Hello Chuck

name = input("What is your name? ")
print('Welcome', name)


#Exercise 3: Write a program to prompt the user for hours and rate per hour to
#compute gross pay.
#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25
#We won’t worry about making sure our pay has exactly two digits after the decimal
#place for now. If you want, you can play with the built-in Python round function
#to properly round the resulting pay to two decimal places.

hour = input('how many hours did you work?')
rate = input('what is your hourly wage?')
gross = (rate*hour)
print(gross)

#Exercise 4: Assume that we execute the following assignment statements:
#width = 17
#height = 12.0
#For each of the following expressions, write the value of the expression and the
#type (of the value of the expression).
#1. width//2     =8 integer
width1 = 17//2
print(width1)


#2. width/2.0      =8.5 float
width2 = 17/2.0
print(width2)

#3. height/3      =4.0 float
height1 = 12/3
print(height1)

#4. 1 + 2 * 5     =42.0 float
answer4 = width1 + width2 * height1
print(answer4)

#Use the Python interpreter to check your answers


#Exercise 5: Write a program which prompts the user for a Celsius temperature,
#convert the temperature to Fahrenheit, and print out the converted temperature.

celsius = input('How many degrees Celsius is it today?')
farenheit = celsius * 1.8 + 32
print(farenheit)