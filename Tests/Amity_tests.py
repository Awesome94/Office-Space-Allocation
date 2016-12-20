import unittest
from amity_functions import Amity


class AmityTest(unittest.TestCase):
    def test_create_room(self):
        amity = Amity()
        amity.all_rooms = []
        self.assertFalse('HOGWARTS' in amity.all_rooms)
        amity.create_room('HOGWARTS', "OFFICE")
        self.assertTrue('HOGWARTS' in amity.all_rooms)
        amity.all_rooms = []

    def test_add_person(self):
        amity = Amity()
        amity.all_people = []
        self.assertFalse('AWESOME' in amity.all_people)
        amity.add_person('AWESOME')
        self.assertTrue('AWESOME' in amity.all_people)
        amity.all_people = []

    def test_room_type(self):
        amity = Amity()
        amity.offices = []
        amity.living_spaces = []
        self.result1 = amity.set_room_type('HOGWARTS', 'OFFICE')
        self.assertTrue('amity.offices.append(result)')
        self.result2 = amity.set_room_type('PHP', 'LIVING SPACE')
        self.assertTrue('amity.living_spaces.append(self.result2)')



    def test_person_type(self):
        """This will test for the type of person. i.e. if person is fellow or staff"""


if __name__ == '__main__':
    unittest.main()
