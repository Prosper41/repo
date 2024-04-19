phone = input("phone: ")
numbers_mapping = {
  '1': 'one',
  '2': 'two',
  '3': 'three',
  '4': 'four'
}
output = ''
for char in phone:
  output += numbers_mapping.get(char, '!') + ' '
print(output)