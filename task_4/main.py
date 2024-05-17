import handlers

commands = ["hello", "add", "change", "phone", "all", "exit", "close"]

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "hello":
            handlers.say_greeting()

        elif command == "add":
            try:
                if len(args) < 2:
                    raise ValueError("Provide name and phone number")
                
                name, phone = args
                handlers.add_contact(name, phone)
                print("Contact added.")  
            except ValueError as error:
                print(f"Error: {error}") 

        elif command == "change":
            try:
                if len(args) < 2:
                    raise ValueError("Provide name and phone number")
                
                name, phone = args
                handlers.change_contact(name, phone)
                print("Contact updated.")
            except ValueError as error:
                print(f"Error: {error}")

        elif command == "phone":
            try:
                if len(args) < 1:
                    raise ValueError("Provide name please")
                name = args[0]
                phone = handlers.show_phone(name)
                print(phone)
            except ValueError as error:
                print(f"Error: {error}")

        elif command == "all":
            contacts = handlers.show_all()
            print(contacts)

        elif command in ["exit", "close"]:
            print("Goodbye!")
            break

        else:
            print("Invalid command.")
            print(f"Existed commands: {commands}")

if __name__ == "__main__":
    main()