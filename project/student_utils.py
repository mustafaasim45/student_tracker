
import pandas as pd

DATA_FILE = "students.csv"

def load_students():
    try:
        df = pd.read_csv(DATA_FILE, dtype={'roll': str}) # Explicitly load 'roll' as string
        if df.empty:
            return {}
        else:
            students_dict = df.set_index('roll').to_dict('index')
            return students_dict
    except FileNotFoundError:
        return {}

def save_students(students_dict):
    df = pd.DataFrame.from_dict(students_dict, orient='index')
    df.index.name = 'roll'
    df.reset_index(inplace=True)
    df.to_csv(DATA_FILE, index=False)

def validate_score(score):
    try:
        score = int(score)
        return 0 <= score <= 100
    except ValueError:
        return False

def get_student_input():
    roll = input("Enter roll number (unique): ")
    name = input("Enter name: ")
    math = input("Math score (0-100): ")
    science = input("Science score (0-100): ")
    english = input("English score (0-100): ")
    attendance = input("Attendance % (0-100): ")

    if not (validate_score(math) and validate_score(science) and validate_score(english) and validate_score(attendance)):
        print("Invalid input. Scores and attendance must be 0–100.")
        return None
    return {"roll": roll, "name": name, "math": math, "science": science, "english": english, "attendance": attendance}


def add_student(students_dict):
    while True:
        try:
            num_students = int(input("How many students do you want to add? "))
            if num_students <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    for _ in range(num_students):
        student_data = get_student_input()
        if student_data is None:
            continue

        if student_data["roll"] in students_dict:
            print(f"Roll number {student_data['roll']} already exists. Skipping.")
            continue

        students_dict[student_data["roll"]] = {
            "name": student_data["name"],
            "math": student_data["math"],
            "science": student_data["science"],
            "english": student_data["english"],
            "attendance": student_data["attendance"]
        }
        print(f"Student {student_data['roll']} added successfully.")

    return students_dict


def view_students(students_dict):
    if not students_dict:
        print("No student records.")
        return
    for roll, student in students_dict.items():
        print(f"Roll: {roll}, Details: {student}")


def search_student(students_dict):
    roll = input("Enter roll number to search: ")
    if roll in students_dict:
        print(f"Roll: {roll}, Details: {students_dict[roll]}")
    else:
        print("Student not found.")


def update_student(students_dict):
    roll = input("Enter roll number to update: ")
    if roll not in students_dict:
        print("Student not found.")
        return students_dict

    student = students_dict[roll]
    print("Leave input blank to keep existing value.")
    student["name"] = input(f"Name ({student['name']}): ") or student["name"]

    for subject in ["math", "science", "english", "attendance"]:
        val = input(f"{subject.capitalize()} ({student[subject]}): ")
        if val:
            if validate_score(val):
                student[subject] = val
            else:
                print(f"Invalid {subject}. Skipping update.")
    print("Student updated.")
    return students_dict


def delete_student(students_dict):
    roll = input("Enter roll number to delete: ")
    if roll in students_dict:
        del students_dict[roll]
        print("Student deleted.")
    else:
        print("Student not found.")
    return students_dict


def generate_report(students_dict):
    if not students_dict:
        print("No data found.")
        return

    df = pd.DataFrame.from_dict(students_dict, orient='index')
    df.index.name = 'roll'
    df.reset_index(inplace=True)

    df[["math", "science", "english", "attendance"]] = df[["math", "science", "english", "attendance"]].astype(float)
    df["average"] = df[["math", "science", "english"]].mean(axis=1)

    print("Total students:", len(df))
    print("Average Math score:", df["math"].mean())
    print("Average Science score:", df["science"].mean())
    print("Average English score:", df["english"].mean())
    print("Average Attendance:", df["attendance"].mean())

    high_achievers = df[df["average"] >= 90]
    print("Students with average >= 90:", len(high_achievers))

    failed = df[(df["average"] < 60) | (df["attendance"] < 75)]
    print("Students who failed:", len(failed))

    print("\nTop Performers:")
    print(df.sort_values(by="average", ascending=False)[["name", "average"]].head())
