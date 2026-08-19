from flask import Flask, request, redirect, url_for, render_template_string
import os

app = Flask(__name__)


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
                radial-gradient(circle at 50% 35%,
                #10264b 0%,
                #061126 38%,
                #020817 75%);
            color: white;
            font-family: Arial, Helvetica, sans-serif;
        }

        .main {
            width: 100%;
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
            box-shadow: 0 0 20px rgba(0, 217, 255, 0.25);
        }

        .timer {
            margin-top: 55px;
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
            border: 0;
            color: #91a6c9;
            background: transparent;
            font-size: 23px;
            font-weight: bold;
        }

        .timer .active {
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
            align-items: center;
            justify-content: center;
            gap: 45px;
        }

        .uid-input {
            width: 560px;
            height: 125px;
            border-radius: 38px;
            border: 3px solid #29466d;
            background: rgba(4, 13, 30, .75);
            color: white;
            padding: 0 40px;
            font-size: 27px;
            letter-spacing: 4px;
            outline: none;
        }

        .uid-input::placeholder {
            color: #35567f;
        }

        .connect-btn {
            width: 325px;
            height: 125px;
            border: 0;
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

        .note {
            margin-top: 45px;
            text-align: center;
            color: #6684ae;
            font-size: 18px;
        }

        @media (max-width: 800px) {
            .main {
                padding: 35px 18px;
            }

            .top {
                flex-direction: column;
                gap: 20px;
            }

            .logo {
                font-size: 42px;
            }

            .vip {
                font-size: 19px;
                padding: 15px 28px;
            }

            .timer {
                width: 100%;
                max-width: 360px;
            }

            .connect-area {
                flex-direction: column;
                gap: 25px;
            }

            .uid-input,
            .connect-btn {
                width: 100%;
                height: 105px;
            }

            .uid-input {
                font-size: 21px;
            }

            .connect-btn {
                font-size: 27px;
            }
        }
    </style>
</head>

<body>

<div class="main">

    <div class="top">
        <div class="logo">SIKKIM</div>
        <div class="vip">PRO VIP</div>
    </div>

    <div class="timer">
        <button type="button">30 SEC</button>
        <button type="button" class="active">1 MIN</button>
    </div>

    <div class="line"></div>

    <form action="/connect" method="POST">

        <div class="connect-area">

            <input
                class="uid-input"
                type="text"
                name="uid"
                placeholder="ENTER SIKKIM UID"
                maxlength="20"
                autocomplete="off"
                required
            >

            <button class="connect-btn" type="submit">
                CONNECT
            </button>

        </div>

    </form>

    {% if error %}
        <div class="error">{{ error }}</div>
    {% endif %}

    <div class="note">
        Demo interface • No guaranteed results
    </div>

</div>

</body>
</html>
"""


PAGE_2 = """
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
                radial-gradient(circle at 50% 35%,
                #102b55 0%,
                #071631 40%,
                #020817 80%);
            color: white;
            font-family: Arial, Helvetica, sans-serif;
        }

        .page {
            width: 100%;
            max-width: 1000px;
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
            color: #00eaff;
            font-size: 30px;
            animation: blink 1s infinite;
            text-shadow:
                0 0 8px #00eaff,
                0 0 18px #00eaff;
        }

        @keyframes blink {
            0%, 45% {
                opacity: 1;
            }

            50%, 100% {
                opacity: 0.15;
            }
        }

        .uid-box {
            width: 85%;
            max-width: 850px;
            height: 105px;
            margin: 45px auto 0;
            border: 3px solid #00bde8;
            border-radius: 20px;
            background: rgba(3, 13, 32, 0.8);

            display: flex;
            align-items: center;
            justify-content: center;

            font-size: 42px;
            font-weight: bold;
            letter-spacing: 12px;

            box-shadow: 0 0 20px rgba(0, 190, 235, 0.18);
        }

        .buttons {
            margin-top: 45px;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            gap: 55px;
        }

        .number-box {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .number-button {
            width: 165px;
            height: 85px;
            background: #071225;
            border: 2px solid #00c9ef;
            border-radius: 18px;
            color: #00d9ff;
            font-size: 28px;
            font-weight: 900;
            cursor: pointer;
        }

        .number-input {
            display: none;
            width: 165px;
            height: 60px;
            margin-top: 15px;
            border: 2px solid #00c9ef;
            border-radius: 14px;
            background: #020817;
            color: white;
            text-align: center;
            font-size: 25px;
            font-weight: bold;
            outline: none;
        }

        .back {
            display: inline-block;
            margin-top: 60px;
            padding: 16px 45px;
            border: 2px solid #00c9ef;
            border-radius: 18px;
            background: transparent;
            color: #00d9ff;
            text-decoration: none;
            font-size: 22px;
            font-weight: bold;
        }

        @media (max-width: 600px) {
            .page {
                padding: 40px 18px;
            }

            .server-title {
                font-size: 29px;
            }

            .uid-box {
                width: 95%;
                height: 85px;
                font-size: 30px;
                letter-spacing: 8px;
            }

            .buttons {
                gap: 20px;
            }

            .number-button {
                width: 130px;
                height: 70px;
                font-size: 23px;
            }

            .number-input {
                width: 130px;
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
        LIVE <span class="live-dot">●</span>
    </div>

    <div class="uid-box">
        5001
    </div>

    <div class="buttons">

        <div class="number-box">

            <button
                class="number-button"
                type="button"
                onclick="showInput('input1')">
                N1
            </button>

            <input
                id="input1"
                class="number-input"
                type="number"
                placeholder="Number"
            >

        </div>

        <div class="number-box">

            <button
                class="number-button"
                type="button"
                onclick="showInput('input2')">
                N2
            </button>

            <input
                id="input2"
                class="number-input"
                type="number"
                placeholder="Number"
            >

        </div>

    </div>

    <a href="/" class="back">
        BACK
    </a>

</div>

<script>
function showInput(id) {
    const input = document.getElementById(id);

    if (input.style.display === "block") {
        input.style.display = "none";
    } else {
        input.style.display = "block";
        input.focus();
    }
}
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE_1)


@app.route("/connect", methods=["POST"])
def connect():
    uid = request.form.get("uid", "").strip()

    if uid == "5001":
        return redirect(url_for("connected"))

    return render_template_string(
        PAGE_1,
        error="Invalid UID. Please enter 5001."
    )


@app.route("/connected")
def connected():
    return render_template_string(PAGE_2)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
