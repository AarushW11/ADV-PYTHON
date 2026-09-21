import csv
import json

# Number of students
n = int(input("Enter number of students: "))

# Store student details in CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Branch", "Marks"])

    for i in range(n):
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        marks = int(input("Enter Marks (out of 500): "))

        writer.writerow([roll, name, branch, marks])

print("Student details stored in students.csv")

# Read CSV and process data
students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks = int(row["Marks"])
        total = marks
        percentage = (marks / 500) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        student = {
            "Roll Number": row["Roll No"],
            "Name": row["Name"],
            "Branch": row["Branch"],
            "Total Marks": total,
            "Percentage": round(percentage, 2),
            "Grade": grade
        }

        students.append(student)

# Store processed records in JSON
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Processed records stored in students.json")
