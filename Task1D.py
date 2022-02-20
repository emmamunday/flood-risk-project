from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river
from test_rivers_with_station import test_rivers_with_station

def run():
    """ Requirments for task 1D"""
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    print(f"Number of rivers with at least one station: {len(rivers)}")
    rivers_sorted = sorted(rivers)
    print(f"First 10 rivers: {rivers_sorted[:10]}")

    stations_by_river_dict = stations_by_river(stations)
    print(f"Stations on River Aire: {sorted(stations_by_river_dict['River Aire'])}")
    print(f"Stations on River Cam: {sorted(stations_by_river_dict['River Cam'])}")
    print(f"Stations on River Thames: {sorted(stations_by_river_dict['River Thames'])}")


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()