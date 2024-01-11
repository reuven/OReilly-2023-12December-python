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
