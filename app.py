from agents.fire_tool_agent import create_fire_agent

def main():
    agent = create_fire_agent()
    print("🔥 Welcome to FireBot (AutoGen + Azure OpenAI + NASA FIRMS)")

    while True:
        message_with_code_block = """This is a message with code block to get fire data.
The code block is below:
```python
import requests
import csv
from io import StringIO
from config import FIRMS_MAP_KEY
from utils.geo_utils import get_state_from_coords
import matplotlib.pyplot as plt
import os

# ✅ Fetch fire data from NASA FIRMS API (by country & days)
def fetch_fire_data(days: int = 3, country_code: str = "IND", dataset: str = "MODIS_NRT") -> list:
    url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{FIRMS_MAP_KEY}/{dataset}/{country_code}/{days}"
    response = requests.get(url)

    if not response.ok:
        raise Exception("🔥 FIRMS API call failed.")

    f = StringIO(response.text)
    reader = csv.DictReader(f)

    return [{k.lower(): v for k, v in row.items()} for row in reader]

# ✅ Summarize fires by state (used by AutoGen agent)
def summarize_fire_data(days: int = 3) -> str:
    fires = fetch_fire_data(days)
    state_map = {}

    for fire in fires:
        try:
            lat = float(fire["latitude"])
            lon = float(fire["longitude"])
            state = get_state_from_coords(lat, lon)
            state_map.setdefault(state, []).append((lat, lon))
        except Exception as e:
            print(f"⚠️ Error processing row: {e}")

    save_fire_map(state_map)

    summary_lines = [f"Fire Report (Last {days} Days) "]
    for state, points in sorted(state_map.items(), key=lambda x: -len(x[1])):
        summary_lines.append(f"{state}: {len(points)} fires")

    summary_lines.append("Fire location map saved to: output/india_fire_map.png")
    return "\n".join(summary_lines)
def save_fire_map(state_map: dict):
    lats, lons = [], []
    for points in state_map.values():
        for lat, lon in points:
            lats.append(lat)
            lons.append(lon)

    if not os.path.exists("output"):
        os.makedirs("output")

    plt.figure(figsize=(10, 8))
    plt.scatter(lons, lats, alpha=0.6)
    plt.title("🔥 NASA FIRMS Fire Detections in India")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/india_fire_map.png")
```
This is the end of the message.
"""
        result = agent.generate_reply(messages=[{"role": "user", "content": message_with_code_block}])
        print(result)

if __name__ == "__main__":
    main()
