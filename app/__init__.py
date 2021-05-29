from logging import debug
from flask import Flask

app=Flask(__name__)

app.config['DEBUG']= True

@app.route('/')
def inicioapp():
    return 'inicio de la aplicion'

 