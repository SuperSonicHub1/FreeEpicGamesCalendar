from requests import Session
from typing import Dict, Any, List

JSONObject = Dict[str, Any]

session = Session()

def get_free_games() -> List[JSONObject]:
	res = session.get("https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=US&allowCountries=US")
	body = res.json()
	return body["data"]["Catalog"]["searchStore"]["elements"]
