from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from Global import *

from Classes.Student_Roster import ROSTER

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

