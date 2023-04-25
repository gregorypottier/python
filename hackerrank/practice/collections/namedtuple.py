# Collections - named tuple
from collections import namedtuple

students_num = int(input())
structure = input().split()
Student = namedtuple("Student", structure)

marks =[]
for _ in range(students_num):
    marks.append(int(Student(*input().split()).MARKS))

print(sum(marks)/students_num)
