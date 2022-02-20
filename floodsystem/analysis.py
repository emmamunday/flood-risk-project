def polyfit(dates,levels,p):
    import matplotlib as mpl
    import numpy as np

    d0 = 1
    dates_as_floats = mpl.dates.date2num(dates)
    coefficients = np.polyfit(dates_as_floats - dates_as_floats[d0 -1], levels, p)
    poly = np.poly1d(coefficients)

    return(poly, d0)



    