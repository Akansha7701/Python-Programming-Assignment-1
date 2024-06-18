''''
# QUESTION - 1

x = input("Enter first value : ")
y = input("Enter second value : ")
sum = int(x) + int(y)
print(sum)

# QUESTION - 2

n = int(input("Enter the value of n : "))
if (n % 2) == 0:
 print("This is even number")
else: 
 print("This is odd number")

 # QUESTION - 3

import math
n= int(input("Enter the value of n : "))
fact = math.factorial(n)
print(fact)

# QUESTION - 4

n= (input("Enter name : "))
print("Good Morning")

# QUESTION - 5



# QUESTION - 6


# QUESTION - 7

str = "Welcome to the world of coding"
print("The length of the string is : ", len(str))

# QUESTION - 8

str1 = "Hello "
str2 = "My name is Harry Potter"
print(str1 + str2)

# QUESTION - 9

str1 = "You are the last hope"
print(str1.find('hope'))

# QUESTION - 10

str1 = "namaste duniya"
print(str1.upper())

# QUESTION - 11

num = 10
num1 = 0
num2 = 1
print(num1)
print(num2)
for i in range(2, num):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3)

# QUESTION - 12

num1 = 5
num2 = 7
sum = num1 + num2
print("The sum is : ", sum)

# QUESTION - 13

n = int(input("Enter your birth year : "))
birthyear = n
currentyear = 2024
age = currentyear - birthyear
print(age)

# QUESTION - 14



# QUESTION - 15




# QUESTION - 16

word = input("enter the character : ")
str1 = 'h', 'e', 'l', 'l', 'o'
for i in range(0, (len(str1) - 1)):
 print(word.count(str1[i]))

# QUESTION - 17

str1 = "namaste duniya"
print(str1.capitalize())

# QUESTION - 18

str1 = "Batman"
str2 = "Superman"
if str1 == str2:
    print("strings are anagrams")
else: 
    print("two strings are not anagrams")

# QUESTION - 19

import string
str1 = "Hello! How are you? I am fine."
new_string = ""
for char in str1:
    if char not in string.punctuation:
         new_string += char
print("The string after removing punctuation is : ", new_string)         

# QUESTION - 20

list1 = [1,2,3,4,5]
sum = 0
for i in list1:
    sum = sum + i
print("The sum of the numbers given in the list is : ", sum)

# QUESTION - 21

list1 = [5,3,2,5,3,8,9,3,2,1]
res = list1.count(3)
print(res)

# QUESTION - 22

list1 = [52,45,75,87,99,24,36]
res = max(list1)
print("Max number in the list is : ", res)
res = min(list1)
print("Min number in the list is : ", res)

# QUESTION - 23

temp = int(input("Enter the temperature : "))
fahrenhiet = (1.8 * temp) + 32
celsius = (temp - 32) * 5/9
print("Temperature in fahrenhiet is : ", fahrenhiet)
print("Temperature in celsius is : ", celsius)

# QUESTION - 24

# Basic Calculations
# Calculator Program in Python by using input() and format() functions

#Promting input from the user

n1 = float(input("Enter the First Number: "))
n2 = float(input("Enter the Second Number: "))

#addition

print("{} + {} = ".format(n1, n2))
print(n1 + n2)

#subtraction

print("{} - {} = ".format(n1, n2))
print(n1 - n2)

#multiplication

print("{} * {} = ".format(n1, n2))
print(n1 * n2)

#division

print("{} / {} = ".format(n1, n2))
print(n1 / n2)

# QUESTION - 25



# QUESTION - 26

str1 = "hello welcome all"
print(str1.startswith("hello"))
print(str1.endswith("welcome"))

# QUESTION - 27

str1 = "hello welcome all"
new_list = list(str1)
print(new_list)
'''           
   


