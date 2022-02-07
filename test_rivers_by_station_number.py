from tkinter import N
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def test_rivers_by_station_number(N):
    stations = build_station_list()
    x = rivers_by_station_number(stations, N)

    assert type(x) is list
    assert len(x) >= N

test_rivers_by_station_number(7)


