from flask_wtf import CSRFProtect, FlaskForm
from wtforms.fields import BooleanField, PasswordField, SubmitField

from wtforms.validators import DataRequired

csrf = CSRFProtect()


class LoginForm(FlaskForm):
    #email = EmailField("Email", required=True)
    #password = PasswordField("Password", required=True)
    #remember_me = BooleanField("Permanecer conectado")
    #submit = SubmitField("Logar")
    pass
