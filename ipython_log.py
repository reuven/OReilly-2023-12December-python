# IPython log file


def count_ips(filename):
    output = {}

    for one_line in open(filename):
        ip_address = one_line.split()[0]

        if ip_address in output:
            output[ip_address] += 1  # seen before? add 1
        else:
            output[ip_address] = 1   # first time? set to 1

    return output

print(count_ips('logfile.txt'))
def count_ips(filename):
    output = {}

    for one_line in open(filename):
        ip_address = one_line.split()[0]

        if ip_address in output:
            output[ip_address] += 1  # seen before? add 1
        else:
            output[ip_address] = 1   # first time? set to 1

    return output

print(count_ips('logfile.txt'))
one_line
for one_line in open('logfile.txt'):
    pass   # do nothing
one_line
one_line[:12]
one_line[13:14]
# let's say I want a random integer
# I can use the "random" module for that, and the "randint" function in that module

import random

# after this line runs, "random" is defined as a variable

type(random)
# if I want to use a function defined in the random module, I say random.FUNCNAME()

random.randint(0, 100)   # this returns a single random int in the range 0-100
# what happens if I tire of saying random.randint? What if I just want to say randint?

randint(0, 100)
# what happens if I tire of saying random.randint? What if I just want to say randint?
# right now, randint doesn't exist as a variable. It exists as an attribute on the random module we loaded

randint(0, 100)
# there are many times that we might be using a function so often that we tire of saying both
# the module name and the function name. In such cases, we want the function to be loaded as a variable,
# rather than the module

# for that, we have this syntax:

from random import randint

# the above still loads the entire random module into memory
# the above does *not* define random as a variable
# but it *does* define "randint" as a variable (function) name that we can use
randint(0, 100)
# are there other options?
# if the module name is long, hard to spell, or just annoying, you can load the module
# and give it an alias, an alternate name

# this is *very* common in the world of data analysis, where everyone calls NumPy np and Pandas pd

import random as r     # this loads the module, but doesn't define "random" as a variable. It defines "r" instead
r.randint(0, 100)
# maybe there's already another "randint" that I don't want to clobber
# maybe I just want a shorter alias

from random import randint as ri     # now, randint won't be defined -- ri will
ri(0, 100)
from random import randint as ri, choice as ch
# I can define multiple aliases within a single module, loading these two names

from random import randint as ri, choice as ch
import random

number = random.randint(0, 100)  

while True:
    s = input('Guess the number: ').strip()

    if not s.isdigit():
        print(f'{s} is not numeric; try again')
        continue

    guess = int(s)    # get an integer based on the user's input

    if guess == number:
        print('You got it!')
        break
    elif guess < number:
        print('Too low')
    else:
        print('Too high')
        
        
dir(random)
# you can always run help on any one of these

help(random.triangular)
# where are modules getting loaded from?

random   # ask the module to show me its printed representation
# where can these files live?

import sys     # load the Python runtime system
sys.path       # list of strings, directory names + zipfiles, where Python looks for modules
