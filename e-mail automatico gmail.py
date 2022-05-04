import smtplib
import email.message


def enviar_email():
    corpo_email = """                
    <p>PARAGRAFO</p> 
    """
# PARA CADA PARAGROFO NOVO COLOCAR <p> </p>

    msg = email.message.Message()
    msg['subject'] = "ASSUNTO"
    msg['from'] = 'REMETENTE' #SEU EMAIL AQUI
    msg['to'] = 'DESTINATARIO' #EMAIL DESTINO
    password = 'SENHA' #SENHA DO SEU EMAIL AQUI
    msg.add_header('content-type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['from'], password)
    s.sendmail(msg['from'], [msg['to']], msg.as_string().encode('utf-8'))
    print('email enviado')

enviar_email()

