FNAME = " الإسم الشخصي"
FNAME_Y = 150
NAME_Y = 160

FMNAME = "الإسم الشخصي واسم الأب"
FMNAME_Y = 175

FLNAME = "الإسم الشخصي واسم العائلة"
FLNAME_Y = 200

LNAME = "إسم العائلة"
LNAME_Y = 225

ALL_NAME = "الإسم الثلاثي"
ALL_NAME_Y = 250

ID_SEARCH_Y = 275

GENDER = ":الجنس"
GENDERS = ["ذكر", "أنثى"]
GENDER_Y = 160
GENDER_LBL_X = 635
GENDER_WDG_X = 625

ID = ":رقم الهوية"
ID_Y = 160
ID_LBL_X = 830
ID_WDG_X = 820

# BIRTH_Y = 180
# COME_Y = 300
# ABSENT_Y = 340
# DONE_Y = 380

HEALTH = ":الصحة"
HEALTH_Y = 200

COME_DATES = ":تواريخ القدوم"
DATES_Y = 240

DESCRIPTION = ":وصف الحالة"
DESCRIPTION_Y = 314

DIAGNOSIS = ":التشخيص"
DIAGNOSIS_Y = 370

THERAPY = ":العلاج"
THERAPY_Y = 435

SOCIAL = ":الحالة"
SOCIALS = ["أعزب", "متزوج", "مطلّق", "أرمل"]
SOCIAL_Y = 160
SOCIAL_LBL_X = 500
SOCIAL_WDG_X = 490

AGE = ":العمر"
AGE_Y = 160
AGE_LBL_X = 350
AGE_WDG_X = 340

CHILDREN = ":أولاد"
CHILDREN_Y = 160
CHILDREN_LBL_X = 240
CHILDREN_WDG_X = 230

PRAYER = ":صلاة"
PRAYER_Y = 160
PRAYER_LBL_X = 110
PRAYER_WDG_X = 100

LABELS_X = 1110
WIDGETS_X = 1100

WORK = ":العمل"
WORK_Y = 200
WORK_LBL_X = 820
WORK_WDG_X = 810

COMPANION = ":المرافق"
COMPANION_Y = 200
COMPANION_LBL_X = 510
COMPANION_WDG_X = 500

CITY = ":البلد"
CITY_Y = 240
CITY_LBL_X = 1110
CITY_WDG_X = 1100

PHONE = ":الهاتف"
PHONE_Y = 240
PHONE_LBL_X = 810
PHONE_WDG_X = 800

TITLE = "بِسْمِ اللهِ الرَّحْمنِ الرَّحِيمْ"
SUBJECT = "بطاقة علاج"

FIRST = "الأول"
SECOND = "الثاني"
THIRD = "الثالث"
FOURTH = "الرابع"
FIFTH = "الخامس"
SIXTH = "السادس"
SEVENTH = "السابع"
EIGHTH = "الثامن"

THERAPYS_NUMS = [FIRST, SECOND, THIRD, FOURTH,
                 FIFTH, SIXTH, SEVENTH, EIGHTH]

THERAPYS = [THERAPY[1:] + f" {THERAPYS_NUMS[i]}" for i in range(8)]

ALL_DATA = [ALL_NAME, ID[1:], GENDER[1:], SOCIAL[1:], AGE[1:], CHILDREN[1:], PRAYER[1:], HEALTH[1:], WORK[1:],
            COMPANION[1:], CITY[1:], PHONE[1:], DESCRIPTION[1:], DIAGNOSIS[1:], *THERAPYS]  # THERAPY[1:]]

NAME_SEARCH = FNAME[1:]
NAME_SEARCH_X = WIDGETS_X - 450
ID_SEARCH = ID[1:]

NAME_NOT_EXISTS = "!لا يمكن إيجاد الإسم"
ID_NOT_EXISTS = "!لا يمكن إيجاد رقم الهوية"

SEARCH = "البحث"
SEARCH_Y = 150

RESULTS = ":النتائج"
RESULTS_Y = 150

IGNORE = "تجاهل"
IGNORE_X = 5
IGNORE_Y = 700

SAVE = "حفظ"
SAVE_X = 75
SAVE_Y = 700

DONE = "تم"

