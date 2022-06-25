from flask import Flask
import os
import sys

app = Flask(__name__)
app.config['TESTING'] = True

@app.route("/test")
def hello_world():
    return f"<p>Hey! I am running on process : {os.getpid()}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=int(sys.argv[-1]))