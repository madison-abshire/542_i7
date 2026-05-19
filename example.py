from flask import Flask, jsonify
import json
import csv

app = Flask(__name__)

def read_json_file(filename):
    with open(filename) as file:
        data = json.load(file)
    return data

my_dict = read_json_file("data/sbir-search-results.json")

@app.route('/sbir/state/<state>')
def sbir_state(state):
    for i in my_dict:
       if i['State']==state:
          return i['Award_Title'] 
    return 'none'

@app.route('/')
def info():
    message=f"""
       Hello, I am your API.
       You can call my functions
       hello or hello(name)
    """ 
    return message 

@app.route('/hello/name/<username>')
def hello(username):
    return 'hello %s' % username

# station_dict = list(csv.DictReader(open('data/links.csv')))
with open('data/links.csv') as f:
    station_dict = list(csv.DictReader(f))

@app.route('/data/stations')
def stations_info():
    message=f"""
        Use stations/existing for current stations \n
        Use stations/future for future stations \n
    """
    return message

@app.route('/data/stations/<status>')
def stations_status(status):
    status_key = "Future" if status == "future" else "Existing / Under Construction"
    name_list = []
    for station in station_dict:
        # print(station)
        if station['attributes_STATUS']==status_key:
            name_list.append(station['attributes_NAME'])

    return jsonify(name_list)


 
