class Building(object):
    """
    Represents building by its address.
    """
    def __init__(self, address):
        self.address = address

class House(Building):
    """
    Represents a house by an address and a list of flats.
    """
    def __init__(self, address, flats):
        Building.__init__(self, address)
        self.flats = flats
