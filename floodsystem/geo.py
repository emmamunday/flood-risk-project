# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

import pip
from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
   """Builds and returns a set with the names of all the rivers with a monitoring station.
      Stations is a list of MonitoringStation objects."""

   rivers = set()
   for station in stations:
      if station.river != None:
         rivers.add(station.river)

   return rivers

def stations_by_river(stations):
   """Builds and reuturns a dictionary which maps river names (key) to a list of station objects on a given river. 
      Stations is a list of MonitoringStation objects.  """

   stations_by_river_dictionary = {}

   for station in stations:
      if station.river != None:
         stations_by_river_dictionary[station.river] = []
   for station in stations:
      if station.river != None:
         stations_by_river_dictionary[station.river].append(station.name)

   return  stations_by_river_dictionary


def rivers_by_station_number(stations, N):
   """Builds and returns a list of the N rivers with the greatest number of stations (as a tuple: river name, number of stations)
   In the case where there are multiple rivers with the same number of stations as the Nth station, these are also included.   
   """

   rivers = []
   for station in stations:
       rivers.append(station.river)
   counts = set()
   for river in rivers:
      counts.add((river, rivers.count(river), ))
   counts = sorted(counts, reverse = True, key=lambda x: x[1])
   top_n = counts[:N]
   for i in range(N,len(counts)):
      if top_n[N-1][1] == counts[i][1]:
            top_n.append(counts[i])

   return top_n

def stations_by_distance(stations, p):
   rivers =[]
   from haversine import haversine
   for station in stations:
      coords = station.coord
      distance = haversine(p,coords)
      rivers.append((station.name,distance))
   rivers = sorted_by_key(rivers,1)
   return rivers


#def stations_within_radius(stations, centre, r):