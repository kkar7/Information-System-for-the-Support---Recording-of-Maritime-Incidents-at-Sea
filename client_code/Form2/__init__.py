from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.js

class Form2(Form2Template):
    def __init__(self, **properties):
      self.init_components(**properties)
      # Καλέστε τη συνάρτηση για να φορτώσετε και να εμφανίσετε το διάγραμμα
      self.load_chart()

    def load_chart(self):
      # Πάρτε τα δεδομένα από τον server
      data = anvil.server.call('get_nationality_data')
     # Ενημερώστε το διάγραμμα με τα νέα δεδομένα
      anvil.js.call_js('updateChart', data)
