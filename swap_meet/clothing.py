from swap_meet.item import Item

class Clothing(Item):
    """
    A class to represent a Clothing item.

    """

    def __init__(self, condition=0.0):
        super().__init__(category = "Clothing", condition=condition)

    def __str__(self):
        return "The finest clothing you could wear."
