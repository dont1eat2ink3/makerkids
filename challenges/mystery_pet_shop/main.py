import random

pet_name=["bubbles","spark","luna","kite","furry","kid"]
pet_species=["cat","dog","hamster","snake","bunny"]
per traits=["speedy","hunting buff","lazer eyes"]

user_collection[]

def generate_mystery_pet():
    name = random.choice(pet_name)
    species = random.choice(pet_species)
    traits = random.choice(pet_trait)

    pet = {
        "Name":name,
        "Species":species,
        "Trait":trait

    }
    return pet
def display_pet(pet):
    print("mystery pet details: ")
    print("Name: " + pet["name"])
    print("Species: " + pet["species"])
    print("Special Trait: " + pet["trait"])

def mystery_pet_shop:
    print("Welcome to this myster pet shop! hope you enjoy your stay.")

    while True:
        action = input("what would you like to buy, or exit.")
        if action = "exit":
            print("thanks for visiting")
            break
        elif action == "Buy":
            pet = generate_mystery_pet()
            display_pet(pet)

            decision = input("would you like to buy? yes or no?")
            if decision == "YES":
                user_collection.append(pet)
                print(per["name"] + "was added to your cart")
            else:
                print("no worries, lets try another pet!")
        else:
            print("please type exit or buy")




my_pet = generate_mystery_pet
display_pet(my_pet)
# print(my_pet)