import pandas as pd
import math


def calculate_kn(gender, length, weight):
    closest = []

    for length, weight in zip(gender['stature'], gender['weightkg']):
        delta_y = abs(length) - abs(length)
        delta_x = abs(weight) - abs(weight)
        hypo = delta_y ** 2 + delta_x ** 2
        closest.append(math.sqrt(hypo))

    gender['closest'] = closest
    KN = gender.sort_values(by=['closest']).head(10)
    print(f'Recommended T-shirt size', KN['tshirt_size'].value_counts().idxmax())
    print(f'Recommended Pants size', KN['pants_size'].value_counts().idxmax())



def main():
    male_df = pd.read_csv('male_cleaned.csv')
    female_df = pd.read_csv('female_cleaned.csv')

    male_data = male_df[['stature', 'weightkg', 'chestcircumference', 'waistcircumference', 'buttockcircumference']]
    male_data.insert(5, column="tshirt_size", value="-")
    male_data.insert(5, column="pants_size", value="-")
    male_data.insert(6, column="tshirt_colour", value="-")
    male_data.insert(6, column="pants_colour", value="-")

    female_data = female_df[['stature', 'weightkg', 'chestcircumference', 'waistcircumference', 'buttockcircumference']]
    female_data.insert(5, column="tshirt_size", value="-")
    female_data.insert(5, column="pants_size", value="-")
    female_data.insert(6, column="tshirt_colour", value="-")
    female_data.insert(6, column="pants_colour", value="-")



    gender = input('Are you a Male/Female?: ')
    length = input('What is your length?(cm): ')
    weight = input('What is your weight?(kg): ')
    length = int(length)
    weight = int(weight)

    if gender.lower() == 'male':
        gender = male_df
        tshirt_size_male(gender)
        pants_size_male(gender)
        calculate_kn(gender, weight, length)
    else:
        gender = female_df
        tshirt_size_female(gender)
        pants_size_female(gender)
        calculate_kn(gender, length, weight)


def tshirt_size_male(gender):
    tshirt_size = []
    tshirt_colour = []

    for chest, waist in zip(gender['chestcircumference'], gender['waistcircumference']):
        if chest < 880:
            if waist >= 760:
                tshirt_size.append('Small')
                tshirt_colour.append('Blue')
            else:
                tshirt_size.append('X-Small')
                tshirt_colour.append('Yellow')
        elif chest < 960:
            if waist >= 840:
                tshirt_size.append('Medium')
                tshirt_colour.append('Red')
            else:
                tshirt_size.append('Small')
                tshirt_colour.append('Blue')
        elif chest < 1040:
            if waist >= 920:
                tshirt_size.append('Large')
                tshirt_colour.append('Orange')
            else:
                tshirt_size.append('Medium')
                tshirt_colour.append('Red')
        elif chest < 1120:
            if waist >= 1000:
                tshirt_size.append('X-Large')
                tshirt_colour.append('Black')
            else:
                tshirt_size.append('Large')
                tshirt_colour.append('Orange')
        elif chest < 1200:
            if waist >= 1080:
                tshirt_size.append('XX-Large')
                tshirt_colour.append('Pink')
            else:
                tshirt_size.append('X-Large')
                tshirt_colour.append('Black')
        elif chest < 1240:
            if waist >= 1120:
                tshirt_size.append('XXX-Large')
                tshirt_colour.append('Brown')
            else:
                tshirt_size.append('XX-Large')
                tshirt_colour.append('Pink')
        elif chest >= 1240:
            tshirt_size.append('XXX-Large')
            tshirt_colour.append('Brown')

    gender['tshirt_size'] = tshirt_size
    gender['tshirt_colour'] = tshirt_colour


def pants_size_male(gender):
    pants_size = []
    pants_colour = []

    for butt, waist in zip(gender['buttockcircumference'], gender['waistcircumference']):
        if butt < 950:
            if waist >= 800:
                pants_size.append('Small')
                pants_colour.append('Blue')
            else:
                pants_size.append('X-Small')
                pants_colour.append('Yellow')
        elif butt < 1040:
            if waist >= 880:
                pants_size.append('Medium')
                pants_colour.append('Red')
            else:
                pants_size.append('Small')
                pants_colour.append('Blue')
        elif butt < 1070:
            if waist >= 920:
                pants_size.append('Large')
                pants_colour.append('Orange')
            else:
                pants_size.append('Medium')
                pants_colour.append('Red')
        elif butt < 1130:
            if waist >= 1020:
                pants_size.append('X-Large')
                pants_colour.append('Black')
            else:
                pants_size.append('Large')
                pants_colour.append('Orange')
        elif butt < 1180:
            if waist >= 1070:
                pants_size.append('XX-Large')
                pants_colour.append('Pink')
            else:
                pants_size.append('X-Large')
                pants_colour.append('Black')
        elif butt < 1220:
            if waist >= 1170:
                pants_size.append('XXX-Large')
                pants_colour.append('Brown')
            else:
                pants_size.append('XX-Large')
                pants_colour.append('Pink')
        elif butt < 1280:
            if waist >= 1220:
                pants_size.append('XXXX-Large')
                pants_colour.append('Purple')
            else:
                pants_size.append('XXX-Large')
                pants_colour.append('Brown')
        elif butt >= 1280:
            pants_size.append('XXXX-Large')
            pants_colour.append('Purple')

    gender['pants_size'] = pants_size
    gender['pants_colour'] = pants_colour


def tshirt_size_female(gender):
    tshirt_size = []
    tshirt_colour = []

    for chest, waist in zip(gender['chestcircumference'], gender['waistcircumference']):
        if chest < 800:
            if waist >= 660:
                tshirt_size.append('Small')
                tshirt_colour.append('Blue')
            else:
                tshirt_size.append('X-Small')
                tshirt_colour.append('Yellow')
        elif chest < 880:
            if waist >= 720:
                tshirt_size.append('Medium')
                tshirt_colour.append('Red')
            else:
                tshirt_size.append('Small')
                tshirt_colour.append('Blue')
        elif chest < 960:
            if waist >= 800:
                tshirt_size.append('Large')
                tshirt_colour.append('Orange')
            else:
                tshirt_size.append('Medium')
                tshirt_colour.append('Red')
        elif chest < 1040:
            if waist >= 880:
                tshirt_size.append('X-Large')
                tshirt_colour.append('Black')
            else:
                tshirt_size.append('Large')
                tshirt_colour.append('Orange')
        elif chest < 1160:
            if waist >= 990:
                tshirt_size.append('XX-Large')
                tshirt_colour.append('Pink')
            else:
                tshirt_size.append('X-Large')
                tshirt_colour.append('Black')
        elif chest < 1280:
            if waist >= 1110:
                tshirt_size.append('XXX-Large')
                tshirt_colour.append('Brown')
            else:
                tshirt_size.append('XX-Large')
                tshirt_colour.append('Pink')
        elif chest < 1280:
            tshirt_size.append('XXX-Large')
            tshirt_colour.append('Brown')

    gender['tshirt_size'] = tshirt_size
    gender['tshirt_colour'] = tshirt_colour


def pants_size_female(gender):
    pants_size = []
    pants_colour = []

    for butt, waist in zip(gender['buttockcircumference'], gender['waistcircumference']):
        if butt < 900:
            if waist >= 660:
                pants_size.append('Small')
                pants_colour.append('Blue')
            else:
                pants_size.append('X-Small')
                pants_colour.append('Yellow')
        elif butt < 960:
            if waist >= 720:
                pants_size.append('Medium')
                pants_colour.append('Red')
            else:
                pants_size.append('Small')
                pants_colour.append('Blue')
        elif butt < 1020:
            if waist >= 800:
                pants_size.append('Large')
                pants_colour.append('Orange')
            else:
                pants_size.append('Medium')
                pants_colour.append('Red')
        elif butt < 1100:
            if waist >= 880:
                pants_size.append('X-Large')
                pants_colour.append('Black')
            else:
                pants_size.append('Large')
                pants_colour.append('Orange')
        elif butt < 1200:
            if waist >= 990:
                pants_size.append('XX-Large')
                pants_colour.append('Pink')
            else:
                pants_size.append('X-Large')
                pants_colour.append('Black')
        elif butt < 1300:
            if waist >= 1110:
                pants_size.append('XXX-Large')
                pants_colour.append('Brown')
            else:
                pants_size.append('XX-Large')
                pants_colour.append('Pink')
        elif butt >= 1300:
            pants_size.append('XXX-Large')
            pants_colour.append('Brown')

    gender['pants_size'] = pants_size
    gender['pants_colour'] = pants_colour




if __name__ == '__main__':
    main()
