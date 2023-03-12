import uuid


class User:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name):
        self.name = new_name

    def increment_rate(self):
        self.rate += 1

    def ban_user(self):
        self.is_banned = True

    def unban_user(self):
        if self.is_banned:
            self.is_banned = False
        else:
            print('User is not banned now')

    def __repr__(self):
        s = 'User {} with id {} has {} comments, {} rate and {}ban'
        no = ''
        if not self.is_banned:
            no = 'no '
        return s.format(self.name, self.id, self.comments_count, self.rate, no)
