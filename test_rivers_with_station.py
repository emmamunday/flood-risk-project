from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list

def test_rivers_with_station():
    stations = build_station_list()
    x = rivers_with_station(stations)

    assert type(x) is set

test_rivers_with_station()