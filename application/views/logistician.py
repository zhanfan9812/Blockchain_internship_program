from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from application.models import User

logistician_page = Blueprint('logistician_page', __name__)

