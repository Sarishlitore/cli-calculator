import calc_utilities
from tkinter import *

def calculator():
    root = Tk()     # создаем корневой объект - окно
    root.title("Calculator")     # устанавливаем заголовок окна
    root.geometry("300x250")    # устанавливаем размеры окна
    
    label = Label(text="Calculator") # создаем текстовую метку
    label.pack()    # размещаем метку в окне
    
    root.mainloop()


if __name__ == '__main__':
    calculator()