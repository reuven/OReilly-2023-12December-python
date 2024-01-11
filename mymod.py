if __name__ == '__main__':
    print(f'Hello from {__name__}!')

x = 100

y = [10, 20, 30]

z = {'a':100, 'b':200, 'c':300}

def hello(name):
    return f'Hello, {name}!'

if __name__ == '__main__':   # this means: never print when mymod.py is imported, only when executed
    print(f'Goodbye from {__name__}!')