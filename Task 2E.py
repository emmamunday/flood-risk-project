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
    highest_stations = stations_highest_rel_level(stations, n_stations)

    for station in highest_stations:
         dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=n_days))
         plot_water_levels(station,dates,levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
