N = int(input())

students = []
for n in range(N):
    Input = input().split()
    students.append((Input[0],int(Input[1])))

students.sort(key=lambda student:student[1])

for student in students:
    print(student[0],end=" ")