from flask import Blueprint, Response, render_template
from .calendar import get_calendar

views = Blueprint("views", __name__, url_prefix="/")

@views.route('/')
def index():
  return render_template("index.html")

@views.route('/calendar.ics')
def cal():
	cal = get_calendar()
	return Response(response=cal.to_ical(), mimetype="text/calendar")
