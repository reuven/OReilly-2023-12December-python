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
