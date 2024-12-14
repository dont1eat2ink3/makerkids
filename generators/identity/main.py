import random
Birth_genders = ["female", "Male"]

first_names = ["Alex", "Jamie", "Taylor", "Jordan", "Casey", "Morgan", "Riley", "Cameron", "Drew", "Quinn"] 

last_names = ["Smith", "Johnson", "Brown", "Williams", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez"] 

birth_years = [1980, 1985, 1990, 1995, 2000, 2005, 2010, 1975, 1970, 1965] 

addresses = [ "123 Maple St, Toronto, ON M4B 1B3", "456 Oak Ave, Vancouver, BC V5K 0A1", "789 Pine Rd, Calgary, AB T2P 1J9", "321 Elm Blvd, Montreal, QC H2X 3B9", "654 Birch Ln, Halifax, NS B3H 4R2", "987 Cedar Ct, Winnipeg, MB R3B 1H4", "234 Spruce St, Ottawa, ON K1A 0A1", "567 Willow Ave, Edmonton, AB T5J 1R9", "890 Aspen Rd, Quebec City, QC G1R 4P5", "345 Poplar Blvd, Regina, SK S4P 3Y2" ]

phone_numbers = [ "416-555-1234", "604-555-5678", "403-555-7890", "514-555-4321", "902-555-6543", "204-555-8765", "613-555-3456", "780-555-6789", "418-555-0987", "306-555-4567" ]

sin_numbers = ["123-456-789", "234-567-890", "345-678-901", "456-789-012", "567-890-123", "678-901-234", "789-012-345", "890-123-456", "901-234-567", "012-345-678", "437-771-9226"]

ethnicities = ["Caucasian", "Asian", "African", "Hispanic", "Indigenous", "Middle Eastern", "Pacific Islander", "Mixed", "indian", "Other"]

hair_colors = ["Black", "Brown", "Blonde", "Red", "Gray", "White", "Blue", "Pink", "Green", "Purple"] 

eye_colors = ["Brown", "Blue", "Green", "Hazel", "Gray", "Amber", "Violet"]

blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

occupations = ["Teacher", "Engineer", "Artist", "Doctor", "Chef", "Musician", "Writer", "Athlete", "Designer", "Scientist"]

hobbies = ["Reading", "Gaming", "Hiking", "Cooking", "Painting", "Knitting", "Dancing", "Fishing", "Gardening", "Traveling"]

relationship_statuses = ["Single", "Married", "In a relationship", "Divorced", "Widowed"]

secret_talents = ["Juggling", "Whistling", "Solving Rubik's Cube", "Impersonations", "Moonwalking", "Speed reading", "Writing backwards", "Origami", "Beatboxing", "Spinning plates"] 

birth_gender = random.choice(Birth_genders)
first_name = random.choice(first_names)
last_name = random.choice(last_names)
birth_year = random.choice(birth_years)
address = random.choice(addresses)
phone_number = random.choice(phone_numbers)
sin_number = random.choice(sin_numbers)
ethnicity = random.choice(ethnicities)
hair_color = random.choice(hair_colors)
eye_color = random.choice(eye_colors)
blood_type = random.choice(blood_types)
occupation = random.choice(occupations)
hobbie = random.choice(hobbies)
relationship_status = random.choice(relationship_statuses)
secret_talent = random.choice(secret_talents)

print("=== Fake identity generator ===")
print("Name:" + first_name + " " + last_name + " " + ("year of birth" + " " +str(birth_year)))
print("Birth gender:" +birth_gender)
print("Adress:" + address)
print("Phone Number:" +str(phone_number ) + " |" + "Sin number:" +str(sin_number))
print("Email:" +first_name +"." +last_name + "@email.ca")
print("Ethnicity:" +ethnicity)
print("Hair color:" +hair_color + " |" + "Eye color:" +eye_color)

print( )
print("---additional details---")
print("Occupation:" +occupation)
print("Hobby:" +hobbie)
print("Secret talent:" +secret_talent)
print("================================")