#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storage


class State(BaseModel):
    """ State class """
    name = ""
#    if storage_type != 'db':
 #       @property
  #      def cities(self):
   #         """Get method to return list of cities"""
    #        cities_list = []
     #       for city in list(storage.all(City).values()):
      #          if city.state_id == self.id:
       #             cities_list.append(city)
        #    return cities_list
