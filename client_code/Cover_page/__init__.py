from ._anvil_designer import Cover_pageTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Cover_page(Cover_pageTemplate):
  def __init__(self, **properties):
    #Set Form properties and Data Bindings.
    self.init_components(**properties)

  def log_in_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Start')
    pass


