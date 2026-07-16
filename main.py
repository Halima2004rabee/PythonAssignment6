students = []

file = open("students.txt", "r")

for line in file:
    name, score = line.strip().split(",")
    students.append({"name": name, "score": int(score)})

file.close()

name = input("Enter student name: ")
score = int(input("Enter student score: "))

students.append({"name": name, "score": score})

students.sort(key=lambda x: x["name"])

for student in students:
    print(student)