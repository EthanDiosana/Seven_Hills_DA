from Classes.Session import Session
import json

class Student():
    """Holds all of the information of a single Student."""

    def __init__(self, first_name:str, last_name:str, address:str
    , email:str, phone_number:str, license_number:str, license_expiry_date:str):
        self.first_name = str(first_name).rstrip()
        self.last_name = str(last_name).rstrip()
        self.name = self.first_name + " " + self.last_name
        self.address = str(address).rstrip()
        self.email = str(email).rstrip()
        self.phone_number = str(phone_number).rstrip()
        self.license_number = str(license_number).rstrip()
        self.license_expiry_date = str(license_number).rstrip()
        self.sessions = {} # Sessions are appended.

    def to_dictionary(self):
        """Returns a dictionary version of the Student."""
        student_info = {
            "first name" : self.first_name,
            "last name" : self.last_name,
            "address" : self.address,
            "email" : self.email,
            "phone number" : self.phone_number,
            "license number" : self.license_number,
            "license expiry date" : self.license_expiry_date,
            "sessions" : self.sessions
        }
        return student_info

    def add_session(self):
        """Adds a session. Automatically records date and time."""
        current_number_of_sessions = len(self.sessions)
        new_session = Session()
        self.sessions[current_number_of_sessions + 1] = new_session

    def to_string(self):
        """Prints all of the Student information as a reasable string."""

    def save_information(self):
        """Dumps all of the student info into a .json file as a dictionary."""
        file_name = ("Save_Files/" + self.first_name + "_" + self.last_name + ".json")
        
        with open(file_name, 'w') as file_object:
            json.dump(self.to_dictionary(), file_object)

    def load_information(self):
        """Loads all of the student info from a .json file from a dictionary."""

def init_from_dictionary(dictionary):
        """Returns a Student from a dictionary."""
        new_student = Student(
             dictionary["first name"]
        , dictionary["last name"]
        , dictionary["address"]
        , dictionary["email"]
        , dictionary["phone number"]
        , dictionary["license number"]
        , dictionary["license expiry date"])
        if "sessions" not in dictionary:
            dictionary["sessions"] = {}
        else:
            new_student.sessions = dictionary["sessions"]
        return new_student


