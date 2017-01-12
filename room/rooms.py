class Room (object):
    def __init__(self, room_name=None, r_type=None, room_residents=None, capacity=None):
        self.room_name = room_name
        self.r_type = r_type
        self.capacity = capacity

class OfficeSpace(Room):
    def __init__(self, room_name):
        super(OfficeSpace, self).__init__(room_name, r_type="OFFICE", capacity=6)
        self.members = []


class LivingSpace(Room):
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name, r_type="LIVING SPACE", room_residents="MALE" or "FEMALE",
                                          capacity=4)
