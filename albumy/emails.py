from flask import current_app, render_template
from albumy.extensions import mail
from flask_mail import Message

from threading import Thread


def _send_async_email(app, message):
    with app.app_context():
        mail.send(message)


def send_email(to, subject, template, **kwargs):
    message = Message(current_app.config['ALBUMY_MAIL_SUBJECT_PREFIX'] + subject, recipients=[to])
    message.body = render_template(template + '.txt', **kwargs)
    message.html = render_template(template + '.html', **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=_send_async_email, args=(app, message))
    thr.start()
    return thr


def send_confirm_email(user, token, to=None):
    send_email(to=to or user.email, subject='Email Confirm', template='emails/confirm', user=user, token=token)


def send_reset_password_email(user, token):
    send_email(to=user.email, subject='Password Reset', template='emails/reset_password', user=user, token=token)


def send_change_email_email(user, token, to=None):
    send_email(to=to or user.email, subject='Email Confirm', template='emails/change_email', user=user, token=token)
