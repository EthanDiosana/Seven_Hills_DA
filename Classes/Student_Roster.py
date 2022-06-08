import os
import json

from Classes.Student import *

class Student_Roster():
    """Holds multiple students."""

    all_students = {}

    current_student = None

    def add_student(self, student):
        """Adds a Student to the all_students dictionary."""
        if(student.name in self.all_students):
            print("Student already in all_students. Updating.")
            self.all_students[student.name] = student
        else:
            self.all_students[student.name] = student

    def delete_student(self, student):
        """Removes a Student from save files."""
        os.remove("Save_Files/" + student.first_name + "_" + student.last_name + ".json")
        del self.all_students[student.name]
        

    def load_student_from_json(self, file_name):
        """Returns a Student from a .json file."""
        dictionary = {}
        with open(file_name, 'r') as file_object:
            dictionary = json.load(file_object)
        loaded_student = init_from_dictionary(dictionary)
        return loaded_student


    def load_students(self):
        """Loads all Students from files."""
        path = "Save_Files/"
        dir_list = os.listdir(path)
        if len(dir_list) == 0:
            print("No students in " + path)
        else:
            for file in dir_list:
                loaded_student = self.load_student_from_json(path + str(file))
                self.add_student(loaded_student)

    def save_all_students(self, student):
        """Saves a Student to a .json file."""
        pass

    def set_current_student(self, student):
        """Sets the current_student field."""
        self.current_student = student

    def print_all_students(self):
        """Prints all of the students in the roster to the console."""
        for student in self.all_students:
            print(student)


ROSTER = Student_Roster()
ROSTER.load_students()
ALL_STUDENTS = ROSTER.all_students