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

   rivers = {}
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
         stations_by_river_dictionary[station.river] = (station.name)

   return  stations_by_river_dictionary