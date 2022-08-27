'''
#1. Write a Python function to find the Max of three numbers.
def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y
def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))
print(max_of_three(2, 12, 13))
'''
#Task 2
'''Write a Python function to sum all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
'''
'''def addition(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

print(addition((8, 2, 3, 0, 7)))

'''
# Task 3
'''
Write a Python function to multiply all the numbers in a list.
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
'''
'''
def multiply(numbers):
    total = 1
    for i in numbers:
        total = total * i
    return total
print(multiply((8, 2, 3, -1, 7)))
'''
'''
# Task 4
Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
'''
'''
def rev(string):
    m = string[::-1]
    for i in m:
        print(i, end="")
rev("1234abcd")
'''
"""
# 2nd way
def rev(string):
    i = string[::-1]
    print(i)
rev("1234abcd")
"""
"""
#3rd way
def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))
"""
'''
#Task 5
Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
'''
'''def factorial(n):
    if n == 0:
        return 1
    else:
        return n + factorial(n)
n = int(input("Enter the number: "))
print(factorial(n))
'''

#Task 6
'''
Write a Python function to check whether a number falls in a given range. 
'''
"""
def test_number(n):
    if n in range(4,16):
        print(str(n), "is in the range.")
    else:
        print(str(n), "is outside the given range.")
test_number(6)
"""
'''
# Task 7
Write a Python function that input a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''
'''
def checker(n):
    d = {"UPPER_CASE":0, "LOWER_CASE":0}
    for i in n:
        if i.isupper():
            d["UPPER_CASE"]+=1
        elif i.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("Original String : ", n)
    print("No. of Upper case characters : ", d["UPPER_CASE"])
    print("No. of Lower case Characters : ", d["LOWER_CASE"])
n = input("Enter the string: ")
(checker(n))
'''
# Task 8
'''Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''
'''
def simple_list(lst):
    l = []
    for i in lst:
        if i not in l :
            l.append(i)
        else:
            pass
    return l
print(simple_list([1,2,3,3,3,3,4,5]))
'''
# task 9
'''
Write a Python function that takes a number as a parameter and check the number is prime or not.
'''
'''
def prime_checker(number):
    if number==1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2,number):
            if (number%i==0):
                return False
        return True
print(prime_checker(3))
'''
# Task 10
'''
Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
'''
'''
def sample_list(lst):
    k = []
    for i in lst:
        if i%2 == 0:
            k.append(i)
        else:
            pass
    print("Expected result:", k)
sample_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
'''
                                    #####Assignment Problem

#Task1
"""
Write a function called even_checker that takes a number as an argument and prints whether the number is even or odd inside the function.
===================================

Example1:
Function Call:
even_checker(5)
Output:
Odd!!

=============================

Example2:
Function Call:
even_checker(2)
Output:
Even!!
"""
'''
def even_checker(number):
  if number%2 == 0:
    print("Even!!")
  else:
    print("Odd!!")
number = int(input("Enter the number: "))
even_checker(number)
'''

#Task 2
'''
Write a python function that takes the limit as an argument of the Fibonacci series and prints till that limit.

===================================

Function Call:
fibonacci(10)
Output:
0 1 1 2 3 5 8
======================
Function Call:
fibonacci(5)
Output:
0 1 1 2 3 5
'''
'''
def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(0)

    else:
        print(a)
        print(b)
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
            print(c)
n = int(input("Please enter a number: "))
fib(n)
'''

# Task 3
'''
Write a function called foo_moo that takes a number as an argument and returns the following statements according the below mentioned conditions. Then, finally prints the statement in the function call.

If the number is divisible by 2, it should return "Foo".
If the number is divisible by 3, it should return "Moo".
If the number is divisible by both 2 and 3, it should return "FooMoo".
Otherwise, it returns "Boo".

===================================

Example1:
Function Call:
foo_moo(5)
Output:
Boo

=================

Example2:
Function Call:
foo_moo(4)
Output:
Foo

=================

Example3:
Function Call:
foo_moo(6)
Output:
FooMoo
'''
'''
def foo_moo(number):
    if number%2 == 0 and number%3 == 0:
        return "FooMoo"
    elif number%2 == 0:
        return "Foo"
    elif number%3 == 0:
        return "Moo"
    else:
        return "Boo"
number = int(input("Enter the number: "))
print(foo_moo(number))
'''
'''
Task 4
Write a python function that takes a string as an argument. Your task is to calculate the number of uppercase letters and lowercase letters and print them in the function.

===================================

Function Call:
function_name('The quick Sand Man')
Output:
No. of Uppercase characters : 3
No. of Lowercase Characters: 12
============================
Function Call:
function_name('HaRRy PotteR')
Output:
No. of Uppercase characters : 5
No. of Lowercase Characters: 6
'''
'''
def up_low(string):
    up = 0
    low = 0
    for i in string:
        if i>='A' and i <= 'Z':
            up = up + 1
        elif i >= 'a' and i <= 'z':
            low = low + 1
    print("No. of Uppercase characters : ", str(up))
    print("No. of Lowercase Characters: ", str(low))
string = input("Enter the String")
up_low(string)
'''
'''
# Task 5
Task 5
Write a function called calculate_tax that takes 3 arguments: your age, salary, and current job designation.

Your first task is to take these arguments as user input and pass these values to the function.

Your second task is to implement the function and calculate the tax as the following conditions:

NO TAX IF YOU ARE LESS THAN 18 YEARS OLD.
NO TAX IF YOU ARE THE PRESIDENT OF THE COMPANY
No tax if you get paid less than 10,000
5% tax if you get paid between 10K and 20K
10% tax if you get paid more than 20K
Finally return this tax value. Then print the returned value in the function call.

===================================

Hints:
Here the job designation is a string, so it can be written in both uppercase and lower cases. So, you need to check the value ignoring the case.

===================================

Example1:
Input:
16
20000
Student
Function Call:
calculate_tax(16, 20000, 'Student')
Output:
0

===================================

Example2:
Input:
20
18000
assistant manager
Function Call:
calculate_tax(20, 18000, 'assistant manager')
Output:
900.0

===================================

Example3:
Input:
20
22000
assistant manager
Function Call:
calculate_tax(20, 22000, 'Assistant manager')
Output:
2200.0

===================================

Example4:
Input:
20
122000
president
Function Call:
calculate_tax(20, 122000, 'president')
Output:
0
'''


'''
def calculate_tax(age, salary, current_job):
    tax = 0
    if age<=18:
        return tax
    elif (current_job.lower) == ('president'):
        return tax
    elif (salary < 10000):
        return tax
    elif salary >=10000 and salary <= 20000:
        tax = salary*(0.05)
        return tax
    else:
        tax = salary*(0.10)
        return tax
age = int(input("Your age: "))
salary = float(input("Your Salary"))
current_job = input("Your designation")
tax = calculate_tax(age, salary, current_job)
print(tax)
'''













