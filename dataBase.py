import time
import csv


class db():
    def __init__(self):
        self.state = False

    def save(self, date):
        if self.state == True:
            date.append(time.asctime())
            with open("telemetry_data.csv", "a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(date)

    def start(self):
        self.state = True
        print('Data Logging Started')

    def end(self):
        self.state = False
        print('Data Logging Ended')
