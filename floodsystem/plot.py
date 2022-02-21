from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):

    typical_min = station[0].typical_range[0]
    typical_max = station[0].typical_range[1]
    typical_min_list = np.full(len(dates), typical_min)
    typical_max_list = np.full(len(dates), typical_max)
    
    plt.plot(dates, levels, label= f"{station} level")
    plt.plot(dates, typical_min_list, label = "typical min")
    plt.plot(dates, typical_max_list, label = "typical max")
    plt.xlabel('date')
    plt.ylabel('water level /m ')
    plt.xticks(rotation=45);
    plt.title(station[0].name)
    
    plt.tight_layout()  
    plt.show()

def plot_water_level_with_fit(station,dates,levels,p):
   dates_as_floats = mpl.dates.date2num(dates)
   poly,d0 = polyfit(dates,levels,p)
   
   typical_min = station[0].typical_range[0]
   typical_max = station[0].typical_range[1]
   typical_min_list = np.full(len(dates), typical_min)
   typical_max_list = np.full(len(dates), typical_max)
    
   plt.plot(dates,poly(dates_as_floats - dates_as_floats[d0 - 1]), label= f"{station} level")
   
   plt.plot(dates, typical_min_list, label = "typical min")
   plt.plot(dates, typical_max_list, label = "typical max")
   plt.xlabel('date')
   plt.ylabel('water level /m ')
   plt.xticks(rotation=45);
   plt.title(station[0].name)
   
   plt.tight_layout() 
   plt.show()
    


