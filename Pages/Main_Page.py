
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from settings import *
from Classes.Student import *
from Classes.Student_Roster import ALL_STUDENTS
from Classes.Student_Roster import ROSTER
from Global import WINDOW_MANAGER


class Student_Widget(BoxLayout):
    """Displays the first and last name of a student."""
    def __init__(self, student):
        super(Student_Widget, self).__init__()
        self.orientation="horizontal"

        self.size_hint = student_widget_size_hint
        self.size_hint_y = None
        self.padding = 10

        self.student = student
        print(self.student.name)

        label=Label(text=student.name, font_size=student_widget_font_size)

        edit_button = Button(text="info", )
        edit_button.bind(on_release=self.edit_button_handler)

        sessions_button = Button(text="sessions")
        sessions_button.bind(on_release=self.sessions_button_handler)


        self.add_widget(label)
        self.add_widget(edit_button)
        self.add_widget(sessions_button)

    def edit_button_handler(self, instance):
        ROSTER.set_current_student(self.student)
        WINDOW_MANAGER.current = "second"
        WINDOW_MANAGER.transition.direction="left"

    def sessions_button_handler(self, instance):
        ROSTER.set_current_student(self.student)
        WINDOW_MANAGER.current = "sessions_window"
        WINDOW_MANAGER.transition.direction="left"

class Search_Bar(BoxLayout):
    """A search bar for clients."""

    def __init__(self):

        super(Search_Bar, self).__init__()
        self.orientation = "horizontal"

        self.size_hint = search_bar_size_hint

        self.clear_button = Button(text="clear", font_size=search_bar_button_font_size)

        self.text_input = TextInput(multiline=False
        , font_size = search_bar_text_input_font_size
        , size_hint = search_bar_text_input_size_hint)

        self.search_button = Button(text="search", font_size=search_bar_button_font_size)

        self.clear_button.bind(on_press=self.clear_button_handler)
        self.search_button.bind(on_press=self.search_button_handler)

        self.add_widget(self.clear_button)
        self.add_widget(self.text_input)
        self.add_widget(self.search_button)

    def clear_button_handler(self, instance):
        self.text_input.text = ""
    
    def search_button_handler(self, instance):
        print("Search!")

class Create_Student_Button(BoxLayout):
    """A button to create a new student."""

    def __init__(self):
        super(Create_Student_Button, self).__init__()
        self.orientation="horizontal"
        self.padding = 10

        self.size_hint=create_student_button_size_hint

        self.button = Button(text="new student"
        , font_size=create_student_button_font_size)
        self.button.bind(on_press=self.new_student)

        self.add_widget(self.button)
    
    def new_student(self, instance):
        ROSTER.current_student = None
        WINDOW_MANAGER.current = "second"
        WINDOW_MANAGER.transition.direction = "left"

class Student_Roster(ScrollView):
    """Displays all of the students."""

    def __init__(self):
        super(Student_Roster, self).__init__()
        self.grid = GridLayout(cols=1, size_hint=(1, None))
        self.do_scroll_y = True
        self.do_scroll_x = False
        self.grid.padding = 10

        for student in ALL_STUDENTS.keys():
            self.grid.add_widget(Student_Widget(ALL_STUDENTS[student]))
        
        self.add_widget(self.grid) 

class Page_1(BoxLayout):
    """Displays Page 1."""

    def __init__(self):
        super(Page_1, self).__init__()
        self.orientation="vertical"

        #self.add_widget(Search_Bar())

        self.student_roster = Student_Roster()
        self.add_widget(self.student_roster)

        self.add_widget(Create_Student_Button())     