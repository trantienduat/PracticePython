from Libraries import *
from Student import Student
from StudentManager import StudentManager


def main():
    # Add item into Menu
    menu = Menu()
    menu.add_item_to_menu("Add 1 student.")
    menu.add_item_to_menu("Display all students.")
    menu.add_item_to_menu("Delete a student.")
    menu.add_item_to_menu("Quit the application.")

    # Create instance of Student Manager
    student_manager = StudentManager()

    is_continue = True
    while is_continue:
        # Display menu list
        menu.display_menu(' <=-=-=-=-=-=> Welcome to Student Management Application <=-=-=-=-=-=> ')
        print()
        # get input option from user and validate until valid
        choice = menu.get_option_from_user()
        print()

        if choice == 1:
            # Add new a student
            add_new_a_student(student_manager)

        if choice == 2:
            # Display all student information
            student_manager.display_all_students()
            print()

        if choice == 3:
            # Delete a student by input ID
            delete_a_student(student_manager)

        if choice == menu.items.__len__():
            # End the Application
            is_continue = False
            print()
            print('---THANKS FOR USING APPLICATION---')


def add_new_a_student(student_manager):
    print('[ Adding a new student information ]')
    new_student = Student()
    new_student.create_new_student()
    student_manager.add_student(new_student)
    print()


def delete_a_student(student_manager):
    student_id = input('Enter studentID for deleting: ')
    student = student_manager.delete_student(student_id)
    if (student != None):
        print('---Deleted Student---')
        print(student)
    else:
        print(Constants.ERROR_STATUS, '', 'Entered studentID is not found')
    print()


if __name__ == "__main__":
    main()

