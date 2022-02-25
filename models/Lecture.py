from collections import namedtuple
import json
from sqlalchemy import Column, Integer, String
from app.app import Base


def lecture_json_decoder(JSON):
    return namedtuple("Lecture", JSON.keys())(*JSON.values())


class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True)
    class_name = Column(String, nullable=False)
    creator_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    phone_number = Column(String)
    wa_group_link = Column(String)
    dc_server_link = Column(String)

    def __repr__(self) -> str:
        return f"id: {self.id}, class_name: {self.class_name}, creator_name: {self.creator_name}, description: {self.description}, phone_number: {self.phone_number}, wa_group_link: {self.wa_group_link}, dc_server_link: {self.dc_server_link}"

    def from_json(self, json):
        for attr in dir(self):
            if not attr.startswith("_"):
                try:
                    setattr(self, attr, json[attr])
                except KeyError:
                    pass
    
    def serialize(self):
        return {
            "id": self.id,
            "class_name": self.class_name,
            "creator_name": self.creator_name,
            "description": self.description,
            "phone_number": self.phone_number,
            "wa_group_link": self.wa_group_link,
            "dc_server_link": self.dc_server_link
        }
