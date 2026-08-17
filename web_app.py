from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sikkim Pro VIP</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background:
                radial-gradient(circle at 50% 20%, #102344 0%, #050b1b 55%, #02050d 100%);
            color: white;
            font-family: Arial, sans-serif;
        }

        .container {
            max-width: 1100px;
            margin: auto;
            padding: 35px 30px;
        }

        .top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 25px;
            flex-wrap: wrap;
        }

        .logo {
            font-size: 58px;
            font-weight: 900;
            letter-spacing: 8px;
        }

        .vip {
            padding: 15px 30px;
            border: 2px solid #00d9ff;
            border-radius: 18px;
            color: #00d9ff;
            font-size: 22px;
            font-weight: bold;
            letter-spacing: 3px;
            box-shadow: 0 0 18px rgba(0,217,255,.35);
        }

        .period {
            display: flex;
            background: #050b19;
            border: 2px solid #1a2b4a;
            border-radius: 25px;
            overflow: hidden;
        }

        .period button {
            border: 0;
            padding: 20px 35px;
            background: transparent;
            color: #8397b8;
            font-size: 22px;
            font-weight: bold;
            cursor: pointer;
        }

        .period button.active {
            background: #09c5e8;
            color: #00101b;
            box-shadow: 0 0 25px rgba(0,210,255,.55);
        }

        .line {
            margin: 45px 0;
            border-top: 2px dashed #06445c;
        }

        .form-row {
            display: flex;
            gap: 35px;
            align-items: stretch;
        }

        .uid {
            flex: 1;
            padding: 30px;
            border-radius: 28px;
            border: 3px solid #203451;
            background: #070e20;
            color: white;
            font-size: 28px;
            outline: none;
            box-shadow: inset 0 0 30px rgba(0,0,0,.35);
        }

        .uid::placeholder {
            color: #29415f;
            letter-spacing: 4px;
        }

        .connect {
            width: 35%;
            border: 0;
            border-radius: 28px;
            background: #08bddd;
            color: #001018;
            font-size: 30px;
            font-weight: 900;
            letter-spacing: 5px;
            cursor: pointer;
            box-shadow: 0 10px 25px rgba(0,190,230,.35);
        }

        .connect:hover {
            background: #19d8f5;
        }

        .result {
            margin-top: 40px;
            padding: 35px;
            border-radius: 28px;
            border: 2px solid #123b58;
            background: rgba(5,13,30,.9);
            text-align: center;
            display: none;
        }

        .result h2 {
            color: #00d9ff;
            letter-spacing: 4px;
        }

        .result-number {
            font-size: 55px;
            font-weight: 900;
            margin: 20px;
        }

        .note {
            margin-top: 35px;
            color: #647b9b;
            text-align: center;
        }

        @media (max-width: 700px) {
            .container {
                padding: 25px 15px;
            }

            .logo {
                font-size: 38px;
            }

            .form-row {
                flex-direction: column;
            }

            .connect {
                width: 100%;
                min-height: 80px;
            }

            .period button {
                padding: 16px 20px;
                font-size: 17px;
            }
        }
    </style>
</head>

<body>

<div class="container">

    <div class="top">

        <div style="display:flex;align-items:center;gap:25px;">
            <div class="logo">SIKKIM</div>
            <div class="vip">PRO VIP</div>
        </div>

        <div class="period">
            <button id="sec30" onclick="setPeriod('30 SEC')">
                30 SEC
            </button>

            <button id="min1" class="active" onclick="setPeriod('1 MIN')">
                1 MIN
            </button>
        </div>

    </div>

    <div class="line"></div>

    <form class="form-row" onsubmit="showPrediction(event)">

        <input
            id="uid"
            class="uid"
            type="text"
            placeholder="ENTER SIKKIM UID"
            required
        >

        <button class="connect" type="submit">
            CONNECT
        </button>

    </form>

    <div class="result" id="result">

        <h2>PREDICTION RESULT</h2>

        <div class="result-number" id="resultText">
            DEMO
        </div>

        <p id="periodText">1 MIN MODE</p>

    </div>

    <div class="note">
        Demo prediction interface • No guaranteed results
    </div>

</div>

<script>

let selectedPeriod = "1 MIN";

function setPeriod(period) {

    selectedPeriod = period;

    document.getElementById("sec30").classList.remove("active");
    document.getElementById("min1").classList.remove("active");

    if (period === "30 SEC") {
        document.getElementById("sec30").classList.add("active");
    } else {
        document.getElementById("min1").classList.add("active");
    }
}

function showPrediction(event) {

    event.preventDefault();

    const uid = document.getElementById("uid").value.trim();

    if (!uid) {
        return;
    }

    document.getElementById("result").style.display = "block";

    document.getElementById("resultText").innerText = "DEMO";

    document.getElementById("periodText").innerText =
        selectedPeriod + " MODE";

}

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
