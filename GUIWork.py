import os
from tkinter import *
from tkinter.messagebox import askyesno


class GUI:
    def __init__(self):
        self.__root = Tk()
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(anchor="sw", side=LEFT)
        self.__canvas.configure(bg='grey', height=960, width=723)
        self.__buttons = []
        self.__canvas_content = []

    def starting_the_window(self):
        """
        this method starts the window of the game
        :return: returns nothing
        """
        self.__root.configure(background='grey')
        self.__root.geometry("960x750")
        self.__root.title("المعالجة بالرقية الشرعية")
        self.starting_buttons()
        self.__root.mainloop()

    def delete_canvas_content(self):
        for content in self.__canvas_content:
            content.destroy()
            # self.__canvas.delete(content)
            # self.__canvas_content.remove(content)
        self.__canvas_content = []

    def __search_button_func(self):
        self.delete_canvas_content()
        name = StringVar()

        def done_func(event="<Return>"):
            nonlocal name
            name = name.get()
            search_entry.destroy()
            done_search.destroy()
            print(name)
        done_search = Button(self.__canvas, text="البحث", font=("Times", 12), command=done_func)
        done_search.place(relx=1, rely=0.1, anchor="e")
        # self.__canvas_content.append(done_search)
        search_entry = Entry(self.__canvas, width=48, font=("Times", 20), textvariable=name, justify="right")
        search_entry.place(relx=0.92, rely=0.099, anchor="e")
        search_entry.bind("<Return>", done_func)
        self.__canvas_content += [done_search, search_entry]

    def add_new_button_func(self):
        # self.__canvas.delete(0, END)
        self.delete_canvas_content()
        name_label = Label(self.__canvas, text=":الإسم", font=("Times", 15), bg="grey")
        name_label.place(relx=0.99, rely=0.05, anchor="e")
        name_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        # name_text.tag_config(justify="right", tagName="tag-right")
        name_text.place(relx=0.85, rely=0.05, anchor="e")
        name = name_text.get(1.0, "end")

        pid_label = Label(self.__canvas, text=":رقم الهوية", font=("Times", 15), bg="grey")
        pid_label.place(relx=0.99, rely=0.15, anchor="e")
        pid_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        pid_text.place(relx=0.85, rely=0.15, anchor="e")
        pid = int(pid_text.get(1.0, "end"))

        age_label = Label(self.__canvas, text=":العمر", font=("Times", 15), bg="grey")
        age_label.place(relx=0.99, rely=0.25, anchor="e")
        age_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        age_text.place(relx=0.85, rely=0.25, anchor="e")
        age = float(age_text.get(1.0, "end"))

        come_label = Label(self.__canvas, text=":سبب القدوم", font=("Times", 15), bg="grey")
        come_label.place(relx=0.99, rely=0.35, anchor="e")
        come_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        come_text.place(relx=0.85, rely=0.35, anchor="e")
        come_cause = come_text.get(1.0, "end")

        absent_label = Label(self.__canvas, text=":سبب الغياب", font=("Times", 15), bg="grey")
        absent_label.place(relx=0.99, rely=0.45, anchor="e")
        absent_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        absent_text.place(relx=0.85, rely=0.45, anchor="e")
        absent_cause = absent_text.get(1.0, "end")

        finish_label = Label(self.__canvas, text=":سبب الإنتهاء", font=("Times", 15), bg="grey")
        finish_label.place(relx=0.99, rely=0.55, anchor="e")
        finish_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        finish_text.place(relx=0.85, rely=0.55, anchor="e")
        finish_cause = finish_text.get(1.0, "end")

        dates_label = Label(self.__canvas, text=":تواريخ القدوم", font=("Times", 15), bg="grey")
        dates_label.place(relx=0.99, rely=0.65, anchor="e")
        dates_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        dates_text.place(relx=0.85, rely=0.65, anchor="e")
        dates = dates_text.get(1.0, "end").split(',')

        symptoms_label = Label(self.__canvas, text=":الأعراض", font=("Times", 15), bg="grey")
        symptoms_label.place(relx=0.99, rely=0.75, anchor="e")
        symptoms_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        symptoms_text.place(relx=0.85, rely=0.75, anchor="e")
        symptoms = symptoms_text.get(1.0, "end")

        # todo add command
        save_button = Button(self.__canvas, text="حفظ", font=("Times", 15))
        save_button.place(relx=0.8, rely=0.9, anchor="e")

        finish_button = Button(self.__canvas, text="الإنتهاء", font=("Times", 15), command=self.delete_canvas_content)
        finish_button.place(relx=0.3, rely=0.9, anchor="e")
        self.__canvas_content += [name_label, name_text, pid_label, pid_text, age_label, age_text, come_label, come_text, absent_label, absent_text, finish_label, finish_text, dates_label,
                                  dates_text, symptoms_label, symptoms_text, save_button, finish_button]

    def remove_button_func(self):
        remove_label = Label()
        remove_text = Text()

    def quit_button_func(self):
        quitting = askyesno("!الخروج", "هل أنت متأكد من الخروج؟")
        if quitting:
            quit()
        else:
            pass

    # def how_to_use_func(self):
    #     pass
    #
    # def destroy_how(self):
    #     pass

    # def destroy_buttons(self):
    #     for button in self.__buttons:
    #         button.destroy()

    def update_button_func(self):
        pass

    def starting_buttons(self):
        search_button = Button(self.__root, text="إبحث عن مريض", font=("Times", 20), command=self.__search_button_func)
        search_button.place(relx=1, rely=0.1, anchor="e")
        add_new_button = Button(self.__root, text="إضافة مريض جديد", font=("Times", 20), command=self.add_new_button_func)
        add_new_button.place(relx=1, rely=0.2, anchor="e")
        remove_button = Button(self.__root, text="حذف مريض", font=("Times", 20), command=self.remove_button_func)
        remove_button.place(relx=1, rely=0.3, anchor="e")
        update_button = Button(self.__root, text="تعديل معلومات مريض", font=("Times", 20), command=self.update_button_func)
        update_button.place(relx=1, rely=0.4, anchor="e")
        # how_to_use_button = Button(self.__root, text="كيفية الإستخدام؟", font=("Times", 20), command=self.how_to_use_func)
        # how_to_use_button.place(relx=1, rely=0.4, anchor="e")
        quit_button = Button(self.__root, text="الخروج", font=("Times", 20), command=self.quit_button_func)
        quit_button.place(relx=1, rely=0.5, anchor="e")


if __name__ == "__main__":
    gui = GUI()
    gui.starting_the_window()
