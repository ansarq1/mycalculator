from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation

Window.size = (500, 700)

Builder.load_file('calculator1.kv')

class MyCalculator(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def number_press(self, button):
        prior = self.ids.calc_input.text

        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"

        elif prior == "Syntax Error":
            self.ids.calc_input.text = f"{button}"

        else:
            self.ids.calc_input.text = f"{prior}{button}"

    def operator(self, button):
        prior = self.ids.calc_input.text
        number_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        last_character = prior[-1]
        if last_character in number_array:
            self.ids.calc_input.text = f"{prior}{button}"
        else:
            self.ids.calc_input.text = prior


    def decimal(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        num_list[-1]
        number_array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        last_character = prior[-1]
        if last_character in number_array:
            if "+" in prior and "." not in num_list[-1]:
                prior = f"{prior}."
                self.ids.calc_input.text = prior
            elif "." in prior:
                pass
            else:
                self.ids.calc_input.text = f"{prior}."
        else:
            self.ids.calc_input.text = prior

        if "." in prior:
            pass
        else:
            self.ids.calc_input.text = f"{prior}."




    def equals(self):
        try:
            prior = self.ids.calc_input.text
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except ZeroDivisionError:
            self.ids.calc_input.text = "Syntax Error"

    def delete(self):
        prior = self.ids.calc_input.text[:-1]
        self.ids.calc_input.text = prior

    def sign(self):
        prior = self.ids.calc_input.text

        if "-" in prior:
            self.ids.calc_input.text = f"{prior.replace('-', '')}"
        else:
            self.ids.calc_input.text = f"-{prior}"







class CalculatorApp(App):
    def build(self):
        return MyCalculator()

if __name__ == '__main__':
    CalculatorApp().run()