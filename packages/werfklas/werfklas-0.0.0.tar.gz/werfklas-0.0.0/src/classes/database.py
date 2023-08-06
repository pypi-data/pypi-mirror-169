from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, Session


def sessionSetup():
    engine = create_engine(
        'sqlite:///werfklas.db' + '?check_same_thread=False',
        echo=False,
    )
    return Session(bind=engine, autoflush=True)


def __init__():
    session = sessionSetup()


Base = declarative_base()


class Audit(Base):
    __tablename__ = 'tbl_audit'
    id = Column(Integer, primary_key=True)
    date = Column(Integer)
    action = Column(String)

    def __init__(self, aid, date, action):
        super().__init__()
        self.aid = aid
        self.date = date
        self.action = action


class Teacher(Base):
    __tablename__ = 'tbl_teachers'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)

    def __init__(self, tid, firstname, lastname):
        super().__init__()
        self.tid = tid
        self.firstname = firstname
        self.lastname = lastname


class Class(Base):
    __tablename__ = 'tbl_classes'
    id = Column(Integer, primary_key=True)
    class_name = Column(String)
    teacher = Column(Integer, ForeignKey('tbl_teachers.id'))
    teacher_r = relationship("Teacher", backref=backref("tbl_teachers", uselist=False))
    start_date = Column(Integer)
    end_date = Column(Integer)

    def __init__(self, class_id, class_name, teacher, start_date, end_date):
        super().__init__()
        self.class_id = class_id
        self.class_name = class_name
        self.teacher = teacher
        self.start_date = start_date
        self.end_date = end_date


class Family(Base):
    __tablename__ = 'tbl_families'
    id = Column(Integer, primary_key=True)
    lastname = Column(String)
    parent1 = Column(String)
    parent2 = Column(String)
    parent2_lastname = Column(String)
    divorced = Column(Boolean)

    def __init__(self, oid, lastname, parent1, parent2, parent2_lastname, divorced):
        super().__init__()
        self.oid = oid
        self.lastname = lastname
        self.parent1 = parent1
        self.parent2 = parent2
        self.parent2_lastname = parent2_lastname
        self.divorced = divorced


class Child(Base):
    __tablename__ = 'tbl_children'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    date_of_registration = Column(Integer)
    parents = Column(Integer, ForeignKey('tbl_families.id'))
    parents_r = relationship("Family", backref=backref("tbl_families", uselist=False))
    date_of_birth = Column(Integer)
    class_id = Column(Integer, ForeignKey('tbl_classes.id'))
    class_id_r = relationship("Class", backref=backref("tbl_classes", uselist=False))
    redo_school_year = Column(Boolean)
    _age = int

    def __init__(self, kid, firstname, lastname, date_of_registration, parents, date_of_birth, class_id,
                 redo_school_year):
        super().__init__()
        self.kid = kid
        self.firstname = firstname
        self.lastname = lastname
        self.date_of_registration = date_of_registration
        self.parents = parents
        self.date_of_birth = date_of_birth
        self.class_id = class_id
        self.redo_school_year = redo_school_year


def create_database(databasefile):
    engine = create_engine('sqlite:///' + databasefile, echo=True)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    app.run(debug=True)

# def __init__(self):

# ------ lisnters
