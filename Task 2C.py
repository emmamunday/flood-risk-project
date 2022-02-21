from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    
    rivers_sorted = stations_highest_rel_level(stations, 10)
    for station in rivers_sorted:

        print(station[0].name,station[1])



if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()