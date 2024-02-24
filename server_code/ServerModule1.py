import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
import anvil.media

#import csv
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


""""
@anvil.server.callable
def download_table_as_csv():
    # Create a StringIO object to write CSV data to
    output = StringIO()
    writer = csv.writer(output)
    
    # Assuming 'your_table' is the name of your Data Table
    rows = app_tables.add_form.search()
    
    # Write a header row, based on the columns in your Data Table
    writer.writerow(['ID',"form_datetime","ship_name","sign","foreign_body","cough","pain","cargo","age","pulses","s_id","kg","zone","nationallity","name","bleeding","surname","days","type","origine","surgeries","chronicdis","other_symptoms","weakness","pharm","dizziness","redness","fever","symptomsfre","wound","hours","breath_shortness","weather","sailor_nationality","swelling","loss_of_senses","vomit","frown","destination","diarrhea","height","eta","speciality","long","lat","piesi","photo_pain"])  # replace with your actual column names
    
    # Write data rows
    for row in rows:
        writer.writerow(['ID',"form_datetime","ship_name","sign","foreign_body","cough","pain","cargo","age","pulses","s_id","kg","zone","nationallity","name","bleeding","surname","days","type","origine","surgeries","chronicdis","other_symptoms","weakness","pharm","dizziness","redness","fever","symptomsfre","wound","hours","breath_shortness","weather","sailor_nationality","swelling","loss_of_senses","vomit","frown","destination","diarrhea","height","eta","speciality","long","lat","piesi","photo_pain"])   # replace with your actual column names
    
    # Return the CSV data as an Anvil Media object
    return anvil.media.from_bytes(output.getvalue(), 'text/csv', name='data.csv')
    pass """



@anvil.server.callable
def get_table_as_csv():
    output = StringIO()
    
    # Write the CSV header
    header = ['ID',"form_datetime","ship_name","sign","foreign_body","cough","pain","cargo","age","pulses","s_id","kg","zone","nationallity","name","bleeding","surname","days","type","origine","surgeries","chronicdis","other_symptoms","weakness","pharm","dizziness","redness","fever","symptomsfre","wound","hours","breath_shortness","weather","sailor_nationality","swelling","loss_of_senses","vomit","frown","destination","diarrhea","height","eta","speciality","long","lat","piesi","photo_pain"]  # Adjust column names as needed
    output.write(','.join(header) + '\n')
    
    # Write the data rows, including the ID
    rows = app_tables.add_form.search()
    for row in rows:
        id_str = str(row.get_id())
        row_data = [id_str] + [str(row[column_name]) for column_name in header[1:]]
        output.write(','.join(row_data) + '\n')
    
    # Get the CSV string and convert it to bytes
    csv_string = output.getvalue()
    csv_bytes = csv_string.encode('utf-8')
    output.close()
    
    # Return the CSV bytes as a media object
    return anvil.BlobMedia('text/csv', csv_bytes, name='data.csv')

