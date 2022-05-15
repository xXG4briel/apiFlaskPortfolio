from flask import Flask, request
from email.service import sendEmail

app = Flask(__name__)

@app.route('/email', methods = ["POST"])
def setEmail():
    EMAIL = request.args.get('email')
    SUBJECT = request.args.get('subject')
    MESSAGE = request.args.get('message')
    return sendEmail(EMAIL, SUBJECT, MESSAGE)

if __name__ == '__main__':
    app.run()