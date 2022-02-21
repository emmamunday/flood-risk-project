import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    n_days = 10
    n_stations = 5
    N = n_stations + 50 # redundancy in cases of no data
    
    stations_list = stations_highest_rel_level(stations, N)
    highest_stations = []
    i = 0
    for station in stations_list:
        date, level = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=n_days))
        if bool(date)==True:
            if i < n_stations:
                highest_stations.append(station)
                i += 1
            else:
                break
        else:
            pass

    for station in highest_stations:
        dates,levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=n_days))
        plot_water_levels(station,dates,levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
