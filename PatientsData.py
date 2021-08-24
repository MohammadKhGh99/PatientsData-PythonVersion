# started at 22.08.2021 at 17:17
import os


class Patient:
    def __init__(self, name: str, pid: int = -1, age: float = -1, come_cause: str = "", absent_cause: str = "",
                 finish_cause: str = "", dates: list = [], symptoms: list = []):
        self.__name = name
        self.__pid = pid
        self.__age = age
        self.__come_cause = come_cause
        self.__absent_cause = absent_cause
        self.__finish_cause = finish_cause
        self.__dates = dates
        self.__symptoms = symptoms

    def get_name(self):
        return self.__name

    def set_name(self, other):
        self.__name = other

    def get_age(self):
        return self.__age

    def set_age(self, other):
        self.__age = other

    def get_pid(self):
        return self.__pid

    def set_pid(self, other):
        self.__name = other

    def get_come_cause(self):
        return self.__come_cause

    def set_come_cause(self, other):
        self.__come_cause = other

    def get_absent_cause(self):
        return self.__absent_cause

    def set_absent_cause(self, other):
        self.__absent_cause = other

    def get_finish_cause(self):
        return self.__finish_cause

    def set_finish_cause(self, other):
        self.__finish_cause = other

    def get_dates(self):
        return self.__dates

    def set_dates(self, other):
        self.__dates = other

    def get_symptoms(self):
        return self.__symptoms

    def set_symptoms(self, other):
        self.__symptoms = other


folder_name = "المعالجة"


class Patients:
    def __init__(self, patients: list):
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        this_dir = os.path.abspath(os.curdir)
        this_dir = os.path.join(this_dir, folder_name)
        self.__patients = patients

    def get_patients(self):
        return self.__patients

    # todo keep or remove?
    def set_patients(self, other):
        self.__patients = other

    def add_patient(self, patient: Patient):
        self.__patients.append(patient)

    def remove_patient(self, patient: Patient):
        self.__patients.remove(patient)

