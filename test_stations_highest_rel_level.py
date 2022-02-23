from distutils.command.build import build
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)

    list = stations_highest_rel_level(stations,50)
    assert (len(list) == 50) is True
    
    for i in list:
        assert type(i[0].name) is str
        assert type(i[1]) is float

    for i in range(len(list)-1):
        assert (list[i][1] >=  list[i+1][1]) is True


test_stations_highest_rel_level()