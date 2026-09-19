from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Demo Application</title>
        </head>
        <body>
            <h1>Hello from DevOps! 🚀</h1>
            <p>Version: 1.0</p>
            <p>Environment: Development</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)