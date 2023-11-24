from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey


class Plan(Base, BaseModel):
    """
    store future plan of user
    """

    __tablename__ = 'planings'
    name = Column(String(60), nullable=False)
    amount = Column(Integer, nullable=False)
    description = Column(String(60))
    category_id = Column(Integer, ForeignKey(
        "categories.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __init__(self, amt, name, desc, user_id, cateid):
        """
        initialize plan class
        """
        self.name = name
        self.amount = amt
        self.description = desc
        self.category_id = cateid
        self.user_id = user_id

    def __repr__(self):
        return f"{self.id}: {self.__tablename__}"


class User(BaseModel, Base):
    __tablename__ = "users"
    username = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    fname = Column(String(60), nullable=False)
    lname = Column(String(60), nullable=False)
    password = Column(String(18), nullable=False)
    location_id = Column(String(60), ForeignKey('location.id'), nullable=False)
    expense = relationship("Expense", backref='users')
    income = relationship("Income", backref="users")
    plan = relationship("Plan", backref="planner")

    def __init__(self, usrname, email, fname, lname, psd, loc_id):
        self.username = usrname
        self.email = email
        self.fname = fname
        self.lname = lname
        self.password = psd
        self.location_id = loc_id


class Location(BaseModel, Base):
    __tablename__ = 'location'
    country = Column(String(60), nullable=False)
    province = Column(String(60), nullable=False)
    user = relationship('User', backref='location')

    def __init__(self, ctr, pr):
        self.country = ctr
        self.province = pr


class Income(BaseModel, Base):
    __tablename__ = 'incomes'
    name = Column(String(60), nullable=False)
    desc = Column(String(60))
    amount = Column(Integer, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    category_id = Column(String(60), ForeignKey(
        'categories.id'), nullable=False)

    def __init__(self, name, desc, amt, usrid, ctid):
        self.name = name
        self.desc = desc
        self.amount = amt
        self.user_id = usrid
        self.category_id = ctid

    def __repr__(self) -> str:
        return f"{self.id}: {self.id}"


class Expense(BaseModel, Base):
    __tablename__ = 'expenses'
    name = Column(String(60), nullable=False)
    desc = Column(String(60), nullable=True)
    amount = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    def __init__(self, name, desc, amt, usrid, ctid):
        self.name = name
        self.amount = amt
        self.desc = desc
        self.user_id = usrid
        self.category_id = ctid

    def __repr__(self):
        return f"<{self.__tablename__}>: <{self.id}>"


class Category(BaseModel, Base):
    __tablename__ = 'categories'
    type = Column(String(60), nullable=False)
    expense = relationship("Expense", backref="spend")
    income = relationship("Income", backref="revenue")
    plans = relationship("Plan", backref="categories")

    def __init__(self, name):
        self.type = name
