matrix = [[],
          [],
          []]

for x in range(9):
    number = int(input("Please enter a prime number: "))
    a = False
    while a == False:
        if number == 2:
            break
        for i in range(2, number):
            if number % i == 0:
                a = False
                break
            else:
                a = True
        if a == False:
            number = int(input("Be sure to enter a prime number: "))

    if len(matrix[0]) < 3:
        matrix[0].append(number)
    elif len(matrix[1]) < 3:
        matrix[1].append(number)
    else:
        matrix[2].append(number)

for b in range(3):
    print(matrix[b])
