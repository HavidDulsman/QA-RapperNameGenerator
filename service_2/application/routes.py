from application import app
import random

@app.route('/generated1', methods=['GET'])
def generated1():
    list = ['Lil','Big','The','Yung', 'Da','Dockta','Hot', 'Eazy', 'Almighty', 'Ol Dirty', 'Ghostface', 'Childish', 'Wonky', 'Crazy', 'Gucci', 'Red', 'West-side', 'East-side', 'South-side', 'North-side', 'Famous', 'Hungry', 'Sneaky', 'Sniper', 'Lethal']
    listcount = len(list)

    return list[random.randrange(listcount - 1)]