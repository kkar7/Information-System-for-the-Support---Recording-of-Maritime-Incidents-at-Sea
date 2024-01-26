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

  def map_1_bounds_changed(self, **event_args):
    """This method is called when the viewport bounds have changed."""
    pass

 
    

marker = GoogleMap.Marker(
  animation=GoogleMap.Animation.DROP,
  position=GoogleMap.LatLng(52.2053, 0.1218)
)
map.map_1(marker)




