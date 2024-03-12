import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
import anvil.media
from collections import Counter

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

@anvil.server.callable
def get_unique_sign_count():
    # Μετράει τα μοναδικά σήματα στη στήλη 'sign'
    unique_signs = set(row['sign'] for row in app_tables.add_form.search() if row['sign'] is not None)
    return len(unique_signs)

@anvil.server.callable
def get_unique_sailorid_count():
    # Μετράει τους μοναδικούς αριθμούς διαβατηρίου ή ΜΕΘ 's_id'
    unique_sailorid = set(row['s_id'] for row in app_tables.add_form.search() if row['s_id'] is not None)
    return len(unique_sailorid)



@anvil.server.callable
def get_age_statistics():
    ages = []
    for row in app_tables.add_form.search():
        try:
            # Μετατροπή της τιμής σε ακέραιο και προσθήκη στη λίστα
            age = int(row['age'])
            ages.append(age)
        except (ValueError, TypeError):
            # Αγνοήστε την τιμή αν δεν είναι μετατρέψιμη σε ακέραιο
            continue

    if not ages:
        return {"mean_age": 0, "median_age": 0, "age_range": 0, "min_age": 0, "max_age": 0}

    sorted_ages = sorted(ages)
    mean_age = sum(ages) / len(ages)
    median_age = sorted_ages[len(sorted_ages) // 2] if len(sorted_ages) % 2 != 0 else (sorted_ages[len(sorted_ages) // 2 - 1] + sorted_ages[len(sorted_ages) // 2]) / 2
    age_range = sorted_ages[-1] - sorted_ages[0]
    min_age = sorted_ages[0]
    max_age = sorted_ages[-1]

    return {
        "mean_age": mean_age,
        "median_age": median_age,
        "age_range": age_range,
        "min_age": min_age,
        "max_age": max_age
    }

import anvil.server
from anvil.tables import app_tables
from collections import Counter

@anvil.server.callable
def get_nationality_counts():
    # Retrieve all records from the table and extract the list of nationalities
    all_records = app_tables.add_form.search()
    nationalities = [record['nationallity'] for record in all_records if record['nationallity'] is not None]

    # Use Counter to count the occurrences of each nationality
    nationality_counts = Counter(nationalities)

    # Return the dictionary of nationalities and their respective counts
    return dict(nationality_counts)


