def fizzbuzz(n):
    if n % 15 == 0:
        n = 'FizzBuzz'
    elif n % 3 == 0:
        n = 'Fizz'
    elif n % 5 == 0:
        n = 'Buzz'
    return n


def main():
    for i in range (100):
        number = (i + 1)
        number = fizzbuzz(number)
        print (number)
    return number


if __name__ == '__main__':
    main()
