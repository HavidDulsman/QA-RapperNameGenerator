import pytest
import urllib3
from flask import Flask, render_template, request
import os
from flask_mysqldb import MySQL
import requests
import csv

app = Flask(__name__)

app.config['MYSQL_HOST']=os.environ['MYSQLHOST']
app.config['MYSQL_USER']=os.environ['MYSQLUSER']
app.config['MYSQL_PASSWORD']=os.environ['MYSQLPASSWORD']
app.config['MYSQL_DB']=os.environ['MYSQLDB']

mysql = MySQL(app)

url = "http://34.89.30.20/"
url2 = "http://35.246.119.11/"

def test_node_manager():
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    assert 200 == r.status

def test_node_worker():
    http = urllib3.PoolManager()
    r = http.request('GET', url2)
    assert 200 == r.status

def test_getresponse():
    r = requests.get(url2)
    assert isinstance(r.text, str)

def test_getresponse2():
    r = requests.get(url)
    assert isinstance(r.text, str)

def test_csv_service2():
    for row in open("../service_2/application/first.txt"):
        coloumnlist = str(row)
        coloumnlist = coloumnlist.split(",")
    assert len(coloumnlist) == 25

def test_csv_service3():
    for row in open("../service_3/application/last.txt"):
        coloumnlist = str(row)
        coloumnlist = coloumnlist.split(",")
    assert len(coloumnlist) == 16


# def test_sql_insert():
#     with app.app_context():
#         response = requests.get('http://end_product:5003/generated3')
#         generatedname = response.text
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO entries(name_old, name_new) VALUES ('Mark', %s)", (generatedname))
#         mysql.connection.commit()
#         numEntries = cur.execute("SELECT * FROM entries")
#         mysql.connection.commit()
#         cur.close()
#         assert 0 < numEntries