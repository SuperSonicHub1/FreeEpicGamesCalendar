from datetime import datetime, timedelta
from icalendar import Event, Calendar
from .scraper import get_free_games

ONE_WEEK = timedelta(weeks=1)

def custom_attributes_to_dict(custom_attributes: list) -> dict:
	return dict(
		map(
			lambda x: (x["key"], x["value"]),
			custom_attributes
		)
	)

def create_event(game: dict):
	event = Event()
	
	custom_attributes = custom_attributes_to_dict(game["customAttributes"])
	if "com.epicgames.app.productSlug" in custom_attributes:
		url_slug = custom_attributes["com.epicgames.app.productSlug"]
	else:
		url_slug = game['urlSlug']
	
	uid = url_slug

	promotions = game["promotions"]
	offers = promotions["upcomingPromotionalOffers"] or promotions["promotionalOffers"]
	offer = offers[0]["promotionalOffers"][0]
	start_at = datetime.fromisoformat(offer["startDate"][:-1])
	end_at = datetime.fromisoformat(offer["endDate"][:-1])

	event.add('dtstart', start_at)
	event.add('dtend', end_at)
	event.add(
		'location',
		f"https://www.epicgames.com/store/en-US/p/{url_slug}"
	)
	event.add('summary', game["title"])
	event.add('description', game["description"])
	event.add('uid', uid)

	return event

def get_calendar():
	games = get_free_games()

	cal = Calendar()
	cal.add('prodid', '-//KAWCCO (@supersonichub1)/EN')
	cal.add('version', '2.0')
	cal.add('name', f"Free Epic Games")
	cal.add("method", "PUBLISH")

	events = map(create_event, filter(lambda x: x["promotions"], games))
	for event in events:
		cal.add_component(event)

	return cal
