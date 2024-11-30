cup_price = 0.50
cone_price = 0.80
scoop_price = 1.20
flake_price = 0.40
chocolate_price = 0.30
strawberry_price = 0.60


price = 0
container = input("would you like a cup, or a cone?")
if container.upper() == "CUP":
    price = cup_price
else:
    price = cone_price
scoops = int(input("how many scoops would you like?"))
price = price + (scoops * scoop_price)

flakes = input("would you like flakes on your ice cream?")
if flakes.upper() == "YES":
    price = flake_price
chocolate_sprinkles = input(" would you like chocolate sprinkles on your ice cream?")
if chocolate_sprinkles.upper() == "YES":
    price = chocolate_price
strawberries = input("would you like strawberries on your ice cream?")
if strawberries.upper() == "YES":
    price = strawberry_price    

print("your total price is $" + str(price))