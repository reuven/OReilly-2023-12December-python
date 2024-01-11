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
