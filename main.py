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

        # Create container for keypad
        keypad_container = qtw.QWidget()
        keypad_container.setLayout(qtw.QGridLayout())

        # Widgets ---------------
        self.display_field = qtw.QLineEdit()

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
        btn_open_bracket = qtw.QPushButton('(', clicked=lambda: self.num_press('('))
        btn_close_bracket = qtw.QPushButton(')', clicked=lambda: self.num_press(')'))

        # Operators
        btn_add = qtw.QPushButton('+', clicked=lambda: self.func_press('+'))
        btn_subtract = qtw.QPushButton('-', clicked=lambda: self.func_press('-'))
        btn_multiply = qtw.QPushButton('x', clicked=lambda: self.func_press('*'))
        btn_divide = qtw.QPushButton('÷', clicked=lambda: self.func_press('/'))

        # Functions
        btn_equals = qtw.QPushButton('=', clicked=lambda: self.result())
        btn_clear = qtw.QPushButton('C', clicked=lambda: self.clear())

        # Layout ---------------
        keypad_container.layout().addWidget(self.display_field, 0, 0, 1, 4)
        keypad_container.layout().addWidget(btn_clear, 1, 0)
        keypad_container.layout().addWidget(btn_open_bracket, 1, 1)
        keypad_container.layout().addWidget(btn_close_bracket, 1, 2)
        keypad_container.layout().addWidget(btn_divide, 1, 3)

        keypad_container.layout().addWidget(btn_7, 2, 0)
        keypad_container.layout().addWidget(btn_8, 2, 1)
        keypad_container.layout().addWidget(btn_9, 2, 2)
        keypad_container.layout().addWidget(btn_multiply, 2, 3)

        keypad_container.layout().addWidget(btn_4, 3, 0)
        keypad_container.layout().addWidget(btn_5, 3, 1)
        keypad_container.layout().addWidget(btn_6, 3, 2)
        keypad_container.layout().addWidget(btn_subtract, 3, 3)

        keypad_container.layout().addWidget(btn_1, 4, 0)
        keypad_container.layout().addWidget(btn_2, 4, 1)
        keypad_container.layout().addWidget(btn_3, 4, 2)
        keypad_container.layout().addWidget(btn_add, 4, 3)

        keypad_container.layout().addWidget(btn_0, 5, 0, 1, 2)
        keypad_container.layout().addWidget(btn_decimal, 5, 2)
        keypad_container.layout().addWidget(btn_equals, 5, 3)

        self.layout().addWidget(keypad_container)

    # Logic -----------------
    def num_press(self, num):
        """Stores the digits entered and displays it onscreen."""

        self.temp_inputs.append(num)
        input = ''.join(self.temp_inputs)
        # Display inputs
        self.display_field.setText(input)
        # ----------
        print('num_press()')
        print(self.temp_inputs)
        print(self.temp_equation)

    def func_press(self, operator):
        """Creates the equation."""

        # Append all digits entered to the equation list
        input = ''.join(self.temp_inputs)
        self.temp_equation.append(input)

        # Append operator to equation
        self.temp_equation.append(operator)
        equation = ''.join(self.temp_equation)
        # Display equation
        self.display_field.setText(equation)
        self.temp_inputs = []
        # ----------
        print('fun_press()')
        print(self.temp_inputs)
        print(self.temp_equation)

    def result(self):
        """Display result of equation"""

        equation = ''.join(self.temp_equation)
        answer = eval(equation)
        self.display_field.setText(answer)
        # Clear all lists
        self.clear()

    def clear(self):
        """Clears elements from both lists"""
        self.temp_num = []
        self.temp_equation = []
        self.display_field.setText('')
        # ----------
        print('clear()')
        print(self.temp_num)
        print(self.temp_equation)


# Create Application
app = qtw.QApplication([])

# Create Calculator
calc = Window()
calc.show()

# Execute Application
app.exec()
