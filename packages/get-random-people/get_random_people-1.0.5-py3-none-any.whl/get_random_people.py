from random import randint
from countries import countries
from countries_capital import countries_capital
from qualifications import qualifications
from get_name_gender_religion import get_name_gender_religion
from uuid import uuid1
from datetime import date, datetime

def get_address(nationality):
    country = nationality
    region = countries_capital[nationality]
    street = f"{randint(11, 124)}th street"
    house = f"House no {randint(1, 30)}"
    return f"{house}, {street}, {region}, {country}"

def get_skin_color():
    skin_colors = ("white","brown", "pale", "black")
    return skin_colors[randint(0, len(skin_colors) - 1)]

def get_eye_color(skin_color):
    eye_colors = []
    if skin_color == "white" or skin_color == "pale":
        eye_colors = ["blue", "green", "grey", "brown", "black"]
    else:
        eye_colors = ["brown", "black"]

    return eye_colors[randint(0, len(eye_colors) - 1)]

def get_hair_style(gender):
    hair_styles = ['short', 'medium', 'long', 'bald', 'sides short center long']
    if gender == "female":
        hair_styles.remove("bald")
    return hair_styles[randint(0, len(hair_styles) - 1)]

def get_hair_color(skin_color, age, hair_style):
    hair_color = []
    if skin_color == "white" or skin_color == "pale":
        hair_color = ["blonde", "brown", "black", "red", "white"]
    else:
        hair_color = ["brown", "black"]
    
    if(age > 65):
        hair_color = ["white"]
    
    if(hair_style == "bald"):
        hair_color = ["bald"]

    return hair_color[randint(0, len(hair_color) - 1)]

def get_email(firstname, lastname, age):
    domains = ("gmail", "yahoo", "outlook", "hotmail", "live")
    random_index = randint(0, len(domains) - 1)
    email = f"{firstname.lower()}{lastname.lower()}{date.today().year - age}@{domains[random_index]}.com"
    return email

def get_highest_education():
    return qualifications[randint(0, len(qualifications) - 1)]

def get_nationality():
    random_index = randint(0,len(countries) - 1)
    return countries[random_index]

def get_DOB(age):
    year = date.today().year - age
    month = randint(1, 12)
    day = randint(1, 28)
    return datetime(year, month, day).strftime("%b %dth, %Y")

def get_phone_number(length = 10):
    phone_number = str(randint(7, 9))
    for _ in range(0, length - 1):
        phone_number += str(randint(0, 9))
    return phone_number

def get_person():
    firstname, lastname, gender, religion = get_name_gender_religion()
    age = randint(18, 110)
    nationality = get_nationality()
    side_bussiness = ("Youtuber", "Vlogger", "Blogger", "Tiktoker", "Gamer")
    skin_color = get_skin_color()
    hair_style = get_hair_style(gender)
    person = {
        "id": str(uuid1()),
        "firstname": firstname,
        "lastname": lastname,
        "dob": get_DOB(age),
        "email": get_email(firstname, lastname, age),
        "phone_number": get_phone_number(),
        "address": get_address(nationality),
        "gender": gender,
        "religion": religion,
        "age": age,
        "skin_color": skin_color,
        "eye_color": get_eye_color(skin_color),
        "hair_style": hair_style,
        "hair_color": get_hair_color(skin_color, age, hair_style),
        "is_married": True if randint(0, 1) else False,
        "highest_education": get_highest_education(),
        "occupation": "Bussiness" if randint(0, 1) else "Service",
        "side_bussiness": side_bussiness[randint(0, len(side_bussiness) - 1)],
        "annaul_income_USD": randint(2500, 20000) * 12,
        "nationality": nationality,
        "height_in_feet": round(randint(15, 24) / 10 * 3.281, 1),
        "weight_in_kg": randint(35, 90)    
    }
    return person

def get_peoples(totalPeoples = 10):
    peoples = []
    for _ in range(0, totalPeoples):
        peoples.append(get_person())

    return peoples

print(get_peoples(3))