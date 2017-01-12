import os
import unittest
import sys
sys.path.append('../Office-Space-Allocation')
from amity_functions import *

class TestAmity(unittest.TestCase):

    def test_create_office(self):
        Amity.all_rooms = []
        initial_num_rooms = len(Amity.all_rooms)
        self.assertEqual(len(Amity.all_rooms), 0)
        Amity.create_room(self, 'o', 'Oculus')
        self.assertEqual(len(Amity.all_rooms), initial_num_rooms+1)
        self.assertIn('OCULUS', Amity.office_spaces.keys())

    def test_create_living_area(self):
        Amity.create_room(self, 'l', 'Arduino')
        self.assertEqual(len(Amity.all_rooms), 1)
        self.assertIn('ARDUINO', Amity.living_spaces.keys())

    def test_add_person(self):
        all_people = len(Amity.all_people)
        Amity.all_people = []
        Amity.add_person("Kironde", "david", "F", "Y")
        self.assertEqual(len(Amity.all_people), all_people+1)

    def test_save_state(self):
        Amity.save_state('testdb')
        self.assertTrue(os.path.isfile('testdb.sqlite'))
        os.remove('testdb.sqlite')

    def test_print_allocations(self):
        Amity.print_allocations('testfile')
        self.assertTrue(os.path.isfile('testfile.txt'))
        os.remove('testfile.txt')

    def test_print_unallocated(self):
        Amity.print_unallocated('testfile')
        self.assertTrue(os.path.isfile('testfile.txt'))
        os.remove('testfile.txt')

if __name__ == '__main__':
    unittest.main()
