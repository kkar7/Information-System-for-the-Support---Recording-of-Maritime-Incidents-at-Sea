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
      data = anvil.server.call('get_nationality_data')
      # Χρησιμοποιήστε την anvil.js.call_js για να περάσετε τα δεδομένα στην JavaScript συνάρτηση που θα δημιουργήσει το διάγραμμα
      anvil.js.call_js('drawNationalityChart', data)
