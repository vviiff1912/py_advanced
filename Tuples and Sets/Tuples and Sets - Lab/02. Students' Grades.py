num = int(input())

students = {}

for _ in range(num):
    student = input().split()
    if student[0] not in students.keys():
        students[student[0]] = []
    students[student[0]].append(float(student[1]))

for stdnt, grades in students.items():
    grades_formatted = ' '.join(f"{grade:.2f}" for grade in grades)
    print(f"{stdnt} -> {grades_formatted} (avg: {sum(grades) / len(grades):.2f})")



