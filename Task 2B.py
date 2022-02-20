from floodsystem.stationdata import build_station_list
#from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold



def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    rivers_sorted = stations_level_over_threshold(stations,0.8)
    print(f"number of stations with inconsistent data: {len(rivers_sorted)}")
    print(f"stations with inconsistent data: {rivers_sorted}")



if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()