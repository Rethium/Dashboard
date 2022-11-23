var DashboardStat = function (StatId) {
    if (StatId == "BatteriesUsedToday") {
        document.getElementById(StatId).innerHTML = "1";
    }
    else if (StatId == "BatteriesDispatched") {
        document.getElementById(StatId).innerHTML = "";
    }
    else if (StatId == "NoOfCompanies") {
        document.getElementById(StatId).innerHTML = "";
        let xhr = new XMLHttpRequest();
        xhr.open('GET', 'http://165.232.181.217:8000/GetAllUsers')
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
        xhr.send();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                const jsondata = JSON.parse(xhr.responseText);

                //console.log("jsondata",jsondata)

                let obj = {};
                for(let i = 0; i < jsondata.length; i++) {
                    if(!obj[jsondata[i][3]]){
                        obj[jsondata[i][3]] = 1;
                    }else{
                        obj[jsondata[i][3]] += 1;
                    }
                }
                document.getElementById(StatId).innerHTML = Object.keys(obj).length;

                console.log("jsondatalength", jsondata.values)

                document.getElementById("BatteriesDispatched").innerHTML = jsondata.length;


            }
        }
    }
}



