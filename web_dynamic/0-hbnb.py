#!/usr/bin/python3
"""starts a flash web app"""

from flask import Flask, render_template
from os import environ
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from uuid import uuid4


app == Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

@app.teardown_appcontext
def close_db(error):
    """ remove the current sqlalchemy session"""
    storage.close()

@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB """
    states = storage.all(State).value()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    place = storage.all(Place).value()
    place = sorted(place, key=lambda k: k.name)

    #generate a uuid and convert it to a string
    cache_id = str(uuid4())

    return render_template('0-hbnb.html',
            states=st_ct,
            amenities=amenities,
            place=places,
            cache_id=cache_id)

if __name__ == "__main__":
    """main function"""
    app.run(host='0.0.0.0', port=5000)
