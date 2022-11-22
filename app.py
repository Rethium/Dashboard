import logging as lg
import os
import subprocess
from os import getcwd, path

from flask import *
from flask import render_template
from flask_cors import CORS, cross_origin

from modules.modules import *
from modules.setup_instance import *

lg.basicConfig(
    filename='logs/app.log',
    filemode='a',
    level=lg.DEBUG,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = '/static/uploads'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route('/')
@app.route('/signin')
def sign_in():
    return render_template('sign_in.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/registeruser')
@cross_origin()
def registeruser():
    return render_template('registeruser.html')


@app.route('/update')
def update():
    os.system("git stash")
    sp = subprocess.Popen("git pull", shell=True, stdout=subprocess.PIPE)
    subprocess_return = sp.stdout.read()
    subprocess_return = subprocess_return.decode('utf-8')
    return subprocess_return


@app.route('/API/<Action>', methods=['POST', 'GET'])
def API(Action):
    # print(request.data,Action)
    return api(Action, request.data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5050)
