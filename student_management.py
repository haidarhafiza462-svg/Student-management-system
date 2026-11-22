
students = []

def add_student():
    name = input("Enter student name: ")
    matric_number = input("Enter matric number: ")
    department = input("Enter department: ")

    student = {
        "Name": name,
        "Matric Number": matric_number,
        "Department": department
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No student records found.")
    else:
        for student in students:
            print(student)

while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
