
command = ""
started = False
while True:
  command =  input("> ").lower()
  if command == "start":
    if started:
      print('car has started already ')
    else:
      started = True 
      print('')
    print("car started...")
  elif command == "stop":
    if not started:
      print('car has already stopped.')
    else:
      started = False
    print("car stopped")
  elif command == "help":
    print("""
start -- to start
stop -- to stop 
quit -- to quit
""")
  elif command == "quit":
    break
  else:
    print("sorry, Come again")

 