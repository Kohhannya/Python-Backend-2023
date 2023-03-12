import uuid


class User:
    id: uuid.UUID
    name: str
    comments_count: int
    rate: int
    is_banned: bool

    def __init__(self, name: str) -> None:
        self.id = uuid.uuid4()
        self.name = name
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name: str) -> None:
        self.name = new_name

    def increment_rate(self) -> None:
        self.rate += 1

    def ban_user(self) -> None:
        self.is_banned = True

    def unban_user(self) -> None:
        if self.is_banned:
            self.is_banned = False
        else:
            print('User is not banned now')

    def __repr__(self) -> str:
        s = 'User {} with id "{}" has {} comments, {} rate{}'
        ban = ''
        if self.is_banned:
            ban = ' and has been banned'
        return s.format(self.name, self.id, self.comments_count, self.rate, ban)
