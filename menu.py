def menu(choices):
    while True:
        s = input(f'Enter your choice ({choices}): ').strip()
    
        if s in choices:
            return s