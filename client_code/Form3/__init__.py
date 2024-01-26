from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def google_maps_1_bounds_changed(self, **event_args):
    """This method is called when the viewport bounds have changed."""
    pass

  
  def button_set_marker_click(self, **event_args):
    # Get user input for latitude and longitude
    latitude = float(self.text_box_latitude.text)
    longitude = float(self.text_box_longitude.text)
    # Call the set_marker function
    self.set_marker(latitude, longitude)
  
 # def set_marker(self, latitude, longitude):
    # Call the server function to set the marker position
  #  result = anvil.server.call('set_marker_position', latitude, longitude)

    # Update the marker position on the Google Maps component
   # self.google_maps_1.center = {"lat": result['latitude'], "lng": result['longitude']}
    #self.google_maps_1.add_marker(self.google_maps_1.center)
  
  def set_marker(self, latitude, longitude):
    # Update the center and markers properties on the Google Maps component
    self.google_maps_1.center = {"lat": latitude, "lng": longitude}
    self.google_maps_1.markers = [{"lat": latitude, "lng": longitude, "title": "Marker Title"}]




#marker = GoogleMap.Marker(
#  animation=GoogleMap.Animation.DROP,
 # position=GoogleMap.LatLng(52.2053, 0.1218)
#)
#map.map_1(marker)




