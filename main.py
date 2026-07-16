students = []

file = open("students.txt", "r")

for line in file:
    if line.strip():
        data = line.strip().split(",")
        name = ",".join(data[:-1])   
        score = data[-1]             
        students.append({"name": name, "score": int(score)})

file.close()

name = input("Enter student name: ")
score = int(input("Enter student score: "))

students.append({"name": name, "score": score})

file = open("students.txt", "a")
file.write(f"\n{name},{score}")
file.close()

students.sort(key=lambda x: x["name"])

for student in students:
    print(student)