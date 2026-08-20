from flask import Flask, request, redirect, url_for, render_template_string
from datetime import datetime
import os

app = Flask(__name__)


# =========================================================
# PAGE 1
# =========================================================

PAGE_1 = """
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>SIKKIM PRO VIP</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;

    background:
        radial-gradient(
            circle at 50% 35%,
            #10264b 0%,
            #061126 45%,
            #020817 85%
        );

    color: white;
    font-family: Arial, sans-serif;
}

.main {
    max-width: 1000px;
    margin: auto;
    padding: 55px 30px;
}

.top {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 45px;
}

.logo {
    font-size: 58px;
    font-weight: 900;
    letter-spacing: 9px;
}

.vip {
    padding: 18px 40px;

    border: 2px solid #00d9ff;
    border-radius: 25px;

    color: #00d9ff;

    font-size: 25px;
    font-weight: bold;

    letter-spacing: 4px;
}

.timer {
    margin: 55px auto 0;

    width: 360px;
    height: 85px;

    display: flex;

    border: 2px solid #203b63;
    border-radius: 30px;

    overflow: hidden;

    background: #050e20;
}

.timer button {
    width: 50%;
    height: 100%;

    border: none;

    background: transparent;
    color: #91a6c9;

    font-size: 23px;
    font-weight: bold;

    cursor: pointer;
}

.timer button.active {
    background: #16c1df;
    color: #001018;
}

.line {
    margin-top: 60px;

    border-top: 2px dashed #08718a;
}

.connect-area {
    margin-top: 58px;

    display: flex;
    justify-content: center;
    align-items: center;

    gap: 45px;
}

.uid-input {
    width: 560px;
    height: 125px;

    border-radius: 38px;

    border: 3px solid #29466d;

    background: #040d1e;
    color: white;

    padding: 0 40px;

    font-size: 27px;

    outline: none;
}

.uid-input::placeholder {
    color: #35567f;
}

.connect-btn {
    width: 325px;
    height: 125px;

    border: none;
    border-radius: 38px;

    background: #16c1df;
    color: #001018;

    font-size: 32px;
    font-weight: 900;

    letter-spacing: 5px;

    cursor: pointer;
}

.error {
    margin-top: 25px;

    text-align: center;

    color: #ff6868;
}

@media (max-width: 800px) {

    .top {
        flex-direction: column;
        gap: 20px;
    }

    .logo {
        font-size: 42px;
    }

    .connect-area {
        flex-direction: column;
    }

    .uid-input,
    .connect-btn {
        width: 100%;
        height: 105px;
    }

    .timer {
        width: 100%;
    }
}

</style>

</head>

<body>

<div class="main">


    <div class="top">

        <div class="logo">
            SIKKIM
        </div>

        <div class="vip">
            PRO VIP
        </div>

    </div>


    <!-- 30 SEC / 1 MIN -->

    <div class="timer">

        <button
            type="button"
            id="thirtyBtn"
            onclick="selectTime(30)">
            30 SEC
        </button>

        <button
            type="button"
            id="oneMinBtn"
            class="active"
            onclick="selectTime(60)">
            1 MIN
        </button>

    </div>


    <div class="line"></div>


    <form action="/connect" method="POST">

        <input
            type="hidden"
            name="time"
            id="selectedTime"
            value="60"
        >

        <div class="connect-area">

            <input
                class="uid-input"
                type="text"
                name="uid"
                placeholder="ENTER SIKKIM UID"
                required
            >

            <button
                class="connect-btn"
                type="submit">
                CONNECT
            </button>

        </div>

    </form>


    {% if error %}

    <div class="error">
        {{ error }}
    </div>

    {% endif %}


</div>


<script>

function selectTime(seconds) {

    const thirty =
        document.getElementById("thirtyBtn");

    const oneMin =
        document.getElementById("oneMinBtn");

    const selected =
        document.getElementById("selectedTime");


    selected.value = seconds;


    if (seconds === 30) {

        thirty.classList.add("active");
        oneMin.classList.remove("active");

    } else {

        oneMin.classList.add("active");
        thirty.classList.remove("active");

    }

}

</script>

</body>
</html>
"""


# =========================================================
# PAGE 2
# =========================================================

PAGE_2 = """
<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>SERVER CONNECTED</title>


<style>

* {
    box-sizing: border-box;
}


body {

    margin: 0;

    min-height: 100vh;

    background:
        radial-gradient(
            circle at 50% 35%,
            #102b55 0%,
            #071631 45%,
            #020817 85%
        );

    color: white;

    font-family: Arial, sans-serif;
}


.page {

    max-width: 950px;

    min-height: 100vh;

    margin: auto;

    padding: 55px 25px;

    text-align: center;
}


/* SERVER */

.server-title {

    font-size: 42px;

    font-weight: 900;

    letter-spacing: 3px;
}


/* LIVE + REMAIN TIME */

.status-row {

    margin-top: 15px;

    display: flex;

    justify-content: center;

    align-items: center;

    gap: 30px;
}


.live {

    font-size: 23px;

    font-weight: bold;
}


.live-dot {

    color: red;

    font-size: 27px;

    animation: blink 1s infinite;

    text-shadow:
        0 0 8px red,
        0 0 18px red;
}


@keyframes blink {

    0% {
        opacity: 1;
    }

    50% {
        opacity: 0.15;
    }

    100% {
        opacity: 1;
    }
}


/* REMAIN TIME */

.remaining {

    font-size: 21px;

    font-weight: bold;

    color: #8fb6df;
}


.remaining-time {

    color: #16c1df;

    font-size: 24px;

    font-weight: 900;

    letter-spacing: 2px;
}


/* PERIOD BOX */

.period-box {

    width: 85%;

    max-width: 850px;

    height: 110px;

    margin: 45px auto;

    border: 3px solid #00cfff;

    border-radius: 20px;

    background: #061426;

    display: flex;

    flex-direction: column;

    align-items: center;

    justify-content: center;
}


.period-title {

    font-size: 15px;

    color: #6e9bc5;

    margin-bottom: 7px;

    letter-spacing: 3px;

    font-weight: bold;
}


.period-number {

    font-size: 36px;

    font-weight: bold;

    letter-spacing: 7px;

    color: white;
}


/* N1 / N2 */

.number-area {

    width: 85%;

    max-width: 850px;

    margin: auto;

    display: flex;

    gap: 25px;
}


.number-input {

    width: 50%;

    height: 90px;

    border: 3px solid #00cfff;

    border-radius: 20px;

    background: #07172b;

    color: white;

    font-size: 28px;

    font-weight: bold;

    text-align: center;

    outline: none;
}


.number-input::placeholder {

    color: #4d7da5;
}


/* BUTTONS */

.bottom-buttons {

    margin-top: 45px;

    display: flex;

    justify-content: center;

    gap: 25px;
}


.bottom-button {

    width: 180px;

    height: 65px;

    display: flex;

    justify-content: center;

    align-items: center;

    border-radius: 18px;

    text-decoration: none;

    font-size: 21px;

    font-weight: bold;
}


.connect-button {

    background: #16c1df;

    color: #001018;
}


.back-button {

    background: #000000;

    color: white;

    border: 2px solid #333333;
}


@media (max-width: 600px) {

    .server-title {

        font-size: 29px;
    }

    .status-row {

        gap: 15px;

        flex-direction: column;
    }

    .period-box {

        width: 95%;
    }

    .period-number {

        font-size: 24px;

        letter-spacing: 4px;
    }

    .number-area {

        width: 95%;

        gap: 12px;
    }

    .number-input {

        height: 75px;

        font-size: 20px;
    }

    .bottom-button {

        width: 145px;

        height: 60px;

        font-size: 18px;
    }

}

</style>

</head>


<body>


<div class="page">


    <div class="server-title">
        SERVER CONNECTED
    </div>


    <!-- LIVE + REMAIN TIME -->

    <div class="status-row">

        <div class="live">

            LIVE

            <span class="live-dot">
                ●
            </span>

        </div>


        <div class="remaining">

            REMAIN TIME:

            <span
                class="remaining-time"
                id="remainingTime">
                01:00
            </span>

        </div>

    </div>


    <!-- PERIOD NUMBER -->

    <div class="period-box">

        <div class="period-title">
            PERIOD NUMBER
        </div>

        <div
            class="period-number"
            id="periodNumber">
            {{ period_number }}
        </div>

    </div>


    <!-- N1 / N2 -->

    <div class="number-area">

        <input
            class="number-input"
            type="number"
            placeholder="N1"
            inputmode="numeric"
            autocomplete="off"
        >


        <input
            class="number-input"
            type="number"
            placeholder="N2"
            inputmode="numeric"
            autocomplete="off"
        >

    </div>


    <!-- CONNECT / BACK -->

    <div class="bottom-buttons">

        <a
            href="/connected?time={{ selected_time }}"
            class="bottom-button connect-button">
            CONNECT
        </a>


        <a
            href="/"
            class="bottom-button back-button">
            BACK
        </a>

    </div>


</div>


<script>


/*
    Selected time:
    30 seconds OR 60 seconds
*/

const ROUND_SECONDS =
    {{ selected_time }};


/*
    Server time information.

    ഇതുകൊണ്ട് page refresh ആവശ്യമില്ല.
*/

let currentPeriod =
    "{{ period_number }}";


/*
    Period Number-ന്റെ അവസാന 5 digits
    എടുത്ത് +1 ചെയ്യുന്നു.
*/

function nextPeriodNumber(period) {

    const text =
        String(period);

    const prefix =
        text.slice(0, -5);

    const lastFive =
        parseInt(
            text.slice(-5),
            10
        );


    const nextNumber =
        lastFive + 1;


    const formatted =
        String(nextNumber)
        .padStart(5, "0");


    return prefix + formatted;
}


/*
    Countdown.
*/

function startCountdown() {

    let remaining =
        ROUND_SECONDS;


    function updateTime() {

        const minutes =
            Math.floor(
                remaining / 60
            );


        const seconds =
            remaining % 60;


        const display =
            String(minutes).padStart(2, "0")
            + ":"
            + String(seconds).padStart(2, "0");


        document.getElementById(
            "remainingTime"
        ).textContent = display;


        /*
            00:00 എത്തിയാൽ
            അടുത്ത Period.
        */

        if (remaining <= 0) {

            currentPeriod =
                nextPeriodNumber(
                    currentPeriod
                );


            document.getElementById(
                "periodNumber"
            ).textContent =
                currentPeriod;


            /*
                പുതിയ round വീണ്ടും തുടങ്ങുന്നു.
            */

            remaining =
                ROUND_SECONDS;

        } else {

            remaining--;

        }

    }


    updateTime();


    setInterval(
        updateTime,
        1000
    );

}


startCountdown();

</script>


</body>
</html>
"""


# =========================================================
# PERIOD NUMBER
# =========================================================

def get_period_number(seconds):

    now = datetime.now()

    date_part =
        now.strftime("%Y%m%d")


    midnight = now.replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0
    )


    elapsed_seconds = int(
        (now - midnight).total_seconds()
    )


    round_number =
        elapsed_seconds // seconds


    last_five =
        round_number % 100000


    last_five_text =
        str(last_five).zfill(5)


    return (
        date_part
        + "1000"
        + last_five_text
    )


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():

    return render_template_string(
        PAGE_1
    )


# =========================================================
# CONNECT
# =========================================================

@app.route(
    "/connect",
    methods=["POST"]
)
def connect():

    uid =
        request.form.get(
            "uid",
            ""
        ).strip()


    selected_time =
        request.form.get(
            "time",
            "60"
        )


    if uid == "5001":

        return redirect(
            url_for(
                "connected",
                time=selected_time
            )
        )


    return render_template_string(
        PAGE_1,
        error="Invalid UID. Please enter 5001."
    )


# =========================================================
# SECOND PAGE
# =========================================================

@app.route("/connected")
def connected():

    selected_time =
        request.args.get(
            "time",
            "60"
        )


    try:

        selected_time =
            int(selected_time)

    except ValueError:

        selected_time = 60


    if selected_time not in [30, 60]:

        selected_time = 60


    period_number =
        get_period_number(
            selected_time
        )


    return render_template_string(

        PAGE_2,

        period_number=period_number,

        selected_time=selected_time

    )


# =========================================================
# START SERVER
# =========================================================

if __name__ == "__main__":

    port =
        int(
            os.environ.get(
                "PORT",
                5000
            )
        )


    app.run(
        host="0.0.0.0",
        port=port
    )
