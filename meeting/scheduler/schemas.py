from ninja import Schema


class EventSchema(Schema):
    name: str
    start_time: str
    end_time: str
    atendees: int
    email: str
