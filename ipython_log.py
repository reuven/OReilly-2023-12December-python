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
