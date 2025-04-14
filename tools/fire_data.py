import requests
from datetime import datetime, timedelta, timezone
import csv
from io import StringIO

def fetch_fire_data(api_key, days=5):
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=days)

    # Bounding box for India (lon1, lat1, lon2, lat2)
    bbox = "68.7,6.5,97.25,35.7"

    url = (
        f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{api_key}"
        f"/VIIRS_SNPP_NRT/world/{bbox}/{start.strftime('%Y-%m-%d')}/{end.strftime('%Y-%m-%d')}"
    )

    res = requests.get(url)
    if not res.ok:
        raise Exception("NASA API call failed")

    content = res.text
    f = StringIO(content)
    reader = csv.DictReader(f)
    return list(reader)

def fetch_fire_data_by_country(map_key, country_code="IND", days=3, dataset="MODIS_NRT"):
    url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{map_key}/{dataset}/{country_code}/{days}"
    response = requests.get(url)
    
    if not response.ok:
        raise Exception("FIRMS API call failed")
    print(response.text)
    print(type(response))
    f = StringIO(response.text)
    reader = csv.DictReader(f)
    print(reader._fieldnames)  # Debugging line to check field names
    # Normalize field names
    return [{k.lower(): v for k, v in row.items()} for row in reader]