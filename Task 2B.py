from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    
    rivers_sorted = stations_level_over_threshold(stations,0.8)
    for station in rivers_sorted:

        print(station[0],station[1])



if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()