car_started = False

while True:
    user_input = input("Enter a command (start, stop, help, quit): ").lower()

    if user_input == "start":
        if car_started:
            print("Car is already started.")
        else:
            car_started = True
            print("Car started... Ready to go!")

    elif user_input == "stop":
        if not car_started:
            print("Car is already stopped.")
        else:
            car_started = False
            print("Car stopped.")

    elif user_input == "help":
        print("Commands:")
        print("start - to start the car")
        print("stop - to stop the car")
        print("help - to display available commands")
        print("quit - to exit")
        
    elif user_input == "quit":
        print("Exiting the car control system.")
        break

    else:
        print("Invalid command. Type 'help' to see available commands.")
