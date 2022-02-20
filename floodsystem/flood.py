from .utils import sorted_by_key
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import  update_water_levels

def stations_level_over_threshold(stations, tol):
    rivers = []
    #stations= build_station_list()
    for station in stations:

        if  station.relative_water_level() > tol:
            rivers.append((station.name,station.relative_water_level()))
    rivers = sorted_by_key(rivers,1)  