import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
import anvil.media
import csv
from io import StringIO

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
def add_form(form_datetime, ship_name, sign, nationallity, type, eta, zone, weather, long, lat,
  origine, destination, cargo, pharm, surname, name, age, speciality, sailor_nationality,
  height, kg, s_id, symptomsfre, hours, days, piesi, pulses, chronicdis, surg, pain,   
  fever, frown, dizziness, vomit, diarrhea, wound, redness, swelling, bleeding, foreign_body,     
  cough, breath_shortness, weakness, loss_of_senses, other_symptoms, photo_pain):
  app_tables.add_form.add_row(
    
    #ship_data
    form_datetime = form_datetime,
    ship_name=ship_name,
    sign = sign,
    nationallity = nationallity,
    type = type,
    eta = eta,
    zone = zone,
    weather = weather,
    long = long,
    lat = lat,
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

    piesi = piesi,
    pulses = pulses,
    chronicdis = chronicdis,
    surgeries = surg,
    
    #check box symptoms
    pain = pain,   
    fever = fever,        
    frown = frown,    
    dizziness = dizziness, 
    vomit = vomit,
    diarrhea = diarrhea,
    wound = wound,
    redness = redness, 
    swelling = swelling,   
    bleeding = bleeding, 
    foreign_body = foreign_body,     
    cough = cough, 
    breath_shortness = breath_shortness,
    weakness = weakness,  
    loss_of_senses = loss_of_senses, 
    
    other_symptoms = other_symptoms,

    photo_pain = photo_pain,
    #email=email, 
    #feedback=feedback, 
    #created=datetime.now()
  )

#map
@anvil.server.callable
def set_marker_position(latitude, longitude):
    return {"latitude": latitude, "longitude": longitude}


import anvil.server
import anvil.media
import csv
from io import StringIO

@anvil.server.callable
def download_table_as_csv():
    # Create a StringIO object to write CSV data to
    output = StringIO()
    writer = csv.writer(output)
    
    # Assuming 'your_table' is the name of your Data Table
    rows = app_tables.your_table.search()
    
    # Write a header row, based on the columns in your Data Table
    writer.writerow(['column1', 'column2', 'column3'])  # replace with your actual column names
    
    # Write data rows
    for row in rows:
        writer.writerow([row['column1'], row['column2'], row['column3']])  # replace with your actual column names
    
    # Return the CSV data as an Anvil Media object
    return anvil.media.from_bytes(output.getvalue(), 'text/csv', name='data.csv')
