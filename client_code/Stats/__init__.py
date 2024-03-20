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

   #Asynchronously call 'get_user_role' to get the current user's role
    user_role = anvil.server.call('get_current_user_role')
        
    # Hide the buttons if the user's role is 'guest'
    self.form_page_button.visible = (user_role != 'guest')

    
    #The code that is written here runs before the form opens
    #Calls the server function to get the number of unique ship signs
    unique_sign_count = anvil.server.call('get_unique_sign_count')
    #Displays the number in a label
    self.label_unique_signs.text = f"Πλοία που έχουν ζητήσει βοήθεια: {unique_sign_count}"
  
    #Calls the server function to get the names and count shio nationalities
    nationality_counts = anvil.server.call('get_nationality_counts')
    display_text = ""
    for nationality, count in nationality_counts:
      display_text += f"{nationality}: {count}\n"
        
    self.label_nationalities.text = display_text

    #Calls the server function to get the number and names of ship types
    ship_type_counts = anvil.server.call('get_ship_type_counts')
    display_text = ""
    for ship_type, count in ship_type_counts:
      display_text += f"{ship_type}: {count}\n"
       
      self.label_ship_types.text = display_text

    #Calls the server function to get the number of sailors (patients)
    unique_sailorid_count = anvil.server.call('get_unique_sailorid_count')
    self.label_unique_sailorid.text = f"Ασθενείς που έχουν ζητήσει βοήθεια: {unique_sailorid_count}"

    #Calls the server function to calculate statistical measures about age
    stats = anvil.server.call('get_age_statistics')
    self.label_mean_age.text = f"Μέση Ηλικία: {stats['mean_age']:.2f}"
    self.label_median_age.text = f"Διάμεσος: {stats['median_age']:.2f}"
    self.label_age_range.text = f"Εύρος Ηλικίας: {stats['age_range']}"
    self.label_min_age.text = f"Ελάχιστη Ηλικία: {stats['min_age']}"
    self.label_max_age.text = f"Μέγιστη Ηλικία: {stats['max_age']}"

    #Calls the server function to get sailor nationalities
    sailor_nationality_counts = anvil.server.call('get_sailor_nationality_counts')
    display_text = ""
    for sailor_nationality, count in sailor_nationality_counts:
      display_text += f"{sailor_nationality}: {count}\n"
      self.label_sailor_nationalities.text = display_text

    #Calls the server function to count sailor specialties
    speciality_counts = anvil.server.call('get_speciality_counts')
    display_text = ""
    for speciality, count in speciality_counts:
      display_text += f"{speciality}: {count}\n"
      self.label_specialties.text = display_text

  def start_page_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Start')
    pass

  def form_page_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Form1')
    pass

  def exit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
     # Log out the current user
    anvil.users.logout()
    
    #redirect to first page
    anvil.open_form('Cover_page')
    pass

