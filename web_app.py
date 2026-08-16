from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>My Prediction App</title>
    </head>
    <body>
        <h1>?? My Prediction App</h1>
        <p>Welcome to my first web app!</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
