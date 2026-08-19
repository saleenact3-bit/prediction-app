# =========================================================
# PAGE 2 - BLUE CONNECTED INTERFACE
# =========================================================

PAGE_2 = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>SIKKIM PRO VIP - Connected</title>

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
                    #071631 40%,
                    #020817 80%
                );

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

        /* SERVER CONNECTED */

        .server-title {
            font-size: 42px;
            font-weight: 900;
            letter-spacing: 3px;
        }

        /* LIVE */

        .live {
            margin-top: 12px;
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
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

        /* UID */

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

            box-shadow:
                0 0 20px rgba(0, 190, 235, 0.18);
        }

        /* BUTTON AREA */

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

            box-shadow:
                0 0 15px rgba(0, 217, 255, 0.12);
        }

        .number-button:hover {
            background: #0b2342;
        }

        .number-button:active {
            transform: scale(0.96);
        }

        /* NUMBER INPUT */

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

        .number-input:focus {
            box-shadow:
                0 0 15px rgba(0, 217, 255, 0.3);
        }

        /* BACK */

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

            cursor: pointer;
        }

        .back:hover {
            background: #00c9ef;
            color: #001018;
        }

        /* MOBILE */

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

        <!-- N1 -->

        <div class="number-box">

            <button
                class="number-button"
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


        <!-- N2 -->

        <div class="number-box">

            <button
                class="number-button"
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


    <!-- BACK -->

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
