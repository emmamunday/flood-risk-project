from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list

def test_typical_range_consistent():
    stations = build_station_list()
    for i in stations:
        x = test_typical_range_consistent()
        assert type(x) is bool

test_typical_range_consistent()