import flask
from flask import request, jsonify
import os
import napalm
from cryptography.fernet import Fernet
from passFunc import decryptPass

app = flask.Flask(__name__)
app.config['DEBUG'] = True

def connect(host, getFunc):

    results = []

    driver = napalm.get_network_driver('eos')

    decPass = decryptPass()

    device = driver(hostname=host, username='vagrant', password=decPass, optional_args={'port': 12443})

    device.open()

    if getFunc == 'facts':
        results = jsonify(device.get_facts())
    if getFunc == 'config':
        results = device.get_config()
    else:
        results = device.get_facts()

    device.close()

    return results

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Testing for Napalm APIs</h1>
<p>A prototype API for Napalm fuctions.</p>'''

@app.route('/api/v1/resources/ping', methods=['GET'])
def api_all():

    if 'host' in request.args:
        hostname = request.args['host']
    else:
        return 'Error: No Hostname provided'

    response = os.system("ping -c 1 " + hostname)

    if response == 0:
        var = 'Host is up'
    else:
        var = 'Host is down'

    return var

@app.route('/api/v1/resources/napalm/get-facts', methods=['GET'])
def api_facts():

    if 'host' in request.args:
        hostname = request.args['host']
    else:
        return 'Error: No Hostname provided'

    results = []
    driver = napalm.get_network_driver('eos')

    results = connect(host = hostname, getFunc = 'facts')

    return jsonify(results)

@app.route('/api/v1/resources/napalm/get-config', methods=['GET'])
def api_config():

    if 'host' in request.args:
        hostname = request.args['host']
    else:
        return 'Error: No Hostname provided'

    results = connect(host = hostname, getFunc = 'config')

    return jsonify(results)

app.run()
