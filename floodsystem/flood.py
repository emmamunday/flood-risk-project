#from pyparsing import empty
from .utils import sorted_by_key
from .station import MonitoringStation



def stations_level_over_threshold(stations, tol):
    rivers = []
    
    
    for station in stations:
        if station.typical_range_consistent() ==True:
            if  station.relative_water_level()==None:
                pass

            elif  station.relative_water_level() > tol:
                
                
                rivers.append((station.name,station.relative_water_level()))
    rivers = sorted_by_key(rivers,1,True)
    return rivers  