"""The main module of the application."""

import sys

from input_output.user_input import Input
from input_output.terminal_output import Output
from models.user import User
from models.ticket import Ticket
from controllers.user_controller import UserController
from controllers.ticket_controller import TicketController

def main():
    """Run the application."""
    userc = UserController()
    ticketc = TicketController()
    ticket_id = 0
    while True:
        Output.print_bold("What would you like to do?")
        user_input = Input.get_input()

        if user_input == "create person":
            user_name = Input.get_person_name()
            person = User(user_name)
            Output.print_bold(f"{person.get_name()} has been created.")
            if not userc.has_person_named(person):
                userc.add_person(person)
            else:
                Output.print_error(
                    f"A person named {user_name} is already present."
                )

        elif user_input == "list people":
            people = userc.get_people()
            if not people:
                Output.print_bold("There are no people.")
            else:
                print("These are the people known to the system:")
                for person in userc.get_people():
                    print(f"- {person.get_name()}")

        elif user_input == "open ticket":
            ticket_name = Input.get_ticket_name()
            ticket_id = ticket_id + 1
            ticket = Ticket(ticket_name, ticket_id)
            ticketc.add_ticket(ticket)
            Output.print_bold(f"A ticket {ticket.get_name()} is created with ID {ticket.get_id()}")

        elif user_input == "close ticket":
            ticket_id = Input.get_ticket_id()
            if ticketc.has_ticket_id(ticket_id):
                ticket = ticketc.get_ticket(ticket_id)
                ticket_name = ticket.get_name()
                ticket.set_status()
                Output.print_bold(f"Ticket {ticket_name} is closed")
            else:
                Output.print_error(f"Ticket with ID:{ticket_id} do not exist.")

        elif user_input == "assign ticket":
            ticket_id = Input.get_ticket_id()
            if ticketc.has_ticket_id(ticket_id):
                ticket_owner = Input.get_ticket_owner()
                if userc.has_person_named(ticket_owner):
                    ticket = ticketc.get_ticket(ticket_id)
                    ticket.set_assignee(ticket_owner)
                    Output.print_bold(f"Ticket {ticket.get_name()} has been assigned to "
                                      f"{ticket.get_assignee()}.")
                else:
                    Output.print_error(
                        f"Person with name {ticket_owner} do not exist."
                    )
            else:
                Output.print_error(
                    f"Ticket with ID:{ticket_id} do not exist."
                )

        elif user_input == "list open tickets":
            tickets = ticketc.get_tickets()
            if not tickets:
                Output.print_bold("There are no tickets.")
            else:
                Output.print_bold("These are open tickets:")
                for ticket in tickets:
                    if ticket.get_status() == 'open':
                        print(f"{ticket.get_id()}: {ticket.get_name()} ({ticket.get_assignee()})")

        elif user_input == "list all tickets":
            tickets = ticketc.get_tickets()
            if not tickets:
                Output.print_bold("There are no tickets.")
            else:
                Output.print_bold("These tickets are known to the system:")
                for ticket in tickets:
                    print(f"{ticket.get_id()}: {ticket.get_name()} ({ticket.get_assignee()})")

        elif user_input == "exit":
            sys.exit()

if __name__ == "__main__":
    main()
