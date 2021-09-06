product1 = input ("hoeveel kost product 1?: ")
product2 = input ("hoeveel kost product 2?: ")
product3 = input ("hoeveel kost product 3?: ")
product4 = input ("hoeveel kost product 4?: ")
product5 = input ("hoeveel kost product 5?: ")

product1 = int(product1)
product2 = int(product2)
product3 = int(product3)
product4 = int(product4)
product5 = int(product5)

totaal = product1 + product2 + product3 + product4 + product5

print("\nde nettokosten zijn: " , totaal)
print("\nde belasting op de producten is 7%")
print("\nde brutokosten zijn: " , totaal * 0.93)
