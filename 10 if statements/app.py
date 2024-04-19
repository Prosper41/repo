# is_hot = False
# is_cold =  True
# if is_hot:
#   print("It's a hot day")
#   print("Drink plenty of water.")
# elif is_cold:
#     print("It is a cold day")
#     print("wear warm cloth")
# else:
#   print('ENJOY THE DAY')


# Poor version 😖😖
house_price = "$1m"
buyer = False
if buyer:
  print("pay 10%")
else:
  print("pay 20%")  

# better version😅
house_price = 1000000
buyer = False
if buyer:
  down_payment = 0.1 * house_price
else:
  down_payment = 0.2 * house_price
print(f"Down payment: ${down_payment}")
