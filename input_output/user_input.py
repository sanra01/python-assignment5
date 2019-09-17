"""The input module, containing the input class."""

from input_output.terminal_output import Output

class Input:
    """The input class, containing functions related to user input."""

    valid_commands = [
        "create person",
        "list people",
        "open ticket",
        "close ticket",
        "assign ticket",
        "list open tickets",
        "list all tickets",
        "exit"
    ]

    @classmethod
    def get_person_name(cls):
        """Request the person name from the user."""
        Output.print_bold("What is the name of the person?")
        user_input = input()
        return user_input

    @classmethod
    def get_ticket_name(cls):
        """Request the person name from the user."""
        Output.print_bold("What is the title of the ticket?")
        ticket_name = input()
        return ticket_name 

    @classmethod
    def get_ticket_id(cls):
        """Request the person name from the user."""
        Output.print_bold("What is the ticket ID?")
        ticket_id = input()
        return int(ticket_id)       

    @classmethod
    def get_ticket_owner(cls):
        """Request the person name from the user."""
        Output.print_bold("Who would you like to assign it to?")
        ticket_owner = input()
        return ticket_owner

    @classmethod
    def get_input(cls):
        """Get input from the command line and verfies its content."""
        user_input = input()
        if user_input not in cls.valid_commands:
            Output.print_error(f"'{user_input}' is not a valid command.")
            cls.print_help()
        return user_input

    @classmethod
    def print_help(cls):
        """Print a list of valid commands to stdout."""
        Output.print_bold("Valid commands:")
        for command in cls.valid_commands:
            print(command)
