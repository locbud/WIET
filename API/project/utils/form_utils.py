# -*- coding: utf-8 -*-
# Author: Rowan
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField


class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
