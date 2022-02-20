from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):

    typical_min = station.typical_range[0]
    typical_max = station.typical_range[1]
    
    plt.plot(dates, levels)
    plt.plot(dates, typical_min)
    plt.plot(dates, typical_max)
    plt.xlabel('date')
    plt.ylabel('water level /m ')
    plt.xticks(rotation=45);
    plt.title(station.name)
    
    plt.tight_layout()  
    plt.show()

def plot_water_level_with_fit(station,dates,levels,p):
   dates_as_floats = mpl.dates.date2num(dates)
   poly,d0 = polyfit(dates,levels,p)
   plt.plot(dates,poly(dates_as_floats - dates_as_floats[d0 - 1]))
   plot_water_levels(station,dates,levels,p)
    


