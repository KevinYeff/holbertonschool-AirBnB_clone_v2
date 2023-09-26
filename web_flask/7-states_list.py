#!/usr/bin/python3
"""Starts a web flask application"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of states in a html page"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def t_down(self):
    """Removes te current session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
