from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def test_stations_by_river():
    stations = build_station_list()
    x = stations_by_river(stations)
    assert type(x) is dict
    assert type(x["River Cam"]) is list

test_stations_by_river()