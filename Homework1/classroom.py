class Classroom(object):
    """
    Represents classroom by number, capacity and equipment.
    """
    def __init__(self, number, capacity, equipment):
        """
        Creates attributes.
        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def is_larger(self, classroom):
        """
        If first classroom is more capacious than second, method returns True.
        """
        if self.capacity > classroom.capacity:
            return True
        else:
            return None

    def equipment_differences(self, classroom):
        """
        Returns a list of equipment which is only in first classroom.
        """
        return list(set(self.equipment) - set(classroom.equipment))

    def __str__(self):
        """
        Returns a string of classroom representation.
        """
        equip = str()
        for i in range(len(self.equipment) - 1):
            equip += self.equipment[i] + ", "
        equip += self.equipment[-1]
        return "Classroom " + self.number + " has a capacity of " + str(self.capacity) + " persons and has the following equipment: " + equip + "."

    def __repr__(self):
        """
        Returns a string of classroom representation.
        """
        return "Classroom" + "(" + self.number + ", " + str(self.capacity) + ", " + str(self.equipment) + ")"

classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])

print(classroom_016.number)
print(classroom_016.capacity)
print(classroom_016.equipment)
print(classroom_016.is_larger(classroom_007))
print(classroom_016.equipment_differences(classroom_007))
print(classroom_016)
