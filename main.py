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
from Pages.Student_Delete_Page import *

from Global import WINDOW_MANAGER

class Main_Grid(BoxLayout):
    """This is the main app grid."""

    def __init__(self, **kwargs):
        super(Main_Grid, self).__init__(**kwargs)
        self.orientation = "vertical"
        # test_student
        self.add_widget(Page_1())

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