import unittest
from amity_functions import Amity
import os


class AmityTest(unittest.TestCase):

    def test_it_creates_office(self):
        amity = Amity()
        amity.create_room('o', 'Oculus')
        self.assertNotEqual(len(amity.all_rooms), 0)
        self.assertIn('OCULUS', Amity.office_spaces.keys())
        amity.all_rooms = []

    def test_it_creates_living_area(self):
        amity = Amity()
        amity.create_room('l', 'Arduino')
        self.assertNotEqual(len(amity.all_rooms), 0)
        self.assertIn('ARDUINO', Amity.living_spaces.keys())
        amity.all_rooms = []

    def test_add_person(self):
        amity = Amity()
        amity.all_people = []
        self.assertFalse('kironde' in amity.all_people)
        amity.add_person("kironde", "suubi", "F", "Y")
        self.assertNotEqual(len(Amity.all_people), 0)

    def test_it_saves_state(self):
        amity = Amity()
        amity.save_state('testdb')
        self.assertTrue (os.path.isfile ('testdb.sqlite'))
        os.remove ('testdb.sqlite')

    def test_it_prints_allocations(self):
        Amity.print_allocations('testfile')
        self.assertTrue(os.path.isfile('testfile.txt'))
        os.remove('testfile.txt')

    def test_it_prints_unallocated(self):
        amity.print_unallocated('testfile')
        self.assertTrue(os.path.isfile('testfile.txt'))
        os.remove('testfile.txt')

if __name__ == '__main__':
    unittest.main()
