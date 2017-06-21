def is_prime(number):

    if number == 0 or number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            #print("Number {} is not prime number.".format(number))
            return False
    else:
        #print("Number {} is prime number.".format(number))
        return True

if __name__ == '__main__':
    print('-'*20)
    print([i for i in range(1001) if is_prime(i)])
