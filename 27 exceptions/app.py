try:
  age = int(input('Age >:  '))
  print(age)
  income = 2000
  risk = income / age
  print(age)
except ZeroDivisionError:
  print('Age cannot be 0')
except ValueError:
  print('invaild value')
