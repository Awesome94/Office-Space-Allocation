class Person(object):
    def __init__(self, person_id, first_name, last_name, person_type, wants_accommodation):
        self.Id = person_id
        self.name = first_name + " " + last_name
        self.person_type = person_type
        self.wants_accommodation = wants_accommodation


class Fellow(Person):
    def __init__(self, person_id, first_name, last_name):
        super(Fellow, self).__inti__(person_id, first_name, last_name, person_type="FELLOW", wants_acomodation="N")
    pass


class Staff(Person):
    def __init__(self, person_id, first_name, last_name):
        super(Fellow, self).__inti__(person_id, first_name, last_name, person_type="STAFF")
    pass
