from decimal import DivisionByZero
from attr import validate
from idna import valid_contextj
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Cgrid(GridLayout):
    def cal(self,result):
        if result:
            try:
                self.show.text=str(eval(result))
            except:
                self.show.text = "ERROR"


        

class calculatorApp(App):
    def build(self):
        return Cgrid()


calculatorApp().run()