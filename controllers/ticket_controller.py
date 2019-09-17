"""The operation_ticket module, containing the OperateT object."""

class TicketController:
    """The operatet object."""

    # this is a class variable

    def __init__(self):
        """Instantiate the operatet object."""
        self._tickets = []

    def add_ticket(self, ticket):
        """Add a ticket."""
        self._tickets.append(ticket)

    def get_tickets(self):
        """Get a list of all the tickets."""
        return self._tickets

    def get_ticket(self, id):
        """Get ticket object if the id matches."""
        for ticket in self._tickets:
            if ticket.get_id() == id:
                return ticket

    def has_ticket_named(self, name):
        """Loop over all tickets and return True if the name matches."""
        for ticket in self._tickets:
            if ticket.get_name() == name:
                return True
        return False

    def has_ticket_id(self, id):
        """Loop over all tickets and return True if the id matches."""
        for ticket in self._tickets:
            if ticket.get_id() == id:
                return True, ticket
        return False
