from application import app
import requests

@app.route('/generated3', methods=['GET'])
def generated3():
    firstname = requests.get('http://part_one:5001/generated1')
    secondname = requests.get('http://part_two:5002/generated2')
    response = firstname.text + " " + secondname.text
    print(response)
    return response