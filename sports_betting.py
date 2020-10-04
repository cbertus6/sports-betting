import requests

headers = {
	'apikey': '4f25c790-b1ba-11ea-bdfa-4f3d9abfebb8',
}

params = (
	('sport', 'american-football'),
	('country', 'usa'),
	('league', 'american-football-usa-ncaa')
)

response = requests.get('https://app.oddsapi.io/api/v1/odds', headers=headers, params=params)

print(response.json())