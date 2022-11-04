import datetime
import getpass
import csv
import json


class MyOpen:
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
            file_log.write(f'{getpass.getuser()} {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")} {name_file} {action}\n')


#task 2
def reform_txt_file_in_csv(txt_file):
    with open(txt_file) as file_txt:
        data_txt =[]
        for line in file_txt.readlines():
            line = line.rstrip()
            data_txt.append(line.split(' '))

        with open('logs.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data_txt)


#task3
def get_info_log_file():
    with open('logs.csv') as file_logs:
        reader = csv.reader(file_logs)
        count = 0
        last_time_opened = ''
        for row in reader:
            if row[4] == 'OPEN':
                last_time_opened = row[2]
                count += 1
        data = {'file.txt': {'count_open': count, "last_time_opened": last_time_opened}}
        with open('logs.json', 'w') as file_json:
            json.dump(data, file_json, indent=4)


with MyOpen('file.txt', 'w') as file:
    file.write('1\n2\n3\n4\n')

reform_txt_file_in_csv('logs.txt')
get_info_log_file()

