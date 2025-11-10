school_diary = {}

while True:
    info = input()

    if info == "graduation":
        average_grade = float(input())
        break

    parts = info.split(":")
    name, subject, grade = parts[0], parts[1], float(parts[2])

    if name not in school_diary.keys():
        school_diary[name] = {}

    if subject not in school_diary[name]:
        school_diary[name][subject] = []
    school_diary[name][subject].append(grade)

qualified_students = []

for student, subjects in school_diary.items():
    total_grades = sum(sum(subject_grades) for subject_grades in subjects.values())
    number_of_grades = sum(len(subject_grades) for subject_grades in subjects.values())

    if number_of_grades > 0:
        average_grades = total_grades / number_of_grades
        if average_grades >= average_grade:
            qualified_students.append((student, average_grades))

qualified_students.sort(key=lambda x: x[1], reverse=True)

for student_name, grades in qualified_students:
    print(f"{student_name} -> {grades:.2f}")

