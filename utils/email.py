
def sendEmail(subject, message, email):
    import smtplib
    from email.message import EmailMessage

    EMAIL = "your@email.com"
    PASSWORD = "yourpassword"

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = EMAIL

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    status = 0
    try:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()
        status = 200
    except:
        status = 400
    finally:
        return status