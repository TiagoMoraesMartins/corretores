from app import mail
from flask import current_app, render_template
from flask_mail import Message


class Helper:
    @staticmethod
    def enviar_email(cls, subject, to, template, **kwargs) -> None:
        msg = Message(
            subject=subject,
            sender=current_app.config["MAIL_SENDER"],
            recipients=[to],
        )

        msg.body = render_template(f"mails/{template}.txt", **kwargs)
        msg.html = render_template(f"mails/{template}.html", **kwargs)
        mail.send(msg)
