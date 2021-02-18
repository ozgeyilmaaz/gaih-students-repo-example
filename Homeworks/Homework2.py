num_students = 5
names = []
all_grades = []
info = {}
average_list = []
average_dict = {}

for student in range(num_students):
    total = 0.0
    print("\tStudent", student+1)
    print("-----------------")
    name = input("Name/Surname: ")
    names.append(name)
    grades = []

    for x in range(3):
        if x == 0:
            score = int(input("Midterm: "))
        elif x == 1:
            score = int(input("Final: "))
        else:
            score = int(input("Homework: "))
        total += score
        grades.append(score)

    print()

    all_grades.append(grades)
    info[name] = grades
    average = format((total / 3), ".2f")
    average_list.append(average)
    average_dict[average] = name

average_list.sort()
average_list.reverse()
print("Congratulations ", average_dict[average_list[0]], "!", "The highest grade is yours.")

"""print("names:", names)
print("all_grades:", all_grades)
print("info:", info)
print("average_list:", average_list)
print("average_dict:", average_dict)"""