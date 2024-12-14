import random

first_names = ["Aria","joanne","light", "chasca","orion"]
last_names = ["yagami", "jackson", "blight", "younameit" ,"smith"]
species = ["fairy","elf","sword master","NPC", "siren", "mermaid"]
powers = ["incubation", "possesion","healing","pyrokenisis", "intelect","strength"]

first_name = random.choice(first_names)
last_name = random.choice(last_names)
specie = random.choice(species)
power = random.choice(powers)
print("Here is your fantasy character:")
print("name:" + first_name + " " + last_name)
print("species:" +specie )
print("power:" +power)