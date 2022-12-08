###  ВСЕ ПЕРЕРОБИВ ВІД ПЕРШОГО ВАРІАНТУ.. ЦЕ ВСЕ УСКЛАДНЕННЯ ДЛЯ ВЛАСНОЇ ПРАКТИКИ...
import datetime
import getpass
import csv
import json


class MyOpen:
    """
    Реалізован так що можна відкривати різні файли і він буде в логи заносить ім'я та данні різних файлів, не лише одного File.txt..
    """
    def __init__(self, file_name: str, mode: str = 'r'):
        self.file_name = file_name
        MyOpen.write_log(self.file_name, 'OPEN')
        self.file = open(file_name, mode=mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        MyOpen.write_log(self.file_name, 'CLOSE')

    @classmethod
    def write_log(cls, name_file, action):
        with open('logs.txt', 'a') as file_log:
            file_log.write(
                f'{getpass.getuser()} {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} {name_file} {action}\n')


# task 2 __зробив більш універсальною функцію, тепер можна передавати як аргументи вихідний файл та кінцевий файл.
# Також за допомогою декоратора реалізував перевірку, та виправлення ім'я файла, на випадок якщо користувач забув вказати розширення файла...
def check_file_extension(func):
    def wrapper(file_txt, file_csv):
        file_txt = file_txt if file_txt[-4:] == '.txt' else file_txt + '.txt'
        file_csv = file_csv if file_csv[-4:] == '.csv' else file_csv + '.csv'
        func(file_txt, file_csv)
    return wrapper


@check_file_extension
def reform_txt_file_in_csv(txt_file: str, name_file_csv: str):
    with open(txt_file) as file_txt:
        data_txt = []
        for line in file_txt.readlines():
            line = line.strip()
            data_txt.append(line.split(' '))

        with open(name_file_csv, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['user', 'data', 'time', 'file', 'action'])
            writer.writerows(data_txt)



# task3
#Варіант 1 - згідно з завданням
# def set_data_in_json():
#     with open('logs.csv') as file_logs:
#         reader = csv.DictReader(file_logs, delimiter=',')
#         count = 0
#         last_time_opened = ''
#         for row in reader:
#             if row['action'] == 'OPEN':
#                 last_time_opened = row['data'] + ' ' + row['time']
#                 count += 1
#         data = {"file.txt": {"count_open": count, "last_time_opened": last_time_opened}}
#         with open('logs.json', 'w') as file_json:
#             json.dump(data, file_json, indent=4)


# task3
# Варіант 2 - розширив можливість функцї. Тепер вона буди заносити в json данні про всі файли окремо що є у логах.
def set_data_in_json():
    with open('logs.csv') as file_logs:
        reader = csv.DictReader(file_logs, delimiter=',')
        data = {}.fromkeys(row['file'] for row in reader)  #створюю словник, ключ буде ім'я файлу, значення поки що None
        for key in data.keys():
            data[key] = {"count_open": 0, "last_time_opened": None}  #ключам присвоюємо значення у вигляді вкладеного словника, в якому буде 2 значення(формат як вимагається в завданні). Ці дії потрібні щоб встановити значення Сount = 0, для того щоб далі можна було його додавати.
        file_logs.seek(26)  #перевів каретку не на "0", так в моєму файлі logs.csv першою строкою іде іменування колонок
        for row in reader:  #далі циклом проходимо по строках logs.csv, підраховуємо кількість відкривань файлів. Час останнього відкривання буде на останній ітерації конкретного файла, він і залишиться в data.
            if row['action'] == 'OPEN':
                data[row['file']]['count_open'] += 1
                data[row['file']]['last_time_opened'] = row['data'] + ' ' + row['time']
        print(data)
        with open('logs.json', 'w') as file_json:
            json.dump(data, file_json, indent=4)


if __name__ == "__main__":
    # with MyOpen('file.txt', 'w') as file:
    #     file.write('1\n2\n3\n4\n')
    with MyOpen('logs.txt') as file:
        print(file.readlines())

    reform_txt_file_in_csv('logs.txt', 'logs')  # побую передати ім'я файла без розширення.. Працює)))
    set_data_in_json()

