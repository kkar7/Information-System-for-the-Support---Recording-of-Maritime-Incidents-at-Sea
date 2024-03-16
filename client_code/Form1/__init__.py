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
    origine = self.ship_origin.text
    destination = self.ship_destination.text
    cargo = self.ship_cargo.text
    pharmacy = self.ship_pharmacy.text

    #sailor (patient) data
    surname = self.s_surname.text
    name = self.s_name.text
    age = self.s_age.text
    speciality = self.s_speciality.text
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
    
    anvil.server.call('add_form', form_datetime, ship_name, national_sign, ship_nationality, ship_type, eta, naval_zone, weather, longitude, 
    latitude, origine, destination, cargo, pharmacy, 
    surname, name, age, speciality, sailor_nationality, height, weight,
    sailor_id,
                       symptomsfre, hours, days, piesi, pulses, chronicdis, surg, 
                      
                      pain,   
    fever, frown, dizziness, vomit, diarrhea, wound, redness, swelling, bleeding, foreign_body,     
    cough, breath_shortness, weakness, loss_of_senses, other_symptoms,
                      
                      photo_pain)
    
    Notification("Η Φόρμα καταχωρήθηκε").show()
    
    #Print form 
    if anvil.js.window.confirm("Θέλετε να εκτυπώσετε τη φόρμα;"):
        anvil.js.window.print()
    #self.clear_inputs()
    pass
    
 # def clear_inputs(self):
    #self.name_box.text = ""
    #self.email_box.text = ""
    #self.feedback_box.text = ""

  def showbutton_click(self, **event_args):
    "This method is called when the button Show on Map is clicked"
    long = self.pi_longitude.text
    lat = self.pi_latitude.text
    
    # Δημιουργούμε το URL για τους Χάρτες Google
    google_maps_url = f"https://www.google.com/maps?q={lat},{long}"
    
    # Ανοίγουμε το URL σε νέο παράθυρο του browser
    anvil.js.window.open(google_maps_url)
    pass

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.open_form('Start')
    pass

  def button_download_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def print_hide(self, **event_args):
    "This method is called when the Button is removed from the screen""
    #if form is not saved
    pass

  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Log out the current user
    anvil.users.logout()
    
    #redirect to first page
    anvil.open_form('Cover_page')
    pass

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    #redirect to stats page
    anvil.open_form('Stats')
    pass

 


  
    
