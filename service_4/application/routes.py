from application import app
import requests

@app.route('/generated3', methods=['GET'])
def generated3():
    firstname = requests.get('http://rappernamegenerator_part_one_1:5001/generated1')
    secondname = requests.get('http://rappernamegenerator_part_two_1:5002/generated2')
    response = firstname.text + " " + secondname.text
    print(response)
    return response