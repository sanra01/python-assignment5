"""The person module, containing the Person object."""

class User:
    """The person object."""

    # this is a class variable

    def __init__(self, name):
        """Instantiate the person object and set the name for the person."""
        self._name = name

    def get_name(self):
        """Return the name of the person."""
        return self._name
