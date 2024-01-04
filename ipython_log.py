# IPython log file


# f-strings and printing values

x = 10
y = [10, 20, 30]
z = {'a':10, 'b':20, 'c':30}

# how can I print x, y, and z -- both the variable names and their values?
print(f'x={x}, y={y}, z={z}')
# in modern versions of Python, you can use special syntax as a shortcut to the above:
print(f'{x=}, {y=}, {z=}')
def hello():
    print('Hello!')
# once I have defined a function, I can run it -- also "call it" or "execute it" with parentheses

hello()
# You *must* put the parentheses there -- otherwise, you get the function itself, not the result of running it

hello
# let's redefine our function

def hello():
    print('Hello?')
hello()
type(hello)
# I can now use my function in other code

for i in range(5):
    hello()
def calc():
    first = input('Enter first number: ').strip()
    op = input('Enter operator: ').strip()
    second = input('Enter second number: ').strip()

    first = int(first)
    second = int(second)

    if op == '+':
        result = first + second
    elif op == '-':
        result = first - second
    else:
        result = f'(Bad operator {op})'

    print(f'{first} {op} {second} = {result}')
calc()
calc()
# CD

def calc():

  first_num = input("Enter the first number: ").strip()
  if first_num.isdigit():
    first_num = int(first_num)

  operator = input("Enter an operator: ").strip()

  second_num = input("Enter the second number: ").strip()
  if second_num.isdigit():
    second_num = int(first_num)

  if operator == '+':
    output = first_num + second_num

  if operator == '-':
    output = first_num - second_num

  if operator == '*':
    output = first_num * second_num

  if operator == '/':
    output = first_num / second_num


  print(f'{output=}')

calc()
# CD

def calc():

  first_num = input("Enter the first number: ").strip()
  if first_num.isdigit():
    first_num = int(first_num)

  operator = input("Enter an operator: ").strip()

  second_num = input("Enter the second number: ").strip()
  if second_num.isdigit():
    second_num = int(second_num)

  if operator == '+':
    output = first_num + second_num

  if operator == '-':
    output = first_num - second_num

  if operator == '*':
    output = first_num * second_num

  if operator == '/':
    output = first_num / second_num


  print(f'{output=}')

calc()
# SJ
def calc():
    first_num=int(input("enter num1"))
    second_num=int(input("enter num2"))
    print(first_num+second_num)

calc()
# AJ

def calc():
    num1 = input('Enter first number: ').strip()
    oper = input('Enter the operator (+/-)').strip()
    num2 = input('Enter second number: ').strip()
    
    if not num1.isdigit() or not num2.isdigit():
        print('Please enter numbers')
        break
    
    if not oper in ('+-'):
        print('Please enter correct operator')
        break
    
    if oper == '+':
        tot = int(num1) + int(num2)
    else:
        tot = int(num1) - int(num2)
    
    print(f'{num1} {oper} {num2} = {tot}')

calc()
def hello(name):    # this function requires one argument, which will be assigned to name
    return f'Hello, {name}'
hello('world')
def hello(name):    # this function requires one argument, which will be assigned to name
    print(f'Hello, {name}')
hello('world')
# parameters:  name
# arguments:  'world'

hello('world')
# what happens if I want to call it without any argument?

hello()
# think about this:

x = 5
x = 7

print(x)
# can I define a function with more than one parameter? Yes!

def hello(first, last):
    print(f'Hello, {first} {last}!')
hello('Reuven', 'Lerner')
hello('Reuven')
hello()
def calc():
    first = input('Enter first number: ').strip()
    op = input('Enter operator: ').strip()
    second = input('Enter second number: ').strip()

    first = int(first)
    second = int(second)

    if op == '+':
        result = first + second
    elif op == '-':
        result = first - second
    else:
        result = f'(Bad operator {op})'

    print(f'{first} {op} {second} = {result}')
def calc(first, op, second):
    if op == '+':
        result = first + second
    elif op == '-':
        result = first - second
    else:
        result = f'(Bad operator {op})'

    print(f'{first} {op} {second} = {result}')
calc(10, '+', 3)
calc('a', 'b', 'c')
calc('a', '-', 'c')
for one_number in range(10):
    print(calc(one_number, '+', 5))
for one_number in range(10):
    calc(one_number, '+', 5)
# because the function "calc" no longer requires any interactive
# inputs, I can put it inside of a "for" loop, and use it non-interactively.

for one_number in range(10):
    calc(one_number, '+', 5)
# AJ 

num1 = input('Enter first number: ').strip()
oper = input('Enter the operator (+/-)').strip()
num2 = input('Enter second number: ').strip()

if not num1.isdigit() or not num2.isdigit():
    print('Please enter numbers')

if not oper in ('+-'):
    print('Please enter correct operator')
    
def calc(n1, op, n2):
    if op == '+':
        tot = int(n1) + int(n2)
    elif op =='-':
        tot = int(n1) - int(n2)
    
    print(f'{n1} {op} {n2} = {tot}')

calc(num1, oper, num2)
# AJ 

def calc(n1, op, n2):
    if op == '+':
        tot = int(n1) + int(n2)
    elif op =='-':
        tot = int(n1) - int(n2)
    
    print(f'{n1} {op} {n2} = {tot}')

calc(10, '+', 20)
# HS

def calc(a, b, op):
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    else:
        result = f'Unrecognized operator: {op}'
    return result

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
op = input('Enter operator (+ or -): ')

result = calc(a, b, op)

print(f'Result of operator {op} is {result}')
# HS

def calc(a, b, op):
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    else:
        result = f'Unrecognized operator: {op}'
    return result

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
op = input('Enter operator (+ or -): ')

result = calc(a, b, op)

print(f'Result of operator {op} is {result}')
# PD

a= int(input('enter 1st No').strip())
b= input('enter the operator').strip()
c= int(input('enter 2nd No.').strip())

def calc(first,op,second):
  if op == '+':
    print(a+b)
  elif op=='-':
    print(a-b)
  else:
    print('Dont Know')
      
calc(a,b,c)
# PD

a = int(input('enter 1st No').strip())
b = input('enter the operator').strip()
c = int(input('enter 2nd No.').strip())

def calc(first,op,second):
  if op == '+':
    print(first+second)
  elif op=='-':
    print(first-second)
  else:
    print('Dont Know')
      
calc(a,b,c)
# PD

a = int(input('enter 1st No').strip())
b = input('enter the operator').strip()
c = int(input('enter 2nd No.').strip())

def calc(first,op,second):
  if op == '+':
    print(first+second)
  elif op=='-':
    print(first-second)
  else:
    print('Dont Know')
      
calc(a,b,c)
def hello(name):
    print(f'Hello, {name}!')
hello('world')
hello(5)
hello([10, 20, 30])
hello(hello)
def add(x, y):
    print(f'{x} + {y} = {x+y}')   
# parameters: x  y
# arguments   3  5   

add(3, 5)    # positional arguments, because they're assigned based on their positions
# we can also use keyword arguments:

# parameters:   x    y
# arguments:    3    5

add(x=3, y=5)
# it's usually up to the caller (whoever is calling the function) to decide whether
# to use positional or keyword arguments. Positional are easier, keyword are more explicit

# can I change the order? (The answer: Yes!)

add(y=8, x=4)
# let's mix and match them

add(5, y=10)
# what if I try the other way around?

add(x=5, 10)
add(first=5, second=10)
# part of a function's "signature" in Python includes the names of the parameters
# so that you can pass them in keyword arguments.
add(x='abc', y='def')
# notice that the keyword argument itself (the variable name) comes before
# the =, and doesn't have any quotes around it. The string value (after the =)
# can have quotes.

add(x='abc', y='def')
add(5, 10)
# parameters: x  y
# arguments:  5 10
add(5, 10)
# if, with add, I want to pass x as a keyword argument, then y *must* be a keyword argument, too.

add(x=5, y=10)
add()
def hello(name):
    print(f'Hello, {name}!')

hello('world')
# how many characters are in the output from hello('world')?

len(hello('world'))
# let's use return instead:

def hello(name):
    return f'Hello, {name}!'

hello('world')
# let's use return instead:

def hello(name):
    return f'Hello, {name}!'

hello('world')   # we see the value in Jupyter, which then prints it - -but the function didn't print it
len(hello('world'))   # hello returns a string, which then becomes the input to len
s = hello('world')
s = hello('world')   # assign the result to a variable

s.upper()
def calc(first, op, second):
    if op == '+':
        result = first + second
    elif op == '-':
        result = first - second
    else:
        result = f'(Bad operator {op})'

    return f'{first} {op} {second} = {result}'

x = calc(10, '+', 3)
x
# add a check for non-integers 
# (not the best way to do it)

def calc(first, op, second):
    if type(first) != int:
        return f'{first} is not an integer'

    if type(second) != int:
        return f'{second} is not an integer'

    if op == '+':
        result = first + second
    elif op == '-':
        result = first - second
    else:
        result = f'(Bad operator {op})'

    return f'{first} {op} {second} = {result}'

x = calc(10, '+', 3)
# add a check for non-integers 
# (not the best way to do it)

def calc(first, op, second):
    if type(first) != int:
        return f'{first} is not an integer'

    if type(second) != int:
        return f'{second} is not an integer'

    if op == '+':
        result = first + second
    elif op == '-':
        result = first - second
    else:
        result = f'(Bad operator {op})'

    return f'{first} {op} {second} = {result}'

calc(10, '+', 3)
calc('abcd', '+', [10, 20, 30])
First = int(input('Enter the First Number :').strip())
Second = int(input('Enter the Second Number :').strip())
Oper = input('Enter the operator +, -').strip()

def calc(n1=First, op=Oper, n2=Second):
  if n1.isdigit() and n2.isdigit():
    if op == '+':
      result = n1 + n2
    elif op == '-':
      result = n1-n2
    else:
      result = f'Operator is undefined'
  else:
    result = f'Either of inputs are non-numeric'
  return(f'{n1} {op} {n2} = {result}')
First = int(input('Enter the First Number :').strip())
Second = int(input('Enter the Second Number :').strip())
Oper = input('Enter the operator +, -').strip()

def calc(n1, op, n2):
  if n1.isdigit() and n2.isdigit():
    if op == '+':
      result = n1 + n2
    elif op == '-':
      result = n1-n2
    else:
      result = f'Operator is undefined'
  else:
    result = f'Either of inputs are non-numeric'
  return(f'{n1} {op} {n2} = {result}')
calc(First, Second, Oper)
First = int(input('Enter the First Number :').strip())
Second = int(input('Enter the Second Number :').strip())
Oper = input('Enter the operator +, -').strip()

def calc(n1, op, n2):
  if type(n1) == int and type(n2) == int:
    if op == '+':
      result = n1 + n2
    elif op == '-':
      result = n1-n2
    else:
      result = f'Operator is undefined'
  else:
    result = f'Either of inputs are non-numeric'
  return(f'{n1} {op} {n2} = {result}')
calc(First, Second, Oper)
# isdigit -- is a string method, that you can only run on strings
# but I wanted to pass integers as arguments...

# VC

def calc(first,operator,second):

    if first.isdigit() == False or second.isdigit() == False:
        return f'Entry is not a digit'

    first = int(first)
    second = int(second)

    if op == '+':
        result = first + second
    elif op == '-':
        result = first - second
    else:
        result = f'(Bad operator {op})'
    
    return f'{first} {op} {second} = {result}'

first = input('Enter first number: ').strip()
op = input('Enter operator: ').strip()
second = input('Enter second number: ').strip()

calc(first,op,second)
# isdigit -- is a string method, that you can only run on strings
# but I wanted to pass integers as arguments...

# VC

def calc(first,operator,second):

    if first.isdigit() == False or second.isdigit() == False:
        return f'Entry is not a digit'

    first = int(first)
    second = int(second)

    if op == '+':
        result = first + second
    elif op == '-':
        result = first - second
    else:
        result = f'(Bad operator {op})'
    
    return f'{first} {op} {second} = {result}'

first = input('Enter first number: ').strip()
op = input('Enter operator: ').strip()
second = input('Enter second number: ').strip()

calc(first,op,second)
# AD

def calc(op1, op, op2):
    if (type(op1) != int) or (type(op2) != int):
        return 'Invalid Operands'
    else:        
        op1 = int(op1)
        op2 = int(op2)
        if op == '+':
            result = op1 + op2
        elif op == '-':
            result = op1 - op2
        else:
            return 'Invalid Operator'
        return result

op1 = input("Enter First Number: ").strip()
op = input("Enter Operator: ").strip()
op2 = input("Enter Second Number: ").strip()    
print(calc(op1, op, op2))
def smallest(numbers):
    output = numbers[0]

    for one_number in numbers:
        if one_number < output:   # is the current number smaller than our planned output?
            output = one_number   # if so, then update the planned output to be one_number

    return output
    
smallest([10, 20, 30, 40, 50])
smallest([10, 20, 30, -5, 40, 50])
# AD

def smallest(mylist):
    small = mylist[0]
    for num in mylist[1:]:
        if num < small:
            small = num
    return small
print(smallest([-12, -210, 20, 8, -9, 30, 9]))
# AJ

def smallest(lst):
    sm = 0
    
    for each_num in lst:
        if each_num < sm:
            sm = each_num
            
    return sm
    
s = smallest([10, 20, -5, 30, 7, 8, -2])
print(f'{s=}')
# VC

def smallest(entry):
  min = 0

  for digit in range(entry):
    if min > digit:
      min = digit
  return min

smallest([3,35,-2,7]) 
# VC

def smallest(entry):
  min = 0

  for digit in entry:
    if min > digit:
      min = digit
  return min

smallest([3,35,-2,7]) 
# HS

user_input = input("Enter elements of the list separated by spaces: ")
lst_of_int = list(map(int, user_input.split()))

def smallest_integer(lst_of_int):
    smallest = lst_of_int[0]
    for number in lst_of_int:
        if number < smallest:
            smallest = number
    return smallest

result = smallest_integer(lst_of_int)

print(f"The smallest integer in the list is: {result}")
def smallest(numbers):
    output = numbers[0]          # pretend the first element is the smallest

    for one_number in numbers:
        if one_number < output:   # is the current number smaller than our planned output?
            output = one_number   # if so, then update the planned output to be one_number

    return output
    
# here's a function that takes a list of integers as its input, 
# and returns a dict whose keys are "odds" and "evens", and whose values
# are lists of integers -- the odd and even values from our input

def odds_and_evens(numbers):
    output = {'odds':[], 'evens':[]}

    for one_number in numbers:
        if one_number % 2 == 0:    # if the remainder after dividing by 2 is 0
            output['evens'].append(one_number)
        else:
            output['odds'].append(one_number)

    return output
odds_and_evens([10, 15, 20, 25, 30, 35])
d = odds_and_evens([10, 15, 20, 25, 30, 35])

for key, value in d.items():
    print(f'{key}: {value}')
# I can return a tuple, as well

def myfunc():
    return (10, 'hello', [10, 20, 30])   # returning a tuple from our function

myfunc()
# we don't need to put parentheses around a tuple -- the commas are enough
# it's traditional when returning a tuple from a function not to put them there

def myfunc():
    return 10, 'hello', [10, 20, 30]   # still returning a tuple from our function!

myfunc()
mylist = [10, 20, 30]
mylist.append(40)   # I have now added 40 to the end of mylist

mylist
odds_and_evens(5)
# remember unpacking? That's where we take an interable on the right, and multiple variables
# on the left of assignment

myfunc()
# we can combine our function that returns a tuple with several variables,
# and thus effectively get multiple values back from our function

x, y, z = myfunc()
x
y
z
# If a function returns a value, then that value can be used as the argument for another function

def first_word(s):
    return s.split()[0]   # turn s into a list of strings, and return the first word

first_word('this is a test')
len(first_word('this is a test'))   # the returned value from first_word is the argument to len
def biggest_and_smallest(numbers):
    # set both to be the first value in numbers
    biggest = numbers[0]
    smallest = numbers[0]

    # go through each number, updating biggest/smallest as needed
    for one_number in numbers:
        if one_number > biggest:
            biggest = one_number
        if one_number < smallest:
            smallest = one_number

    return biggest, smallest   # return a tuple with what we found

    
biggest_and_smallest([10, 20, -5, -3, 12])
biggest_int, smallest_int = biggest_and_smallest([10, 20, -5, -3, 12])
biggest_int
smallest_int
# 2-element tuple on the right
# assigned to two variables on the left via unpacking

biggest_int, smallest_int = biggest_and_smallest([10, 20, -5, -3, 12])
# AJ

def biggest_and_smallest(num_list):
    bigg = num_list[0]
    sma = num_list[0]
    
    for each_num in num_list[1:]:
        if each_num < sma:
            sma = each_num
        if each_num > bigg:
            bigg = each_num
    
    return bigg, sma

b1, s1 = biggest_and_smallest([10,20,-5,-3,12,45,50])
print(f'{b1=}, {s1=}')
# HS

#lst_of_int  = [10,20,-5,30,10,0]
user_input = input("Enter elements of the list separated by spaces: ")
lst_of_int = list(map(int, user_input.split()))

def find_smallest_and_largest(lst_of_int):
    
    smallest = largest = lst_of_int[0]

    for number in lst_of_int:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number

    return smallest, largest

result = find_smallest_and_largest(lst_of_int)

print(f"The smallest and largest integers in the list are: {result}")
# VC

def biggest_and_smallest(entry):
  smallest_num = entry[0]
  

  for digit in entry:
    if smallest_num > digit:
      smallest_num = digit
    else:
      biggest_num = digit
  
  return biggest_num, smallest_num 

biggest_and_smallest([3,-1,-5,5,7])

biggest, smallest = biggest_and_smallest
# VC

def biggest_and_smallest(entry):
  smallest_num = entry[0]
  

  for digit in entry:
    if smallest_num > digit:
      smallest_num = digit
    else:
      biggest_num = digit
  
  return biggest_num, smallest_num 

biggest, smallest = biggest_and_smallest([3,-1,-5,5,7])
biggest
smallest
# PD

def bignsmall(nos):
  small= nos[0]
  big = nos[0]

  for one_number in nos:
    if one_number < small:
     small= one_number
    if one_number> big:
      big= one_number

  return small, big

bignsmall(10,29,30)
# PD

def bignsmall(nos):
  small= nos[0]
  big = nos[0]

  for one_number in nos:
    if one_number < small:
     small= one_number
    if one_number> big:
      big= one_number

  return small, big

bignsmall([10,29,30])
def frequencies(s):
    output = {}

    for one_character in s:
        if one_character in output:     # have we seen this character before?
            output[one_character] += 1  #   if so, add 1 to its count
        else:                           # no, it's the first time?
            output[one_character] = 1   #   that's OK -- add the key-value pair to the dict
            

    return output
frequencies('this is a test')
sentence = input('Enter a sentence: ').strip()
frequencies(sentence)
d = frequencies(sentence)

for key, value in d.items():
    print(f'{key}: {value')
d = frequencies(sentence)

for key, value in d.items():
    print(f'{key}: {value}')
# AD

def frequency(s):
    myDictionary = {}
    for char in s:
        if char in myDictionary:
            myDictionary[char] += 1
        else:
            myDictionary[char] = 1
    return myDictionary

def printFrequencies(s):
    freq = frequency(s)
    for item in freq.items():
        print(f'{item}: {freq[item]}')
printFrequencies('this is a test')
# AD

def frequency(s):
    myDictionary = {}
    for char in s:
        if char in myDictionary:
            myDictionary[char] += 1
        else:
            myDictionary[char] = 1
    return myDictionary

def printFrequencies(s):
    freq = frequency(s)
    for key, value in freq.items():    # items returns (key, value)
        print(f'{key}: {value}')
printFrequencies('this is a test')
