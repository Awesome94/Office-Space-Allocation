class Room (object):
    def __init__(self, room_name=None, room_type=None, room_residents=None, room_capacity=None):
        self.room_name = room_name
        self.room_type = room_type
        self.room_capacity = room_capacity
        self.residents = room_residents
        self.people_in_room = []


class OfficeSpace(Room):
    def __init__(self, room_name):
        super(OfficeSpace, self).__init__(room_name, room_type="OFFICE", room_capacity=6)
        self.members = []


class LivingSpace (Room):
    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name, room_type="LIVING SPACE", room_residents="MALE" or "FEMALE",
                                          room_capacity=4)
        self.members = []


# class MaleLivingSpace (LivingSpace):
#     def __init__(self, room_name):
#         super(MaleLivingSpace, self).__init__(room_name, room_type="LIVING_SPACE", room_capacity=4)
