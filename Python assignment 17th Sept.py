#!/usr/bin/env python
# coding: utf-8

# For Loop :-

# 1 Write a Python program to print numbers from 1 to 10 using a for loop.

# In[4]:


for i in range(1,11):
    print(i)


# In[ ]:





# Explain the difference between a for loop and a while loop in Python.

# #For Loop
# """in my opinion a 'for' loop is used to repeat a  block of code number of  times.
# example:for i in range(1,11):
#             print(i)
# """
# #While loop
# """in my opinion 'While' Loop is used to execute a block of statements repeatedly until a given condition is satisfied.
# example:
# count=5
# while (count>0):
#     print(count)
#     count=count-1
# """

# In[ ]:





# Write a Python program to calculate the sum of all numbers from 1 to 100 using a for loop.

# In[53]:


sum=0
for i in range(1,101):
    sum=sum+i
print(sum)


# In[ ]:





# How do you iterate through a list using a for loop in Python?

# In[7]:


list=[1,2,3,4,5]
for i in list:
    print(i)


# In[ ]:





# Write a Python program to find the product of all elements in a list using a for loop.

# In[54]:


l=[1,2,3,4,5,6,7,8,9]
product=1
for i in l:
    product*=i
print(product)
    


# In[ ]:





# Create a Python program that prints all even numbers from 1 to 20 using a for loop.

# In[21]:


for i in range(1,21):
    if i%2==0:
        print(i)


# In[ ]:





# Write a Python program that calculates the factorial of a number using a for loop.

# In[38]:


n=int(input("Enter the number for factorial :"))
if n==0 or n==1:
    print(1)
else:
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    print(factorial)
    


# In[ ]:





# How can you iterate through the characters of a string using a for loop in Python?

# In[43]:


str=("a","b","c","d")
for i in str:
    print(i)


# In[ ]:





# Write a Python program to find the largest number in a list using a for loop.

# In[51]:


alist = [3, 10, 90, 5, -2, 4, 18, 45, 100, 1, 6]

largest = alist[0]

for element in alist:
    if element > largest:
        largest = element

print( largest)


# In[ ]:





# Create a Python program that prints the Fibonacci sequence up to a specified limit using a for loop.

# In[52]:


limit = int(input("Enter the limit for the Fibonacci sequence: "))

if limit < 2:
    print("Invalid limit. Please enter a limit of 2 or greater.")
else:
    a, b = 0, 1
    
    print(a, end=", ")
    print(b, end=", ")
    
    for i in range(2, limit):
        c = a + b
        print(c, end=", ")
        
        a, b = b, c


# In[ ]:





# Write a Python program to count the number of vowels in a given string using a for loop.

# In[69]:


string=("My name is abdullah khan")
vowels=("a","e","i","o","u")
vowels_count=0
for char in string:
    if char in vowels:
        vowels_count+=1
print(vowels_count)
    


# In[ ]:





# Create a Python program that generates a multiplication table for a given number using a for loop.

# In[72]:


num=int(input("Enter the number for multiplication :"))
for i in range(1,11):
    print(num,"X",i,"=",num*i)


# In[ ]:





# Write a Python program to reverse a list using a for loop.

# In[2]:


original_list = ["sudh","pwskills"]

original_list = list(original_list)

reversed_list = []

for i in range(len(original_list) - 1, -1, -1):
    reversed_list.append(original_list[i])

print("Reversed list:", reversed_list)


# In[ ]:





# Write a Python program to find the common elements between two lists using a for loop.

# In[4]:


list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
result=[]
for element in list1:
    if element in list2:
        result.append(element)
print(result)


# In[ ]:





# Explain how to use a for loop to iterate through the keys and values of a dictionary in Python.

# In[22]:


dict1={"name":"Abdullah","roll no":12345,"city":"Lahore"}
for key,value in dict1.items():
    print(f"key : {key} , Value : {value}")


# In[ ]:





# Write a Python program to find the GCD (Greatest Common Divisor) of two numbers using a for loop.

# In[25]:


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")


# In[ ]:





# Create a Python program that checks if a string is a palindrome using a for loop.

# In[1]:


word = input("Enter a word: ")
word = word.lower()

length_word = len(word)

correct_matches = 0
for index in range(len(word)):
    if word[index] == word[-1-index]:
        correct_matches += 1
if correct_matches == length_word:
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")


# In[ ]:





# Write a Python program to remove duplicates from a list using a for loop.

# In[3]:


input_list = [1, 2, 2, 3, 4, 4, 5]

unique_list = []
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)

input_list[:] = unique_list

print(input_list)


# In[ ]:





# Create a Python program that counts the number of words in a sentence using a for loop.

# In[5]:


sentence="my name is abdullah"
word_count=0
for word in sentence:
    word_count+=1
print("total words in sentence :",word_count)


# In[ ]:





# Write a Python program to find the sum of all odd numbers from 1 to 50 using a for loop.

# In[10]:


sum_odd=0
for char in range(1,50):
    if char%2!=0:
        print(char)
        sum_odd+=char
        
        
print("the sum of odd_numbers is",sum_odd)


# In[ ]:





# Write a Python program that checks if a given year is a leap year using a for loop

# In[12]:


year = int(input("Enter a year: "))
is_leap = False
for i in range(4, year + 1, 4):
    if i == year:
        is_leap = True
        break

if is_leap:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


# In[ ]:





# Create a Python program that calculates the square root of a number using a for loop.

# In[14]:


number = float(input("Enter a number: "))
guess = number / 2

num_iterations = 10

for _ in range(num_iterations):
    guess = 0.5 * (guess + (number / guess))

# Print the square root
print("The square root of", number, "is approximately", guess)


# In[ ]:





# Write a Python program to find the LCM (Least Common Multiple) of two numbers using a for loop.

# In[ ]:


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result_lcm = lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is", result_lcm)


# In[ ]:





# if else:

# Write a Python program to check if a number is positive, negative, or zero using an if-else statement.

# In[36]:


num=int(input("Enter the number :"))
if num==0:
    print(f"Number is {num} ")
elif num>0:
    print(f"{num} is Positve")
else:
    print(f"{num} is Negative")


# In[ ]:





# Create a Python program that checks if a given number is even or odd using an if-else statement.

# In[39]:


num=int(input("Enter the number :"))
if num%2==0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")


# In[ ]:





# How can you use nested if-else statements in Python, and provide an example?

# In[48]:


year=int(input("Enter a year :"))
if year%4==0:
    if year%400==0:
        print("Leap year")
    else:
        print("Leap year") 
else:
    print("Not leap year")


# In[ ]:





# Write a Python program to determine the largest of three numbers using if-else.

# In[58]:


n1=int(input("Enter the first number :"))
n2=int(input('Enter the second number :'))
n3=int(input('Enter the third number :'))
if n1>n2 and n1>n3:
    print(f"{n1} is largest")
elif n2>n1 and n2>n3:
    print(f"{n2} is largest")
else:
    print(f"{n3} is largest")


# In[ ]:





# Write a Python program that calculates the absolute value of a number using if-else.

# In[69]:


num = float(input("Enter a number: "))

if num < 0:
    absolute_value = -num
else:
    absolute_value = num

print("The absolute value of", num, "is", absolute_value)


# In[ ]:





# Create a Python program that checks if a given character is a vowel or consonant using if-else.

# In[7]:


char=input("Enter a single character :")
vowels=("a,e,i,o,u,A,E,I,O,U")
if char in vowels:
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")


# In[ ]:





# Write a Python program to determine if a user is eligible to vote based on their age using if-else.

# In[9]:


age=int(input("Enter your age :"))
if age>=18:
    print("You can cast your vote")
else:
    print("You can not cast your vote")


# In[ ]:





# Create a Python program that calculates the discount amount based on the purchase amount using if-else.

# In[11]:


purchase_amount = float(input("Enter the purchase amount: "))

discount_rate = 0.0

if purchase_amount < 100:
    discount_rate = 0.0  
elif purchase_amount < 500:
    discount_rate = 0.05  
elif purchase_amount < 1000:
    discount_rate = 0.1   
else:
    discount_rate = 0.15  

discounted_price = purchase_amount - (purchase_amount * discount_rate)

print(f"Original Price: ${purchase_amount:.2f}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Discounted Price: ${discounted_price:.2f}")


# In[ ]:





# Write a Python program to check if a number is within a specified range using if-else.

# In[16]:


num=int(input("Enter the number :"))
if num>=1 and num<=100:
    print(f"{num} is in range")
else:
    print(f"{num} is not in range")


# In[ ]:





# Create a Python program that determines the grade of a student based on their score using if-else.

# In[17]:


score=int(input("Enter the Numbers :"))
if score>=90:
    print(" You Got 'A+' Grades")
elif score>=80:
    print("You Got 'A' Grade")
elif score>=70:
    print("You Got 'B' Grade")
elif score>=60:
    print("You Got 'C' Grade")
elif score>=50:
    print("You Got 'D' Grade")
else:
    print("Fail")


# In[ ]:





# Write a Python program to check if a string is empty or not using if-else.

# In[21]:


str=("aaaa")
if str=="":
    print("The string is empty")
else:
    print("the string is not empty")


# In[ ]:





# Create a Python program that identifies the type of a triangle (e.g., equilateral, isosceles, or scalene) based on input values using if-else.

# In[22]:


side1=float(input("Enter the lenght :"))
side2=float(input("Enter the lenght :"))
side3=float(input("Enter the lenght :"))
if (side1+side2>side3) and (side1+side3>side2) and (side2+side3>side1):
    if side1==side2==side3:
        print("Equilibrium triangle")
    elif side1==side2 or side2==side3 or side1==side3:
        print("isisceles triangle")
    else:
        print("Scalene Triangle")
else:
    print("You entered the wrong lenght")


# In[ ]:





# Write a Python program to determine the day of the week based on a user-provided number using if-else.

# In[23]:


num=int(input("Enter the single number b/w (1--7) :"))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("invalid input")


# In[ ]:





# How do you use the "assert" statement in Python to add debugging checks within if-else blocks?

# In[26]:


"""In Python, the assert statement is often used for debugging purposes to add checks within your code and ensure that certain conditions are met."""
x = 10
if x >= 0:
    print("x is positive")
else:
    assert False, "x is not positive" 

print("Program continues running...")


# In[ ]:





# Create a Python program that determines the eligibility of a person for a senior citizen discount based on age using if-else.

# In[29]:


age=int(input("Enter your age :"))
if age>=50:
    print("You are eligible for Discounts")
elif age<50:
    print("You are not eligible for discounts")
else:
    print("invalid input!")


# In[ ]:





# Write a Python program to categorize a given character as uppercase, lowercase, or neither using if-else.

# In[5]:


given=input("Enter a single character :")
special_characters=("!","@","#","$","%","^","&","*")
if len(given)==1:
    if given.isupper():
        print("Upper case character")
    elif given.islower():
        print("Lower case character")
    elif given in special_characters:
        print(" Special case character")
    else:
        print("invalid input")
else:
    print("invalid input")


# In[ ]:





# Write a Python program to determine the roots of a quadratic equation using if-else.

# In[ ]:


a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + (discriminant)**0.5) / (2*a)
    root2 = (-b - (discriminant)**0.5) / (2*a)
    print(f"Two distinct real roots: {root1} and {root2}")
elif discriminant == 0:
    root1 = -b / (2*a)
    print(f"One real root (repeated): {root1}")
else:
    realPart = -b / (2*a)
    imaginaryPart = ((-discriminant)**0.5) / (2*a)
    print(f"Complex roots: {realPart} + {imaginaryPart}i and {realPart} - {imaginaryPart}i")


# In[ ]:





# Create a Python program that checks if a given year is a century year or not using if-else.

# In[6]:


year=int(input("Enter the Year :"))
if year%100==0:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")


# In[ ]:





# Write a Python program to determine if a given number is a perfect square using if-else.

# In[1]:


import math
number=int(input("Enter the number :"))
sqrt=math.sqrt(number)
if sqrt.is_integer():
    print(f"{number} is a perfect square")
else:
    print(f"{number} is not a perfect square")


# In[ ]:





# Explain the purpose of the "continue" and "break" statements within if-else loops.

# In[11]:


#Break
a="BREAK"
print(a.center(50))
print("Break statements are used to stop the code at perticular point ")
for i in range(1,11):
    if i==6:
        break
    print(i)
    
#Continue
b="CONTINUE"
print(b.center(50))
print("continue statements are used to perform a task at particular point and then continue the code.")
for i in range(1,11):
    if i==6:
        print("hello")
        continue
    print(i)
    


# In[ ]:





# Create a Python program that calculates the BMI (Body Mass Index) of a person based on their weight and height using if-else.

# In[16]:


height=float(input("Enter the height in meters:"))
weight=float(input("Enter your weight in kg :"))
BMI=weight/height**2
print(f"your BMI is {BMI}")
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 24.9:
    print("Your weight is normal.")
elif 25 <= BMI < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")


# In[ ]:





# How can you use the "filter()" function with if-else statements to filter elements from a list?

# In[19]:


number=[1,2,3,4,5,6,7,8,9]
filtered_number=[]
for x in number:
    if x%2==0:
        filtered_number.append(x)
print(filtered_number)


# In[ ]:





# Write a Python program to determine if a given number is prime or not using if-else.

# In[24]:


number=int(input("Enter the number :"))
if number==2:
    print(f"{number} is a prime number")
elif number%2!=0:
    print(f"{number} is a Prime number")
else:
    print(f"{number} is Not Prime number")


# In[ ]:





# Map :-

# Explain the purpose of the `map()` function in Python and provide an example of how it can be used to apply a function to each element of an iterable.

# In[25]:


print("""Map function applies a function to each element in a sequence and
return a new sequence containing the transformed element""")
l=[1,2,3,4,5,6,7,8,9]
cube=list(map(lambda x:x*2,l))
print(cube)


# In[ ]:





# Write a Python program that uses the `map()` function to square each element of a list of numbers.

# In[26]:


l=[1,2,3,4,5,6,7,8,9]
square=list(map(lambda x:x*x,l))
print(square)


# In[ ]:





# How does the `map()` function differ from a list comprehension in Python, and when would you choose one over the other?

# In[ ]:


print("""in my opinion the 'Map' function is more easy for beginners than the list comprehension in python.
Map function is more easy to under stand and also easy to use in code. """)
# MAP syntax
result = map(function, iterable)
#LIst comprihension Syntax:
new_list = [expression for item in iterable if condition]

print("""Use map() when you want to apply a function to each element of one or more iterables and prefer lazy evaluation.
Use list comprehensions when you want to create
a new list by applying an expression or transformation to each element, optionally with filtering, and when readability and
concise syntax are important.""")


# In[ ]:





# Create a Python program that uses the `map()` function to convert a list of names to uppercase.

# In[27]:


names=["abdullah","khan","pw skills"]
names_upper=list(map(lambda x:x.upper(),names))
print(names_upper)


# In[ ]:





# Write a Python program that uses the `map()` function to calculate the length of each word in a list of strings.

# In[32]:


string=["abdullah","khan","pw skills"]
string_len=map(lambda x:len(x),string)
print(list(string_len))


# In[ ]:





# How can you use the `map()` function to apply a custom function to elements of multiple lists simultaneously in Python?

# In[37]:


list1=[1,2,3,4]
list2=[5,6,7,8]
def add_list_elementwise(x,y):
    return x+y
result=list(map(add_list_elementwise,list1,list2))
print(result)


# Create a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit.

# In[33]:


list_temp=[23,45,65,34,21]
list_fahr=list(map(lambda x:(x*9/5)+32,list_temp))
print(list_fahr)


# In[ ]:





# Write a Python program that uses the `map()` function to round each element of a list of floating-point numbers to the nearest integer.

# In[36]:


f_num=[23.222,12.998,34.234,67.987]
r_list=list(map(lambda x:round(x),f_num))
print(r_list)


# In[ ]:





# Reduce :-

# What is the `reduce()` function in Python, and what module should you import to use it? Provide an example of its basic usage.

# In[39]:


print("""The reduce function is a higher-order function that applies a function to a sequence and returns a single value.""")
from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9]
sum=reduce(lambda x,y:x+y,numbers)
print(sum)


# In[ ]:





# Write a Python program that uses the `reduce()` function to find the product of all elements in a list.

# In[40]:


numbers=[1,2,3,4,5,6,7,8,9]
sum=reduce(lambda x,y:x+y,numbers)
print(sum)


# In[ ]:





# Create a Python program that uses `reduce()` to find the maximum element in a list of numbers.

# In[3]:


from functools import reduce
numbers=[10,20,30,40,50,60,70,80,90,100]
def find_max(x,y):
    return x if x>y else y
maximum=reduce(find_max,numbers)
print(maximum)


# In[ ]:





# How can you use the `reduce()` function to concatenate a list of strings into a single string?

# In[7]:


string=("my","name","is","abdullah")
s_string=reduce(lambda x,y:x+" "+y,string)
print(s_string)


# In[ ]:





# Write a Python program that calculates the factorial of a number using the `reduce()` function.

# In[17]:


from functools import reduce
def factorial(x,y):
    return x*y
number=int(input("Enter the number :"))
if number<0:
    print("negative number")
elif number==0:
    print("the factorial of 0 is 1")
else:
    result=reduce(factorial,range(1,number+1))
    print(f"Factorial of {number} is {result}")


# In[ ]:





# Create a Python program that uses `reduce()` to find the GCD (Greatest Common Divisor) of a list of numbers.

# In[22]:


from functools import reduce
import math
number=[12,18,24,30,36]
def find_gcd(x,y):
    return math.gcd(x,y)
gcd=reduce(find_gcd,number)
print("The Geatest Common Divisor of numbers is",gcd)


# In[ ]:





# Write a Python program that uses the `reduce()` function to find the sum of the digits of a given number.

# In[32]:


number=input("Enter the number :")
sum=reduce(lambda x,y:int(x)+int(y),number)
print("The sum of digits of number is",sum)


# In[ ]:





# Filter :-

# Explain the purpose of the `filter()` function in Python and provide an example of how it can be used to filter elements from an iterable

# In[33]:


print("""The filter function filters a sequence of elements based on a given predicate
(a function that returns a boolean value) and
returns a new sequence containing only the elements that meet the predicate""")
numbers=[1,2,3,4,5,6,7,8,9]
even_list=list(filter(lambda x:x%2==0,numbers))
print(even_list)


# In[ ]:





# Write a Python program that uses the `filter()` function to select even numbers from a list of integers.

# In[34]:


numbers=[1,2,3,4,5,6,7,8,9]
even_list=list(filter(lambda x:x%2==0,numbers))
print("the even numbers from the list are",even_list)


# In[ ]:





# Create a Python program that uses the `filter()` function to select names that start with a specific letter from a list of strings.

# In[39]:


str_list=["abdullah","afghanistan","italy","india"]
name=list(filter(lambda x:x[0]=="a",str_list))
print(name)


# In[ ]:





# Write a Python program that uses the `filter()` function to select prime numbers from a list of integers.

# In[50]:


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(is_prime, numbers))
print("Prime numbers in the list are:", prime_numbers)


# In[ ]:





# How can you use the `filter()` function to remove None values from a list in Python?

# In[3]:


test_list=[1,None,2,None,3,None,4,5]
result=list(filter(lambda x:x is not None,test_list))
print(result)


# In[ ]:





# Create a Python program that uses `filter()` to select words longer than a certain length from a list of strings.

# In[16]:


list_of_strings = ["Hello, this is a sample sentence.", "Python programming is fun.", "Filter words by length."]
def filter_words_by_length(words, length):
    return list(filter(lambda word: len(word) > length, words))
min_length = 5
filtered_words = list(map(lambda string: filter_words_by_length(string.split(), min_length), list_of_strings))
for i, filtered_list in enumerate(filtered_words):
    print(f"Words longer than {min_length} characters in string {i + 1}: {filtered_list}")


# In[ ]:





# Write a Python program that uses the `filter()` function to select elements greater than a specified threshold from a list of values.

# In[18]:


values=[10,20,30,40,50,60,70,80,90]
threshold=50
result=list(filter(lambda x:x>threshold,values))
print(result)


# In[ ]:





# RECURSION:

# Explain the concept of recursion in Python. How does it differ from iteration?

# In[ ]:


#Recursion in Python
"""Recursion is a programming technique where a function calls itself in order to solve a problem.
In Python, a recursive function is a function thatperforms a task in part and delegates the remaining
task to a call of itself."""
#example
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
#Iterarion in Python
"""Iteration is a programming construct that involves a 
loop to repeatedly execute a set of instructions until a specific condition is met."""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
#in my opinion recursion is much easier and understandable


# In[ ]:





# Write a Python program to calculate the factorial of a number using recursion.

# In[20]:


n=int(input("Enter the Number :"))
def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))


# In[ ]:





# Create a recursive Python function to find the nth Fibonacci number.

# In[2]:


n=int(input("Enter the number :"))
def fibunacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return fibunacci(0)+fibunacci(1)
    else:
        return fibunacci(n-1)+fibunacci(n-1)
print(fibunacci(n))


# In[ ]:





# Write a recursive Python function to calculate the sum of all elements in a list.

# In[5]:


numbers=[1,2,3,4,5,6,7,8]
def recursive_sum(numbers):
    return sum(numbers)
print(recursive_sum(numbers))


# In[ ]:





# How can you prevent a recursive function from running indefinitely, causing a stack overflow error?

# In[7]:


"""
To prevent a recursive function from running indefinitely and causing a stack overflow error,
you need to ensure that your recursive function has a well-defined termination condition, often referred to as a "base case."
The base case is the condition under which the recursion stops and the function returns a result.
"""
n=int(input("Enter the number :"))
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(n))


# In[ ]:





# Create a recursive Python function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

# In[9]:


def gcd_euclidean(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclidean(b, a % b)
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
result = gcd_euclidean(num1, num2)
print(f"GCD of {num1} and {num2} is {result}")


# In[ ]:





# Write a recursive Python function to reverse a string.

# In[10]:


string=("my name is abdullah")
def reverse_str(string):
    return string[::-1]
print(reverse_str(string))


# In[ ]:





# Create a recursive Python function to calculate the power of a number (x^n).

# In[11]:


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
base = 2
exponent = 5
result = power(base, exponent)
print(f"{base}^{exponent} =", result)


# In[ ]:





# Write a recursive Python function to find all permutations of a given string.

# In[12]:


def find_permutations(string, start=0):
    if start == len(string) - 1:
        yield string
    else:
        for i in range(start, len(string)):
            string_list = list(string)
            string_list[start], string_list[i] = string_list[i], string_list[start]
            new_string = ''.join(string_list)

            for perm in find_permutations(new_string, start + 1):
                yield perm

input_string = "abc"
permutations = list(find_permutations(input_string))

for perm in permutations:
    print(perm)


# In[ ]:





# Write a recursive Python function to check if a string is a palindrome.

# In[16]:


string=input("Enter the string :")
def check_palindrome(string):
    if string==string[::-1]:
        return "The string is Palindrome"
    else:
        return "The string is not Palindrome"
print(check_palindrome(string))


# In[ ]:





# Create a recursive Python function to generate all possible combinations of a list of elements.

# In[21]:


def generate_combinations(elements, k):
    if k == 0:
        yield []
    elif elements:
        first, rest = elements[0], elements[1:]
        for combo in generate_combinations(rest, k - 1):
            yield [first] + combo
        for combo in generate_combinations(rest, k):
            yield combo

my_list = [1, 2, 3]
k = 2

combinations = list(generate_combinations(my_list, k))
for combo in combinations:
    print(combo)


# In[ ]:





# Basics of Functions:

# What is a function in Python, and why is it used?
# 
# function:
# 
#     Basically a function is a lines of code to perform a specific task and it is easy to use in multiple times.Once we
#     write a code then we can use it many times it depends on us how many can we use it.It helps the programer and save 
#     his time also.

# In[ ]:





# How do you define a function in Python? Provide an example.

# In[2]:


#Function
print("In python we can define a function by 'def '.")
#example
n=int(input("Enter the number :"))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))


# In[ ]:





# Explain the difference between a function definition and a function call.

# """Function Definition: Specifies what a function does, its name, parameters, and return value. It defines the function's behavior.
# 
# 
# Function Call: Executes a function with provided arguments. It invokes the function to perform a specific task and may return a result.
# """

# In[ ]:





# Write a Python program that defines a function to calculate the sum of two numbers and then calls the function.

# In[4]:


a=int(input("Enter the First number :"))
b=int(input("Enter the Second Number"))
def add_sum(a,b):
    return a+b
print(add_sum(a,b))


# In[ ]:





# What is a function signature, and what information does it typically include?

# """A function signature is a specific part of a function declaration or definition that provides
# essential information about the function's name, parameters, and return type.
# It serves as a concise summary of how the function can be used and what it expects."""
# 
# "Example"
# def add_num(a,b):

# In[ ]:





# Create a Python function that takes two arguments and returns their product.

# In[5]:


a=int(input("Enter the First number :"))
b=int(input("Enter the Second Number"))
def add_sum(a,b):
    return a*b
print(add_sum(a,b))


# In[ ]:





# Function Parameters and Arguments:

# In[ ]:





# Explain the concepts of formal parameters and actual arguments in Python functions.

# Formal Parameters: These are variables declared in a function's definition, representing the values the function expects to receive when called.
# 
# Actual Arguments: These are the actual values or expressions provided when calling a function, which fill in the formal parameters within the function's code.

# In[ ]:





# Write a Python program that defines a function with default argument values.

# In[6]:


def add_num(a=9,b=10):
    return a+b
print(add_num())


# In[ ]:





# How do you use keyword arguments in Python function calls? Provide an example.

# In[9]:


"""
In Python, you can use keyword arguments in function calls by specifying the parameter names 
and their corresponding values explicitly. This allows you to pass arguments out of order and
makes your code more readable and self-explanatory"""
def add_num(a,b):
    return a+b
print(add_num(a=9,b=10))


# In[ ]:





# Create a Python function that accepts a variable number of arguments and calculates their su

# In[16]:


def calculate_sum(*args):
    total=0
    for num in args:
        total+=num
    return total
result=calculate_sum(12,23,34,45)
print(result)


# In[ ]:





# What is the purpose of the `*args` and `**kwargs` syntax in function parameter lists?

# The *args syntax in a function parameter list allows the function to accept a variable number of positional arguments, which are collected into a tuple named args. It provides flexibility for functions with an arbitrary number of arguments.
# 
# The **kwargs syntax in a function parameter list allows the function to accept a variable number of keyword arguments (key-value pairs), which are collected into a dictionary named kwargs. It provides flexibility for functions with an arbitrary set of named parameters.

# In[ ]:





# Function Parameters and Arguments:

# Explain the concepts of formal parameters and actual arguments in Python functions.

# In[2]:


"""Formal parameters are placeholders in a function's definition,
while actual arguments are the values provided when calling the function.
Formal parameters define the interface, and actual arguments are the concrete data used by the function."""
#Formal paameters Example
def add(x,y):
    result= x+y
    return result
#Actual Arguments Example
print(add(12,23))


# In[ ]:





# Write a Python program that defines a function with default argument values.

# In[3]:


def sum(a=12,b=12):#these are the default values
    result=a*b
    return result
print(sum())


# In[ ]:





# How do you use keyword arguments in Python function calls? Provide an example.

# In[7]:


"""In Python, you can use keyword arguments to specify which formal parameter you are passing a value to when calling a function.
This allows you to provide arguments out of order and makes your code more readable and self-explanatory."""
def average(a,b):
    result=(a+b)/2
    return result
print(average(a=12,b=24))


# In[ ]:





# Create a Python function that accepts a variable number of arguments and calculates their sum.

# In[15]:


def add_num(*args):
    total=0
    for num in args:
        total+=num
    return total
result=add_num(10,20,30,40,50,60,70,80,90)
print(result)


# In[ ]:





# What is the purpose of the `*args` and `**kwargs` syntax in function parameter lists?

# *args allows functions to accept a variable number of positional arguments,
# 
# and **kwargs allows them to accept a variable number of keyword arguments, making functions more flexible and versatile.

# In[ ]:





# In[ ]:





# Return Values and Scoping:

# Describe the role of the `return` statement in Python functions and provide examples.

# In[16]:


"""The return statement in Python functions is used to provide a value as the function's output and to terminate the function."""
#Example
def add_num(a,b):
    result=a+b
    return result
print(add_num(12,12))


# In[ ]:





# Explain the concept of variable scope in Python, including local and global variables.

# In[17]:


"""
Variable scope in Python determines where a variable can be accessed or modified.
Local variables are confined to a specific block or function,
while global variables can be accessed from anywhere in the code. """


# In[ ]:





# Write a Python program that demonstrates the use of global variables within functions.

# In[21]:


global_variable=10
def mul_num(value):
    return value * global_variable
print(mul_num(23))


# In[ ]:





# Create a Python function that calculates the factorial of a number and returns it.

# In[2]:


n=int(input("Enter the number :"))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))
    


# In[ ]:





# How can you access variables defined outside a function from within the function?

# In[3]:


"""We can access by calling the variable name from inside the function"""
#Example just like n accessed from inside
#it also called global variable
n=int(input("Enter the number :"))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))


# In[ ]:





# Lambda Functions and Higher-Order Functions:

# What are lambda functions in Python, and when are they typically used?

# In[4]:


"""Lambda functions in Python are concise, anonymous functions used for simple operations,
often as arguments to other functions or for short tasks where a full function definition would be excessive."""
number=[1,2,3,4,5,6,7,8,9]
multiply=list(map(lambda x:x*2,number))
print(multiply)


# In[ ]:





# Write a Python program that uses lambda functions to sort a list of tuples based on the second element.

# In[7]:


data=[(1,3),(3,4),(8,9),(4,3)]
sorted_data=sorted(data,key=lambda x:x[1])
print(sorted_data)


# In[ ]:





# Explain the concept of higher-order functions in Python, and provide an example.

# In[9]:


"""A function that is having another function as an argument or a function that returns another
function as a return in the output is called the High order function"""
#Example
n=int(input("Enter the number :"))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))


# In[ ]:





# Create a Python function that takes a list of numbers and a function as arguments, applying the function to each element in the list.

# In[10]:


def apply_function_to_list(numbers, custom_function):
    result = []
    for num in numbers:
        result.append(custom_function(num))
    return result

# Define a custom function to double a number
def double(x):
    return x * 2

# Example usage:
numbers = [1, 2, 3, 4, 5]
doubled_numbers = apply_function_to_list(numbers, double)
print(doubled_numbers)



# In[ ]:





# Built-in Functions:

# Describe the role of built-in functions like `len()`, `max()`, and `min()` in Python.

# In[11]:


#len()
"""it gives the lenght of a variable"""
#max()
"""it gives the highest number from the list"""
#min()
"""it gives the lowest or minimum number from the list"""


# In[ ]:





# Write a Python program that uses the `map()` function to apply a function to each element of a list.

# In[12]:


numbers=[1,2,3,4,5,6,7,8,9]
mult_num=list(map(lambda x:x*2,numbers))
print(mult_num)


# In[ ]:





# How does the `filter()` function work in Python, and when would you use it?

# In[13]:


"""in my opinion the filter function filters a sequence of elements based on a given predicate 
 (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate."""
numbers=[1,2,3,4,5,6,7,8,9]
even_num=list(filter(lambda x:x%2==0,numbers))
print(even_num)


# In[ ]:





# Create a Python program that uses the `reduce()` function to find the product of all elements in a list.

# In[16]:


from functools import reduce
numbers=[1,2,3,4,5,6,7,8,9]
mult_num=reduce(lambda x,y:x*y,numbers)
print(mult_num)


# In[ ]:





# Function Documentation and Best Practices:

# Explain the purpose of docstrings in Python functions and how to write them.

# In[17]:


"""The purpose of the docstring is create documents in multiple lines and 
it can be writen in the same way as i wrote this exlpanation"""


# In[ ]:




