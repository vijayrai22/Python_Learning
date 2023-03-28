#Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird

if __name__ == '__main__':
    n = int(input('Ener any number').strip())
if n % 2 == 0:
    if n in range(2, 5 + 1):
        print('Not Weird')
    elif n in range(6, 20 + 1):
        print('Weird')
    elif n > 20:
        print('Not Weird')

else:
    print('Weird')