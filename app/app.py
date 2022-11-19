from flask import *
from requests import request as req
from modules import *
from flask import render_template
from flask_cors import CORS, cross_origin
import subprocess
import os

app = Flask(__name__, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@app.route('/signin')
def hello_world():
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
