URL='https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=US&allowCountries=US'

curl $URL | jq '.data.Catalog.searchStore.elements[].promotions'
