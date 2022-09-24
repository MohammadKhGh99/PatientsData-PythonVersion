import os
from tkinter import *
from tkinter.messagebox import askyesno
from PatientsData import *
# from PIL import Image


class GUI:
    def __init__(self):
        self.__root = Tk()

        # self.__root.attributes("-fullscreen", True)
        self.__canvas = Canvas(self.__root, width=self.__root.winfo_screenwidth(),
                               height=self.__root.winfo_screenheight(), bd=10, bg="white")
        # self.__canvas.config(high)
        # self.__canvas.place(x=100, y=100)
        # self.__canvas.pack(anchor="sw", side=LEFT)
        # self.__canvas.configure(bg='grey', height=684, width=720)
        self.__buttons = []
        self.__canvas_content = []
        self.__add_texts = []
        self.__patients = Patients([])

    def starting_the_window(self):
        """
        this method starts the window of the
        :return: returns nothing
        """
        # self.__root.configure(background='grey')
        width = self.__root.winfo_screenwidth()
        height = self.__root.winfo_screenheight()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title("المعالجة بالرقية الشرعية")
        title = Label(self.__root, text="بسم الله الرحمن الرحيم", font=("Traditional Arabic", 30))
        title.place(relx=0.6, rely=0.029, anchor="e")
        # bg = Label(self.__canvas, image=PhotoImage(file="one.png"))
        # bg.place(relx=1, rely=0.5, anchor="e")
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
        done_search.place(x=100, y=50, anchor="e")
        # self.__canvas_content.append(done_search)
        search_entry = Entry(self.__canvas, width=48, font=("Times", 20), textvariable=name, justify="right")
        search_entry.place(x=550, y=50, anchor="e")
        search_entry.bind("<Return>", done_func)
        self.__canvas_content += [done_search, search_entry]

    def add_new_button_func(self):
        # self.__canvas.delete(0, END)
        self.delete_canvas_content()
        name_label = Label(self.__canvas, text=":الإسم", font=("Times", 15), bg="grey")
        name_label.place(relx=0.98, rely=0.05, anchor="e")
        name_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        # name_text.tag_config(justify="right", tagName="tag-right")
        name_text.place(relx=0.85, rely=0.05, anchor="e")

        pid_label = Label(self.__canvas, text=":رقم الهوية", font=("Times", 15), bg="grey")
        pid_label.place(relx=0.98, rely=0.15, anchor="e")
        pid_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        pid_text.place(relx=0.85, rely=0.15, anchor="e")

        age_label = Label(self.__canvas, text=":العمر", font=("Times", 15), bg="grey")
        age_label.place(relx=0.98, rely=0.25, anchor="e")
        age_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        age_text.place(relx=0.85, rely=0.25, anchor="e")

        come_label = Label(self.__canvas, text=":سبب القدوم", font=("Times", 15), bg="grey")
        come_label.place(relx=0.98, rely=0.35, anchor="e")
        come_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        come_text.place(relx=0.85, rely=0.35, anchor="e")

        absent_label = Label(self.__canvas, text=":سبب الغياب", font=("Times", 15), bg="grey")
        absent_label.place(relx=0.98, rely=0.45, anchor="e")
        absent_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        absent_text.place(relx=0.85, rely=0.45, anchor="e")

        finish_label = Label(self.__canvas, text=":سبب الإنتهاء", font=("Times", 15), bg="grey")
        finish_label.place(relx=0.98, rely=0.55, anchor="e")
        finish_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        finish_text.place(relx=0.85, rely=0.55, anchor="e")

        dates_label = Label(self.__canvas, text=":تواريخ القدوم", font=("Times", 15), bg="grey")
        dates_label.place(relx=0.98, rely=0.65, anchor="e")
        dates_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        dates_text.place(relx=0.85, rely=0.65, anchor="e")

        symptoms_label = Label(self.__canvas, text=":الأعراض", font=("Times", 15), bg="grey")
        symptoms_label.place(relx=0.98, rely=0.75, anchor="e")
        symptoms_text = Text(self.__canvas, height=1, width=60, font=("Times", 15))
        symptoms_text.place(relx=0.85, rely=0.75, anchor="e")

        self.__add_texts += [name_text, pid_text, age_text, come_text, absent_text, finish_text, dates_text, symptoms_text]

        # todo add command
        save_button = Button(self.__canvas, text="حفظ", font=("Times", 15), command=self.save_button_func)
        save_button.place(relx=0.8, rely=0.9, anchor="e")

        finish_button = Button(self.__canvas, text="الإنتهاء", font=("Times", 15), command=self.delete_canvas_content)
        finish_button.place(relx=0.3, rely=0.9, anchor="e")
        self.__canvas_content += [name_label, name_text, pid_label, pid_text, age_label, age_text, come_label, come_text, absent_label, absent_text, finish_label, finish_text, dates_label,
                                  dates_text, symptoms_label, symptoms_text, save_button, finish_button]

    def save_button_func(self):
        name = self.__add_texts[0].get(1.0, "end-1c")
        pid = int(self.__add_texts[1].get(1.0, "end-1c"))
        age = float(self.__add_texts[2].get(1.0, "end-1c"))
        come_cause = self.__add_texts[3].get(1.0, "end-1c")
        absent_cause = self.__add_texts[4].get(1.0, "end-1c")
        finish_cause = self.__add_texts[5].get(1.0, "end-1c")
        dates = self.__add_texts[6].get(1.0, "end-1c").split(',')
        symptoms = self.__add_texts[7].get(1.0, "end-1c")
        patient = Patient(name, pid, age, come_cause, absent_cause, finish_cause, dates, symptoms)

        # print(patient.get_name())
        # print(patient.get_pid())
        # print(patient.get_age())
        # print(patient.get_come_cause())
        # print(patient.get_absent_cause())
        # print(patient.get_finish_cause())
        # print(patient.get_dates())
        # print(patient.get_symptoms())

    def remove_button_func(self):
        remove_label = Label()
        remove_text = Text()

    def quit_button_func(self):
        quitting = askyesno("!المغادرة", "هل أنت متأكد من المغادرة؟")
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
        search_button.place(relx=1, rely=0.15, anchor="e")
        add_new_button = Button(self.__root, text="إضافة مريض جديد", font=("Times", 20), command=self.add_new_button_func)
        add_new_button.place(relx=1, rely=0.25, anchor="e")
        remove_button = Button(self.__root, text="حذف مريض", font=("Times", 20), command=self.remove_button_func)
        remove_button.place(relx=1, rely=0.35, anchor="e")
        update_button = Button(self.__root, text="تعديل معلومات مريض", font=("Times", 20), command=self.update_button_func)
        update_button.place(relx=1, rely=0.45, anchor="e")
        # how_to_use_button = Button(self.__root, text="كيفية الإستخدام؟", font=("Times", 20), command=self.how_to_use_func)
        # how_to_use_button.place(relx=1, rely=0.4, anchor="e")
        quit_button = Button(self.__root, text="الخروج", font=("Times", 20), command=self.quit_button_func)
        quit_button.place(relx=1, rely=0.55, anchor="e")


if __name__ == "__main__":
    gui = GUI()
    gui.starting_the_window()
