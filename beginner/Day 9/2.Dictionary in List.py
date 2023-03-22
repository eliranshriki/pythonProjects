travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country,visits,cities):
    new_country=country
    new_visits=visits
    new_cities=cities
    add_country={}
    add_country["country"]=new_country
    add_country["visits"]=new_visits
    add_country["cities"]=new_cities
    travel_log.append(add_country)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)