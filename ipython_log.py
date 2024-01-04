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
