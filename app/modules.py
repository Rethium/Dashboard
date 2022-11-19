import json
import requests


def api(action, requestdata):
    if action == 'dashboardsignin':
        return dashboardsignin(requestdata)
    elif action == 'signup':
        return signup(requestdata)


def dashboardsignin(requestdata):
    data = json.loads(requestdata.decode('utf-8'))
    baseurl = "http://165.232.181.217:8000/DashboardSignIn?"
    # baseurl = "http://localhost:8000/DashboardSignIn?"
    username = data['username']
    password = data['password']
    posturl = baseurl+"username="+username+"&password="+password
    response = requests.get(posturl)
    responsedict=json.loads(response.text)
    status=responsedict['status']
    if(status == 'success'):
        return{'status': status,"redirect":"/dashboard"}
    else:
        return{'status': status,"redirect":"/"}


def signup(requestdata):
    pass
