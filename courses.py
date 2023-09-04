n = int(input())
courses = []
for _ in range(n):
    course = input()
    if course not in courses:
        print(course)
        courses.append(course)
