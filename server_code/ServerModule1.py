import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
import anvil.media
from collections import Counter
from io import StringIO

#Different user permissions
@anvil.server.callable
def print_my_permissions():
  super_user = 'konstantinoschios@hotmail.com'
  if anvil.users.get_user() is None:
    print("Nobody is logged in.")
  elif anvil.users.get_user()['email'] == super_user:
    print(f"{super_user} is allowed to see this.")
  else:
    print("This path is for minimum-access users.")
    
#Form 
#Store Form data
@anvil.server.callable
def Incidents_table(form_datetime, ship_name, national_sign, ship_nationality, ship_type, eta, naval_zone, weather, longitude, 
    latitude, origin, destination, cargo, pharmacy, surname, name, age, specialty, sailor_nationality, height, weight,
    sailor_id, symptoms_frequency, hours, days, blood_pressure, pulses, chronic_diseases, previous_surgeries,                  
    pain, fever, frown, dizziness, vomit, diarrhea, wound, redness, swelling, bleeding, foreign_body, cough, breath_shortness, weakness,
    loss_of_senses, other_symptoms, pain_diagram_position):
  app_tables.incidents_table.add_row(
    
    form_datetime = form_datetime,
   
    #ship data
    ship_name = ship_name,
    national_sign = national_sign, 
    ship_nationality = ship_nationality,
    ship_type = ship_type, 
    eta = eta,
    naval_zone = naval_zone,   
    weather = weather,
    longitude = longitude,   
    latitude = latitude,     
    origin = origin,
    destination = destination,
    cargo = cargo,
    pharmacy = pharmacy, 

    #sailor_data
    surname = surname,
    name = name,
    age = age,
    specialty = specialty,  
    sailor_nationality = sailor_nationality,
    height = height,
    weight = weight,    
    sailor_id = sailor_id, 
    
    #symptoms
    symptoms_frequency = symptoms_frequency,  
    hours = hours,
    days = days,

    blood_pressure = blood_pressure,    
    pulses = pulses,
    chronic_diseases = chronic_diseases,  
    previous_surgeries = previous_surgeries,    
    
    #symptoms checkboxes
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

    pain_diagram_position = pain_diagram_position,    
  )

#Download the form data table (Incidents_table) to CSV
@anvil.server.callable
def get_table_as_csv():
    output = StringIO()
    
    #CSV header
    header = ['ID',"form_datetime","ship_name","sign","foreign_body","cough","pain","cargo","age","pulses","s_id","kg","zone","nationallity","name","bleeding","surname","days","type","origine","surgeries","chronicdis","other_symptoms","weakness","pharm","dizziness","redness","fever","symptomsfre","wound","hours","breath_shortness","weather","sailor_nationality","swelling","loss_of_senses","vomit","frown","destination","diarrhea","height","eta","speciality","long","lat","piesi","photo_pain"]  # Adjust column names as needed
    output.write(','.join(header) + '\n')
    
    # Write the data rows, including the ID
    rows = app_tables.incidents_table.search()
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

#Stats
#Find the number of ships in the data table
@anvil.server.callable
def get_unique_sign_count():
    # Count unique 'national_sign's to find
    unique_signs = set(row['national_sign'] for row in app_tables.incidents_table.search() if row['national_sign'] is not None)
    return len(unique_signs)

#Find ship nationalities
@anvil.server.callable
def get_nationality_counts():
    # Fetch all rows from the 'Incidents_table' table
    all_entries = app_tables.incidents_table.search()
    
    # Create a dictionary to count nationalities
    nationality_counts = {}
    for entry in all_entries:
        nationality = entry['ship_nationality'] 
        if nationality in nationality_counts:
            nationality_counts[nationality] += 1
        else:
            nationality_counts[nationality] = 1
            
    # Convert the counts to a list of tuples and return
    return list(nationality_counts.items())

#Get ship types
@anvil.server.callable
def get_ship_type_counts():
    # Fetch all rows from the 'Incidents_table' table
    all_entries = app_tables.incidents_table.search()
    
    # Create a dictionary to count ship types
    type_counts = {}
    for entry in all_entries:
        ship_type = entry['ship_type']  # Adjusted to focus on the 'type' column
        if ship_type in type_counts:
            type_counts[ship_type] += 1
        else:
            type_counts[ship_type] = 1
            
    # Convert the counts to a list of tuples and return
    return list(type_counts.items())

#Get the number of patients 
@anvil.server.callable
def get_unique_sailorid_count():
    unique_sailorid = set(row['sailor_id'] for row in app_tables.incidents_table.search() if row['sailor_id'] is not None)
    return len(unique_sailorid)

#Get age statistics
@anvil.server.callable
def get_age_statistics():
    ages = []
    for row in app_tables.incidents_table.search():
        try:
            age = int(row['age'])
            ages.append(age)
        except (ValueError, TypeError):
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

#Get sailor nationalities
@anvil.server.callable
def get_sailor_nationality_counts():
    # Fetch all rows from the 'Incidents_table' table
    all_entries = app_tables.incidents_table.search()
    
    # Create a dictionary to count sailor nationalities
    sailor_nationality_counts = {}
    for entry in all_entries:
        sailor_nationality = entry['sailor_nationality']  # Focus on the 'sailor_nationality' column
        if sailor_nationality in sailor_nationality_counts:
            sailor_nationality_counts[sailor_nationality] += 1
        else:
            sailor_nationality_counts[sailor_nationality] = 1
            
    # Convert the counts to a list of tuples and return
    return list(sailor_nationality_counts.items())

#Get sailors speciality
@anvil.server.callable
def get_speciality_counts():
    # Fetch all rows from the 'Incidents_table' table
    all_entries = app_tables.incidents_table.search()
    
    # Create a dictionary to count sailor specialties
    speciality_counts = {}
    for entry in all_entries:
        speciality = entry['specialty']  # Focus on the 'speciality' column
        if speciality in speciality_counts:
            speciality_counts[speciality] += 1
        else:
            speciality_counts[speciality] = 1
            
    # Convert the counts to a list of tuples and return
    return list(speciality_counts.items())

#User role check
@anvil.server.callable
def get_current_user_role():
    user = anvil.users.get_user()
    if user:
        # Assuming 'role' is the column name in the 'Users' table where roles are stored
        return user['role']
    return None  # No user is logged in
