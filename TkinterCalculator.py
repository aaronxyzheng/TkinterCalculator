import customtkinter as ctk

class Calculator(ctk.CTk):
    def __init__(self):
        # Window Setup
        super().__init__(fg_color = '#000000')
        self.geometry('400x600')
        self.title('Calculator')

        # Frames + Grid Layout Setup
        self.text_frame = ctk.CTkFrame(self, fg_color = 'transparent')
        self.button_frame = ctk.CTkFrame(self, fg_color = 'transparent')
        self.columnconfigure(0, weight = 1, uniform = 'a')
        self.rowconfigure(0, weight = 9, uniform = 'a')
        self.rowconfigure((1,2,3,4,5), weight = 4, uniform = 'a')

        # Setup Buttons
        self.setup_buttons()

        self.mainloop()
    def setup_buttons(self):
        # Setup Rows + Columns
        self.button_frame.columnconfigure((0,1,2,3), weight = 1, uniform = 'a')
        self.button_frame.rowconfigure((0,1,2,3,4), weight = 1, uniform = 'a')

        # All Button Attributes
        font = ('Calibri', 32, 'bold')
        corner_radius = 1
        padding = 1.5

        buttons = { # Value in Format: [Text, Bg color, Column, Row, Columnspan, Function]
            'AC': ['AC', '#A5A5A5', 0, 0, 1, self.clear],
            '±': ['±', '#A5A5A5', 1, 0, 1, self.negate],
            '%': ['%', '#A5A5A5', 2, 0, 1, self.percentage],
            '÷': ['÷', '#FF9F0A', 3, 0, 1, self.operation],
            '7': ['7', '#333333', 0, 1, 1, self.number],
            '8': ['8', '#333333', 1, 1, 1, self.number],
            '9': ['9', '#333333', 2, 1, 1, self.number],
            'x': ['x', '#FF9F0A', 3, 1, 1, self.operation],
            '4': ['4', '#333333', 0, 2, 1, self.number],
            '5': ['5', '#333333', 1, 2, 1, self.number],
            '6': ['6', '#333333', 2, 2, 1, self.number],
            '-': ['-', '#FF9F0A', 3, 2, 1, self.operation],
            '1': ['1', '#333333', 0, 3, 1, self.number],
            '2': ['2', '#333333', 1, 3, 1, self.number],
            '3': ['3', '#333333', 2, 3, 1, self.number],
            '+': ['+', '#FF9F0A', 3, 3, 1, self.operation],
            '0': ['0', '#333333', 0, 4, 2, self.number],  # Note columnspan of 2
            '.': ['.', '#333333', 2, 4, 1, self.decimal],
            '=': ['=', '#FF9F0A', 3, 4, 1, self.equals]     
        }
        buttons_with_values = ['0','1','2','3','4','5','6','7','8','9','+','x','÷','-']
        for item in buttons:
            if item in buttons_with_values:
                button = ctk.CTkButton(self.button_frame, text = buttons[item][0], fg_color = buttons[item][1], font = font, corner_radius = corner_radius, command = lambda x = item: buttons[x][5](buttons[x][0]))
                button.grid(column = buttons[item][2], row = buttons[item][3], columnspan = buttons[item][4], sticky = 'nsew', padx = padding, pady = padding)
            else:
                button = ctk.CTkButton(self.button_frame, text = buttons[item][0], fg_color = buttons[item][1], font = font, corner_radius = corner_radius, command = buttons[item][5])
                button.grid(column = buttons[item][2], row = buttons[item][3], columnspan = buttons[item][4], sticky = 'nsew', padx = padding, pady = padding)
        
        self.button_frame.grid(column = 0, row = 1, rowspan = 5, sticky = 'nsew')
    def clear(self):
        print('clear')
    def negate(self):
        print('negate')
    def percentage(self):
        print('percentage')
    def operation(self, input):
        print(input)
    def decimal(self):
        print('decimal')
    def number(self, input):
        print(input) 
    def equals(self):
        print('equals')


calculator = Calculator()

