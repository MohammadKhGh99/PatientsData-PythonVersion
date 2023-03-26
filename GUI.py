from tkinter import *
from tkinter.messagebox import askyesno
# import pyodbc
import Patients as p
from Constants import *
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox


class GUI:
    """
    A class to handle GUI things
    """
    # variable to check if this add is the first one or not
    first_add = True
    # variable to check if this search is the first one or not
    first_search = True
    # variable to check if this add/search is the first one or not
    first_time = True

    after_search = False

    def __init__(self):
        """
        This is the constructor for the GUI class
        """
        self.__root = Tk()
        self.__width = self.__root.winfo_screenwidth()
        self.__height = self.__root.winfo_screenheight()
        self.__canvas = Canvas(self.__root, width=self.__width, height=self.__height, bd=10, bg="white")
        self.__canvas.place(x=0, y=0)
        self.__canvas_content = []
        self.__patients = p.Patients()
        self.widgets = []
        self.options_values = []
        self.widgets_dict = dict()
        self.search_content = []
        self.search_dict = dict()

    def starting_the_window(self):
        """
        this method starts the window of the
        :return: returns nothing
        """
        self.__root.geometry(f"{self.__width}x{self.__height}")
        self.__root.title("المعالجة بالرقية الشرعية")
        title = Label(self.__root, text=TITLE, font=("Traditional Arabic", 30), bg="white")
        title.place(x=self.__width // 2 - 80, y=5)

        subject = Label(self.__root, text=SUBJECT, font=("Traditional Arabic", 20), bg="white")
        subject.place(x=self.__width // 2 - 10, y=63)
        self.starting_buttons()
        self.__root.mainloop()

    def starting_buttons(self):
        """
        This function starts the starting buttons (add, search)
        :return: Nothing
        """
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
        quit_button = Button(self.__root, text="الخروج", font=("Times", 20), command=self.quit_button_func)
        quit_button.place(x=self.__width, y=550, anchor="e")

    def hide_canvas_content(self):
        """
        This function hide the canvas content and deletes each widget's content
        :return: nothing
        """
        for content in self.__canvas_content:
            if content is None or type(content) is StringVar:
                continue
            if type(content) is ScrolledText:
                content.delete('1.0', END)
                content.frame.place_forget()
            elif type(content) is Entry:
                content.delete(0, END)
                content.place_forget()
            else:
                content.place_forget()

        # hiding the content of search process
        for content in self.search_content:
            if content is None:
                continue
            if type(content) is ScrolledText:
                content.delete('1.0', END)
                content.frame.place_forget()
            elif type(content) is Entry:
                content.delete(0, END)
                content.place_forget()
            else:
                content.place_forget()

    def insert_date(self, our_choice):
        """
        this function insert the required date after searching on someone
        :param our_choice: the searched row
        :return: nothing
        """
        self.widgets_dict[ALL_NAME][1].insert(0, our_choice[ALL_NAME])
        self.widgets_dict[ID][1].insert(0, our_choice[ID[1:]])
        self.widgets_dict[GENDER][2].set(our_choice[GENDER[1:]])
        self.widgets_dict[SOCIAL][2].set(our_choice[SOCIAL[1:]])
        self.widgets_dict[AGE][1].insert(0, our_choice[AGE[1:]])
        self.widgets_dict[CHILDREN][1].insert(0, our_choice[CHILDREN[1:]])
        self.widgets_dict[PRAYER][2].set(our_choice[PRAYER[1:]])
        self.widgets_dict[HEALTH][1].insert(0, our_choice[HEALTH[1:]])
        self.widgets_dict[WORK][1].insert(0, our_choice[WORK[1:]])
        self.widgets_dict[COMPANION][1].insert(0, our_choice[COMPANION[1:]])
        self.widgets_dict[CITY][1].insert(0, our_choice[CITY[1:]])
        self.widgets_dict[PHONE][1].insert(0, our_choice[PHONE[1:]])
        self.widgets_dict[DESCRIPTION][1].insert('1.0', our_choice[DESCRIPTION[1:]])
        self.widgets_dict[DIAGNOSIS][1].insert('1.0', our_choice[DIAGNOSIS[1:]])
        self.widgets_dict[THERAPY][1].insert('1.0', our_choice[THERAPY[1:]])

    def search_options_buttons(self, search_option):
        """
        This function show the check circles, to choose in which way the user wants to search.
        :param search_option: the chosen option
        :return: the check buttons
        """
        fname_search = ttk.Radiobutton(self.__canvas, text=FNAME, value=FNAME, variable=search_option,
                                       style="Wild.TRadiobutton")
        fname_search.place(x=NAME_SEARCH_X, y=FNAME_Y, anchor="e")

        fmname_search = ttk.Radiobutton(self.__canvas, text=FMNAME, value=FMNAME, variable=search_option,
                                        style="Wild.TRadiobutton")
        fmname_search.place(x=NAME_SEARCH_X, y=FMNAME_Y, anchor="e")

        flname_search = ttk.Radiobutton(self.__canvas, text=FLNAME, value=FLNAME, variable=search_option,
                                        style="Wild.TRadiobutton")
        flname_search.place(x=NAME_SEARCH_X, y=FLNAME_Y, anchor="e")

        lname_search = ttk.Radiobutton(self.__canvas, text=LNAME, value=LNAME, variable=search_option,
                                       style="Wild.TRadiobutton")
        lname_search.place(x=NAME_SEARCH_X, y=LNAME_Y, anchor="e")

        all_name_search = ttk.Radiobutton(self.__canvas, text=ALL_NAME, value=ALL_NAME, variable=search_option,
                                          style="Wild.TRadiobutton")
        all_name_search.place(x=NAME_SEARCH_X, y=ALL_NAME_Y, anchor="e")

        id_search = ttk.Radiobutton(self.__canvas, text=ID[1:], value=ID[1:], variable=search_option,
                                    style="Wild.TRadiobutton")
        id_search.place(x=NAME_SEARCH_X, y=ID_SEARCH_Y, anchor="e")

        return fname_search, fmname_search, flname_search, lname_search, all_name_search, id_search

    def __search_button_func(self):
        """
        This function given to the search button to activate when the button pressed
        :return: nothin
        """
        self.hide_canvas_content()
        GUI.after_search = True

        if GUI.first_search:
            search_value = StringVar()

            def search_func():
                nonlocal search_value
                search_val = search_value.get()
                self.hide_canvas_content()

                if search_option.get() == ID_SEARCH:
                    patients_lst = self.__patients.search_patient(option=search_option.get(), id_number=search_val)
                else:
                    patients_lst = self.__patients.search_patient(option=search_option.get(), name=search_val)

                if type(patients_lst) is tuple:
                    messagebox.showwarning("لا يوجد", patients_lst[1])
                    return

                data_dict = {f'{row[ALL_NAME]} - {row[CITY[1:]]}': row for row in patients_lst}

                search_option_value = StringVar(self.__canvas)
                result_label = Label(self.__canvas, text=RESULTS, font=("Times", 20), bg="white")
                result_label.place(x=LABELS_X, y=RESULTS_Y, anchor="w")
                result_options = OptionMenu(self.__canvas, search_option_value, *data_dict.keys())
                result_options.place(x=WIDGETS_X, y=RESULTS_Y, anchor="e")

                self.search_content += [result_label, result_options]
                self.search_dict[RESULTS] = (result_label, result_options)

                def show_data():
                    self.search_dict[RESULTS][0].place_forget()
                    self.search_dict[RESULTS][1].place_forget()
                    self.search_dict[DONE].place_forget()
                    self.hide_canvas_content()

                    our_choice = data_dict[search_option_value.get()]
                    if GUI.first_time:
                        # GUI.first_time = False


                        self.create_all()
                    else:
                        self.unhide_widgets()
                    self.insert_date(our_choice)

                done_button = Button(self.__canvas, text=DONE, command=show_data)
                done_button.place(x=WIDGETS_X - 70, y=RESULTS_Y + 40, anchor="e")
                self.search_dict[DONE] = done_button
                self.search_content.append(done_button)

            search_option = StringVar(self.__canvas)
            search_option.set(FNAME)

            style = ttk.Style(self.__canvas)
            style.configure("Wild.TRadiobutton", background="white")

            res = self.search_options_buttons(search_option)
            fname_search, fmname_search, flname_search, lname_search, all_name_search, id_search = res

            search_button = Button(self.__canvas, text=SEARCH, font=("Times", 15), command=search_func)
            search_button.place(x=LABELS_X, y=SEARCH_Y, anchor="w")

            search_entry = Entry(self.__canvas, width=30, font=("Times", 20), textvariable=search_value,
                                 justify="right", highlightthickness=5)
            search_entry.place(x=WIDGETS_X, y=SEARCH_Y, anchor="e")

            self.search_content += [search_button, search_entry, all_name_search, fmname_search, flname_search,
                                    fname_search, id_search, lname_search]

            self.search_dict[SEARCH] = (search_entry, search_button)
            self.search_dict[ALL_NAME] = all_name_search
            self.search_dict[FLNAME] = flname_search
            self.search_dict[FMNAME] = fmname_search
            self.search_dict[FNAME] = fname_search
            self.search_dict[LNAME] = lname_search
            self.search_dict[ID] = id_search
        else:
            self.search_dict[SEARCH][0].place(x=WIDGETS_X, y=SEARCH_Y, anchor="e")
            self.search_dict[SEARCH][1].place(x=LABELS_X, y=SEARCH_Y, anchor="w")
            self.search_dict[ALL_NAME].place(x=NAME_SEARCH_X, y=ALL_NAME_Y, anchor="e")
            self.search_dict[FLNAME].place(x=NAME_SEARCH_X, y=FLNAME_Y, anchor="e")
            self.search_dict[FMNAME].place(x=NAME_SEARCH_X, y=FMNAME_Y, anchor="e")
            self.search_dict[FNAME].place(x=NAME_SEARCH_X, y=FNAME_Y, anchor="e")
            self.search_dict[LNAME].place(x=NAME_SEARCH_X, y=LNAME_Y, anchor="e")
            self.search_dict[ID].place(x=WIDGETS_X - 450, y=ID_SEARCH_Y, anchor="e")
            self.search_dict[RESULTS][0].place(x=LABELS_X, y=RESULTS_Y, anchor="w")
            self.search_dict[RESULTS][1].place(x=WIDGETS_X, y=RESULTS_Y, anchor="e")

    def create_name(self):
        """
        This function create the label and entry for the name input
        :return: name's label, entry and value
        """
        name_value = StringVar(self.__canvas)
        name_label = Label(self.__canvas, text=":" + ALL_NAME, font=("Times", 20), bg="white")
        name_label.place(x=LABELS_X, y=NAME_Y, anchor="w")
        name_entry = Entry(self.__canvas, textvariable=name_value, width=15, font=("Times", 15), justify="right",
                           highlightthickness=5)
        name_entry.place(x=WIDGETS_X, y=NAME_Y, anchor="e")

        return name_label, name_entry, name_value

    def create_id(self):
        """
        This function create the label and entry for the id number input
        :return: id's label, entry and value
        """
        id_value = StringVar(self.__canvas)
        pid_label = Label(self.__canvas, text=ID, font=("Times", 20), bg="white")
        pid_label.place(x=ID_LBL_X, y=ID_Y, anchor="w")
        pid_entry = Entry(self.__canvas, textvariable=id_value, width=10, font=("Times", 15), highlightthickness=5,
                          justify="right")
        pid_entry.place(x=ID_WDG_X, y=ID_Y, anchor="e")
        return pid_label, pid_entry, id_value

    def create_gender(self):
        """
        This function create the label and option menu for the gender input
        :return: gender's label, option menu and value
        """
        gender_value = StringVar(self.__canvas)
        gender_label = Label(self.__canvas, text=GENDER, font=("Times", 20), bg="white")
        gender_label.place(x=GENDER_LBL_X, y=GENDER_Y, anchor="w")
        gender_options = OptionMenu(self.__canvas, gender_value, *GENDERS)
        gender_options.place(x=GENDER_WDG_X, y=GENDER_Y, anchor="e")
        return gender_label, gender_options, gender_value

    def create_social(self):
        """
        This function create the label and option menu for the social situation input
        :return: social situation's label, entry and value
        """
        social_value = StringVar(self.__canvas)
        social_label = Label(self.__canvas, text=SOCIAL, font=("Times", 20), bg="white")
        social_label.place(x=SOCIAL_LBL_X, y=SOCIAL_Y, anchor="w")
        social_options = OptionMenu(self.__canvas, social_value, *SOCIALS)
        social_options.place(x=SOCIAL_WDG_X, y=SOCIAL_Y, anchor="e")
        return social_label, social_options, social_value

    def create_age(self):
        """
        This function create the label and entry for the age input
        :return: age's label, entry and value
        """
        age_value = StringVar(self.__canvas)
        age_label = Label(self.__canvas, text=AGE, font=("Times", 20), bg="white")
        age_label.place(x=AGE_LBL_X, y=AGE_Y, anchor="w")
        age_entry = Entry(self.__canvas, textvariable=age_value, width=3, font=("Times", 15), highlightthickness=5)
        age_entry.place(x=AGE_WDG_X, y=AGE_Y, anchor="e")
        return age_label, age_entry, age_value

    def create_children(self):
        """
        This function create the label and entry for the children input
        :return: children's label, entry and value
        """
        children_value = StringVar(self.__canvas)
        children_label = Label(self.__canvas, text=CHILDREN, font=("Times", 20), bg="white")
        children_label.place(x=CHILDREN_LBL_X, y=CHILDREN_Y, anchor="w")
        children_entry = Entry(self.__canvas, textvariable=children_value, width=3, font=("Times", 15),
                               highlightthickness=5)
        children_entry.place(x=CHILDREN_WDG_X, y=CHILDREN_Y, anchor="e")
        return children_label, children_entry, children_value

    def create_prayer(self):
        """
        This function create the label and entry for the prayer input
        :return: prayer's label, option menu and value
        """
        prayer_value = StringVar(self.__canvas)
        prayer_label = Label(self.__canvas, text=PRAYER, font=("Times", 20), bg="white")
        prayer_label.place(x=PRAYER_LBL_X, y=PRAYER_Y, anchor="w")
        prayer_options = OptionMenu(self.__canvas, prayer_value, *["نعم", "لا"])
        prayer_options.place(x=PRAYER_WDG_X, y=PRAYER_Y, anchor="e")
        return prayer_label, prayer_options, prayer_value

    def create_health(self):
        """
        This function create the label and entry for the health input
        :return: health's label, entry and value
        """
        health_value = StringVar(self.__canvas)
        health_label = Label(self.__canvas, text=HEALTH, font=("Times", 20), bg="white")
        health_label.place(x=LABELS_X, y=HEALTH_Y, anchor="w")
        health_entry = Entry(self.__canvas, textvariable=health_value, width=20, font=("Times", 15),
                             highlightthickness=5, justify="right")
        health_entry.place(x=WIDGETS_X, y=HEALTH_Y, anchor="e")
        return health_label, health_entry, health_value

    def create_work(self):
        """
        This function create the label and entry for the work input
        :return: work's label, entry and value
        """
        work_value = StringVar(self.__canvas)
        work_label = Label(self.__canvas, text=WORK, font=("Times", 20), bg="white")
        work_label.place(x=WORK_LBL_X, y=WORK_Y, anchor="w")
        work_entry = Entry(self.__canvas, textvariable=work_value, width=20, font=("Times", 15),
                           highlightthickness=5, justify="right")
        work_entry.place(x=WORK_WDG_X, y=WORK_Y, anchor="e")
        return work_label, work_entry, work_value

    def create_companion(self):
        """
        This function create the label and entry for the companion input
        :return: companion's label, entry and value
        """
        companion_value = StringVar(self.__canvas)
        companion_label = Label(self.__canvas, text=COMPANION, font=("Times", 20), bg="white")
        companion_label.place(x=COMPANION_LBL_X, y=COMPANION_Y, anchor="w")
        companion_entry = Entry(self.__canvas, textvariable=companion_value, width=20, font=("Times", 15),
                                highlightthickness=5, justify="right")
        companion_entry.place(x=COMPANION_WDG_X, y=COMPANION_Y, anchor="e")
        return companion_label, companion_entry, companion_value

    def create_city(self):
        """
        This function create the label and entry for the city input
        :return: city's label, entry and value
        """
        city_value = StringVar(self.__canvas)
        city_label = Label(self.__canvas, text=CITY, font=("Times", 20), bg="white")
        city_label.place(x=CITY_LBL_X, y=CITY_Y, anchor="w")
        city_entry = Entry(self.__canvas, textvariable=city_value, width=20, font=("Times", 15),
                           highlightthickness=5, justify="right")
        city_entry.place(x=CITY_WDG_X, y=CITY_Y, anchor="e")
        return city_label, city_entry, city_value

    def create_phone(self):
        """
        This function create the label and entry for the phone number input
        :return: phone number's label, entry and value
        """
        phone_value = StringVar(self.__canvas)
        phone_label = Label(self.__canvas, text=PHONE, font=("Times", 20), bg="white")
        phone_label.place(x=PHONE_LBL_X, y=PHONE_Y, anchor="w")
        phone_entry = Entry(self.__canvas, textvariable=phone_value, width=20, font=("Times", 15),
                            highlightthickness=5, justify="right")
        phone_entry.place(x=PHONE_WDG_X, y=PHONE_Y, anchor="e")
        return phone_label, phone_entry, phone_value

    def create_description(self):
        """
        This function create the label and entry for the description input
        :return: description's label and text
        """
        description_label = Label(self.__canvas, text=DESCRIPTION, font=("jameel noori nastaleeq", 20), bg="white")
        description_label.place(x=LABELS_X, y=DESCRIPTION_Y - 30, anchor="w")
        description_text = ScrolledText(self.__canvas, height=4, width=86, font=("Times", 15), highlightthickness=5)
        description_text.place(x=WIDGETS_X, y=DESCRIPTION_Y, anchor="e")
        return description_label, description_text

    def create_diagnosis(self):
        """
        This function create the label and entry for the diagnosis input
        :return: diagnosis's label and text
        """
        diagnosis_label = Label(self.__canvas, text=DIAGNOSIS, font=("Times", 20), bg="white")
        diagnosis_label.place(x=LABELS_X, y=DIAGNOSIS_Y + 15, anchor="w")
        diagnosis_text = ScrolledText(self.__canvas, height=2, width=86, font=("Times", 15), highlightthickness=5)
        diagnosis_text.place(x=WIDGETS_X, y=DIAGNOSIS_Y, anchor="ne")
        return diagnosis_label, diagnosis_text

    def create_therapy(self):
        """
        This function create the label and entry for the therapy input
        :return: therapy's label and text
        """

        therapy_label = Label(self.__canvas, text=THERAPY, font=("Times", 20), bg="white")
        therapy_label.place(x=LABELS_X, y=THERAPY_Y + 10, anchor="w")
        therapy_text = ScrolledText(self.__canvas, height=4, width=86, font=("Times", 15), highlightthickness=5)
        therapy_text.place(x=WIDGETS_X, y=THERAPY_Y, anchor="ne")
        return therapy_label, therapy_text

    def create_all(self):
        """
        This function creates all the inputs labels, entries, texts and values and the save and ignore buttons.
        :return: nothing
        """
        name_label, name_entry, name_value = self.create_name()
        pid_label, pid_entry, id_value = self.create_id()
        gender_label, gender_options, gender_value = self.create_gender()
        social_label, social_options, social_value = self.create_social()
        age_label, age_entry, age_value = self.create_age()
        children_label, children_entry, children_value = self.create_children()
        prayer_label, prayer_options, prayer_value = self.create_prayer()
        health_label, health_entry, health_value = self.create_health()
        work_label, work_entry, work_value = self.create_work()
        companion_label, companion_entry, companion_value = self.create_companion()
        city_label, city_entry, city_value = self.create_city()
        phone_label, phone_entry, phone_value = self.create_phone()
        description_label, description_text = self.create_description()
        diagnosis_label, diagnosis_text = self.create_diagnosis()
        therapy_label, therapy_text = self.create_therapy()

        id_flag, age_flag, child_flag, phone_flag = False, False, False, False
        id_err_label, age_err_label, child_err_label, phone_err_label = None, None, None, None

        def save_button_func():
            print(GUI.after_search)
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
            if name == "" and id_number == "" and gender == "" and social == "" and age == "" and children == "" \
                    and prayer == "" and health == "" and work == "" and companion == "" and city == "" \
                    and phone == "" and description == "" and diagnosis == "" and therapy == "":
                messagebox.showwarning("!فارغ", "!لا يوجد معلومات للحفظ")
                return
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

                child_err_label = Label(self.__canvas, text="!عدد الأولاد من أرقام فقط", font=("Times", 15),
                                        bg="red")
                child_err_label.place(x=CHILDREN_LBL_X + 40, y=CHILDREN_Y - 35, anchor="e")
            elif child_err_label is not None:
                child_flag = False
                child_err_label.destroy()

            # check for phone number
            if len(phone) != 0 and not phone.isnumeric():
                phone_flag = True
                if phone_err_label is not None:
                    phone_err_label.destroy()

                phone_err_label = Label(self.__canvas, text="!رقم الهاتف من أرقام فقط", font=("Times", 15),
                                        bg="red")
                phone_err_label.place(x=PHONE_LBL_X + 40, y=PHONE_Y - 35, anchor="e")
            elif phone_err_label is not None:
                phone_flag = False
                phone_err_label.destroy()

            if not phone_flag and not id_flag and not child_flag and not age_flag:
                patient = p.Patient(name, id_number, gender, social, age, children, prayer, health, work, companion,
                                    city, phone, description, diagnosis, therapy)

                # try:
                self.__patients.add_patient(patient, GUI.after_search)
                messagebox.showinfo("! تم الحفظ", "! تم الحفظ")
                # except pyodbc.IntegrityError:
                #     messagebox.showwarning("ّ!موجود", "!لقد أدخلت هذا الإسم مسبقًا")
                # finally:
                for widget in self.widgets:
                    if type(widget) is Entry:
                        widget.delete(0, END)
                    elif type(widget) is ScrolledText:
                        widget.delete('1.0', END)
                for value in self.options_values:
                    value.set('-')
            else:
                messagebox.showerror("! فشل الحفظ", "! فشل الحفظ")

        save_button = Button(self.__canvas, text=SAVE, font=("Times", 15), command=save_button_func)
        save_button.place(x=SAVE_X, y=SAVE_Y, anchor="w")

        # todo: saving
        ignore_button = Button(self.__canvas, text=IGNORE, font=("Times", 15), command=self.hide_canvas_content)
        ignore_button.place(x=IGNORE_X, y=IGNORE_Y, anchor="w")

        # todo - don't change the order of this list, "delete" VERY IMPORTANT!!!
        if GUI.first_time:
            GUI.first_time = False
            self.__canvas_content += [name_label, name_entry, pid_label, pid_entry, gender_label, gender_options,
                                      gender_value, social_label, social_options, social_value, age_label, age_entry,
                                      children_label, children_entry, prayer_label, prayer_options, prayer_value,
                                      health_label, health_entry, work_label, work_entry, companion_label,
                                      companion_entry, city_label, city_entry, phone_label, phone_entry,
                                      description_label, description_text, diagnosis_label, diagnosis_text,
                                      therapy_label, therapy_text, save_button, ignore_button, id_err_label,
                                      age_err_label, phone_err_label, child_err_label, age_err_label, id_err_label]

            self.fill_dict(*self.__canvas_content[:-6])

            self.widgets += [name_entry, pid_entry, age_entry, children_entry, health_entry, work_entry,
                             companion_entry, city_entry, phone_entry, description_text, diagnosis_text, therapy_text]

            self.options_values += [gender_value, social_value, prayer_value]

    def add_new_patient_button_func(self):
        """
        This function adds a patient to the database using the add_patient function in Patients file
        :return: nothing
        """
        self.hide_canvas_content()
        GUI.after_search = False
        if GUI.first_add and GUI.first_time:
            GUI.first_add = False
            self.create_all()
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
        else:
            self.unhide_widgets()

    def fill_dict(self, name_label, name_entry, pid_label, pid_entry, gender_label, gender_options, gender_value,
                  social_label, social_options, social_value, age_label, age_entry, children_label, children_entry,
                  prayer_label, prayer_options, prayer_value, health_label, health_entry, work_label, work_entry,
                  companion_label, companion_entry, city_label, city_entry, phone_label, phone_entry, description_label,
                  description_text, diagnosis_label, diagnosis_text, therapy_label, therapy_text, save_button,
                  ignore_button):
        self.widgets_dict[ALL_NAME] = (name_label, name_entry)
        self.widgets_dict[ID] = (pid_label, pid_entry)
        self.widgets_dict[GENDER] = (gender_label, gender_options, gender_value)
        self.widgets_dict[SOCIAL] = (social_label, social_options, social_value)
        self.widgets_dict[AGE] = (age_label, age_entry)
        self.widgets_dict[CHILDREN] = (children_label, children_entry)
        self.widgets_dict[PRAYER] = (prayer_label, prayer_options, prayer_value)
        self.widgets_dict[HEALTH] = (health_label, health_entry)
        self.widgets_dict[WORK] = (work_label, work_entry)
        self.widgets_dict[COMPANION] = (companion_label, companion_entry)
        self.widgets_dict[CITY] = (city_label, city_entry)
        self.widgets_dict[PHONE] = (phone_label, phone_entry)
        self.widgets_dict[DESCRIPTION] = (description_label, description_text)
        self.widgets_dict[DIAGNOSIS] = (diagnosis_label, diagnosis_text)
        self.widgets_dict[THERAPY] = (therapy_label, therapy_text)
        self.widgets_dict[SAVE] = save_button
        self.widgets_dict[IGNORE] = ignore_button

    def unhide_widgets(self):
        """
        This function unhide all the hidden widgets after searching or when we want to add a new patient
        :return: nothing
        """
        self.widgets_dict[ALL_NAME][0].place(x=LABELS_X, y=NAME_Y, anchor="w")
        self.widgets_dict[ID][0].place(x=ID_LBL_X, y=ID_Y, anchor="w")
        self.widgets_dict[GENDER][0].place(x=GENDER_LBL_X, y=GENDER_Y, anchor="w")
        self.widgets_dict[SOCIAL][0].place(x=SOCIAL_LBL_X, y=SOCIAL_Y, anchor="w")
        self.widgets_dict[AGE][0].place(x=AGE_LBL_X, y=AGE_Y, anchor="w")
        self.widgets_dict[CHILDREN][0].place(x=CHILDREN_LBL_X, y=CHILDREN_Y, anchor="w")
        self.widgets_dict[PRAYER][0].place(x=PRAYER_LBL_X, y=PRAYER_Y, anchor="w")
        self.widgets_dict[HEALTH][0].place(x=LABELS_X, y=HEALTH_Y, anchor="w")
        self.widgets_dict[WORK][0].place(x=WORK_LBL_X, y=WORK_Y, anchor="w")
        self.widgets_dict[COMPANION][0].place(x=COMPANION_LBL_X, y=COMPANION_Y, anchor="w")
        self.widgets_dict[CITY][0].place(x=CITY_LBL_X, y=CITY_Y, anchor="w")
        self.widgets_dict[PHONE][0].place(x=PHONE_LBL_X, y=PHONE_Y, anchor="w")
        self.widgets_dict[DESCRIPTION][0].place(x=LABELS_X, y=DESCRIPTION_Y - 30, anchor="w")
        self.widgets_dict[DIAGNOSIS][0].place(x=LABELS_X, y=DIAGNOSIS_Y + 15, anchor="w")
        self.widgets_dict[THERAPY][0].place(x=LABELS_X, y=THERAPY_Y + 10, anchor="w")

        self.widgets_dict[ALL_NAME][1].place(x=WIDGETS_X, y=NAME_Y, anchor="e")
        self.widgets_dict[ID][1].place(x=ID_WDG_X, y=ID_Y, anchor="e")
        self.widgets_dict[GENDER][1].place(x=GENDER_WDG_X, y=GENDER_Y, anchor="e")
        self.widgets_dict[SOCIAL][1].place(x=SOCIAL_WDG_X, y=SOCIAL_Y, anchor="e")
        self.widgets_dict[AGE][1].place(x=AGE_WDG_X, y=AGE_Y, anchor="e")
        self.widgets_dict[CHILDREN][1].place(x=CHILDREN_WDG_X, y=CHILDREN_Y, anchor="e")
        self.widgets_dict[PRAYER][1].place(x=PRAYER_WDG_X, y=PRAYER_Y, anchor="e")
        self.widgets_dict[HEALTH][1].place(x=WIDGETS_X, y=HEALTH_Y, anchor="e")
        self.widgets_dict[WORK][1].place(x=WORK_WDG_X, y=WORK_Y, anchor="e")
        self.widgets_dict[COMPANION][1].place(x=COMPANION_WDG_X, y=COMPANION_Y, anchor="e")
        self.widgets_dict[CITY][1].place(x=CITY_WDG_X, y=CITY_Y, anchor="e")
        self.widgets_dict[PHONE][1].place(x=PHONE_WDG_X, y=PHONE_Y, anchor="e")
        self.widgets_dict[DESCRIPTION][1].place(x=WIDGETS_X, y=DESCRIPTION_Y, anchor="e")
        self.widgets_dict[DIAGNOSIS][1].place(x=WIDGETS_X, y=DIAGNOSIS_Y, anchor="ne")
        self.widgets_dict[THERAPY][1].place(x=WIDGETS_X, y=THERAPY_Y, anchor="ne")

        self.widgets_dict[SAVE].place(x=SAVE_X, y=SAVE_Y, anchor="w")
        self.widgets_dict[IGNORE].place(x=IGNORE_X, y=IGNORE_Y, anchor="w")

    def delete_patient_button_func(self):
        pass

    def update_patient_button_func(self):
        pass

    def quit_button_func(self):
        """
        This function activated when quit button pressed to quit the program
        :return: nothing
        """
        quitting = askyesno("!المغادرة", "هل أنت متأكد من المغادرة؟")
        if quitting:
            self.__root.destroy()


if __name__ == "__main__":
    gui = GUI()
    gui.starting_the_window()
