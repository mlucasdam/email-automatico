import smtplib
import email.message


def enviar_email():
    corpo_email = """               
    <p>FORMULA MAGICA PARA FICAR MAIS SEXY: </p>
    <p>1 - DECA</p>
    <p>2 - WINSTRON</p>
    <p>3 - DURATESTON</p>
    <p>4 - TESTEX</p>
    <p>ATT</p>
    <p>BOT DE EMAIL DO MUNABIS</p>
    """


    msg = email.message.Message()
    msg['subject'] = "QUER SABER COMO FICAR MAIS SEXY?"
    msg['from'] = 'damiani.lucasm@gmail.com'
    msg['to'] = 'damiani.lucasm@gmail.com;rafael264rodrigues@gmail.com;raqueless@hotmail.com'
    password = '111275lk'
    msg.add_header('content-type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['from'], password)
    s.sendmail(msg['from'], [msg['to']], msg.as_string().encode('utf-8'))
    print('email enviado')

enviar_email()

