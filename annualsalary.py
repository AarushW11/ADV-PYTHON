import csv

# Read employee details from CSV file
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Employees with Annual Salary")
    print("-" * 50)

    for row in reader:
        name = row["Name"]
        monthly_salary = int(row["Monthly Salary"])
        annual_salary = monthly_salary * 12

        print("Name:", name)
        print("Monthly Salary: ₹", monthly_salary)
        print("Annual Salary: ₹", annual_salary)

        if monthly_salary > 50000:
            print("Status: Salary above ₹50,000")

        print("-" * 50)
