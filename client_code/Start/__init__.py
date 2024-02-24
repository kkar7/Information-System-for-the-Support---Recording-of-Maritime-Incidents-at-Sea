from ._anvil_designer import StartTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Start(StartTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Start')
    pass

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Form1')
    pass

  def button_download_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    # Call the server function to get the Excel file
    excel_media = anvil.server.call('download_table_as_excel')
    # Trigger a download in the user's browser
    anvil.media.download(excel_media)
    pass
