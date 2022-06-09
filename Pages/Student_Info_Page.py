from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

from Classes.Student_Roster import ROSTER
from Classes.Student import *
from settings import *
from Global import WINDOW_MANAGER

class New_Student_Info_Widget(BoxLayout):
    """Creates an information field widget for a non-existing Student."""

    def __init__(self, attribute_name):
        
        super(New_Student_Info_Widget, self).__init__()
        self.orientation = "horizontal"
        self.padding = student_page_info_padding

        self.label = Label(text=attribute_name)
        self.text_input_field = TextInput(multiline=False, disabled=False, size_hint=(1,1))
        self.empty_label = Label(text="", size_hint=(0.25, 1))
        self.add_widget(self.label)
        self.add_widget(self.text_input_field)
        self.add_widget(self.empty_label)

class Existing_Student_Info_Widget(BoxLayout):
    """Creates an information field widget for an existing Student."""

    def __init__(self, attribute_name, attribute_value):
        
        super(Existing_Student_Info_Widget, self).__init__()
        self.orientation = "horizontal"
        self.padding = student_page_info_padding

        self.label = Label(text=attribute_name)
        self.text_input_field = TextInput(text=attribute_value, multiline=False, disabled=True, size_hint=(1,1), on_text_validate=self.text_input_field_handler)
        self.edit_button = Button(text="edit", size_hint=(0.25, 1), on_release=self.edit_button_handler)
        self.add_widget(self.label)
        self.add_widget(self.text_input_field)
        self.add_widget(self.edit_button)

    def edit_button_handler(self, instance):
        self.text_input_field.disabled = False
        self.text_input_field.focus = True

    def text_input_field_handler(self, instance):
        self.text_input_field.disabled = True

class Student_Page(BoxLayout):
    """Displays the selected Student's information."""

    def __init__(self, student):
        super(Student_Page, self).__init__()
        self.orientation="vertical"

        back_button_grid = BoxLayout(orientation="horizontal", padding=student_page_info_padding, size_hint=student_page_info_back_button_size_hint)
        back_button = Button(text="back")
        back_button_grid.add_widget(back_button)
        back_button.bind(on_release=self.back)

        delete_button = Button(text="delete")
        back_button_grid.add_widget(delete_button)
        delete_button.bind(on_release=self.delete)

        save_button_grid = BoxLayout(orientation="horizontal", padding=student_page_info_padding)
        save_button = Button(text="save")
        save_button.bind(on_release=self.save)

        self.add_widget(back_button_grid)

        fields_grid = BoxLayout(orientation="vertical", size_hint_y=5)

        if student == None:
            delete_button.disabled = True
            for attribute in Student(None, None, None, None, None, None, None).to_dictionary().keys():
                if not (attribute == "sessions"): # Only create if attribute is not session.
                    fields_grid.add_widget(New_Student_Info_Widget(attribute))
        else:
            dictionary = student.to_dictionary()
            for attribute in dictionary.keys():
                if not attribute == "sessions":
                    fields_grid.add_widget(Existing_Student_Info_Widget(attribute, dictionary[attribute]))
            save_button.disabled = True

        self.add_widget(fields_grid)

        save_button_grid.add_widget(save_button)

        self.add_widget(save_button_grid)

    def back(self, instance):
        WINDOW_MANAGER.current = "first"
        WINDOW_MANAGER.transition.direction = "right"

    def delete(self, instance):
        WINDOW_MANAGER.current = "student_deletion_confirmation_screen"
        WINDOW_MANAGER.transition.direction = "left"

    def save(self, instance):
        dictionary = {}
        all_filled = True
        for child in self.children[1].children:
            text_input = child.text_input_field
            label = child.label
            if(text_input.text == None or len(text_input.text) == 0):
                all_filled = False
                text_input.hint_text = "Please enter info."
            else:
                dictionary[label.text] = text_input.text

        if all_filled:
            new_student = init_from_dictionary(dictionary)
            new_student.save_information()
            WINDOW_MANAGER.current = "first"
            WINDOW_MANAGER.transition.direction = "right"

class Page_2(BoxLayout):

    """Displays Page 2."""

    def __init__(self, student):
        super(Page_2, self).__init__()
        self.orientation="vertical"
        self.add_widget(Student_Page(student))

class Student_Info_Window(Screen):
    name="second"
    
    def on_pre_enter(self):
        self.page = Page_2(ROSTER.current_student)
        self.add_widget(self.page)

    def on_pre_leave(self):
        self.remove_widget(self.page)
