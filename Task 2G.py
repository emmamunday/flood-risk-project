import datetime
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
import matplotlib.dates


def run():
    
    def polyfit(dates,levels,p):
    

        d0 = 1
        dates_as_floats = matplotlib.dates.date2num(dates)
        coefficients = np.polyfit(dates_as_floats - dates_as_floats[d0 -1], levels, p)
        poly = np.poly1d(coefficients)

        return(poly, d0)


    stations = build_station_list()
    update_water_levels(stations)
    

    stations_list_severe = stations_level_over_threshold(stations, 3)
    town_severe=[]        
    for station in stations_list_severe:
        
        n_days = 2
        dates,levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=n_days))
        dates_as_floats = matplotlib.dates.date2num(dates)    
        if bool(dates)==True:
            poly,d0 = polyfit( dates, levels, 4)
            if poly.deriv()(poly(dates_as_floats - dates_as_floats[d0 - 1])[-1:]) >0:
                pass
            if poly.deriv()(poly(dates_as_floats - dates_as_floats[d0 - 1])[-1:]) <0:
                if station[1] !=None:
                    town_severe.append(station[1])

        else:
            pass
                        
    stations_list_high = stations_level_over_threshold(stations, 2)
    town_high=[]        
    for station in stations_list_high:
        
        n_days = 2
        dates,levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=n_days))
        dates_as_floats = matplotlib.dates.date2num(dates)    
        if bool(dates)==True:
            poly,d0 = polyfit( dates, levels, 4)
            if poly.deriv()(poly(dates_as_floats - dates_as_floats[d0 - 1])[-1:]) >0:
                pass
            if poly.deriv()(poly(dates_as_floats - dates_as_floats[d0 - 1])[-1:]) <0:
                if station[1] !=None and station[1] not in  town_severe:
                    town_high.append(station[1])
        else:
            pass

    stations_list_moderate = stations_level_over_threshold(stations, 1.7)
    town_moderate=[]        
    for station in stations_list_moderate:
        
        n_days = 2
        dates,levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=n_days))
        dates_as_floats = matplotlib.dates.date2num(dates)    
        if bool(dates)==True:
            poly,d0 = polyfit( dates, levels, 4)
            if poly.deriv()(poly(dates_as_floats - dates_as_floats[d0 - 1])[-1:]) >0:
                pass
            if poly.deriv()(poly(dates_as_floats - dates_as_floats[d0 - 1])[-1:]) <0:
                if station[1] !=None and station[1] not in  town_severe and station[1] not in  town_high:
                    town_moderate.append(station[1])
        else:
            pass
    stations_list_low = stations_level_over_threshold(stations, 1.5)
    town_low=[]        
    for station in stations_list_low:
        
        n_days = 2
        dates,levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=n_days))
        dates_as_floats = matplotlib.dates.date2num(dates)    
        if bool(dates)==True:
            poly,d0 = polyfit( dates, levels, 4)
            if poly.deriv()(poly(dates_as_floats - dates_as_floats[d0 - 1])[-1:]) >0:
                pass
            if poly.deriv()(poly(dates_as_floats - dates_as_floats[d0 - 1])[-1:]) <0:
                if station[1] !=None and station[1] not in  town_severe and station[1] not in  town_high and station[1] not in  town_moderate:
                    town_low.append(station[1])
        else:
            pass        
    
   
    print ("towns with severe risk of flooding",town_severe)
    
    print ("towns with high risk of flooding",town_high)
    print ("towns with moderate risk of flooding",town_moderate)
    print ("towns with low risk of flooding",town_low)



if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
