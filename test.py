from flask import Flask, request
import requests
import re

# ~ logic of the program starts here

app = Flask(__name__)


@app.route("/")
def hello():

    return "##########      Welcome to ask Budget !!      ###############"

@app.route("/test", methods=['POST'])
def sms_reply():
    msg = request.json  # postman
    print(msg)
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
