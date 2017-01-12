import os.path
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import mapper, sessionmaker
from tabulate import tabulate

from Models.models import (Base, PersonModel, RoomModel, DatabaseCreator,
                           OfficeSpaces, LivingSpaces)
from room.rooms import Room, OfficeSpace, LivingSpace
from collections import defaultdict
from Person.PersonClass import Person, Fellow, Staff
from colorama import init
init(autoreset=True)
from termcolor import colored
from  colorama import Fore, Back, Style

class Amity:
    all_rooms = []
    all_people = []
    living_spaces = {"None": []}
    office_spaces = {"None": []}

    def __init__(self):
        pass

    def create_room(self, r_type, room_name):
        # Creates an empty room of the specified type.
        if room_name.upper() in [room.room_name for room in Amity.all_rooms]:
            print(Fore.RED + "Sorry, %s already exists!!!" %room_name.upper())
        else:
            mapping = {'O': OfficeSpace, 'L': LivingSpace}
            new_room = mapping[r_type.upper()](room_name.upper())
            Amity.all_rooms.append(new_room)
            if r_type.upper() == "L":
                Amity.living_spaces[room_name.upper()] = []
            elif r_type.upper() == "O":
                Amity.office_spaces[room_name.upper()] = []
            print(Fore.GREEN + room_name.upper() + " created successfully.")

    @staticmethod
    def generate_random_office():
        # Generates a random room of the given type.
        offices = [room for room in Amity.all_rooms if room.r_type == "OFFICE"]
        available_offices = []
        for office in offices:
            if office.capacity > len(Amity.office_spaces[office.room_name]):
                available_offices.append (office.room_name)
        selected_room = "None"
        if len(available_offices):
            selected_room = random.choice(available_offices)
        return selected_room

    @staticmethod
    def generate_random_living_space():
        l_spaces = [room for room in Amity.all_rooms if room.r_type == "LIVING SPACE"]
        available_living_spaces = []

        for lspace in l_spaces:
            if lspace.capacity > len (Amity.living_spaces[lspace.room_name]):
                available_living_spaces.append (lspace.room_name)
        selected_room = "None"

        if len (available_living_spaces):
            selected_room = random.choice (available_living_spaces)

        return selected_room

    @staticmethod
    def add_person(first_name, last_name, designation, wants_accommodation="N"):
        # Adds a new person and allocates a random room to them.
        allocated_office = Amity.generate_random_office()
        mapping = {"F": Fellow, "S": Staff}
        person_id = len(Amity.all_people) + 1
        new_person = mapping[designation.upper()](person_id, first_name.upper(),
                                                  last_name.upper(),
                                                  designation)
        Amity.all_people.append(new_person)
        Amity.office_spaces[allocated_office].append(first_name.upper()
                                                          + " " + last_name.upper())

        if wants_accommodation.upper() == "Y" and designation.upper() == "F":
            allocated_living_space = Amity.generate_random_living_space()
            Amity.living_spaces[allocated_living_space].append(first_name.upper()
                                                              + " " + last_name.upper())
        print (first_name, last_name, Fore.GREEN + "Added successfully as %s" %designation)

        if wants_accommodation.upper() == "Y" and designation.upper()=="S":
            print (Fore.RED+ "Sorry, Staff can not be given accomodation")

    @staticmethod
    def load_people(filename):
        # Loads people from a file.txt into the app and creates them.
        with open(filename, 'r') as people_file:
            for person_dets in people_file:
                details = person_dets.rstrip().split()
                accommodate = details[3] if len(details) == 4 else "N"
                Amity.add_person(details[0], details[1], details[2],
                                 accommodate)
    @staticmethod
    def reallocate_person_to_office(full_name, new_room_name):
        '''
        use the person full name to remove the person from one office
        to another
        '''
        full_name = full_name.upper()
        if not full_name in Amity.all_people:
            return 'The person called %s does not exist' % full_name

        if len(Amity.office_spaces[new_room_name]) == 6:
            return '%s is already full' % new_room_name

        if full_name in Amity.office_spaces[new_room_name]:
            return '%s is already allocated to %s' % (full_name, new_room_name)

        for room, members in list(Amity.office_rooms.items()):
            if full_name in members:
                Amity.office_spaces[room].remove(full_name)
                Amity.office_rooms[new_room_name].append(full_name)

            print('%s has been reallocated to %s ' % (full_name, new_room_name))

    @staticmethod
    def reallocate_person_to_living_space(full_name, new_room_name):

        # use the person full name to remove the person from one livingspace
        # to another, should not reallocate to the same room or a room that is full

        full_name = full_name.upper()
        if not full_name in Amity.all_people:
            return 'The person called %s does not exist' % full_name

        if len(Amity.living_spaces[new_room_name]) == 4:
            return '%s is already full' % new_room_name

        if full_name in Amity.living_spaces[new_room_name]:
            return '%s is already allocated to %s' % (full_name, new_room_name)

        for room, members in list(Amity.ls_rooms.items()):
            if full_name in members:
                Amity.living_spaces[room].remove(full_name)
                Amity.living_spaces[new_room_name].append(full_name)
                print('%s has been reallocated to %s ' % (full_name, new_room_name))


    @staticmethod
    def print_allocations(file_name=None):
        print ("=" * 30 + "\n" + "Office Allocations\n" + "=" * 30)
        for room in Amity.office_spaces.keys ():
            if room != "None":
                print (room + "\n" + "+" * 30)
                for person in Amity.office_spaces[room]:
                    print (person)
        print ("=" * 30 + "\n" + "Living Space Allocations\n" + "=" * 30)
        for room in Amity.living_spaces.keys ():
            if room != "None":
                print (room + "\n" + "+" * 30)
                for person in Amity.living_spaces[room]:
                    print (person)
        if file_name:
            nfile = open (file_name + ".txt", "a")
            nfile.write ("=" * 30 + "\n" + "Office Allocations\n" + "=" * 30)
            for room in Amity.office_spaces.keys ():
                if room != "None":
                    nfile.write (room + "\n" + "+" * 30)
                    for person in Amity.office_spaces[room]:
                        nfile.write (person)
            nfile.write ("=" * 30 + "\n" + "Living Space Allocations\n" + "=" * 30)
            for room in Amity.living_spaces.keys ():
                if room != "None":
                    nfile.write (room + "\n" + "+" * 30)
                    for person in Amity.living_spaces[room]:
                        nfile.write (person)
            print ("%s.txt written" % file_name)

    @staticmethod
    def print_unallocated(file_name=None):
        """Prints all the people that have no rooms and arranges by room"""
        unallocated_office = Amity.office_spaces["None"]
        unallocated_lspace = Amity.living_spaces["None"]
        print ("=" * 30 + "\n" + "No Office\n" + "=" * 30)
        for person in unallocated_office:
            print (person or "None")
        print ("=" * 30 + "\n" + "No Living Space\n" + "=" * 30)
        for person in unallocated_lspace:
            print (person or "None")

        if file_name:
            file = open (file_name + ".txt", "a")
            file.write ("=" * 30 + "\n" + "No Office\n" + "=" * 30)
            for person in unallocated_office:
                file.write ("\n" + person or "None")
            file.write ("\n" + "=" * 30 + "\n" + "No LivingSpace\n" + "=" * 30)
            for person in unallocated_lspace:
                file.write ("\n" + person or "None")
            print (Fore.GREEN +"%s.txt written successfully" % file_name)

    @staticmethod
    def print_room(room_name):
        offices = [room for room in Amity.office_spaces
                   if room != "None"]
        lspaces = [room for room in Amity.living_spaces
                   if room != "None"]
        if room_name.upper () not in offices and room_name.upper () not in lspaces:
            print (Fore.RED +"The room doesn't exist")
        else:
            print ("=" * 30 + "\n Members \n" + "=" * 30)
            if room_name.upper () in offices:
                for person in Amity.office_spaces[room_name.upper ()]:
                    print (person)
            elif room_name.upper () in lspaces:
                for person in Amity.living_spaces[room_name.upper ()]:
                    print (person)

    @staticmethod
    def load_state(dbname=None):
        dbname = dbname + ".sqlite"
        if not os.path.isfile(dbname):
            print ("database does not exist")
        else:
            engine = create_engine("sqlite:///" + dbname)
            Session = sessionmaker()
            Session.configure(bind=engine)
            session = Session()
            people = session.query(PersonModel).all()
            rooms = session.query(RoomModel).all()
            office_spaces = session.query(OfficeSpaces)
            living_spaces = session.query(LivingSpaces)

            for room in Amity.all_rooms:
                Amity.all_rooms.append(room)
            for person in Amity.all_people:
                Amity.all_people.append(person)
            for office_space in office_spaces:
                all_members = office_space.members.split(",")
                Amity.office_spaces[office_space.room_name]=Amity.all_people
            for living_space in living_spaces:
                all_members = living_space.members.split(","
                )
                Amity.living_spaces[living_space.room_name] = all_members
            print(Fore.GREEN + "Data from %s loaded to the app." %dbname)

    @staticmethod
    def save_state(db_name=None):
        """Persists data saved in the app to a db"""
        if not db_name:
            db = DatabaseCreator("default_db")
        else:
            db = DatabaseCreator(db_name)

        for room in Amity.all_rooms:
            room_to_save = RoomModel(name=room.room_name,
            rtype=room.r_type)
            db.session.add(room_to_save)

        for person in Amity.all_people:
            person_to_save = PersonModel(
            name=person.name, designation=person.designation)
            db.session.add(person_to_save)

        for room in Amity.office_spaces:
            office_members = ",".join(Amity.office_spaces[room])
            office_spaces_sv = OfficeSpaces(
            room_name=room,
            members=office_members
            )
            db.session.add(office_spaces_sv)
        for room in Amity.living_spaces:
            lspace_members = ",".join(Amity.living_spaces
            [room])
            living_spaces_sv = LivingSpaces(
            room_name=room,
            members=lspace_members)
            db.session.add(living_spaces_sv)
        db.session.commit()

        print(Fore.GREEN + "successfully saved state as %s!" %db_name)
