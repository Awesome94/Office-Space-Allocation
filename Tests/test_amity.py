import os
import unittest
import sys
sys.path.append('../Office-Space-Allocation')
from amity_functions import *

class TestAmity(unittest.TestCase):

    def test_create_office(self):
        # tests that an office is created successfully
        Amity.all_rooms = []
        initial_num_rooms = len(Amity.office_spaces)
        self.assertEqual(len(Amity.all_rooms), 0)
        Amity.create_room(self, 'o', 'Oculus')
        self.assertEqual(len(Amity.office_spaces), initial_num_rooms+1)
        self.assertIn('OCULUS', Amity.office_spaces.keys())

    def test_create_living_area(self):
        # tests that the room created is a living space
        lspace = len(Amity.living_spaces)
        Amity.create_room(self, 'l', 'Arduino')
        self.assertIn('ARDUINO', Amity.living_spaces.keys())
        self.assertEqual(len(Amity.living_spaces), lspace+1)

    def test_add_person(self):
        # tests that a person is created
        all_people = len(Amity.all_people)
        Amity.all_people = []
        Amity.add_person("Kironde", "david", "F", "Y")
        self.assertEqual(len(Amity.all_people), all_people+1)

    def test_save_state(self):
        # test that the save state function creates a database when called
        Amity.save_state('testdb')
        self.assertTrue(os.path.isfile('testdb.sqlite'))
        os.remove('testdb.sqlite')

    def test_print_allocations(self):
        # tests if print allocation works
        Amity.print_allocations('testfile')
        self.assertTrue(os.path.isfile('testfile.txt'))
        os.remove('testfile.txt')

    def test_print_unallocated(self):
        # tests for print_allocation function in amity_functions
        Amity.print_unallocated('testfile')
        self.assertTrue(os.path.isfile('testfile.txt'))
        os.remove('testfile.txt')

if __name__ == '__main__':
    unittest.main()
