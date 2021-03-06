from flask import render_template, send_from_directory
from app import app
import shelve
from os import path

STATS_DB = "stats.dict"

@app.route('/')
@app.route('/map')
def index():

    stats = ""

    try:
        stats = shelve.open(path.join(app.root_path, STATS_DB))
    except Exception as e:
        print("ERROR: Could not open STATS_DB")
        print(e)

    attempts = 0
    try:
        attempts = stats['total_attempts']
    except Exception as e:
        print(e)

    ips = 0
    try:
        ips = stats['unique_ips']
    except:
        pass

    countries = 0
    try:
        countries = stats['unique_countries']
    except:
        pass


    updated = "Unavailable"
    try:
        updated = stats['last_updated']
    except:
        pass

    try:
        stats.close()
    except:
        pass

    return render_template('index.html', total_logins=attempts, unique_addresses=ips, unique_countries=countries, last_updated=updated)

@app.route('/folium_map.html')
def getMap():
    return render_template('folium_map.html')

@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory('templates', path)
