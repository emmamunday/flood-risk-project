from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()
    rivers_sorted = MonitoringStation.inconsistent_typical_range_stations(stations)
    print(f"number of stations with inconsistent data: {len(rivers_sorted)}")
    print(f"stations with inconsistent data: {rivers_sorted}")



if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()

    