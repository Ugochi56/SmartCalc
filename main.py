from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class CalculatorLayout(BoxLayout):
    pass


class PyCalcMobileApp(App):
    expression = StringProperty("")  # This fixes the error

    def build(self):
        return CalculatorLayout()

    def tap(self, value):
        self.expression += str(value)

    def clear_expr(self):
        self.expression = ""

    def calculate(self):
        try:
            self.expression = str(eval(self.expression))
        except:
            self.expression = "Error"


if __name__ == "__main__":
    PyCalcMobileApp().run()
