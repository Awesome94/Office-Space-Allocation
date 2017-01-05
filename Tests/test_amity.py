import os
import unittest
from unittest import TestCase
# from mock import patch

from amity_functions import *



class TestAmity(unittest.TestCase):

    def test_it_creates_office(self):
        Amity.all_rooms =[]
        Amity.create_room('o', 'Oculus')
        self.assertNotEqual(len(amity.all_rooms), 0)
        self.assertIn('OCULUS', Amity.office_spaces.keys())
        amity.all_rooms = []

    def test_it_creates_living_area(self):
        Amity.create_room('l', 'Arduino')
        self.assertNotEqual(len(amity.all_rooms), 0)
        self.assertIn('ARDUINO', Amity.living_spaces.keys())
        amity.all_rooms = []

    def test_add_person(self):
        Amity.all_people = []
        Amity.add_person("Kironde", "david", "F", "Y")
        Amity.add_person("dan", "daniels", "S")
        self.assertNotEqual(len(Amity.all_people), 0)

    def test_it_saves_state(self):
        Amity.save_state('testdb')
        self.assertTrue(os.path.isfile('testdb.sqlite'))
        os.remove('testdb.sqlite')

    def test_it_prints_allocations(self):
        Amity.print_allocations('testfile')
        self.assertTrue(os.path.isfile('testfile.txt'))
        os.remove('testfile.txt')

    def test_it_prints_unallocated(self):
        Amity.print_unallocated('testfile')
        self.assertTrue(os.path.isfile('testfile.txt'))
        os.remove('testfile.txt')

if __name__ == '__main__':
    unittest.main()
