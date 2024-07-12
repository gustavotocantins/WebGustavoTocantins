from flask import Flask, render_template, url_for, request, redirect
from pickle import load
from re import match
from glob import glob
from os import chdir
import os
import json

app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
