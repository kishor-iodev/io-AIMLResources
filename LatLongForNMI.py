import requests
import urllib.parse
import pandas as pd

accountsDF = pd.read_csv("accounts.tsv", sep="\t")

lat = []
lon = []

for row in accountsDF.itertuples():
    address = row.site_address
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

    response = requests.get(url).json()
    print(response)
    if len(response) > 0:
        lat.append(response[0]["lat"])
        lon.append(response[0]["lon"])
    else:
        lat.append("NULL")
        lon.append("NULL")

print(lat)
accountsDF['lat'] = lat
accountsDF['lon'] = lon

accountsDF.to_csv( "accountsWithLatLon.csv", index=False, encoding='utf-8-sig')