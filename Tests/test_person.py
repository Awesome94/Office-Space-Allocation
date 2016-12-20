import unittest
from unittest import TestCase

from Person.PersonClass import Fellow, Staff


class TestPerson(TestCase):

    def test_fellow(self):
        person_fellow = Fellow(1, "Nathan", "Robz", "FELLOW")
        self.assertEqual(person_fellow.designation, "FELLOW")

    def test_staff(self):
        person_staff = Staff(1, "Awesome", "Dave", "STAFF")
        self.assertEqual(person_staff.designation, "STAFF")

if __name__ == '__main__':
    unittest.main()