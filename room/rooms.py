class Room(object):
    def __init__(self, room_name=None, room_type=None, room_capacity=None):
        self.room_name = room_name
        self.room_type = room_type
        self.room_capacity = room_capacity


class OfficeSpace(Room):
    def __init__(self, room_name):
        super(OfficeSpace, self).__init__(room_name, room_type="OFFICE", room_capacity=6)


class LivingSpace(Room):
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name, room_type="LIVING_SPACE", room_capacity=4)

