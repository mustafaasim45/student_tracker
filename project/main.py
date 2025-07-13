def main():
   
    correct_username = "admin"
    correct_password = "password123"
    max_attempts = 3

    for attempt in range(max_attempts):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Login successful!")
            students_dict = load_students()
            while True:
                print("\nStudent Management System")
                print("1. Add Student")
                print("2. View Students")
                print("3. Search Student")
                print("4. Update Student")
                print("5. Delete Student")
                print("6. Generate Report")
                print("7. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    students_dict = add_student(students_dict)
                elif choice == "2":
                    view_students(students_dict)
                elif choice == "3":
                    search_student(students_dict)
                elif choice == "4":
                    students_dict = update_student(students_dict)
                elif choice == "5":
                    students_dict = delete_student(students_dict)
                elif choice == "6":
                    generate_report(students_dict)
                elif choice == "7":
                    save_students(students_dict)
                    print("Exiting Student Management System. Data saved.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            break 
        else:
            remaining_attempts = max_attempts - (attempt + 1)
            if remaining_attempts > 0:
                print(f"Invalid username or password. {remaining_attempts} attempts remaining.")
            else:
                print("Maximum login attempts reached. Exiting.")
                return 


if __name__ == "__main__":
    main()