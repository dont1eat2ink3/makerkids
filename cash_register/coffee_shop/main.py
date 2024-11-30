Americano_price = 3.00
cappuccino_price = 3.00
Espresso_price = 2.50
flatwhite_price = 2.50 
macchito_price = 2.50
mocha_price = 3.50
late_price = 2.50

price = 0

drink = input("what drink would you like?")
if drink.upper() == "MOCHA":
    price = mocha_price
else drink.upper() == "MACCHITO,ESPRESSO,FLAT WHITE,LATTE":
    price = Espresso_price
