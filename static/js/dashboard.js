var DashboardStat = function (StatId) {
    if (StatId == "BatteriesUsedToday") {
        document.getElementById(StatId).innerHTML = "15";
    }
    else if (StatId == "BatteriesDispatched") {
        document.getElementById(StatId).innerHTML = "15";
    }
    else if (StatId == "NoOfCompanies") {
        document.getElementById(StatId).innerHTML = "15";
        let xhr = new XMLHttpRequest();
        xhr.open('GET', 'http://165.232.181.217:8000/GetAllCompanies')
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
        xhr.send();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                const jsondata = JSON.parse(xhr.responseText);
                document.getElementById(StatId).innerHTML = jsondata.length;
            }
        }
    }
}
