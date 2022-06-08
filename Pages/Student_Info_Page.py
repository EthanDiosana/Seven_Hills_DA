from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


from Classes.Student import *
from settings import *
from Global import WINDOW_MANAGER


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
                if not attribute == "sessions":
                    grid = BoxLayout(orientation="horizontal")
                    label = Label(text=attribute)
                    text_input = TextInput(multiline=False, disabled=False, size_hint=student_page_text_input_size_hint)
                    grid.add_widget(label)
                    grid.add_widget(text_input)
                    grid.add_widget(Label())
                    grid.padding = student_page_info_padding
                    fields_grid.add_widget(grid)
            self.add_widget(fields_grid)
        else:
            dictionary = student.to_dictionary()
            for attribute in dictionary.keys():
                if not attribute == "sessions":
                    grid = BoxLayout(orientation="horizontal")
                    label = Label(text=attribute)
                    text_input = TextInput(text=dictionary[attribute],multiline=False, disabled=True, size_hint=student_page_text_input_size_hint)
                    grid.add_widget(label)
                    grid.add_widget(text_input)
                    grid.add_widget(Button(text="edit"))
                    grid.padding = student_page_info_padding
                    fields_grid.add_widget(grid)
            self.add_widget(fields_grid)
            save_button.disabled = True

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
            text_input = child.children[1]
            label = child.children[2]
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