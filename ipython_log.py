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
