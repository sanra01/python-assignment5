"""The ticket module, containing the Ticket object."""
class Ticket:
    """The ticket object."""

    # this is a class variable

    def __init__(self, name, ticket_id):
        """Instantiate the ticket object and set the name and id for the ticket."""
        self._name = name
        self._id = ticket_id
        self._person = "unassigned"
        self._people = []
        self._status = "open"

    def get_name(self):
        """Return the name of the ticket."""
        return self._name

    def get_id(self):
        """Return the id of the ticket."""
        return self._id

    def set_assignee(self, person):
        """Set assignee for the ticket."""
        self._person = person

    def get_assignee(self):
        """Get assignee for the ticket."""
        return self._person

    def set_status(self):
        """Set status for the ticket."""
        self._status = "close"

    def get_status(self):
        """Get status for the ticket."""
        return self._status
