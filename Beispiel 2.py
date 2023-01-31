import time
command = ""
started = False
stopped = False
print("Welcome")
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The Car is already started, fool")
        else:
            started = True
            print("The Car started, brum brum")
    elif command == "stop":
        if stopped:
            print("You're not movin', fool")
        else:
            stopped = True
            print("The car has stopped")

    elif command == "quit":
        print("Thank you for the ride!")
        time.sleep(1)
        break
    else:
        print("""I dont understand, this are the following commands:
        
Start - Starting the car
Stop - Stopping the car
Quit - Quitting the Game""")

