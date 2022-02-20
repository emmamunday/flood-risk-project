from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def test_inconsistent_typical_range_stations():
    stations = build_station_list()
    x = MonitoringStation.inconsistent_typical_range_stations(stations)

    assert type(x) is list

test_inconsistent_typical_range_stations()