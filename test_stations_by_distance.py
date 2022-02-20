from typing import Tuple
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_stations_by_river():
    stations = build_station_list()
    p = 52.2053, 0.1218
    x = stations_by_distance(stations, p)

    assert type(x) is list
    
    for i in x:
        assert type(i) is tuple
        assert i[1] >= 0

test_stations_by_river()