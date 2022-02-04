import os
import csv
from zipfile import ZipFile
from pandas import read_excel
from urllib.request import urlopen
from warnings import filterwarnings


paths = {
    'temp': os.path.join('.', 'temp'),
    'zip': os.path.join('.', 'temp', 'grades.zip'),
    'extracted': os.path.join('.', 'temp', 'extracted'),
    'xlsm': os.path.join('.', 'temp', 'extracted', 'ics33win22grades.xlsm'),
    'csv': os.path.join('.', 'temp', 'extracted', 'grades.csv'),
    'url': 'https://www.ics.uci.edu/~pattis/ICS-33/ics33win22grades.zip'
}


def get_grades_data():
    response = urlopen(paths['url'])
    zip_data = response.read()
    return zip_data


def make_temp_folder():
    if not os.path.exists(paths['temp']):
        os.mkdir(paths['temp'])


def write_zip_data(zip_data):
    with open(paths['zip'], 'wb+') as f:
        f.write(zip_data)


def unzip_grades():
    with ZipFile(paths['zip'], 'r') as z:
        z.extractall(paths['extracted'])


def xlsm_to_csv():
    read_file = read_excel(paths['xlsm'])
    read_file.to_csv(paths['csv'], index=None, header=True)


def grade_str_from_csv(sid):
    try:
        with open(paths['csv'], 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == sid:
                    grade_pct, rank, grade_ltr = row[27:30]
                    s = f'Grade: {round(float(grade_pct), 1)}% ({grade_ltr})\n'
                    s += f'Rank: {int(float(rank))}'
                    return s
    except:
        return 'Unable to get grade'
    return 'Unable to get grade'


def get_id():
    try:
        with open('saved_id.txt', 'r') as f:
            hashed_id = f.read().replace('\n', '')
        assert len(hashed_id) > 0
    except:
        hashed_id = input('Enter your hashed student id: ').replace(' ', '')
    return hashed_id


if __name__ == '__main__':

    filterwarnings('ignore')

    make_temp_folder()
    write_zip_data(get_grades_data())
    unzip_grades()
    xlsm_to_csv()

    hashed_id = get_id()
    grade_string = grade_str_from_csv(hashed_id)
    print(grade_string)
