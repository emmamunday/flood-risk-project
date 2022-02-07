from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def test_stations_within_radius():
    stations = build_station_list()
    p = (52.2053, 0.1218)
    r = 10
    x = stations_within_radius(stations, p, r)

    assert type(x) is list
    for i in x:
        assert type(i) is str

test_stations_within_radius()