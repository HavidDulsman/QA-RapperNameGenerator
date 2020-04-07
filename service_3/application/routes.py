from application import app
import random
import csv

@app.route('/generated2', methods=['GET'])
def generated2():
    number = random.randrange(0,15)
    with open('/opt/service3/application/last.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            lastname = str(row[number])
    return lastname
  