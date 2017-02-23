from classroom import Classroom
from building import Building

class AcademicBuilding(Building):
    """
    Represents study building by its address and a list of classrooms.
    """
    def __init__(self, address, classrooms):
        """
        Creates attributes. This class inherits from Building class.
        """
        Building.__init__(self, address)
        self.classrooms = classrooms

    def total_equipment(self):
        """
        Returns list of equipment which is in academic building. 
        """
        equipm = {}
        for room in self.classrooms:
            for e in room.equipment:
                if e not in equipm:
                    equipm[e] = 1
                else:
                    equipm[e] += 1

        equipmt = []
        for i in equipm:
            equipmt.append((i, equipm[i]))
        return equipmt

    def __str__(self):
        """
        Returns strings of classroom representations.
        """
        line = self.address
        for room in self.classrooms:
            line += "\n" + str(room)
        return line


classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = classroom.Classroom('007', 12, ['TV'])
classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]
building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
print(building.address)
classrooms = [classroom_016, classroom_007, classroom_008]
building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
print(building.total_equipment())
print(building)
