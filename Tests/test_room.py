import unittest

from unittest import TestCase

from room.rooms import LivingSpace, OfficeSpace


class TestRooms(TestCase):

    # Testing for the types of rooms i.e. Office of lIVING SPACE as well as the capacity of the rooms
    def test_office_space(self):
        oculus = OfficeSpace("OCULUS")
        self.assertEqual(oculus.room_capacity, 6)
        self.assertEqual(oculus.room_type, "OFFICE")

    def test_living_space(self):
        arduino = LivingSpace("ARDUINO")
        self.assertEqual(arduino.room_capacity, 4)
        self.assertEqual(arduino.room_type, "LIVING SPACE")

if __name__ == '__main__':
    unittest.main()