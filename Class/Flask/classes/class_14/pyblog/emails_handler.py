import flask, flask_mail
from pyblog import mail

def send_mail(sender, receivers, subject, txt_content, html_content):

    msg = flask_mail.Message(
                sender      = sender,
                recipients  = receivers,
                subject     = subject,
                body        = txt_content,
                html        = html_content
    )

    mail.send(msg)
