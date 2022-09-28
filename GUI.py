# -*- coding: UTF-8 -*-

import os
from tkinter import *
from tkinter.messagebox import askyesno
import Patients as p
# from PIL import Image
from Constants import *
import awesometkinter as atk
import datetime as dt
import tkinter.ttk as ttk
import time
import csv
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox


# class Patient:
#     def __init__(self, name, id_number, gender, age, come_dates, symptoms, explanation, social_situation, diagnosis,
#                  health_situation, therapy):
#         self.name = name
#         self.id_number = id_number
#         self.gender = gender
#         self.age = age
#         self.come_dates = come_dates
#         self.symptoms = symptoms
#         self.explanation = explanation
#         self.social_situation = social_situation
#         self.diagnosis = diagnosis
#         self.health_situation = health_situation
#         self.therapy = therapy


class GUI:
    def __init__(self):
        self.__root = Tk()

        # self.__root.attributes("-fullscreen", True)
        self.__width = self.__root.winfo_screenwidth()
        self.__height = self.__root.winfo_screenheight()
        self.__canvas = Canvas(self.__root, width=self.__width, height=self.__height, bd=10, bg="white")
        # self.__canvas.config(high)
        self.__canvas.place(x=0, y=0)
        # self.__canvas.pack(anchor="sw", side=LEFT)
        # self.__canvas.configure(bg='grey', height=684, width=720)
        self.__buttons = []
        self.__canvas_content = []
        self.__add_texts = []
        self.texts = dict()
        self.__patients = p.Patients()
        # self.__frame = Frame(self.__canvas, width=500, height=500, background="black")
        # self.__frame.place(x=200, y=100)
        self.widgets = []
        self.labels = []
        self.options_values = []

    def starting_the_window(self):
        """
        this method starts the window of the
        :return: returns nothing
        """
        # self.__root.configure(background='grey')
        self.__root.geometry(f"{self.__width}x{self.__height}")
        self.__root.title("المعالجة بالرقية الشرعية")
        title = Label(self.__root, text=TITLE, font=("Traditional Arabic", 30), bg="white")
        title.place(x=self.__width // 2 - 80, y=5)
        # bg = Label(self.__canvas, image=PhotoImage(file="one.png"))
        # bg.place(relx=1, rely=0.5, anchor="e")
        self.starting_buttons()
        self.__root.mainloop()

    def starting_buttons(self):
        self.__canvas.create_line(1313, 120, self.__width, 120)
        self.__canvas.create_line(1313, 120, 1313, 600)
        self.__canvas.create_line(1313, 600, self.__width, 600)

        search_button = Button(self.__root, text="إبحث عن مريض", font=("Times", 20), command=self.__search_button_func)
        search_button.place(x=self.__width, y=150, anchor="e")
        add_new_button = Button(self.__root, text="إضافة مريض جديد", font=("Times", 20),
                                command=self.add_new_patient_button_func)
        add_new_button.place(x=self.__width, y=250, anchor="e")
        remove_button = Button(self.__root, text="حذف مريض", font=("Times", 20),
                               command=self.delete_patient_button_func)
        remove_button.place(x=self.__width, y=350, anchor="e")
        update_button = Button(self.__root, text="تعديل معلومات مريض", font=("Times", 20),
                               command=self.update_patient_button_func)
        update_button.place(x=self.__width, y=450, anchor="e")
        # how_to_use_button = Button(self.__root, text="كيفية الإستخدام؟", font=("Times", 20), command=self.how_to_use_func)
        # how_to_use_button.place(relx=1, rely=0.4, anchor="e")
        quit_button = Button(self.__root, text="الخروج", font=("Times", 20), command=self.quit_button_func)
        quit_button.place(x=self.__width, y=550, anchor="e")

    def delete_canvas_content(self):
        for content in self.__canvas_content:
            if content is None:
                continue
            if type(content) is ScrolledText:
                content.frame.destroy()
            else:
                content.destroy()
        self.__canvas_content = []

    def __search_button_func(self):
        self.delete_canvas_content()
        time.sleep(0.1)
        name = StringVar()

        def done_func(event="<Return>"):
            nonlocal name
            name = name.get()
            search_entry.destroy()
            done_search.destroy()

            print(name)

        done_search = Button(self.__canvas, text="البحث", font=("Times", 15), command=done_func)
        done_search.place(x=LABELS_X, y=150, anchor="w")

        search_entry = Entry(self.__canvas, width=48, font=("Times", 20), textvariable=name, justify="right",
                             highlightthickness=5)
        search_entry.place(x=WIDGETS_X, y=150, anchor="e")
        search_entry.bind("<Return>", done_func)

        self.__canvas_content += [done_search, search_entry]

    def add_new_patient_button_func(self):
        # self.__canvas.delete(0, END)
        self.delete_canvas_content()
        time.sleep(0.1)

        # todo: saving
        name_value = StringVar(self.__canvas)
        name_label = Label(self.__canvas, text=NAME, font=("Times", 20), bg="white")
        name_label.place(x=LABELS_X, y=NAME_Y, anchor="w")
        name_entry = Entry(self.__canvas, textvariable=name_value, width=15, font=("Times", 15), highlightthickness=5,
                           justify="right")
        name_entry.place(x=WIDGETS_X, y=NAME_Y, anchor="e")

        # todo: saving
        id_value = StringVar(self.__canvas)
        pid_label = Label(self.__canvas, text=ID, font=("Times", 20), bg="white")
        pid_label.place(x=ID_LBL_X, y=ID_Y, anchor="w")
        pid_entry = Entry(self.__canvas, textvariable=id_value, width=10, font=("Times", 15), highlightthickness=5,
                          justify="right")
        pid_entry.place(x=ID_WDG_X, y=ID_Y, anchor="e")

        # todo: saving
        # gender
        gender_value = StringVar(self.__canvas)
        gender_value.set("-")
        gender_label = Label(self.__canvas, text=GENDER, font=("Times", 20), bg="white")
        gender_label.place(x=GENDER_LBL_X, y=GENDER_Y, anchor="w")
        gender_options = OptionMenu(self.__canvas, gender_value, *GENDERS)
        gender_options.place(x=GENDER_WDG_X, y=GENDER_Y, anchor="e")

        social_value = StringVar(self.__canvas)
        social_value.set("-")
        social_situation_label = Label(self.__canvas, text=SOCIAL_SIT, font=("Times", 20), bg="white")
        social_situation_label.place(x=SOCIAL_LBL_X, y=SOCIAL_Y, anchor="w")
        social_situation_options = OptionMenu(self.__canvas, social_value, *SOCIALS)
        social_situation_options.place(x=SOCIAL_WDG_X, y=SOCIAL_Y, anchor="e")

        age_value = StringVar(self.__canvas)
        age_label = Label(self.__canvas, text=AGE, font=("Times", 20), bg="white")
        age_label.place(x=AGE_LBL_X, y=AGE_Y, anchor="w")
        age_entry = Entry(self.__canvas, textvariable=age_value, width=3, font=("Times", 15), highlightthickness=5)
        age_entry.place(x=AGE_WDG_X, y=AGE_Y, anchor="e")

        children_value = StringVar(self.__canvas)
        children_label = Label(self.__canvas, text=CHILDREN, font=("Times", 20), bg="white")
        children_label.place(x=CHILDREN_LBL_X, y=CHILDREN_Y, anchor="w")
        children_entry = Entry(self.__canvas, textvariable=children_value, width=3, font=("Times", 15),
                               highlightthickness=5)
        children_entry.place(x=CHILDREN_WDG_X, y=CHILDREN_Y, anchor="e")

        prayer_value = StringVar(self.__canvas)
        prayer_label = Label(self.__canvas, text=PRAYER, font=("Times", 20), bg="white")
        prayer_label.place(x=PRAYER_LBL_X, y=PRAYER_Y, anchor="w")
        prayer_options = OptionMenu(self.__canvas, prayer_value, *["نعم", "لا"])
        prayer_options.place(x=PRAYER_WDG_X, y=PRAYER_Y, anchor="e")

        # todo: saving

        health_value = StringVar(self.__canvas)
        health_label = Label(self.__canvas, text=HEALTH, font=("Times", 20), bg="white")
        health_label.place(x=LABELS_X, y=HEALTH_Y, anchor="w")
        health_entry = Entry(self.__canvas, textvariable=health_value, width=20, font=("Times", 15),
                             highlightthickness=5, justify="right")
        health_entry.place(x=WIDGETS_X, y=HEALTH_Y, anchor="e")

        work_value = StringVar(self.__canvas)
        work_label = Label(self.__canvas, text=WORK, font=("Times", 20), bg="white")
        work_label.place(x=WORK_LBL_X, y=WORK_Y, anchor="w")
        work_entry = Entry(self.__canvas, textvariable=work_value, width=20, font=("Times", 15), highlightthickness=5,
                           justify="right")
        work_entry.place(x=WORK_WDG_X, y=WORK_Y, anchor="e")

        companion_value = StringVar(self.__canvas)
        companion_label = Label(self.__canvas, text=COMPANION, font=("Times", 20), bg="white")
        companion_label.place(x=COMPANION_LBL_X, y=COMPANION_Y, anchor="w")
        companion_entry = Entry(self.__canvas, textvariable=companion_value, width=20, font=("Times", 15),
                                highlightthickness=5, justify="right")
        companion_entry.place(x=COMPANION_WDG_X, y=COMPANION_Y, anchor="e")

        city_value = StringVar(self.__canvas)
        city_label = Label(self.__canvas, text=CITY, font=("Times", 20), bg="white")
        city_label.place(x=CITY_LBL_X, y=CITY_Y, anchor="w")
        city_entry = Entry(self.__canvas, textvariable=city_value, width=20, font=("Times", 15),
                           highlightthickness=5, justify="right")
        city_entry.place(x=CITY_WDG_X, y=CITY_Y, anchor="e")

        phone_value = StringVar(self.__canvas)
        phone_label = Label(self.__canvas, text=PHONE, font=("Times", 20), bg="white")
        phone_label.place(x=PHONE_LBL_X, y=PHONE_Y, anchor="w")
        phone_entry = Entry(self.__canvas, textvariable=phone_value, width=20, font=("Times", 15),
                            highlightthickness=5, justify="right")
        phone_entry.place(x=PHONE_WDG_X, y=PHONE_Y, anchor="e")

        # dates_label = Label(self.__canvas, text=COME_DATES, font=("Times", 20), bg="white")
        # dates_label.place(x=LABELS_X, y=DATES_Y, anchor="w")
        # year_value = StringVar(self.__canvas)
        # year_options = ttk.Combobox(self.__canvas, width=4, textvariable=year_value,
        #                             values=list(range(2000, today.year + 1)))
        # year_options.place(x=WIDGETS_X, y=DATES_Y, anchor="e")
        #
        # month_value = StringVar(self.__canvas)
        # month_options = ttk.Combobox(self.__canvas, width=2, textvariable=month_value,
        #                              values=list(range(1, today.month + 1)))
        # month_options.place(x=WIDGETS_X - 63, y=DATES_Y, anchor="e")
        #
        # day_value = StringVar(self.__canvas)
        # day_options = ttk.Combobox(self.__canvas, width=2, textvariable=day_value, values=list(range(1, today.day + 1)))
        # day_options.place(x=WIDGETS_X - 110, y=DATES_Y, anchor="e")
        #
        # def save_date(flag=True):
        #     pass
        #
        # dates_save_button = Button(self.__canvas, text="حفظ التاريخ", font=("Times", 14))
        # dates_save_button.place(x=WIDGETS_X - 200, y=DATES_Y, anchor="e")

        # todo: saving
        description_label = Label(self.__canvas, text=DESCRIPTION, font=("jameel noori nastaleeq", 20), bg="white")
        description_label.place(x=LABELS_X, y=DESCRIPTION_Y - 30, anchor="w")
        description_text = ScrolledText(self.__canvas, height=4, width=86, font=("Times", 15), highlightthickness=5)
        description_text.place(x=WIDGETS_X, y=DESCRIPTION_Y, anchor="e")
        #
        # def rtlRelease(event):
        #     global hebCursorPos
        #     if event.keycode == 114 or event.keycode == 113:
        #         hebCursorPos = event.widget.index(INSERT)
        #     else:
        #         event.widget.icursor(hebCursorPos)
        #     print(str(event.keycode) + " " + str(hebCursorPos))
        #
        # def rtlPress(event):
        #     global hebCursorPos
        #     if event.keycode == 22:
        #         length = len(event.widget.get())
        #         if hebCursorPos == length:
        #             event.widget.insert(hebCursorPos, " ")
        #             event.widget.icursor(hebCursorPos + 1)
        #         else:
        #             if event.keycode == 119:
        #                 if hebCursorPos == 0:
        #                     event.widget.insert(hebCursorPos, " ")
        #                 else:
        #                     hebCursorPos -= 1
        #                 event.widget.icursor(hebCursorPos)
        #
        # def rtlMouse(event):
        #     global hebCursorPos
        #     hebCursorPos = event.widget.index(INSERT)
        #
        # description_text.bind("<KeyPress>", rtlPress)
        # description_text.bind("<KeyRelease>", rtlRelease)
        # description_text.bind("<ButtonRelease>", rtlMouse)

        diagnosis_label = Label(self.__canvas, text=DIAGNOSIS, font=("Times", 20), bg="white")
        diagnosis_label.place(x=LABELS_X, y=DIAGNOSIS_Y + 15, anchor="w")
        diagnosis_text = ScrolledText(self.__canvas, height=2, width=86, font=("Times", 15), highlightthickness=5)
        diagnosis_text.place(x=WIDGETS_X, y=DIAGNOSIS_Y, anchor="ne")

        therapy_label = Label(self.__canvas, text=THERAPY, font=("Times", 20), bg="white")
        therapy_label.place(x=LABELS_X, y=THERAPY_Y + 10, anchor="w")
        therapy_text = ScrolledText(self.__canvas, height=13, width=86, font=("Times", 15), highlightthickness=5)
        therapy_text.place(x=WIDGETS_X, y=THERAPY_Y, anchor="ne")

        # todo add command
        # todo: saving
        id_flag, age_flag, child_flag, phone_flag = False, False, False, False
        id_err_label, age_err_label, child_err_label, phone_err_label = None, None, None, None

        def save_button_func():
            name = name_value.get()
            # check
            id_number = id_value.get()
            gender = gender_value.get()
            social = social_value.get()
            # check
            age = age_value.get()
            # check
            children = children_value.get()
            prayer = prayer_value.get()
            health = health_value.get()
            work = work_value.get()
            companion = companion_value.get()
            city = city_value.get()
            # check
            phone = phone_value.get()
            description = description_text.get(1.0, "end-1c")
            diagnosis = diagnosis_text.get(1.0, "end-1c")
            therapy = therapy_text.get(1.0, "end-1c")
            nonlocal id_flag, age_flag, id_err_label, age_err_label, child_err_label, phone_err_label, child_flag, phone_flag

            # check for id number
            if (len(id_number) != 9 and len(id_number) != 0) or (len(id_number) != 0 and not id_number.isnumeric()):
                id_flag = True
                if id_err_label is not None:
                    id_err_label.destroy()

                id_err_label = Label(self.__canvas, text="!رقم الهوية من 9 أرقام", font=("Times", 15), bg="red")
                id_err_label.place(x=ID_WDG_X + 20, y=ID_Y - 35, anchor="e")
            elif id_err_label is not None:
                id_flag = False
                # if id_err_label is not None:
                id_err_label.destroy()

            # check for age
            if len(age) != 0 and not age.isnumeric():
                age_flag = True
                if age_err_label is not None:
                    age_err_label.destroy()

                age_err_label = Label(self.__canvas, text="!العمر من أرقام فقط", font=("Times", 15), bg="red")
                age_err_label.place(x=AGE_WDG_X + 40, y=AGE_Y - 35, anchor="e")
            elif age_err_label is not None:
                age_flag = False
                age_err_label.destroy()

            # check for children
            if len(children) != 0 and not children.isnumeric():
                child_flag = True
                if child_err_label is not None:
                    child_err_label.destroy()

                child_err_label = Label(self.__canvas, text="!عدد الأولاد من أرقام فقط", font=("Times", 15), bg="red")
                child_err_label.place(x=CHILDREN_LBL_X + 40, y=CHILDREN_Y - 35, anchor="e")
            elif child_err_label is not None:
                child_flag = False
                child_err_label.destroy()

            # check for phone number
            if len(phone) != 0 and not phone.isnumeric():
                phone_flag = True
                if phone_err_label is not None:
                    phone_err_label.destroy()

                phone_err_label = Label(self.__canvas, text="!رقم الهاتف من أرقام فقط", font=("Times", 15), bg="red")
                phone_err_label.place(x=PHONE_LBL_X + 40, y=PHONE_Y - 35, anchor="e")
            elif phone_err_label is not None:
                phone_flag = False
                phone_err_label.destroy()

            if not phone_flag and not id_flag and not child_flag and not age_flag:
                patient = p.Patient(name, id_number, gender, social, age, children, prayer, health, work, companion,
                                    city, phone, description, diagnosis, therapy)

                self.__patients.add_patient(patient)
                for widget in self.widgets:
                    if type(widget) is Entry:
                        widget.delete(0, END)
                    elif type(widget) is ScrolledText:
                        widget.delete('1.0', END)
                for value in self.options_values:
                    value.set('-')
                # gender_options.selection_clear()
                messagebox.showinfo("! تم الحفظ", "! تم الحفظ")
            else:
                messagebox.showerror("! فشل الحفظ", "! فشل الحفظ")

        save_button = Button(self.__canvas, text="حفظ", font=("Times", 15), command=save_button_func)
        save_button.place(x=75, y=700, anchor="w")

        # todo: saving
        finish_button = Button(self.__canvas, text="الإنتهاء", font=("Times", 15), command=self.delete_canvas_content)
        finish_button.place(x=5, y=700, anchor="w")
        self.__canvas_content += [name_label, gender_options, pid_label, pid_entry, description_label, description_text,
                                  save_button, finish_button, gender_options, gender_label, name_entry, age_label,
                                  age_entry, social_situation_label, social_situation_options, diagnosis_text,
                                  diagnosis_label, health_label, health_entry, therapy_text, therapy_label,
                                  children_entry, children_label, prayer_label, prayer_options, work_entry, work_label,
                                  companion_entry, companion_label, city_entry, city_label, phone_label, phone_entry,
                                  id_err_label, age_err_label]

        self.widgets += [name_entry, pid_entry, age_entry, children_entry, health_entry, work_entry, companion_entry,
                         city_entry, phone_entry, description_text, diagnosis_text, therapy_text]

        self.options_values += [gender_value, social_value, prayer_value]

    def delete_patient_button_func(self):
        pass

    def update_patient_button_func(self):
        pass

    def quit_button_func(self):
        quitting = askyesno("!المغادرة", "هل أنت متأكد من المغادرة؟")
        if quitting:
            # self.__patients.csv_file.close()
            self.__root.destroy()
            # return 0
            # exit(0)
            # quit()
        else:
            pass


if __name__ == "__main__":
    gui = GUI()
    gui.starting_the_window()
