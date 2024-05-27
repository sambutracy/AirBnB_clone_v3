#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

# Get all State objects
state_objects = storage.all(State)

# Check if there are any State objects before accessing the first one
if len(state_objects) > 0:
    first_state_id = list(state_objects.values())[0].id
    print("First state: {}".format(storage.get(State, first_state_id)))
else:
    print("No State objects found in the database.")
#first_state_id = list(storage.all(State).values())[0].id
#print("First state: {}".format(storage.get(State, first_state_id)))
