class Base_employee:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def login(self, l, p):
        if (l == self.username) & (p == self.password):
            print('ok')
            return 1
        else:
            print('no')
            return 0

