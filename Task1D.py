from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """ Requirments for task 1D"""
    stations = build_station_list
    n = rivers_with_station(stations)
    print(f"Number of rivers with at least one station: {len(n)}")

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()