from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation

def test_relative_water_level():
    stations = build_station_list()
    update_water_levels(stations)
    list = []
    for i in stations:
        x = i.relative_water_level()
        list.append(x)
        
    for i in range(len(list)):
        if type (list[i]) is float:
            pass
        elif list[i] is None:
            pass
        else: 
           raise AssertionError ("Output should be type float or NoneType") 

test_relative_water_level()

