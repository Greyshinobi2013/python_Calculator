from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class HelloWorld(App):
    def __init__(self, **kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='user Name'))
        self.username=TextInput(multiline=false)
        self.add_widget(Label(text=''))
    def build(self, **kwargs):
        
    