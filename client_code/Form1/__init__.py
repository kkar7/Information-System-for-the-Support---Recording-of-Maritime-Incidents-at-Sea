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
    self.check_boxes = [self.check_box_1, self.check_box_2, self.check_box_3, self.check_box_4]
    #στην πανω γραμμη πρεπει να αλλαξω τα ονοματα με αυτα π εχω εγω στα selfcheck boxes


    
    # Any code you write here will run before the form opens.
    anvil.users.login_with_form()  #call login_form
    anvil.server.call('print_my_permissions')
    
  
  def pi_shipname_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def pi_diethnessima_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def pi_ethnikotita_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def pi_type_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def pi_eta_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def pi_naftikizoni_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def pi_kairos_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def pi_longitude_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def pi_latitude_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def pi_proeleusi_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def pi_destination_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def pi_cargo_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def pi_pharm_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def as_eponimo_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def as_onoma_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def as_ilikia_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def as_eidikotita_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def as_ethnikotitanaft_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def as_ipsos_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def as_varos_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def as_am_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass


  def in_piretos_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_rigos_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_zali_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_emetos_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_diaria_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_travma_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_erithrotita_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_priximo_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
  pass
  
  def in_aimoragia_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_xenosoma_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_vixas_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_dispnia_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_adunamia_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_apolia_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_xafnikiemfanisisiptomaton_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_stadiakiemfsimpt_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def in_ores_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def in_meres_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def outlined_15_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def in_sfixis_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def in_xroniespathisis_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def in_proigoumenesxeirourgikesep_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def in_allasimptomata_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass

  def submit_click(self, **event_args):
    "This method is called when the button is clicked"""
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

    surname = self.as_eponimo.text
    name = self.as_onoma.text
    age = self.as_ilikia.text
    specialty = self.as_eidikotita.text
    pnationallity = self.ethnikotitanaft.text
    hight = self.as_ipsos.text
    kg = self.as_varos.text
    am = self.as_am.text

    #symptomps_intro
    symptomsfre = self.radio_button_1.get_group_value()
    hours = self.in_ores.text
    days = self.in_meres.text

    #piesi
    pulses = self.in_sfixis.text
    chronicdis = self.in_xroniespathisis.text
    surg = self.in_proigoumenesxeirourgikesep.text
    
    #basic symphtoms
      def in_ponos_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass
    #ponos = self.in_ponos
    basic_sympt =  [box.text for box in self.check_boxes if box.checked == True]
    
    
   # email = self.email_box.text
   # feedback = self.feedback_box.text
    anvil.server.call('add_form',ship_name)
    Notification("Η Φόρμα καταχωρήθηκε").show()
    #self.clear_inputs()
    pass
    
 # def clear_inputs(self):
    #self.name_box.text = ""
    #self.email_box.text = ""
    #self.feedback_box.text = ""

  def showbutton_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

 


  
    
