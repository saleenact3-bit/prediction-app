from flask import Flask, request, redirect, url_for, render_template_string
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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

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
                    #061126 40%,
                    #020817 80%
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
            align-items: center;
            justify-content: center;
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

        /* TIMER */

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

            color: #91a6c9;
            background: transparent;

            font-size: 23px;
            font-weight: bold;

            cursor: pointer;

            transition: 0.2s;
        }

        .timer button:hover {
            background: #0b2443;
            color: white;
        }

        .timer button.active {
            background: #16c1df;
            color: #001018;
        }

        .line {
            margin-top: 60px;
            border-top: 2px dashed #08718a;
        }

        /* UID + CONNECT */

        .connect-area {
            margin-top: 58px;

            display: flex;
            align-items: center;
            justify-content: center;

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


    <!-- TIMER -->

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


    <!-- CONNECT FORM -->

    <form
        action="/connect"
        method="POST"
        onsubmit="return saveTime()">

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


function saveTime() {

    return true;

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

    <meta
        name="viewport"
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
                    #102b55 0%,
                    #071631 45%,
                    #020817 85%
                );

            color: white;

            font-family: Arial, sans-serif;
        }


        .page {

            width: 100%;

            max-width: 950px;

            min-height: 100vh;

            margin: auto;

            padding: 55px 25px;

            text-align: center;
        }


        .server-title {

            font-size: 42px;

            font-weight: 900;

            letter-spacing: 3px;
        }


        .live {

            margin-top: 12px;

            font-size: 24px;

            font-weight: bold;
        }


        .live-dot {

            color: red;

            font-size: 30px;

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


        .uid-box {

            width: 85%;

            max-width: 850px;

            height: 105px;

            margin: 45px auto;

            border: 3px solid #00cfff;

            border-radius: 20px;

            background: #061426;

            display: flex;

            align-items: center;

            justify-content: center;

            font-size: 42px;

            font-weight: bold;

            letter-spacing: 12px;
        }


        /* N1 + N2 */

        .number-area {

            width: 85%;

            max-width: 850px;

            margin: auto;

            display: flex;

            justify-content: center;

            align-items: center;

            gap: 25px;
        }


        .number-input {

            width: 50%;

            height: 90px;

            border: 3px solid #00cfff;

            border-radius: 20px;

            background: #07172b;

            color: white;

            padding: 0 20px;

            font-size: 28px;

            font-weight: bold;

            text-align: center;

            outline: none;
        }


        .number-input::placeholder {

            color: #4d7da5;

            opacity: 1;
        }


        .number-input:focus {

            border-color: #36e7ff;

            box-shadow:
                0 0 20px rgba(0, 220, 255, 0.35);
        }


        /* CONNECT + BACK */

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

            align-items: center;

            justify-content: center;

            border-radius: 18px;

            text-decoration: none;

            font-size: 21px;

            font-weight: bold;
        }


        .continue-button {

            background: #16c1df;

            color: #001018;
        }


        .back-button {

            background: #000000;

            color: white;

            border: 2px solid #333333;
        }


        .continue-button:hover {

            background: #31d9f1;
        }


        .back-button:hover {

            background: #151515;
        }


        @media (max-width: 600px) {

            .page {

                padding: 40px 18px;
            }

            .server-title {

                font-size: 29px;
            }

            .live {

                font-size: 21px;
            }

            .uid-box {

                width: 95%;

                height: 85px;

                font-size: 30px;

                letter-spacing: 8px;
            }

            .number-area {

                width: 95%;

                gap: 12px;
            }

            .number-input {

                width: 50%;

                height: 75px;

                font-size: 19px;
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


    <div class="live">

        LIVE

        <span class="live-dot">
            ●
        </span>

    </div>


    <div class="uid-box">
        5001
    </div>


    <!-- N1 AND N2 -->

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


    <!-- CONTINUE + BACK -->

    <div class="bottom-buttons">


        <a
            href="/connected"
            class="bottom-button continue-button">

            CONTINUE

        </a>


        <a
            href="/"
            class="bottom-button back-button">

            BACK

        </a>


    </div>


</div>


</body>
</html>
"""


# =========================================================
# ROUTES
# =========================================================

@app.route("/")
def home():

    return render_template_string(PAGE_1)


@app.route("/connect", methods=["POST"])
def connect():

    uid = request.form.get("uid", "").strip()

    selected_time = request.form.get("time", "60")

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


@app.route("/connected")
def connected():

    return render_template_string(PAGE_2)


# =========================================================
# START SERVER
# =========================================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )
