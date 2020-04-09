from application import app
import random
import csv

@app.route('/generated1', methods=['GET'])
def generated1():
    number = random.randrange(0,24)
    with open('/opt/service2/application/first.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            firstname = str(row[number])
    return firstname