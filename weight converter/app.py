weight = int(input('weight: '))
units = input('(L)bs or (k)g: ')
if units.upper() == "L":
  conv = weight * 0.45
  print(f"You are {conv} kilos")
else: 
  conv = weight / 0.45
  print(f"You are {conv} pounds")