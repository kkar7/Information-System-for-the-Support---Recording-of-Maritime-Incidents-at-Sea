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

  def pi_logitude_pressed_enter(self, **event_args):
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

  def in_ponos_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
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
   # email = self.email_box.text
   # feedback = self.feedback_box.text
    anvil.server.call('add_form',pi_shipname)
    Notification("Η Φόρμα καταχωρήθηκε").show()
    self.clear_inputs()
    pass
    

  
    
