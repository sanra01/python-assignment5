"""The operation module for the tickets."""

class UserController:
    """The operatep object."""

    # this is a class variable

    def __init__(self):
        """Instantiate the operatep object."""
        self._people = []

    def add_person(self, person):
        """Add a person."""
        self._people.append(person)  

    def get_people(self):
        """Get a list of all the people."""
        return self._people      

    def has_person_named(self, name):
        """Loop over all people and return True if the name matches."""
        for person in self._people:
            if person.get_name() == name:
                return True
        return False   