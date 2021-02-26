from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def button():
    return render_template('time.html')


@app.route("/getTime")
def index():
    return datetime.datetime.now().replace(microsecond=0).isoformat()


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
