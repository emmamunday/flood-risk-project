from floodsystem.analysis import polyfit
import datetime
import matplotlib as mpl
import numpy as np

def test_polyfit():
    import datetime

    shift = 1
    power = 2
    x = [0, 1, 2, 3, 4]
    y = [1, 4, 9, 16, 25]
    num = mpl.dates.date2num(x)
    coeff = np.polyfit(num - num[shift - 1], y, power)
    poly1 = np.poly1d(coeff)

    poly2, output_shift = polyfit(x, y, power)

    assert poly1 == poly2

test_polyfit()
