from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate

from Models.models import (Base, Person, Room, DatabaseCreator,
                           OfficeSpaces, LivingSpaces)
from room.rooms import Room
from room.rooms import LivingSpace
from room.rooms import OfficeSpace
from collections import defaultdict
from Person.PersonClass import Person, Fellow, Staff
import random


class Amity:
    all_rooms = []
    all_people = []
    living_spaces = {"None": []}
    office_spaces = {"None": []}

    def create_room(self, room_type, room_name):
        """Creates an empty room of the specified type."""
        if room_name.upper() in [room.name for room in Amity.all_rooms]:
            print("Sorry, Room already exists!!!")
        else:
            mapping = {'O': OfficeSpace, 'L': LivingSpace}
            new_room = mapping[room_type.upper()](room_name.upper())
            Amity.all_rooms.append(new_room)
            if room_type.upper() == "L":
                Amity.living_spaces[room_name.upper()] = []
            elif room_type.upper() == "O":
                Amity.office_spaces[room_name.upper()] = []
            print(room_name.upper() + " created successfully.")


    def generate_random_office(self):
        """Generates a random room of the given type."""
        offices = [room for room in Amity.all_rooms if room.room_type == "OFFICE"]
        available_offices = []
        for office in offices:
            if office.room_capacity > len (Amity.office_spaces[office.room_name]):
                available_offices.append (office.room_name)

        selected_room = "None"

        if len (available_offices):
            selected_room = random.choice (available_offices)
        return selected_room

    def generate_random_living_space(self):
        l_spaces = [room for room in Amity.all_rooms if room.room_type == "LIVING SPACE"]
        available_living_spaces = []

        for lspace in l_spaces:
            if lspace.capacity > len (Amity.living_spaces[lspace.name]):
                available_living_spaces.append (lspace.name)
        selected_room = "None"

        if len (available_living_spaces):
            selected_room = random.choice (available_living_spaces)

        return selected_room

    def add_person(self, first_name, last_name, designation, wants_accommodation="N"):
        """ this function will add a new person to Amity and randomly allocate them a room"""
        allocated_office_space = self.generate_random_office ()
        p_structure = {"F": Fellow, "S": Staff}
        person_id = len (Amity.all_people) + 1
        new_person = p_structure[designation.upper ()] (person_id, first_name.upper (),
                                                        last_name.upper (), designation)
        Amity.all_people.append(new_person)
        Amity.office_spaces[allocated_office_space].append (first_name.upper ()
                                                            + " " + last_name.upper ())

        if wants_accommodation.upper () == "Y" and designation.upper () == "F":
            # if the fellow wants accommodation they will added to a random living_space
            allocated_living_space = self.amity.generate_random_living_space()
            amity.living_spaces[allocated_living_space].append (first_name.upper()
            + " " + last_name.upper())

            print ("Completed Successfully")

    @staticmethod
    def reallocate_person(first_name, last_name, room_type, new_room):
        """This function moves the person from one room to another"""
        full_name = first_name.upper () + " " + last_name.upper ()
        fellows = [p.name for p in Amity.all_people
                   if p.designation == "FELLOW"]
        staff = [p.name for p in Amity.all_people
                 if p.designation == "STAFF"]
        available_lspaces = [r.room_name for r in Amity.all_rooms
                             if r.room_type == "LIVING SPACE"
                             and len (Amity.living_spaces[r.room_name]) < 4]

        available_offices = [r.room_name for r in Amity.all_rooms

                             if r.room_type == "OFFICE"
                             and len (Amity.office_spaces[r.room_name]) < 6]

        if full_name not in fellows and full_name not in staff:
            print ("The person doesn't exist.")

        elif new_room.upper () not in available_lspaces and new_room.upper () not in available_offices:

            print ("The room requested does not exist or is not available")
            print ("Available Offices \n" + available_offices)
            print ("Available living spaces\n" + available_lspaces)
        else:
            if room_type.upper () == "L":
                if new_room in available_offices and new_room not in available_lspaces:
                    print ("The room selected is not a LivingSpace.")
                elif full_name not in fellows:
                    return "The person has to exist and be a fellow!"
                else:
                    for room in Amity.living_spaces.keys ():
                        if full_name in Amity.living_spaces[room]:
                            cur_lspace = Amity.living_spaces[room]
                            cur_lspace.remove (full_name)
                            Amity.living_spaces[new_room.upper ()].append (full_name)
                            print ("Success!")
            elif room_type.upper () == "O":
                if new_room not in available_offices and new_room in available_lspaces:
                    print ("The room selected is not an office")
                else:
                    for room in Amity.living_spaces.keys ():
                        if full_name in Amity.office_spaces[room]:
                            cur_office = Amity.office_spaces[room]
                            cur_office.remove (full_name)
                            Amity.office_spaces[new_room.upper ()].append (full_name)
                            print ("Success!")

    @staticmethod
    def load_people(filename):
        """Loads people from a file.txt into the app and creates them"""
        with open (filename, 'r') as people_file:
            for person_dets in people_file:
                details = person_dets.rstrip ().split ()
                accomodate = details[3] if len (details) == 4 else "N"
                Amity.add_person (details[0], details[1], details[2],
                                  accomodate)

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
            print ("%s.txt written successfully" % file_name)

    @staticmethod
    def print_room(room_name):
        offices = [room for room in Amity.office_spaces
                   if room != "None"]
        lspaces = [room for room in Amity.living_spaces
                   if room != "None"]
        if room_name.upper () not in offices and room_name.upper () not in lspaces:
            print ("The room doesn't exist")
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
        """Loads data from database into the application."""
        engine = create_engine ("sqlite:///" + dbname + ".sqlite")
        Session = sessionmaker ()
        Session.configure (bind=engine)
        session = Session ()
        people = session.query (Person).all ()
        rooms = session.query (Room).all ()
        office_spaces = session.query (OfficeSpace)
        living_spaces = session.query (LivingSpaces)
        if not dbname:
            print ("You must select a db to load.")
        else:
            for room in rooms:
                Amity.all_rooms.append (room)
            for person in people:
                Amity.all_people.append (person)
            for office_space in office_spaces:
                all_members = office_space.members.split (",")
                Amity.office_spaces[office_space.room_name] = all_members
            for living_space in living_spaces:
                all_members = living_space.members.split (",")
                Amity.living_spaces[living_space.room_name] = all_members

            print ("Data from %s loaded to the app." % dbname)

    @staticmethod
    def save_state(db_name=None):
        """Persists data saved in the app to a db"""
        if not db_name:
            db = DatabaseCreator ("default_db")
        else:
            db = DatabaseCreator (db_name)
        Base.metadata.bind = db.engine
        db_session = db.session ()
        for room in Amity.all_rooms:
            room_to_save = Room (
                name=room.name,
                rtype=room.room_type,
                capacity=room.room_capacity
            )
            db_session.merge (room_to_save)
        for person in Amity.all_people:
            person_to_save = Person (
                # person_id=person.person_id,
                name=person.name,
                designation=person.designation
            )
            db_session.merge (person_to_save)
        for room in Amity.office_spaces:
            office_members = ",".join (Amity.office_spaces[room])
            office_spaces_sv = OfficeSpaces (
                room_name=room,
                members=office_members
            )
            db_session.merge (office_spaces_sv)
        for room in Amity.living_spaces:
            lspace_members = ",".join (Amity.living_spaces[room])
            living_spaces_sv = LivingSpaces (
                room_name=room,
                members=lspace_members
            )
            db_session.merge (living_spaces_sv)
        db_session.commit ()
        print ("Success!")
