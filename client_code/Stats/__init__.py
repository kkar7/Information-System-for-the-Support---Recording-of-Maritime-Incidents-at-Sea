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
  
    
    nationallity_counts = anvil.server.call('get_nationallity_counts')
    display_text = ""
    for nationallity, count in nationallity_counts:
      display_text += f"{nationallity}: {count}\n"
        
    # Assuming you have a Label named 'label_nationallities' on your form
    self.label_nationallities.text = display_text


    ship_type_counts = anvil.server.call('get_ship_type_counts')
    display_text = ""
    for ship_type, count in ship_type_counts:
      display_text += f"{ship_type}: {count}\n"
        
      # Assuming you have a Label named 'label_ship_types' on your form
      self.label_ship_types.text = display_text

    
    unique_sailorid_count = anvil.server.call('get_unique_sailorid_count')

    self.label_unique_sailorid.text = f"Ασθενείς που έχουν ζητήσει βοήθεια: {unique_sailorid_count}"


    
    stats = anvil.server.call('get_age_statistics')
    self.label_mean_age.text = f"Μέση Ηλικία: {stats['mean_age']:.2f}"
    self.label_median_age.text = f"Διάμεσος: {stats['median_age']:.2f}"
    self.label_age_range.text = f"Εύρος Ηλικίας: {stats['age_range']}"
    self.label_min_age.text = f"Ελάχιστη Ηλικία: {stats['min_age']}"
    self.label_max_age.text = f"Μέγιστη Ηλικία: {stats['max_age']}"

    sailor_nationality_counts = anvil.server.call('get_sailor_nationality_counts')
    display_text = ""
    for sailor_nationality, count in sailor_nationality_counts:
      display_text += f"{sailor_nationality}: {count}\n"
        
      # Assuming you have a Label named 'label_sailor_nationalities' on your form
      self.label_sailor_nationalities.text = display_text

    
    speciality_counts = anvil.server.call('get_speciality_counts')
    display_text = ""
    for speciality, count in speciality_counts:
      display_text += f"{speciality}: {count}\n"
        
      # Assuming you have a Label named 'label_specialties' on your form
      self.label_specialties.text = display_text
    
 
  


