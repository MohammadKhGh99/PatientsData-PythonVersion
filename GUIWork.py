from tkinter import *


class GUI:
    def __init__(self):
        self.__root = Tk()
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(expand=YES, anchor="sw", fill=BOTH)
        self.__canvas.configure(bg='white', height=621, width=723)

    def starting_the_window(self):
        """
        this method starts the window of the game
        :return: returns nothing
        """
        self.__root.configure(background='white')
        self.__root.geometry("960x750")
        self.__root.title("المعالجة بالرقية الشرعية")
        self.starting_buttons()
        self.__root.mainloop()

    def starting_buttons(self):



if __name__ == "__main__":
    gui = GUI()
    gui.starting_the_window()
