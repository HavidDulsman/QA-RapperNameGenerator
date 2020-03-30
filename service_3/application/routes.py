from application import app
import random 

@app.route('/generated2', methods=['GET'])
def generated2():
    list = ['DevOps Consultant', 'Coder', 'Pump', 'Medic', 'Shooter', 'Money', 'Lamborghini', 'Yeezy', 'Killer', 'Game', 'Driver', 'Man']
    listcount = len(list)

    return list[random.randrange(listcount - 1)]