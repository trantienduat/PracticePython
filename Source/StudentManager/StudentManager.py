from Libraries import Constants

# Class contains List of student for managing students
class StudentManager:
    student_list = []

    # add_student function is used for adding new student into the List
    def add_student(self, student):
        # a List of student used for storing student
        self.student_list.append(student)
        print(Constants.INFO_STATUS + ' Add student success!')

    # delete_student function is used for remove a existed student in the List
    # and return the deleted student value
    def delete_student(self, studentId):
        index = self.__get_index_by_id__(studentId)
        if (index != -1):
            removed_student = self.student_list.pop(index)
            return removed_student
        else:
            return None

    # get index of student in the List with specific id
    def __get_index_by_id__ (self, student_id):
        for student in self.student_list:
            if student_id == student.id:
                index = self.student_list.index(student)
                return index
        return -1;


    # display the list
    def display_all_students(self):
        print('========== Student Information ==========')
        # print top edge
        print(Constants.FORMAT_EDGE % ('-'*10, '-'*17, '-'*7, '-'*12, '-'*22, '-'*32))
        # print column names
        print(Constants.FORMAT_COLUMN.format('ID', 'Name', 'Age', 'Gender', 'Address', 'Email'))
        print(Constants.FORMAT_EDGE % ('-' * 10, '-' * 17, '-' * 7, '-' * 12, '-' * 22, '-' * 32))

        for student in self.student_list:
            student.display_details()

        # print bottom edge
        print(Constants.FORMAT_EDGE % ('-' * 10, '-' * 17, '-' * 7, '-' * 12, '-' * 22, '-' * 32))


    # initialize new list when create new instance of StudentManager static method
    @staticmethod
    def init_new_list(self):
        student_list = []
        return student_list;