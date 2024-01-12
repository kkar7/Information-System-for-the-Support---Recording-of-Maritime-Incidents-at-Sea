from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def in_xenosoma_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def text_box_1_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    pass
