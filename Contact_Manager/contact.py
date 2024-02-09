
import cmd

class ContactManager(cmd.Cmd):
    """A command processor for managing contacts."""

    prompt = "Contact >>>"
    contacts = {}

    def preloop(self):
        """Method called once before the command loop."""
        self.intro = "Welcome to the Contact Manager. Type help or ? to list commands.\n"

    def postloop(self):
        """Method called once after the command loop."""
        print("Exiting the Contact Manager.")

    def do_add(self, line):
        """Add a contact with a name and phone number."""
        try:
            name, phone = line.split()
            self.contacts[name] = phone
            print(f"Contact added: {name} - {phone}")
        except ValueError:
            print("Invalid input. Please enter the name and phone number separated by a space.")

    def do_get(self, name):
        """Retrieve a contact's phone number by name."""
        if name in self.contacts:
            print(f"{name}'s phone number is {self.contacts[name]}")
        else:
            print(f"No contact found with the name '{name}'.")

    def do_list(self, _):
        """List all contacts."""
        if not self.contacts:
            print("No contacts available.")
        else:
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

    def do_delete(self, name):
        """Delete a contact by name."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact deleted: {name}")
        else:
            print(f"No contact found with the name '{name}'.")

    def do_update(self, line):
        """Update a contact's phone number."""
        try:
            name, new_phone = line.split(' ',  1)
            if name in self.contacts:
                self.contacts[name] = new_phone
                print(f"Contact updated: {name} - {new_phone}")
            else:
                print(f"No contact found with the name '{name}'.")
        except ValueError:
            print("Invalid input. Please enter the name and new phone number separated by a space.")

    def do_EOF(self, line):
        """Exit the program."""
        return True
    do_quit = do_EOF

if __name__ == '__main__':
    ContactManager().cmdloop()
