from room.rooms import Room
from room.rooms import LivingSpace
from room.rooms import OfficeSpace
from collections import defaultdict
from Person.PersonClass import Person


class Amity:
    all_rooms = {'Offices': [], 'living_spaces': []}
    # all_people = {'Fellows': [], 'Staff': []}
    all_people = []
    all_fellows = []
    all_staff = []
    living_spaces = []
    offices = []
    male_living_spaces = []
    female_living_spaces = []
    living_spaces = []
    resident_fellows = []
    non_resident_fellows = []

    def create_room(self,):
        """creating an instance room from Room class
        the create room function will create a room that has not been existing"""
        room = Room()
        if room.room_name in Amity.all_rooms:
            print("Room has already been created") '''If the room exists already, it will not be created'''
        else:
            self.all_rooms.append(room.room_name)

    def add_person(self, name):
        person = Person
        person.name = name
        if person.name in Amity.all_people:
            print("Person has already been added")
        else:
            self.all_people.append(person.name)

    # def reallocate_person(self):
    #     people = Person()
    #     if people.name in

        # This function will move a person from one room to another.

        pass

    def load_people(self):
        pass

    def print_allocations(self):
        pass

    def print_unallocated(self):
        pass

    def print_room(self):
        pass

    @staticmethod
    def set_room_type(room_name, room_type):
        amity = Amity()
        room = Room
        room.room_name = room_name
        room.room_type = room_type
        if room.room_type is 'OFFICE':
            print ("The Room you have added is an Office")
            amity.offices.append(room.room_name)
        else:
            room.room_type is 'LIVING SPACE'
            print ("Living Space Successfully Created")
            amity.living_spaces.append(room.room_name)


