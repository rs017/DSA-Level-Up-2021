def fizzbuzz(n):
    """Returns a tuple of strings with numbers from 1 to n based on following conditions:
    1. For multiples of 3, store "Fizz" instead of the number.
    2. For multiples of 5, store "Buzz" instead of the number.
    3. For multiples of both 3 & 5, store "FizzBuzz" instead of the number."""

    # declaring/initializing list to be returned (will be converted to tuple eventually)
    result = []

    for each_num in range(1, n + 1):

        # multiples of both 3 & 5 needs to be checked first
        # multiples of both 3 & 5 would be multiples of 15 (LCM)

        if (each_num % 15) == 0:
            result.append('FizzBuzz')
        elif (each_num % 5) == 0:
            result.append('Buzz')
        elif (each_num % 3) == 0:
            result.append('Fizz')
        else:
            result.append(str(each_num))

    return tuple(result)
