from tkinter import CURRENT
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen

from Classes.Student_Roster import ROSTER

from settings import *
from Global import WINDOW_MANAGER

class Session_Widget(BoxLayout):

    def __init__(self, session):
        super(Sessions_Page, self).__init__()
        self.orientation = "vertical"

        self.expanded = False

        top_bar = BoxLayout(orientation="horizontal")
        self.notes_grid = BoxLayout(orientation="vertical")

        label = Label(text=session.date_string)
        expand_button = Button(text="expand", on_press=self.expand_collapse)
        notes_area = TextInput(text=session.notes)

        top_bar.add_widget(label)
        top_bar.add_widget(expand_button)

        self.notes_grid.add_widget(notes_area)

        self.add_widget(top_bar)
        self.add_widget(self.notes_grid)

    def expand_collapse(self, instance):

        if(not self.expanded):
            self.notes_grid.size_hint = (1,1)
            self.expanded = True
        else:
            self.notes_grid.size_hint = (0,0)
            self.expanded = False

class Session_Roster(ScrollView):

    def __init__(self):
        super(Session_Roster, self).__init__()
        self.grid = GridLayout(cols=1, size_hint=(1, None))
        self.do_scroll_y = True
        self.do_scroll_x = False
        self.grid.padding = 10
        
        CURRENT_STUDENT = ROSTER.current_student

        for session in CURRENT_STUDENT.sessions.keys():
            self.grid.add_widget(Session_Widget(session))
        
        self.add_widget(self.grid)      

class Session_Page_New_Session_Button(BoxLayout):

    """A button to create a new Session."""

    def __init__(self):
        super(Session_Page_New_Session_Button, self).__init__()
        self.orientation="horizontal"
        self.padding = 10

        self.size_hint=create_student_button_size_hint

        self.button = Button(text="new session"
        , font_size=create_student_button_font_size)
        self.button.bind(on_press=self.new_button)

        self.add_widget(self.button)
    
    def new_student(self, instance):
        ROSTER.current_student = None
        WINDOW_MANAGER.current = "second"
        WINDOW_MANAGER.transition.direction = "left"
    pass

class Sessions_Page(BoxLayout):

    def __init__(self, student):
        super(Sessions_Page, self).__init__()
        self.orientation="vertical"
        
        top_bar_grid = BoxLayout(orientation="horizontal")
        back_button = Button(text="back", size_hint=student_page_info_back_button_size_hint, on_press=self.back)
        new_session_button = Button(text="new session")
        top_bar_grid.add_widget(back_button)
        top_bar_grid.add_widget(new_session_button)
        session_roster = Session_Roster()

        self.add_widget(top_bar_grid)
        self.add_widget(session_roster)
    
    def back(self, instance):
        WINDOW_MANAGER.current = "first"
        WINDOW_MANAGER.transition.direction = "right"

class Sessions_Window(Screen):
    name = "sessions_window"
    
    def on_pre_enter(self):
        print("Entering sessions window.")
        self.page = Sessions_Page(ROSTER.current_student)
        self.add_widget(self.page)
