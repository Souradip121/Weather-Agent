from tools.fire_data import fetch_fire_data
from utils.geo_utils import get_state_from_coords
from utils.gemini_llm import ask_gemini
import matplotlib.pyplot as plt
import os
from config import FIRMS_MAP_KEY
from tools.fire_data import fetch_fire_data_by_country
class FireAssistant:
    def handle_query(self, query):
        print("🤖 Gemini is thinking...")
        response = ask_gemini(
            f"You are a fire monitoring assistant for India. Interpret this query: '{query}' "
            "and determine what kind of fire data the user wants to retrieve or summarize."
        )
        print("\n🧠 Gemini Reasoning:\n", response)

        # Always fetch last 3 days for now (can be extended later)
        fires = fetch_fire_data_by_country(map_key=FIRMS_MAP_KEY, country_code="IND", days=3)
        state_map = {}
        print("🔍 Sample fire data row:")
        print(fires)  # Right after the CSV is parsed
        for fire in fires:
            lat = float(fire['latitude'])
            lon = float(fire['longitude'])
            state = get_state_from_coords(lat, lon)
            state_map.setdefault(state, []).append((lat, lon))

        self._print_summary(state_map)
        self._print_table(state_map)
        self._generate_map(state_map)

    def _print_summary(self, state_map):
        print("\n🔥 Fire summary:")
        for state, points in state_map.items():
            print(f"✔️ {state}: {len(points)} fires")

    def _print_table(self, state_map):
        print("\n📋 Coordinates Table:")
        print(f"{'State':<20} {'Latitude':<10} {'Longitude':<10}")
        print("-" * 45)
        for state, points in state_map.items():
            for lat, lon in points[:5]:  # Show 5 per state
                print(f"{state:<20} {lat:<10.4f} {lon:<10.4f}")

    def _generate_map(self, state_map):
        print("\n🗺️ Generating fire map...")
        lats = []
        lons = []
        for points in state_map.values():
            for lat, lon in points:
                lats.append(lat)
                lons.append(lon)

        if not os.path.exists("output"):
            os.makedirs("output")

        plt.figure(figsize=(10, 8))
        plt.scatter(lons, lats, alpha=0.5)
        plt.title("🔥 Fires in India (Last 3 Days)")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.grid(True)
        plt.savefig("output/india_fire_map.png")
        print("✅ Map saved to: output/india_fire_map.png")
