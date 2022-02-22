from floodsystem.stationdata import build_station_list,update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    
    high_stations = stations_level_over_threshold(stations,0.8)


    
    for station in high_stations:
        print(station[0].name,station[2])



if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()