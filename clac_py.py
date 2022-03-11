from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Cgrid(GridLayout):
    pass

class calculatorApp(App):
    def build(self):
        return Cgrid()


calculatorApp().run()