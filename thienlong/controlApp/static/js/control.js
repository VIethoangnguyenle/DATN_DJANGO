// var modal = document.getElementById("myModal").className("modal");
// var modal = document.getElementsByClassName("modal");
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function show_control() {
    var control = document.getElementById("myControl");
    var home = document.getElementById("myHome");
    var report = document.getElementById("myReport");
    var help = document.getElementById("myHelp");

    control.classList.remove("display-none");
    control.classList.add("display-block");

    report.classList.remove("display-block");
    report.classList.add("display-none");

    help.classList.remove("display-block");
    help.classList.add("display-none");

    home.classList.remove("display-block");
    home.classList.add("display-none");
    return false;
}
function show_home() {
    var control = document.getElementById("myControl");
    var home = document.getElementById("myHome");
    var report = document.getElementById("myReport");
    var help = document.getElementById("myHelp");
    home.classList.remove("display-none");
    home.classList.add("display-block");

    control.classList.remove("display-block");
    control.classList.add("display-none");

    report.classList.remove("display-block");
    report.classList.add("display-none");

    help.classList.remove("display-block");
    help.classList.add("display-none");
    return false;
}
function show_report() {
    var control = document.getElementById("myControl");
    var home = document.getElementById("myHome");
    var report = document.getElementById("myReport");
    var help = document.getElementById("myHelp");
    report.classList.remove("display-none");
    report.classList.add("display-block");

    help.classList.remove("display-block");
    help.classList.add("display-none");

    home.classList.remove("display-block");
    home.classList.add("display-none");

    control.classList.remove("display-block");
    control.classList.add("display-none");

    return false;
}
function show_help() {
    var control = document.getElementById("myControl");
    var home = document.getElementById("myHome");
    var report = document.getElementById("myReport");
    var help = document.getElementById("myHelp");

    help.classList.remove("display-none");
    help.classList.add("display-block");

    control.classList.remove("display-block");
    control.classList.add("display-none");

    report.classList.remove("display-block");
    report.classList.add("display-none");

    home.classList.remove("display-block");
    home.classList.add("display-none");

    return false;
}
function close_tab() {
    var control = document.getElementById("myControl");
    var report = document.getElementById("myReport");
    var help = document.getElementById("myHelp");
    var home = document.getElementById("myHome");

    control.classList.remove("display-block");
    control.classList.add("display-none");

    report.classList.remove("display-block");
    report.classList.add("display-none");

    help.classList.remove("display-block");
    help.classList.add("display-none");

    home.classList.remove("display-block");
    home.classList.add("display-none");
    return false;
}

function submitData(){
    if (confirm('Are you sure you want to save this thing into the database?')) {
        var sizepaper = document.getElementById("sizepaper").value;
        var error = document.getElementById("error").value;
        var levelSpeed = document.getElementById("levelSpeed").value;
        var distance = document.getElementById("distance").value;
        var option = document.getElementById("option").value;
        console.log("size", sizepaper);
        console.log("error", error);
        console.log("levelSpeed", levelSpeed);
        console.log("distance", distance)
        console.log("option", option)
        fetch("/api/control/", {
            "method": "POST",
            "headers": {
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9,vi;q=0.8",
                "sec-fetch-dest": "empty",
                "sec-fetch-site": "same-origin",
                'X-CSRFToken': getCookie('csrftoken')
            },
            "referrer": "",
            "referrerPolicy": "same-origin",
            body: JSON.stringify({
                // "new_status_id": new_status_id
                "levelSpeed" :levelSpeed,
                "error": error,
                "sizepaper":sizepaper,
                "distance":distance,
                "option":option,
                "state": "1"
            }),
            "mode": "cors",
            "credentials": "include"
        })
        console.log('Thing was saved to the database.');
        alert("Save to database !!");
    } else {
        alert("Not save");
        console.log('Thing was not saved to the database.');
    }
}
function stop(){
    if (confirm('Are you sure you want to stop ?')) {
        var sizepaper = document.getElementById("sizepaper").value;
        fetch("/api/stop/", {
            "method": "POST",
            "headers": {
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9,vi;q=0.8",
                "sec-fetch-dest": "empty",
                "sec-fetch-site": "same-origin",
                'X-CSRFToken': getCookie('csrftoken')
            },
            "referrer": "",
            "referrerPolicy": "same-origin",
            body: JSON.stringify({
                // "new_status_id": new_status_id
                "levelSpeed" :0,
                "error": 0,
                "sizepaper": sizepaper,
                "option": 1,
                "distance": 0,
                "state": "0"
            }),
            "mode": "cors",
            "credentials": "include"
        })
        console.log('Thing was saved to the database.');
        alert("STOPP NOW !!");
    } else {
        alert("Not save");
        console.log('Thing was not saved to the database.');
    }
}
function sendMail() {
    if (confirm('Are you sure you want to send report to this Email?')) {
        var email = document.getElementById("email").value;
        var date = document.getElementById("Date").value;
        console.log(email);
        console.log(date);
        fetch("/api/sendmail/", {
            "method": "POST",
            "headers": {
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9,vi;q=0.8",
                "sec-fetch-dest": "empty",
                "sec-fetch-site": "same-origin",
                'X-CSRFToken': getCookie('csrftoken')
            },
            "referrer": "",
            "referrerPolicy": "same-origin",
            body: JSON.stringify({
                // "new_status_id": new_status_id
                "email": email,
                "date": date,
            }),
            "mode": "cors",
            "credentials": "include"
        })
        alert("Send mail successfully");
    } else {
        alert("Nothing changes.");
    }
}

function filterResult() {
    var date = document.getElementById("Date").value;
    console.log(date);
    fetch("/api/filter/", {
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,vi;q=0.8",
            "sec-fetch-dest": "empty",
            "sec-fetch-site": "same-origin",
            'X-CSRFToken': getCookie('csrftoken')
        },
        "referrer": "",
        "referrerPolicy": "same-origin",
        body: JSON.stringify({
            // "new_status_id": new_status_id
            "date": date,
        }),
        "mode": "cors",
        "credentials": "include"
    })
    alert("OK");
}