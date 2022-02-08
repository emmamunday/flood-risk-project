from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()
    rivers_sorted = stations_by_distance(stations,(52.2053, 0.1218))
    print(f"closest 10 rivers: {rivers_sorted[:10]}")
    print(f"furthest 10 rivers: {rivers_sorted[-10:]}")


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()