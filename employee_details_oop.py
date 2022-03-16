class Employee:
    # All Employee objects will need:
    # first name        - string
    # last name         - string
    # day               - int
    # month             - int
    # year              - int
    # position          - int
    # graduation status - bool
    # Employee object constructor
    def __init__(self, fn, ln, d, m, y, pos, grad, ids):
        self.first_name = fn
        self.last_name = ln
        self.birth_day = d
        self.birth_month = m
        self.birth_year = y
        self.position = pos
        self.graduated = grad
        self.ids = ids

    # Print output format
    def __str__(self):
        return f"'firstname': '{self.first_name}', 'lastname': '{self.last_name}', 'day': {self.birth_day}, 'month': {self.birth_month}, 'year': {self.birth_year}, 'position': '{self.position}', 'graduated': {self.graduated}, 'id': {self.ids}"

    # Setters and Getters for all Employee's properties
    def set_first_name(self, firstname):
        self.first_name = firstname

    def set_last_name(self, lastname):
        self.last_name = lastname

    def set_birth_day(self, birthday):
        self.birth_day = birthday

    def set_birth_month(self, birthmonth):
        self.birth_month = birthmonth

    def set_birth_year(self, birthyear):
        self.birth_year = birthyear

    def set_position(self, pos):
        self.position = pos

    def set_graduation(self, grad):
        self.graduated = grad

    def set_ids(self, emplid):
        self.ids = emplid

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_birth_day(self):
        return self.birth_day

    def get_birth_month(self):
        return self.birth_month

    def get_birth_year(self):
        return self.birth_year

    def get_position(self):
        return self.position

    def get_graduation(self):
        return self.graduated

    def get_ids(self):
        return self.ids
