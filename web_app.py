from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# PAGE 1
PAGE1 = """
<!DOCTYPE html>
<html>
<head>
    <title>SIKKIM PRO VIP</title>
    <style>
        body {
            margin: 0;
            background: #020817;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
        }

        .box {
            padding: 70px 20px;
        }

        h1 {
            font-size: 55px;
            letter-spacing: 8px;
        }

        input {
            width: 70%;
            max-width: 600px;
            padding: 25px;
            border-radius: 25px;
            border: 2px solid #284568;
            background: #071225;
            color: white;
            font-size: 25px;
            text-align: center;
        }

        button {
            margin-top: 25px;
            padding: 22px 60px;
            border: none;
            border-radius: 25px;
            background: #16c1df;
            color: #001018;
            font-size: 25px;
            font-weight: bold;
            cursor: pointer;
        }

        .error {
            color: #ff5555;
            margin-top: 20px;
        }
    </style>
</head>

<body>
    <div class="box">
        <h1>SIKKIM</h1>

        <form action="/connect" method="POST">
            <input
                type="text"
                name="uid"
                placeholder="ENTER SIKKIM UID"
                required
            >

            <br>

            <button type="submit">CONNECT</button>
        </form>

        {% if error %}
            <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
"""


# PAGE 2
PAGE2 = """
<!DOCTYPE html>
<html>
<head>
    <title>Server Connected</title>

    <style>
        body {
            margin: 0;
            background: #f5f5f5;
            color: #111;
            font-family: Arial, sans-serif;
            text-align: center;
        }

        .page {
            padding: 50px 20px;
        }

        h1 {
            font-size: 42px;
            margin-bottom: 10px;
        }

        .live {
            font-size: 24px;
            margin-bottom: 45px;
        }

        .dot {
            color: red;
            font-size: 30px;
        }

        .uid {
            width: 80%;
            max-width: 800px;
            height: 90px;
            margin: auto;
            background: white;
            border: 3px solid #222;
            border-radius: 10px;

            display: flex;
            align-items: center;
            justify-content: center;

            font-size: 40px;
            letter-spacing: 10px;
        }

        .buttons {
            margin-top: 35px;
            display: flex;
            justify-content: center;
            gap: 50px;
        }

        .number {
            width: 150px;
            height: 80px;
            background: white;
            border: 3px solid #222;
            border-radius: 8px;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
        }

        @media(max-width:600px) {
            h1 {
                font-size: 30px;
            }

            .uid {
                width: 90%;
                font-size: 28px;
            }

            .buttons {
                gap: 20px;
            }

            .number {
                width: 120px;
            }
        }
    </style>
</head>

<body>

<div class="page">

    <h1>SERVER CONNECTED</h1>

    <div class="live">
        LIVE <span class="dot">●</span>
    </div>

    <div class="uid">
        5001
    </div>

    <div class="buttons">
        <button class="number">N1</button>
        <button class="number">N2</button>
    </div>

</div>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE1)


@app.route("/connect", methods=["POST"])
def connect():
    uid = request.form.get("uid", "").strip()

    if uid == "5001":
        return redirect(url_for("connected"))

    return render_template_string(
        PAGE1,
        error="Invalid UID"
    )


@app.route("/connected")
def connected():
    return render_template_string(PAGE2)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
