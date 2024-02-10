import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users

#different user permissions
@anvil.server.callable
def print_my_permissions():
  super_user = 'konstantinoschios@hotmail.com'
  if anvil.users.get_user() is None:
    print("Nobody is logged in.")
  elif anvil.users.get_user()['email'] == super_user:
    print(f"{super_user} is allowed to see this.")
  else:
    print("This path is for minimum-access users.")
    
# Add more server functions as needed for your application

#store data for form
@anvil.server.callable
def add_form(ship_name):
  app_tables.add_form.add_row(
    #ship_data
    ship_name=ship_name,
    sign = sign,
    nationallity = nationallity,
    type = type,
    eta = eta,
    zone = zone,
    weather = weather,
    #na valw longitude latitude
    #££££££££££££££££££££££££
    origine = origine,
    destination = destination,
    cargo = cargo,
    pharm = pharm,

    #sailor_data
    surname = surname,
    name = name,
    age = age,
    speciality = speciality,
    sailor_nationality = sailor_nationality,
    height = height,
    kg = kg,
    s_id = s_id,
    
    #symptoms
    #symptoms_intro
    symptomsfre = symptomsfre,
    hours = hours,
    days = days,

    #piesi####################
    pulses = pulses,
    chronicdis = chronicdis,
    surgeries = surgeries,
    
    #check box symptoms
    ##########################
    other_symptoms = self.in_allasimptomata.text

    
    #email=email, 
    #feedback=feedback, 
    #created=datetime.now()
  )

#map
@anvil.server.callable
def set_marker_position(latitude, longitude):
    return {"latitude": latitude, "longitude": longitude}