"""
Amity helps you allocate rooms to people at random. Select a command to get
started.
Usage:
    create_room <room_type> <room_name>
    add_person <first_name> <last_name> <designation> [--wants_accomodation=N]
    reallocate_person <person_id> <room_type> <new_room>
    load_people <filename>
    print_room <room_name>
    print_allocations [--o=filename]
    print_unallocated [--o=filename]
    load_state [--dbname]
    save_state [--o=db_name]
    quit
    (-i | --interactive)
    Options:
    -h --help Show this screen.
    -i --interactive Interactive mode.
    -v --version
"""
import cmd, os
from docopt import docopt, DocoptExit
from pyfiglet import figlet_format
from termcolor import cprint
from amity_functions import Amity

def app_exec(func):
    """
    Decorator definition for the app.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            msg = "Invalid command! See help."
            print(msg)
            print(e)
            return

        except SystemExit:
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)

    return fn

def intro():
    cprint(figlet_format("Amity Room Allocation", font = "slant"),
           "blue")
    print("Welcome To Amity Interractive.")
    cprint(__doc__, "green")

class AmityInteractive(cmd.Cmd):
    intro()

    prompt = "Amity --> "
    file = None
    amity = Amity()

    @app_exec
    def do_create_room(self, arg):
        """Creates a new room
        Usage: create_room <room_type> <room_name>...
        """
        names = arg["<room_name>"]
        room_type = arg["<room_type>"]
        if not len(names) or not room_type:
            print("Make sure you enter all details")
        elif room_type.upper() not in ["L", "O"]:
            print("Invalid room type entered. Use either O or L")
        else:
            for name in names:
                if not name.isalpha():
                    print("Room name can only contain alphabets. Try again")
                else:
                    self.amity.create_room(room_type, name)
    @app_exec
    def do_add_person(self, arg):
        """
        Adds a person and allocates rooms if available
        Usage: add_person <first_name> <last_name> <designation> [--wants_accommodation=N]
        """
        first_name = arg["<first_name>"]
        last_name = arg["<last_name>"]
        designation = arg["<designation>"]
        wants_accommodation = arg["--wants_accommodation"]
        if not first_name.isalpha() or not last_name.isalpha():
            print("Names can only contain alphabets.")
        elif designation.upper() not in ["F", "S"]:
            print("Invalid designation. Enter F or S")
        else:
            if not wants_accommodation:
                self.amity.add_person(first_name.upper(), last_name.upper(),
                designation.upper())
            else:
                self.amity.add_person(first_name.upper(), last_name.upper(), designation.upper(), arg["--wants_accommodation"])

    @app_exec
    def do_print_room(self, arg):
        """
        Prints all the people in a given rooms
        Usage: print_room <room_name>
        """
        Amity.print_room(arg["<room_name>"])


    @app_exec
    def do_print_allocations(self, arg):
        """
        Prints all rooms and the people in them.
        Usage: print_allocations [--o=filename]
        """
        filename = arg["--o"] or ""
        self.amity.print_allocations(filename)

    @app_exec
    def do_print_unallocated(self, arg):
        """
        Prints all the people that don't have relevant rooms
        Usage: print_unallocated [--o=filename]
        """
        filename = arg["--o"] or ""
        self.amity.print_unallocated(filename)

    @app_exec
    def do_load_people(self, arg):
        """
        Loads people from a text file to the app.
        Usage: load_people <filename>
        """
        file_name = arg["<filename>"]
        if os.path.exists(file_name):
            self.amity.load_people(file_name)
            print("File loaded.")
        else:
            print ("file does not exist")

    @app_exec
    def do_reallocate_person(self, arg):
        """
        Reallocates person
        Usage: reallocate_person <first_name> <last_name> <room_type> <new_room>
        """
        first_name = arg["<first_name>"]
        last_name = arg["<last_name>"]
        room_type = arg["<room_type>"]
        new_room = arg["<new_room>"]
        self.amity.reallocate_person(first_name, last_name, room_type, new_room)

    @app_exec
    def do_load_state(self, arg):
        """
        Loads data from the specified db into the app.
        Usage: load_state <filename>
        """
        self.amity.load_state(arg["<filename>"])

    @app_exec
    def do_save_state(self, arg):
        """
        Persists app data into the given db
        Usage: save_state [--db_name=sqlite_db]
        """
        db = arg['--db_name']
        if db:
            self.amity.save_state(db)
        else:
            self.amity.save_state()

    @app_exec
    def do_quit(self, arg):
        """
        Exits the app.
        Usage: quit
        """
        exit()

if __name__ == '__main__':
    AmityInteractive().cmdloop()
