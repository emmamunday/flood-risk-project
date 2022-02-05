# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
   """Builds and returns a set with the names of all the rivers with a monitoring station.
      Stations is a list of MonitoringStation objects."""

   rivers =set()
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
   """Builds and returns ..................
   ............................
   
   """
   rivers = []
   for station in stations:
       rivers.append(station.river)
   counts = set()
   for river in rivers:
      counts.add((rivers.count(river), river))
   counts = sorted(counts, reverse = True)
   top_n = counts[:N]
   for i in range(N,len(counts)):
      if top_n[N-1][0] == counts[i][0]:
            top_n.append(counts[i])

   return top_n