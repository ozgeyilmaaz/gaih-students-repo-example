def prime_first(num):
    print(num)


def prime_second(num):
    print(num)


for number in range(1000):
    if number == 0:
        print("Prime numbers from 0 to 500:")
    elif number == 500:
        print("Prime numbers from 500 to 1000:")

    if number == 0 or number == 1 or number == 2:
        continue
    else:
        control = True
        for x in range(2, number):
            if number % x == 0:
                control = False
                break
            else:
                control = True

    if control and number < 500:
        prime_first(number)
    elif control and number >= 500:
        prime_second(number)
