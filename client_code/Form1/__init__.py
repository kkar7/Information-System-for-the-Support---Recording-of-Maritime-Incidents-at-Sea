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
    self.check_boxes = [self.in_ponos, self.in_piretos, self.in_rigos, self.in_zali, self.in_emetos, self.in_diaria, self.in_travma, self.in_erithrotita, self.in_priximo, self.in_aimoragia, self.in_xenosoma, self.in_vixas, self.in_dispnia, self.in_adunamia, self.in_apolia]
    #στην πανω γραμμη πρεπει να αλλαξω τα ονοματα με αυτα π εχω εγω στα selfcheck boxes


    
    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()  #call login_form
    anvil.server.call('print_my_permissions')
    
  
  

  def submit_click(self, **event_args):
    "This method is called when the button is clicked"""
    #ship_data
    ship_name = self.pi_shipname.text
    sign = self.pi_diethnessima.text
    nationallity = self.pi_ethnikotita.text
    type = self.pi_type.text
    eta = self.pi_eta.text
    zone = self.pi_naftikizoni.text
    weather = self.pi_kairos.text
    #long = self.pi_logitude.text
    #lat = self.pi_latitude.text
    origine = self.pi_proeleusi.text
    destination = self.pi_destination.text
    cargo = self.pi_cargo.text
    pharm = self.pi_pharm.text

    #sailor (patient) data
    surname = self.as_eponimo.text
    name = self.as_onoma.text
    age = self.as_ilikia.text
    speciality = self.as_eidikotita.text
    sailor_nationality = self.as_ethnikotitanaft.text
    height = self.as_ipsos.text
    kg = self.as_varos.text
    s_id = self.as_am.text

    #symptomps
    #symptomps_intro
    symptomsfre = self.radio_button_1.get_group_value()
    hours = self.in_ores.text
    days = self.in_meres.text

    #piesi££££££££££££££££££££££££££
    pulses = self.in_sfixis.text
    chronicdis = self.in_xroniespathisis.text
    surg = self.in_proigoumenesxeirourgikesep.text
    
    #basic symphtoms (check boxes area)
    if self.in_ponos.checked:
      pain = True
    else:
      pain = False
    
    if self.in_piretos.checked:
      fever = True
    else:
      fever = False      
    
    if self.in_rigos.checked:
      frown = True
    else:
      frown = False  
    
    if self.in_zali.checked:
      dizziness = True
    else:
      dizziness = False  

    if self.in_emetos.checked:
      vomit = True
    else:
      vomit = False 

    if self.in_diaria.checked:
      diarrhea = True
    else:
      diarrhea = False

    if self.in_travma.checked:
      wound = True
    else:
      wound = False

    if self.in_erithrotita.checked:
      redness = True
    else:
      redness = False

    if self.in_priximo.checked:
      swelling = True
    else:
      swelling  = False   

    if self.in_aimoragia.checked:
      bleeding = True
    else:
      bleeding  = False

    if self.in_xenosoma.checked:
      foreign_body = True
    else:
      foreign_body  = False    

    if self.in_vixas.checked:
      cough = True
    else:
      cough  = False

    if self.in_dispnia.checked:
      breath_shortness = True
    else:
      breath_shortness  = False  

    if self.in_adunamia.checked:
      weakness = True
    else:
      weakness  = False  

    if self.in_apolia.checked:
      loss_of_senses = True
    else:
      loss_of_senses  = False  
    #end of check boxes 
    
    other_symptoms = self.in_allasimptomata.text
    
   # email = self.email_box.text
   # feedback = self.feedback_box.text
    anvil.server.call('add_form', ship_name, sign, nationallity, type, eta, zone, weather, origine,
  destination, cargo, pharm, surname, name, age, speciality, sailor_nationality,
  height, kg, s_id, symptomsfre, hours, days, pulses, chronicdis, surg, pain,   
  fever, frown, dizziness, vomit, diarrhea, wound, redness, swelling, bleeding, foreign_body,     
  cough, breath_shortness, weakness, loss_of_senses, other_symptoms)
    Notification("Η Φόρμα καταχωρήθηκε").show()
    #self.clear_inputs()
    pass
    
 # def clear_inputs(self):
    #self.name_box.text = ""
    #self.email_box.text = ""
    #self.feedback_box.text = ""

  def showbutton_click(self, **event_args):
    "This method is called when the button Show on Map is clicked"
    marker = GoogleMap.Marker(
    animation=GoogleMap.Animation.DROP,
    position=GoogleMap.LatLng(52.2053, 0.1218)
    )
    map.add_component(marker)
    pass

 


  
    
