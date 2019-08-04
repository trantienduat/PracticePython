from Libraries import Constants

class Student:
    id = ""
    name = ""
    age = ""
    gender = ""
    address = ""
    email = ""

    # constructor for student class
    def set_attributes(self, id, name, age, gender, address, email):
        # set the attributes with an initial value
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.email = email

    # displayDetails is used for displaying details of student objects
    def display_details(self):
        print(Constants.FORMAT_RECORD % (self.id, self.name, self.age, self.gender, self.address, self.email))

    def __str__(self):
        output ='ID: {}\nName: {}\nAge: {}\nGender: {}\nAddress: {}\nEmail: {}\n'.\
            format(self.id, self.name, self.age, self.gender, self.address, self.email)
        return output

    # create a new student with input data from user
    def create_new_student(self):
        self.id = input('Enter student\'s id: ')
        self.name = input('Enter student\'s name: ')
        self.age = input('Enter student\'s age: ')
        self.gender = input('Enter student\'s gender: ')
        self.address = input('Enter student\'s address: ')
        self.email = input('Enter student\'s email: ')
