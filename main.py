from flask import Flask, request, render_template
import time

app = Flask(__name__)


@app.route("/")
def button():
    return render_template('time.html')


@app.route("/getTime")
def index():
    return render_template("index.html")


@app.route("/getTime", methods=['GET'])
def getTime():
    print("browser time: ", request.args.get("time"))
    print("server time : ", time.strftime('%A %B, %d %Y %H:%M:%S'))
    return "Done"


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
