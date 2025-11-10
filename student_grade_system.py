grade_system = {}

while True:

    course_info = input()

    if course_info == "end of grades":
        break

    parts = course_info.split(":")
    student_name, course_name, grades = parts[0], parts[1], float(parts[2])

    if student_name not in grade_system:
        grade_system[student_name] = {}

    if grades > grade_system[student_name].get(course_name, 0):
        grade_system[student_name][course_name] = grades

while True:

    queries_info = input()

    if queries_info == "end of queries":
        break

    student_name, course_name = queries_info.split(":")

    if student_name in grade_system and course_name in grade_system[student_name]:
        grade = grade_system[student_name][course_name]
        print(f"{student_name} in {course_name}: {grade:.2f}")

    else:
        print(f"{student_name} in {course_name}: Not enrolled")

best_student = ""
best_avg_grade = 0

for name, course in grade_system.items():
   average_grade = sum(course.values()) / len(course)
   if average_grade > best_avg_grade:
       best_student = name
       best_avg_grade = average_grade


# best_student = max(grade_system, key=lambda s: sum(grade_system[s].values()) / len(grade_system[s]))
# best_avg_grade = sum(grade_system[best_student].values()) / len(grade_system[best_student])


print(f"Best student: {best_student} with average {best_avg_grade:.2f}")
