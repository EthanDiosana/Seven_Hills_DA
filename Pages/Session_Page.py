from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from Classes.Student_Roster import ROSTER
from Classes.Session import Session

from settings import *
from Global import WINDOW_MANAGER

class Text_Input_Field(TextInput):

    def insert_text(self, substring, from_undo=False):
        print("aaaaa")
        return super().insert_text(substring, from_undo)


class Session_Widget(BoxLayout):

    def __init__(self, session):
        super(Session_Widget, self).__init__()
        self.orientation = "vertical"

        self.expanded = False

        self.size_hint = (1, None)
        
        self.top_bar = BoxLayout(orientation="horizontal")
        self.top_bar.size_hint = (1, 0.5)

        label = Label(text=session.date_string)
        label.size_hint = (None, 1)
        label2 = Label(text="")
        expand_button = Button(text="expand", on_release=self.expand_collapse)
        expand_button.size_hint = (None, 1)

        self.notes_area = Text_Input_Field(text=session.notes)


        self.top_bar.add_widget(label)
        self.top_bar.add_widget(label2)
        self.top_bar.add_widget(expand_button)

        self.add_widget(self.top_bar)
        self.add_widget(self.notes_area)

    def expand_collapse(self, instance):

        if(not self.expanded):
            instance.text = "collapse"
            self.height = 200
            self.notes_area.height = 200
            self.expanded = True
        else:
            instance.text = "expand"
            self.height = 100
            self.notes_area.height = 50
            self.expanded = False

class Session_Roster(ScrollView):

    def __init__(self):
        super(Session_Roster, self).__init__()
        self.grid = GridLayout(cols=1, size_hint=(1, None))
        self.do_scroll_y = True
        self.do_scroll_x = False
        self.grid.padding = 10
        
        CURRENT_STUDENT = ROSTER.current_student

        for session in CURRENT_STUDENT.sessions:
            self.grid.add_widget(Session_Widget(Session.from_dictionary(self, CURRENT_STUDENT.sessions[session])))
        
        self.add_widget(self.grid)      

class New_Session_Button(Button):
    """The button to create a new Session for the given Student."""

    def __init__(self):
        super(New_Session_Button, self).__init__()
        self.text="new session"
        self.bind(on_release=self.handler)

    def handler(self, instance):
        ROSTER.current_student.add_session()
        ROSTER.current_student.save_information()
        WINDOW_MANAGER.current = "first"
        WINDOW_MANAGER.current = "sessions_window"

class Sessions_Page(BoxLayout):

    def __init__(self, student):
        super(Sessions_Page, self).__init__()
        self.orientation="vertical"
        
        top_bar_grid = BoxLayout(orientation="horizontal")
        back_button = Button(text="back", size_hint=student_page_info_back_button_size_hint, on_press=self.back)
        new_session_button = New_Session_Button()
        top_bar_grid.add_widget(back_button)
        top_bar_grid.add_widget(new_session_button)
        top_bar_grid.size_hint = (1, None)
        session_roster = Session_Roster()

        self.add_widget(top_bar_grid)
        self.add_widget(session_roster)
    
    def back(self, instance):
        WINDOW_MANAGER.current = "first"
        WINDOW_MANAGER.transition.direction = "right"

class Sessions_Window(Screen):
    name = "sessions_window"
    
    def on_pre_enter(self):
        print("Entering Sessions Window.")
        self.page = Sessions_Page(ROSTER.current_student)
        self.add_widget(self.page)

    def on_pre_leave(self):
        self.remove_widget(self.page)
        print("Exiting Sessions Window.")
