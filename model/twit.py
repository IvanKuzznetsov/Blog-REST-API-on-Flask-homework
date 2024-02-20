from model.user import User


class Twit:

    def __init__(self, body: str, author: User, id: int):
        self.body = body
        self.author = author
        self.id = id

    def to_dict(self):
        return {"body": self.body, "author": self.author, "id": self.id}
