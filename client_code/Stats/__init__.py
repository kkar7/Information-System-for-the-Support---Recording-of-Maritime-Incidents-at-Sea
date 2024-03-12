from ._anvil_designer import StatsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Stats(StatsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # Καλεί την server function για να πάρει τον αριθμό των μοναδικών σημάτων
    unique_sign_count = anvil.server.call('get_unique_sign_count')
    # Εμφανίζει τον αριθμό σε ένα label
    self.label_unique_signs.text = f"Πλοία που έχουν ζητήσει βοήθεια: {unique_sign_count}"
    # Αυτή η συνάρτηση μπορεί να καλεστεί όταν φορτώνει η φόρμα ή όταν πατηθεί ένα κουμπί
    #def refresh_unique_sign_count():

    unique_sailorid_count = anvil.server.call('get_unique_sailorid_count')

    self.label_unique_sailorid.text = f"Ασθενείς που έχουν ζητήσει βοήθεια: {unique_sailorid_count}"



    #nationality
    # Call the server function to get the data
    nationality_counts = anvil.server.call('get_nationality_counts')

    # Convert the data into a list of dictionaries for display in the DataGrid
    items_to_display = [{'Nationallity': nat, 'Count': count} for nat, count in nationality_counts.items()]
    print(items_to_display)  # Debug print
    # Set the items for the DataGrid
    self.data_grid_nationalities.items = items_to_display

    self.label_2.items = items_to_display

    #########################

    import anvil.server

    def display_nationalities():
      nationality_counts = anvil.server.call('get_nationality_counts')
      display_text = ""
      for nationality, count in nationality_counts:
        display_text += f"{nationality}: {count}\n"
    
     # Assuming you have a Label named 'label_nationalities'
      self.label_nationalities.text = display_text







    
    #self.load_age_statistics()

    #def load_age_statistics(self):
    stats = anvil.server.call('get_age_statistics')
    self.label_mean_age.text = f"Μέση Ηλικία: {stats['mean_age']:.2f}"
    self.label_median_age.text = f"Διάμεσος: {stats['median_age']:.2f}"
    self.label_age_range.text = f"Εύρος Ηλικίας: {stats['age_range']}"
    self.label_min_age.text = f"Ελάχιστη Ηλικία: {stats['min_age']}"
    self.label_max_age.text = f"Μέγιστη Ηλικία: {stats['max_age']}"

    
 
  


