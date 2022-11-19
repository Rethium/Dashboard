var Authenticate = function (data) {
    data = JSON.parse(data);
    if (data.status === 'success') {
        window.location.href = data.redirect;
    }
    else {
        console.log(data);
    }
}

var APICall = function (type, data, url) {
    let xhr = new XMLHttpRequest();
    xhr.open(type, url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(data));
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(xhr.responseText);
            Authenticate(xhr.responseText);
        }
    }
}

var SignIn = function () {
    let username = document.getElementById('Username');
    let password = document.getElementById('password');
    let usernameval = username.value;
    let passwordval = password.value;
    if (usernameval === '' || passwordval === '') {
        alert('Please fill in all fields');
    }
    else {
        const data = {
            "username": usernameval,
            "password": passwordval
        }
        const url = '/API/dashboardsignin';
        APICall('POST', data, url);
        username.value = '';
        password.value = '';
    }
}

var logout = function () {
    alert("logout");
}

