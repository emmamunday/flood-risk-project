from distutils.command.build import build
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    list = stations_level_over_threshold(stations,1)
    
    for i in range(len(list)-1):
        assert (list[i][2] >=  list[i+1][2]) is True
    
    for i in list:
        assert type(i[0].name) is str
        assert type(i[2]) is float

test_stations_level_over_threshold()