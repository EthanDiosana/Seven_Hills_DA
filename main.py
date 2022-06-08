from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from Classes.Student_Roster import ROSTER

from settings import *

from Pages.Main_Page import *
from Pages.Student_Info_Page import *
from Pages.Session_Page import *

from Global import WINDOW_MANAGER

class Main_Grid(BoxLayout):
    """This is the main app grid."""

    def __init__(self, **kwargs):
        super(Main_Grid, self).__init__(**kwargs)
        self.orientation = "vertical"
        # test_student
        self.add_widget(Page_1())
        
# Define our different screens.
class First_Window(Screen):
    name="first"

    def on_pre_enter(self):
        ROSTER.load_students()
        self.page = Page_1()
        self.add_widget(self.page)

    def on_pre_leave(self):
        self.remove_widget(self.page)

class Student_Info_Window(Screen):
    name="second"
    
    def on_pre_enter(self):
        self.page = Page_2(ROSTER.current_student)
        self.add_widget(self.page)

    def on_pre_leave(self):
        self.remove_widget(self.page)

class Student_Deletion_Confirmation_Screen(Screen):
    name="student_deletion_confirmation_screen"

    def on_pre_enter(self):
        if(not ROSTER.current_student == None):
            self.main_grid = BoxLayout(orientation="vertical")
            label_grid = BoxLayout(orientation="horizontal")
            button_grid = BoxLayout(orientation="horizontal", padding=10)

            label = Label(text=("Are you sure you want to delete \n" + ROSTER.current_student.name + "?"))
            label_grid.add_widget(label)
            
            no_button = Button(text="no", on_press=self.no)
            yes_button = Button(text="yes", on_press=self.yes)

            button_grid.add_widget(no_button)
            button_grid.add_widget(yes_button)

            self.main_grid.add_widget(label_grid)
            self.main_grid.add_widget(button_grid)

            self.add_widget(self.main_grid)

    def on_pre_leave(self):
        self.remove_widget(self.main_grid)
    
    def yes(self, instance):
        ROSTER.delete_student(ROSTER.current_student)
        ROSTER.set_current_student(None)
        WINDOW_MANAGER.current = "first"
        WINDOW_MANAGER.transition.direction = "left"

    def no(self, instance):
        WINDOW_MANAGER.current = "second"
        WINDOW_MANAGER.transition.direction = "right"


first_window = First_Window()
second_window = Student_Info_Window()
sessions_screen = Sessions_Window()
student_deletion_confirmation_screen = Student_Deletion_Confirmation_Screen()

class Seven_Hills_Driving_Academy(App):
    def build(self):

        WINDOW_MANAGER.add_widget(first_window)
        WINDOW_MANAGER.add_widget(second_window)
        WINDOW_MANAGER.add_widget(sessions_screen)
        WINDOW_MANAGER.add_widget(student_deletion_confirmation_screen)
        return WINDOW_MANAGER


if __name__ == "__main__":
    Seven_Hills_Driving_Academy().run()