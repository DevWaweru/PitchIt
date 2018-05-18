from flask import render_template, redirect, url_for, flash, request
from ..models import User
from . import auth
from flask_login import login_user, login_required, logout_user
from .. import db
