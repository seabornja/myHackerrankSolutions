#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    line_1 = "Hello "
    outputString = line_1 + first
    outputString = outputString + " " + last
    outputString = outputString + "! You have just delved into python."
    print(outputString)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)