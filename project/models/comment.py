import uuid
from datetime import datetime


class Comment:
    author_id: uuid.UUID
    text: str
    create_data: datetime
    update_data: datetime
    like_count: int

    def __init__(self, author_id: uuid.UUID, text: str) -> None:
        self.author_id = author_id
        self.text = text
        self.create_data = datetime.now()
        self.update_data = self.create_data
        self.like_count = 0

    def edit_comment(self, new_text: str) -> None:
        self.text = new_text
        self.update_data = datetime.now()

    def like(self) -> None:
        self.like_count += 1

    def dislike(self) -> None:
        self.like_count -= 1

    def __repr__(self) -> str:
        s = 'Comment by user {} created {} and rated {} times with the words \n"{}"\nLast update: {}'
        return s.format(self.author_id, self.create_data, self.like_count, self.text, self.update_data)
