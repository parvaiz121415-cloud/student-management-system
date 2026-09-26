students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    course = input("Enter Course: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("\nStudent added successfully!")


def view_students():
    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n---------- Student List ----------")

    for student in students:
        print("ID     :", student["id"])
        print("Name   :", student["name"])
        print("Age    :", student["age"])
        print("Course :", student["course"])
        print("---------------------------------")


def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("ID     :", student["id"])
            print("Name   :", student["name"])
            print("Age    :", student["age"])
            print("Course :", student["course"])
            return

    print("\nStudent not found.")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("\nStudent deleted successfully!")
            return

    print("\nStudent not found.")


while True:

    print("\n==============================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")
