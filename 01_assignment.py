# Function to check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

# Input from the user
try:
    number = float(input("Enter a number: "))
    result = check_number(number)
    print(result)
except ValueError:
    print("Please enter a valid number.")



# Function to calculate the factorial of a number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Input from the user
try:
    number = int(input("Enter a non-negative integer: "))
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")
except ValueError:
    print("Please enter a valid non-negative integer.")


# Function to generate Fibonacci series up to a given range
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while a <= n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Input from the user
try:
    number = int(input("Enter a positive integer to define the range: "))
    if number < 0:
        print("Please enter a integer.")
    else:
        result = fibonacci_series(number)
        print(f"The Fibonacci series up to {number} is: {result}")
except ValueError:
    print("Please enter a valid integer.")


'''question 9) Write python program that swap two number with temp variable
               and without temp variable'''

# Swapping using a temporary variable
a = 5
b = 10

# Display original values
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap using a temporary variable
temp = a
a = b
b = temp

# Display swapped values
print("After swapping:")
print("a =", a)
print("b =", b)

# Swapping without using a temporary variable
a = 5
b = 10

# Display original values
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap without a temporary variable
a, b = b, a

# Display swapped values
print("After swapping:")
print("a =", a)
print("b =", b)


'''10) Write a Python program to find whether a given number is even
or odd, print out an appropriate message to the user.'''

# Program to check if a number is even or odd

# Get user input
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

'''11) Write a Python program to test whether a passed letter is a vowel
       or not'''

# Program to check if a letter is a vowel

# Get user input
letter = input("Enter a letter: ").lower()

# Check if the input is a single letter
if len(letter) != 1 or not letter.isalpha():
    print("Please enter a single alphabetic character.")
else:
    # Check if the letter is a vowel
    if letter in 'aeiou':
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is not a vowel.")
        

'''question12)'''
def sum_of_integers(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c

# Example usage
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

result = sum_of_integers(num1, num2, num3)
print("The result is:", result)

'''question 13)'''
def check_values(a, b):
    if a == b:
        return True
    elif abs(a + b) == 5 or abs(a - b) == 5:
        return True
    else:
        return False

# Example usage
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

result = check_values(num1, num2)
print("The result is:", result)

'''question 14)'''
def sum_of_integers(n):
    
    return n * (n + 1) // 2

n = int(input("Enter a positive integer: "))

if n > 0:
    result = sum_of_integers(n)
    print(f"The sum of the first {n} positive integers is {result}.")
else:
    print("Please enter a positive integer.")

'''question 15)'''

def string_length(s):
    return len(s)

user_string = input("Enter a string: ")

length = string_length(user_string)
print(f"The length of the string is {length}.")



'''question 16)'''
def count_characters(s):
    # Create a dictionary to store character frequencies
    frequency = {}
    
    # Iterate over each character in the string
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency

# Get user input
user_string = input("Enter a string: ")

# Calculate character frequencies
char_count = count_characters(user_string)

# Display the character frequencies
print("Character frequencies:")
for char, count in char_count.items():
    print(f"'{char}': {count}")

'''Question 17)'''

my_list = [10, 20, 30, 40, 50]
print(my_list[-1])
print(my_list[-2])


my_str= "Manoj Patel"
print(my_str[-1])
print(my_str[-2])

'''Question 18)'''

def count_occurrences(string, substring):
    count = 0
    start = 0
    
    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += len(substring)
    
    return count

# Example usage:
string = "This is a test string. Testing the function to count test occurrences."
substring = "test"
print(f"The substring '{substring}' occurs {count_occurrences(string, substring)} times.")


'''question19)'''
from collections import Counter
import re

def count_word_occurrences(sentence):
    # Convert the sentence to lowercase to ensure case-insensitivity
    sentence = sentence.lower()
    
    # Use regex to find words and ignore punctuation
    words = re.findall(r'\b\w+\b', sentence)
    
    # Use Counter to count occurrences of each word
    word_count = Counter(words)
    
    return word_count

# Example usage:
sentence = "This is a test sentence. This test is only a test."
word_counts = count_word_occurrences(sentence)

for word, count in word_counts.items():
    print(f"'{word}' occurs {count} times.")

'''Question 20)'''

def swap_and_combine(str1, str2):
    # Swap the first two characters of each string
    if len(str1) >= 2:
        str1 = str2[:2] + str1[2:]
    if len(str2) >= 2:
        str2 = str1[:2] + str2[2:]
    
    # Combine the two strings separated by a space
    combined = str1 + ' ' + str2
    return combined

# Example usage:
string1 = "hello"
string2 = "world"
result = swap_and_combine(string1, string2)
print(result)

































    
