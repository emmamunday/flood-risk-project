import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit

def run():
    stations = build_station_list()
    update_water_levels(stations)
    # add list of highest stations
    n_days = 2
    for station in ##list
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=n_days))
    plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
