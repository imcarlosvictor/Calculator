import sys

from PyQt5 import QtWidgets as qtw


class Window(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()

        self.temp_inputs = []
        self.temp_equation = []

        self.show()

    def keypad(self):
        """Create buttons for calculator."""

        self.display_label = qtw.QLabel()

        # Buttons ---------------
        # Numbers
        btn_decimal = qtw.QPushButton('.', clicked=lambda: self.num_press('.'))
        btn_0 = qtw.QPushButton('0', clicked=lambda: self.num_press('0'))
        btn_1 = qtw.QPushButton('1', clicked=lambda: self.num_press('1'))
        btn_2 = qtw.QPushButton('2', clicked=lambda: self.num_press('2'))
        btn_3 = qtw.QPushButton('3', clicked=lambda: self.num_press('3'))
        btn_4 = qtw.QPushButton('4', clicked=lambda: self.num_press('4'))
        btn_5 = qtw.QPushButton('5', clicked=lambda: self.num_press('5'))
        btn_6 = qtw.QPushButton('6', clicked=lambda: self.num_press('6'))
        btn_7 = qtw.QPushButton('7', clicked=lambda: self.num_press('7'))
        btn_8 = qtw.QPushButton('8', clicked=lambda: self.num_press('8'))
        btn_9 = qtw.QPushButton('9', clicked=lambda: self.num_press('9'))

        # Operators
        btn_add = qtw.QPushButton('+', clicked=lambda: self.func_press('+'))
        btn_subtract = qtw.QPushButton('-', clicked=lambda: self.func_press('-'))
        btn_multiply = qtw.QPushButton('x', clicked=lambda: self.func_press('*'))
        btn_divide = qtw.QPushButton('÷', clicked=lambda: self.func_press('/'))

        # Functions
        btn_result = qtw.QPushButton('C', clicked=lambda: self.result())
        btn_clear = qtw.QPushButton('C', clicked=lambda: self.clear())

    def num_press(self, num):
        """Stores the digits entered and displays it onscreen."""
        self.temp_inputs.append(num)
        input = ''.join(self.temp_inputs)
        self.display_label.setText(input)

    def func_press(self, operator):
        """Creates the equation."""

        # TODO: convert elements to string?

        # Append all digits entered to the equation list
        input = ''.join(self.temp_inputs)
        self.temp_equation.append(input)
        # Append operator to equation
        equation = self.temp_equation.append(operator)
        equation = ''.join(self.temp_equation)
        # Display equation
        self.display_label.setText(equation)
        self.temp_num = []

    def result(self):
        equation = ''.join(self.temp_equation)
        answer = eval(equation)
        self.display_label.setText(answer)
        # Clear storage
        self.clear()

    def clear(self):
        """Clears elements from both lists"""
        self.temp_num = []
        self.temp_equation = []

# Create Application
app = qtw.QApplication([])

# Create Calculator
calc = Window()
calc.show()

# Execute Application
app.exec()
