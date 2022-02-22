from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    rivers = []
    
    
    for station in stations:
        if station.typical_range_consistent() ==True:
            if  station.relative_water_level()==None:
                pass

            elif  station.relative_water_level() > tol:
                rivers.append((station,station.town,station.relative_water_level()))

    rivers = sorted_by_key(rivers,2,True)
    return rivers  

def stations_highest_rel_level(stations, N):
    rivers = []
    for station in stations:
        if station.typical_range_consistent() ==True:
            if  station.relative_water_level()==None:
                pass
            else:
                rivers.append((station,station.relative_water_level()))
    rivers = sorted_by_key(rivers,1,True)[:N]
    return rivers