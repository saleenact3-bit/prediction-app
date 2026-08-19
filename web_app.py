from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# =========================================================
# PAGE 1 - SIKKIM PRO VIP
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
                radial-gradient(circle at 50% 35%, #10264b 0%, #061126 38%, #020817 75%);
            color: white;
            font-family: Arial, Helvetica, sans-serif;
        }

        .main {
            width: 100%;
            max-width: 1000px;
            margin: auto;
            padding: 55px 30px;
        }

        /* TOP */
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

        /* TIMER */
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
            cursor: pointer;
        }

        .timer .active {
            background: #16c1df;
            color: #001018;
            box-shadow: 0 0 25px rgba(22,193,223,.35);
        }

        /* LINE */
        .line {
            margin-top: 60px;
            border-top: 2px dashed #08718a;
        }

        /* CONNECT AREA */
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

        .uid-input:focus {
            border-color: #00d9ff;
            box-shadow: 0 0 20px rgba(0,217,255,.18);
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
            box-shadow: 0 12px 30px rgba(0,193,223,.25);
        }

        .connect-btn:hover {
            background: #25d4f1;
        }

        .error {
            margin-top: 25px;
            text-align: center;
            color: #ff6868;
            font-size: 18px;
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


# =========================================================
# PAGE 2 - NOTEBOOK DESIGN
# =========================================================

PAGE_2 = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Server Connected</title>

    <style>

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background: #f4f4f4;
            color: #111;
            font-family: Arial, Helvetica, sans-serif;
        }

        .connected-page {
            width: 100%;
            max-width: 1050px;
            margin: auto;
            padding: 45px 25px;
            text-align: center;
        }

        .server-title {
            font-size: 40px;
            font-weight: 800;
            letter-spacing: 2px;
            margin-top: 10px;
        }

        .live {
            margin-top: 8px;
            font-size: 23px;
            font-weight: bold;
        }

        .live-dot {
            color: red;
            font-size: 28px;
        }

        .uid-box {
            width: 85%;
            max-width: 850px;
            height: 105px;
            margin: 40px auto 0;

            background: white;
            border: 3px solid #222;
            border-radius: 8px;

            display: flex;
            align-items: center;
            justify-content: center;

            font-size: 40px;
            font-weight: bold;
            letter-spacing: 12px;
        }

        .number-buttons {
            margin-top: 35px;

            display: flex;
            justify-content: center;
            align-items: center;
            gap: 55px;
        }

        .number-button {
            width: 155px;
            height: 85px;

            background: white;
            border: 3px solid #222;
            border-radius: 8px;

            font-size: 28px;
            font-weight: bold;

            cursor: pointer;
        }

        .number-button:active {
            transform: scale(.97);
        }

        .back {
            display: inline-block;
            margin-top: 45px;
            padding: 13px 25px;

            border: 2px solid #333;
            border-radius: 8px;

            color: #111;
            text-decoration: none;
            font-weight: bold;
        }

        @media (max-width: 600px) {

            .server-title {
                font-size: 28px;
            }

            .uid-box {
                width: 95%;
                height: 85px;
                font-size: 28px;
                letter-spacing: 7px;
            }

            .number-buttons {
                gap: 20px;
            }

            .number-button {
                width: 125px;
                height: 70px;
                font-size: 24px;
            }
        }

    </style>
</head>

<body>

<div class="connected-page">

    <div class="server-title">
        SERVER CONNECTED
    </div>

    <div class="live">
        LIVE <span class="live-dot">●</span>
    </div>

    <div class="uid-box">
        5001
    </div>

    <div class="number-buttons">

        <button class="number-button">
            N1
        </button>

        <button class="number-button">
            N2
        </button>

    </div>

    <a href="/" class="back">
        BACK
    </a>

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

    # Only 5001 opens Page 2
    if uid == "5001":
        return redirect(url_for("connected"))

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
    app.run(
        host="0.0.0.0",
        port=5000
    )
