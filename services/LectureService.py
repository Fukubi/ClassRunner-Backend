from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.app import Base
from models.Lecture import Lecture


class LectureService:
    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///Database.db", echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)

    def create(self, lecture: Lecture):
        self.session.add(lecture)
        self.session.commit()

        return self.read()[-1]

    def read(self):
        return self.session.query(Lecture).all()

    def read_by_id(self, id):
        return self.session.query(Lecture).filter_by(id=id).first()

    def update(self, lecture: Lecture):
        if not lecture.id:
            return

        old_lecture = self.read_by_id(lecture.id)

        for attr in dir(lecture):
            if not attr.startswith("_") and not callable(getattr(lecture, attr)):
                if getattr(lecture, attr):
                    setattr(old_lecture, attr, getattr(lecture, attr))

        self.session.commit()

    def delete(self, id):
        self.session.delete(self.read_by_id(id))
        self.session.commit()
