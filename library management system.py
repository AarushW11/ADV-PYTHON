from datetime import date



def border(func):
    def wrapper(self):
        return "***************************\n" + func(self) + "\n***************************"
    return wrapper

def uppercase(func):
    def wrapper(self):
        return func(self).upper()
    return wrapper

def footer(func):
    def wrapper(self):
        return func(self) + "\nEND OF REPORT"
    return wrapper




class Report:

    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        self.date = date.today()

    # Class Method
    @classmethod
    def student_template(cls):
        content = "Student Name : Aarush\nMarks : 95\nGrade : A"
        return cls("Student Report", "Aarush", content)

    
    def __str__(self):
        return (f"Title : {self.title}\n"
                f"Author : {self.author}\n"
                f"Date : {self.date}\n"
                f"{self.content}")

    def __len__(self):
        return len(str(self))

    def __eq__(self, other):
        return self.content == other.content

    # Apply Multiple Decorators
    @border
    @uppercase
    @footer
    def generate_report(self):
        return str(self)

report = Report.student_template()

print(report.generate_report())

print("\nLength of Report:", len(report))
