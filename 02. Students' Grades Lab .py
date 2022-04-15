n = int(input())


data_base = {}
while n > 0:
    name_grade = input()
    n -= 1
    name, grade = tuple(name_grade.split())

    if name not in data_base:
        data_base[name] = []
    data_base[name].append(float(grade))

for key, value in data_base.items():
    average_grade = 0

    for el in value:
        grade_round = round(el)
        average_grade += el

    grades_str = ' '.join(str(f'{el:.2f}') for el in value)
    average_grade = average_grade / len(value)



    print(f"{key} -> {grades_str} (avg: {average_grade:.2f})")


