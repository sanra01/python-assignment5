"""The operation_ticket module, containing the OperateT object."""

from models.ticket import Ticket


class TicketController:
    """The operatet object."""

    _tickets = []

    @classmethod
    def create_ticket(cls, data):
        """Create a new ticket."""
        highest_ticket_id = cls._get_highest_ticket_id() + 1
        new_ticket = Ticket(
            ticket_id=highest_ticket_id,
            name=data["name"],
            status=data["status"]
        )
        cls._tickets.append(new_ticket)
        return new_ticket

   @classmethod
   def delete_ticket(cls, ticket_id):
       """Delete an existing ticket."""
       for ticket in cls._tickets:
           if ticket.get_id == ticket_id:
               cls._tickets.remove(ticket)

    @classmethod
    def get_tickets(self):
        """Get a list of all the tickets."""
        return cls._tickets

    @classmethod
    def get_ticket_by_id(cls, ticket_id):
        """Get the ticket by ID."""
        tickets_by_id = list(
            filter(lambda d: d.get_ticket_id() == ticket_id, cls._tickets)
        )

        return tickets_by_id[0]

    @classmethod
    def has_ticket_named(cls, name):
        """Loop over all tickets and return True if the name matches."""
        for ticket in self._tickets:
            if ticket.get_name() == name:
                return True
        return False

    @classmethod
    def has_ticket_id(cls, id):
        """Loop over all tickets and return True if the id matches."""
        for ticket in cls._tickets:
            if ticket.get_id() == id:
                return True, ticket
        return False

    @classmethod
    def get_highest_ticket_id(cls):
        """Return the highest ticket id."""
        if not cls._tickets:
            return 0
        else:
            return max([u.get_id() for u in cls._tickets])

    @classmethod
    def update_ticket(cls, ticket_id):            
