import glob, csv, shutil
from os import getcwd, access, W_OK
from os.path import abspath, dirname, split
from os.path import join as os_join
from random import randint, choice, randrange
from datetime import datetime, timedelta, timezone

from rndinfo import sql
#sys.path.append("/rndinfo/")

__title__ = 'rndinfo'
__version__ = '1.0.0'
__author__ = 'Alex Panchenko based on Bhuvan Gandhi'
__license__ = 'MIT'

full_path = abspath(os_join(dirname(__file__), "data.csv"))
startRange = datetime(1950, 1, 1, 0, 0, 0, 0, timezone.utc)
endRange = datetime.today() - timedelta(days=4839)


def get_csv(min_blank: bool = True):
    with open(full_path, encoding='utf-8') as csv_file:
        read_data = csv.reader(csv_file)
        for row in read_data:
            # Use minimum filter for input data
            if min_blank:
                if row.count('') > 3 or 'lastname' in row:
                    continue
                else:
                    sql.insert(row)
            else:
                sql.insert(row)


get_csv()


def reformatted_datetime(out_format, str_date, str_format: str = "%d-%m-%Y %H:%M:%S"):
    return datetime.strptime(str_date, str_format).strftime(out_format)


def get_digit():
    return randint(0, 9)


def get_id(length: int = 6, seq_number=None, step=1, prefix=None, postfix=None):
    generated_id = ""
    if seq_number is None:
        for _ in range(length):
            generated_id += str(get_digit())
    else:
        if type(seq_number).__name__ != 'int' or type(step).__name__ != 'int':
            raise TypeError("Sequence number must be an integer.")
        else:
            generated_id = str(seq_number + step)
    if prefix is not None:
        prefix += generated_id
        generated_id = prefix
    if postfix is not None:
        generated_id += postfix
    return generated_id


def get_first_name(gender=None):
    if gender is None:
        gender = get_gender()
    if gender.lower() == "male":
        fn = sql.get_equal("gender", 'male')
    elif gender.lower() == "female":
        fn = sql.get_equal("gender", 'female')
    else:
        fn = sql.get_equal("gender", '')
    return choice(fn)[0], gender


def get_last_name():
    last_name = sql.get_any()
    return choice(last_name)[1]


def get_gender():
    return choice(['male', 'female'])


def get_full_name(gender: str = None):
    return get_first_name(gender)[0] + " " + get_last_name()


def get_special_characters():
    spec_chars = '!@#$%^&*()=+|<>?/;:"[]{}-'
    return choice(spec_chars)


def get_alfa_upper():
    alpha = "abcdefghijklmnopqrstuvwxyz".upper()
    return choice(alpha)


def get_alfa_lower():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return choice(alpha)


def get_alfa():
    return choice([get_alfa_upper(), get_alfa_lower()])


def get_otp(length: int = 6, digits: bool = True, alpha: bool = True, lowercase: bool = True, uppercase: bool = True):
    chars = ""
    if not digits and not alpha:
        raise ValueError("One of parameters 'digits' or 'alpha' must be True.")
    if not lowercase and not uppercase:
        raise ValueError("One of parameters 'lowercase' or 'uppercase' must be True.")
    for _ in range(length):
        fun = []
        if lowercase and alpha:
            fun.append(get_alfa_lower())
        if uppercase and alpha:
            fun.append(get_alfa_upper())
        if digits:
            fun.append(str(get_digit()))
        chars += choice(fun)
    return chars


def get_email(person = None):
    domains = ["gmail", "yahoo", "hotmail", "express", "meta", "nexus",
               "online", "omega", "institute", "finance", "smalloffice", "alpha", "sales"]
    extentions = ['com', 'in', 'jp', 'us', 'uk', 'org', 'edu', 'au', 'de', 'ua',
                  'co', 'me', 'biz', 'dev', 'ngo', 'site', 'xyz', 'zero', 'tech']
    if person is None:
        person = Person()

    method = randint(1, 4)
    fn = person.first_name.lower()
    ln = person.last_name.lower()
    dmn = f'@{choice(domains)}.{choice(extentions)}'

    if method == 1:
        email = fn + reformatted_datetime("%Y", person.birthdate, "%d %b, %Y")
    elif method == 2:
        email = fn + "_" + ln
    elif method == 3:
        email = fn[0] + "." + ln
    else:
        email = ln + reformatted_datetime("%Y", person.birthdate, "%d %b, %Y")
    return email + dmn


def get_random_password(length: int = 8, digits: bool = True, special_chars: bool = True):
    chars = ""
    chars += get_alfa_lower()
    chars += get_alfa_upper()
    if digits:
        chars += str(get_digit())
    if special_chars:
        chars += get_special_characters()
    for _ in range(length-len(chars)):
        fun = []
        fun.append(get_alfa_lower())
        fun.append(get_alfa_upper())
        if digits:
            fun.append(str(get_digit()))
            fun.append(str(get_digit()))
        if special_chars:
            fun.append(get_special_characters())
            fun.append(get_special_characters())
        chars += choice(fun)
    return chars


def get_phone_number(country_code: bool = True):
    phone = ""
    if country_code is True:
        c_codes = [91, 144, 141, 1, 44, 86, 52, 61, 32, 20, 33, 62, 81, 31, 7]
        phone = "+"
        phone += str(choice(c_codes))
        phone += " "
    for i in range(0,10):
        if i == 0:
            phone += str(randint(6,9))
        else:
            phone += str(randint(0,9))
    return phone


def get_alphabetic_profile_img(char, filePath, imgName, charColor = None, bgColor = None):
    chars = "qwertyuioplkjhgfdsazxcvbnmQAZXSWEDCVFRTGBNHYUJMKLIOP0123456789 ,.+=-_()[]{}"
    if all((c in chars) for c in imgName):
        if access(dirname(filePath), W_OK):
            if charColor != None:
                if not charColor.isalpha():
                    raise ValueError("Character color must be a name of color.")
            if bgColor != None:
                if not bgColor.isalpha():
                    raise ValueError("Background color must be a name of color.")
            char = char[:1].upper()
            if bgColor == None:
                colors = ['red', 'green', 'royalblue', 'violet', 'pink', 'indigo', 'grey', 'yellowgreen', 'teal']
                bgColor = choice(colors)
            if charColor == None:
                charColor = (40, 40, 40)
            img = "" #  Image.new('RGB', (512, 512), color = bgColor)
            d = "" #  ImageDraw.Draw(img)
            font = "" #  ImageFont.truetype("Candara.ttf", 280)
            d.text((170,140), char, fill=charColor, font = font)
            filePath = filePath + "\\" + str(imgName) + ".jpg"
            img.save(filePath)
        else:
            raise OSError("Invalid or insufficient privileges for specified file path.")
    else:
        raise OSError(
            "Invalid Image name. Image name must contains characher including digits, " +
            "alphabets, white space, dot, comma, ( ) [ ] { } _ + - =.")
    return filePath


def get_face_profile_img(filePath, imgName, gender = None):
    dir_name, file_name = split(abspath(__file__))
    chars = "qwertyuioplkjhgfdsazxcvbnmQAZXSWEDCVFRTGBNHYUJMKLIOP0123456789 ,.+=-_()[]{}"
    if all((c in chars) for c in imgName):
        if access(dirname(filePath), W_OK):
            if gender == None:
                orig_file = choice(glob.glob(dir_name + "\\Images\\people\\*.jpg"))
            elif gender.lower() == "female":
                orig_file = choice(glob.glob(dir_name + "\\Images\\people\\female_*.jpg"))
            elif gender.lower() == "male":
                orig_file = choice(glob.glob(dir_name + "\\Images\\people\\male_*.jpg"))
            else:
                return ValueError("Invalid gender. It must be male or female.")
            return shutil.copy(orig_file, filePath + "\\" + str(imgName) + ".jpg")
        else:
            raise OSError("Invalid or insufficient privileges for specified file path.")
    else:
        raise OSError("Invalid Image name. mage name must contains characher including digits, alphabets, white space, dot, comma, ( ) [ ] { } _ + - =.")


def get_today(_format="%d-%m-%Y %H:%M:%S"):
    return datetime.today().strftime(_format)


def get_date(tstamp = None, _format="%d %b, %Y"):
    if tstamp == None:
        startTs = startRange.timestamp()
        endTs = endRange.timestamp()
        tstamp = randrange(int(startTs), int(endTs))
    else:
        if type(tstamp).__name__ != 'int':
            raise ValueError("Timestamp must be an integer.")
    return datetime.utcfromtimestamp(tstamp).strftime(_format)


def get_birthdate(startAge=13, endAge=67, _format="%d %b, %Y"):
    if startAge != None:
        if type(startAge).__name__ != 'int':
            raise ValueError("Starting age value must be integer.")
    if endAge != None:
        if type(endAge).__name__ != 'int':
            raise ValueError("Ending age value must be integer.")
    if startAge != None and endAge != None: #If both are given in arg
        if startAge >= endAge:
            raise ValueError("Starting age must be less than ending age.")
        else:
            startRange = datetime(datetime.now().year - startAge, 12, 31, 23, 59, 59, 0, timezone.utc)
            endRange = datetime(datetime.now().year - endAge, 1, 1, 0, 0, 0, 0, timezone.utc)
    startTs = startRange.timestamp()
    endTs = endRange.timestamp()
    rnd_date = randrange(int(endTs), int(startTs))
    if rnd_date <0:
        return (datetime.fromtimestamp(0) + (datetime.fromtimestamp(0) - datetime.fromtimestamp(abs(rnd_date)))).strftime(_format)
    else:
        return datetime.fromtimestamp(rnd_date).strftime(_format)


def get_land():
    land = sql.get_not("landmark", "")
    return choice(land)[0]


def get_street():
    streets = sql.get_not("street", "")
    return choice(streets)[0]


def get_area():
    area = sql.get_not("area", "")
    return choice(area)[0]


def get_city():
    city = sql.get_not("city", "")
    return choice(city)[0]


def get_province():
    province = sql.get_not("province", "")
    return choice(province)[0]


def get_zip():
    zip = sql.get_not("zip", "")
    return choice(zip)[0]


def get_address():
    full_addr = [get_street(), get_area(), get_land(), get_province(), get_city(), get_zip()]
    addr_param = ['street', 'area', 'landmark', 'province', 'city', 'zip']
    full_addr = dict(zip(addr_param, full_addr))
    return full_addr


def get_hobbies():
    hobbies = sql.get_not("hobbies", "")
    return choice(hobbies)[0]


class Person:
    def __init__(self, gender=None):
        self.first_name, self.gender = get_first_name(gender)
        self.last_name = get_last_name()
        self.full_name = self.first_name + " " + self.last_name
        self.birthdate = get_birthdate()
        self.phone = get_phone_number()
        self.email = get_email(self)
        self.login = (self.email.split("@")[0]).lower()
        self.land = get_land()
        self.password = get_random_password()
        self.hobbies = get_hobbies()
        self.address = get_address()
        self.customAttr = {}

    def set_attr(self, attr_name, value = None):
        if attr_name.isalnum():
            if attr_name[0].isalpha():
                self.customAttr[attr_name] = value
                print("Attribute '" + str(attr_name) + "' added.")
            else:
                raise ValueError("First character of attribute must be an alphabet.")
        else:
            raise ValueError("Attribute name only contains alphabets and digits.")

    def get_attr(self, attr_name):
        if attr_name.isalnum():
            if attr_name[0].isalpha():
                if attr_name in self.customAttr.keys():
                    return self.customAttr[attr_name]
                else:
                    raise AttributeError("Specified attribute is not exists.")
            else:
                raise ValueError("First character of attribute must be an alphabet.")
        else:
            raise ValueError("Attribute name only contains alphabets and digits.")

    def get_details(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "email": self.email,
            "login": self.login,
            "phone": self.phone,
            "password": self.password,
            "land": self.land,
            "hobbies": self.hobbies,
            "address": self.address,
            "other_attr": self.customAttr
        }

'''
REFERENCE:
http://www.first-names-meanings.com/country-indian-names.html
https://www.familyeducation.com/baby-names/browse-origin/surname/indian
https://thispersondoesnotexist.com/
https://en.wikipedia.org/wiki/List_of_hobbies
'''

if __name__ == "__main__":
    person = Person()
    print(person.get_details())
