print("Calculate fuel consumtion.")
Matk=input("Enter travel distance(kilometer):")
Distance=int(Matk)
FuelUsage=int(input("Enter fuel usage(liters):"))
matk2= Distance / 100
Consumption=int(FuelUsage / matk2)
print("Fuel consumption is",Consumption,"l per 100 km")

