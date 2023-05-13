command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started.... ")
        else:
            started = True
            print("car starting...")
    elif command == "stop":
        if not started:
            print("The car has already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - To start the car
stop - To stop the car
quit - To quit
""")
    elif command == "quit":
        break
    else:
        print("sorry i don't understand that!")