from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()
    rivers_sorted = stations_within_radius(stations,(52.2053, 0.1218),10)
    print(f"stations within 10km radius: {rivers_sorted}")



if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
 