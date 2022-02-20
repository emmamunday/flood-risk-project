from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def test_rivers_by_station_number():
    stations = build_station_list()
    x = rivers_by_station_number(stations, 7)

    assert type(x) is list
    assert len(x) >= 7
    for i in range(len(x)):
        assert type(x[i]) is tuple
        assert x[i][1] >= 1

test_rivers_by_station_number()


