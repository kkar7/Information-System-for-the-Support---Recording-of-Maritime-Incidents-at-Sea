from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
import datetime
import anvil.js

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.check_boxes = [self.check_pain, self.check_fever, self.check_frown, self.check_dizziness, self.check_vomit, self.check_diarrhea, self.check_wound, self.check_redness,
                        self.check_swelling, self.check_bleeding, self.check_foreign_body, self.check_cough, self.check_breath_shortness, self.check_weakness, self.check_loss_of_senses]

#Τhis code runs when the Submit (Καταχώρηση) button is clicked
  def submit_click(self, **event_args):
    "This method is called when the button is clicked"
   
    # Initializing list to store the names of empty fields
    empty_fields = []

    # Check each field in the form and add its name to the list if it's empty
    if not self.ship_name.text:
        empty_fields.append("Όνομα Πλοίου")
    if not self.ship_national_sign.text:
        empty_fields.append("Διεθνές Σήμα Πλοίου")
    if not self.ship_nationality.text:
        empty_fields.append("Εθνικότητα Πλοίου")

    if not self.s_surname.text:
        empty_fields.append("Επίθετο Ασθενή")
    if not self.s_name.text:
        empty_fields.append("Όνομα Ασθενή")
    if not self.s_age.text:
        empty_fields.append("Ηλικία Ασθενή")
    if not self.s_speciality.text:
       empty_fields.append("Ειδικότητα Πλοίου")
    if not self.s_speciality.text:
       empty_fields.append("Ειδικότητα Πλοίου")
    
    # If there are empty fields, display a warning message and prevent form submission
    if empty_fields:
        alert(f"Παρακαλώ συμπληρώστε τα εξής πεδία: {', '.join(empty_fields)}")
        return

    #If all required fields are filled, proceed with form submission
   
    #ship_data
    form_datetime = datetime.datetime.now()
    ship_name = self.ship_name.text
    national_sign = self.ship_national_sign.text
    ship_nationality = self.ship_nationality.text
    ship_type = self.ship_type.text
    eta = self.ship_eta.text
    naval_zone = self.naval_zone.text
    weather = self.ship_weather.text
    longitude = self.ship_longitude.text
    latitude = self.ship_latitude.text
    origin = self.ship_origin.text
    destination = self.ship_destination.text
    cargo = self.ship_cargo.text
    pharmacy = self.ship_pharmacy.text

    #sailor (patient) data
    surname = self.s_surname.text
    name = self.s_name.text
    age = self.s_age.text
    specialty = self.s_speciality.text
    sailor_nationality = self.s_nationality.text
    height = self.s_height.text
    weight = self.s_weight.text
    sailor_id = self.s_id.text

    #symptomps
    #symptomps intro
    symptoms_frequency = self.radio_button_1.get_group_value()
    hours = self.hours.text
    days = self.days.text
    blood_pressure = self.b_pressure.text
    pulses = self.pulses.text
    chronic_diseases = self.c_diseases.text
    previous_surgeries = self.prev_surgeries.text
    
    #basic symphtoms (check boxes area)
    if self.check_pain.checked:
      pain = True
    else:
      pain = False
    
    if self.check_fever.checked:
      fever = True
    else:
      fever = False      
    
    if self.check_frown.checked:
      frown = True
    else:
      frown = False  
    
    if self.check_dizziness.checked:
      dizziness = True
    else:
      dizziness = False  

    if self.check_vomit.checked:
      vomit = True
    else:
      vomit = False 

    if self.check_diarrhea.checked:
      diarrhea = True
    else:
      diarrhea = False

    if self.check_wound.checked:
      wound = True
    else:
      wound = False

    if self.check_redness.checked:
      redness = True
    else:
      redness = False

    if self.check_swelling.checked:
      swelling = True
    else:
      swelling  = False   

    if self.check_bleeding.checked:
      bleeding = True
    else:
      bleeding  = False

    if self.check_foreign_body.checked:
      foreign_body = True
    else:
      foreign_body  = False    

    if self.check_cough.checked:
      cough = True
    else:
      cough  = False

    if self.check_breath_shortness.checked:
      breath_shortness = True
    else:
      breath_shortness  = False  

    if self.check_weakness.checked:
      weakness = True
    else:
      weakness  = False  

    if self.check_loss_of_senses.checked:
      loss_of_senses = True
    else:
      loss_of_senses  = False  
    #end of check boxes 
    
    other_symptoms = self.other_symptoms.text

    #Photo grid
    pain_diagram_position = self.pain_box.text
    
    anvil.server.call('Incidents_table', form_datetime, ship_name, national_sign, ship_nationality, ship_type, eta, naval_zone, weather, longitude, 
    latitude, origin, destination, cargo, pharmacy, surname, name, age, specialty, sailor_nationality, height, weight,
    sailor_id, symptoms_frequency, hours, days, blood_pressure, pulses, chronic_diseases, previous_surgeries,                  
    pain, fever, frown, dizziness, vomit, diarrhea, wound, redness, swelling, bleeding, foreign_body, cough, breath_shortness, weakness,
    loss_of_senses, other_symptoms, pain_diagram_position)
    
    Notification("Η Φόρμα καταχωρήθηκε").show()
    
    #Print form 
    if anvil.js.window.confirm("Θέλετε να εκτυπώσετε τη φόρμα;"):
        anvil.js.window.print()
    pass
    
  def show_map_button_click(self, **event_args):
    "This method is called when the button Show on Map is clicked"
    long = self.ship_longitude.text
    lat = self.ship_latitude.text
    #Creates URL for Google Maps
    google_maps_url = f"https://www.google.com/maps?q={lat},{long}"
    
    #Opens the URL to new Window
    anvil.js.window.open(google_maps_url)
    pass

  def start_page_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Start')
    pass

  def stats_page_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Stats')
    pass
 
  def exit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Log out the current user
    anvil.users.logout()
    
    #Redirect to first page
    anvil.open_form('Cover_page')
    pass

  def new_form_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #Open new clean form
    anvil.open_form('Form1') 
     # Call JavaScript function to scroll to the top of the page
    anvil.js.window.scrollTo(0, 0)
    pass


  
