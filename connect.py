import napalm
from passFunc import decryptPass
#from flask import jsonify


def connect(host, getFunc):

    results = []

    driver = napalm.get_network_driver('eos')

    decPass = decryptPass()

    device = driver(hostname=host, username='vagrant', password=decPass, optional_args={'port': 12443})

    device.open()

    if getFunc == 'facts':
        results = device.get_facts()
    if getFunc == 'config':
        results = device.get_config()
    else:
        results = device.get_facts()

    device.close()

    return results
