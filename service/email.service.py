
def sendEmail(EMAIL, SUBJECT, MESSAGE):
    from flask import Response
    from datetime import datetime as dt
    from email import sendEmail as send

    BODY = f'''
    [+] Data: {dt.now()}
    [+] Subject: {SUBJECT}
    [+] Email: {EMAIL}
    [+] Message: {MESSAGE}
    '''

    status = send(SUBJECT, BODY, EMAIL)
    
    if status == 200:
        return Response("E-mail enviado com sucesso", status)
    return Response("Não foi possível enviar o e-mail", status)
