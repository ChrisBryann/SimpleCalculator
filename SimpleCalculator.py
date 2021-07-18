#Created by: Christopher Bryan
#Purpose: Create a simple calculator

import tkinter as tk
import tkinter.messagebox as tkmb

class Calculator(tk.Tk):
    def __init__(self):
        '''constructor for the calculator'''
        super().__init__()
        self.operatorList = []
        self.numberList = []
        self.geometry('355x350')
        self.resizable(False, False)
        self.title('Simple Calculator')
        self.configure(background='#7C83FD')
        self.display = tk.StringVar()
        self.display.set('0')
        displayFrame = tk.Frame(self)
        self.displayLabel = tk.Label(displayFrame, textvariable=self.display, fg='blue', width=50, bg='#96BAFF', anchor='e')
        self.displayLabel.pack()
        displayFrame.grid(sticky='e', columnspan=4)
        tk.Button(self, text='7', width=5, height=3, command=lambda: self.numbers('7')).grid(row=1, column=0, sticky='we', padx=5, pady=5)
        tk.Button(self, text='8', width=5, height=3, command=lambda: self.numbers('8')).grid(row=1, column=1, sticky='we', padx=5, pady=5)
        tk.Button(self, text='9', width=5, height=3, command=lambda: self.numbers('9')).grid(row=1, column=2, sticky='we', padx=5, pady=5)
        tk.Button(self, text='+', width=5, height=3, command=lambda: self.operator('+', self.display.get())).grid(row=1, column=3, sticky='we', padx=5, pady=5)
        tk.Button(self, text='4', width=5, height=3, command=lambda: self.numbers('4')).grid(row=2, column=0,
                                                                                             sticky='we', padx=5, pady=5)
        tk.Button(self, text='5', width=5, height=3, command=lambda: self.numbers('5')).grid(row=2, column=1,
                                                                                             sticky='we', padx=5, pady=5)
        tk.Button(self, text='6', width=5, height=3, command=lambda: self.numbers('6')).grid(row=2, column=2,
                                                                                             sticky='we', padx=5, pady=5)
        tk.Button(self, text='-', width=5, height=3, command=lambda: self.operator('-', self.display.get())).grid(row=2,
                                                                                                                  column=3,
                                                                                                                  sticky='we', padx=5, pady=5)
        tk.Button(self, text='1', width=5, height=3, command=lambda: self.numbers('1')).grid(row=3, column=0,
                                                                                             sticky='we', padx=5,
                                                                                             pady=5)
        tk.Button(self, text='2', width=5, height=3, command=lambda: self.numbers('2')).grid(row=3, column=1,
                                                                                             sticky='we', padx=5,
                                                                                             pady=5)
        tk.Button(self, text='3', width=5, height=3, command=lambda: self.numbers('3')).grid(row=3, column=2,
                                                                                             sticky='we', padx=5,
                                                                                             pady=5)
        tk.Button(self, text='x', width=5, height=3, command=lambda: self.operator('x', self.display.get())).grid(row=3,
                                                                                                                  column=3,
                                                                                                                  sticky='we',
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        tk.Button(self, text='0', width=5, height=3, command=lambda: self.numbers('0')).grid(row=4, columnspan=3,
                                                                                             sticky='we', padx=5,
                                                                                             pady=5)
        tk.Button(self, text='/', width=5, height=3, command=lambda: self.operator('/', self.display.get())).grid(row=4,
                                                                                                                  column=3,
                                                                                                                  sticky='we',
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        tk.Button(self, text='AC', width=5, height=3, command=self.clear).grid(row=5, columnspan=2,
                                                                                             sticky='we', padx=5,
                                                                                             pady=5)
        tk.Button(self, text='=', width=5, height=3, command=lambda: self.results(self.display.get())).grid(row=5, column=2, columnspan=2,
                                                                                             sticky='we', padx=5,
                                                                                             pady=5)
        self.protocol("WM_DELETE_WINDOW", self.enterX)

    def numbers(self, number):
        if self.display.get() == '0' or self.display.get() == 'ERROR':
            self.display.set(str(number))
        else:
            if '.' in self.display.get():
                self.display.set(str(number))
            else:
                self.display.set(self.display.get() + str(number))

        self.displayLabel['textvariable'] = self.display

    def operator(self, operator, number): #repeatedly pressing operators causes error (corrected)
        if number != 'ERROR' and number != '':
            self.operatorList.append(operator)
            self.numberList.append(float(number))
            self.display.set('')
        elif number == 'ERROR':
            tkmb.showerror('Error', 'Cannot operate ERROR with a number. Will clear the display now!')
            self.clear()

    def results(self, number):
        if len(self.operatorList) != 0:
            self.numberList.append(int(number))
            result = 0

            for operator in self.operatorList:
                if result == "ERROR":
                    break
                if operator == '+':
                    result = self.numberList[0] + self.numberList[1]
                elif operator == '-':
                    result = self.numberList[0] - self.numberList[1]
                elif operator == 'x':
                    result = self.numberList[0] * self.numberList[1]
                else:
                    result = self.numberList[0] / self.numberList[1] if self.numberList[1] != 0 else "ERROR"
                self.numberList = self.numberList[1:]
                self.numberList[0] = result
            if result != 'ERROR':
                result = float(result)
            self.display.set(str(result))
            self.displayLabel['textvariable'] = self.display
            self.operatorList = []
            self.numberList = []

    def clear(self):
        self.display.set('0')
        self.operatorList = []
        self.numberList = []

    def enterX(self):
        tkmb.showinfo('Thank You!', 'Thank you for using Simple Calculator created by Christopher Bryan!')
        self.destroy()
        self.quit()


# the code below is to run the SimpleCalculator application -- mainloop() runs the application.
calc = Calculator()
calc.mainloop()




