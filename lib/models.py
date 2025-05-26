from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import Base
from config import session



class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)

    freebies = relationship('Freebie', back_populates='company')

    @property
    def devs(self):
        return list({freebie.dev for freebie in self.freebies})

    def give_freebie(self, dev, item_name, value):
        return Freebie(item_name=item_name, value=value, dev=dev, company=self)

    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    freebies = relationship('Freebie', back_populates='dev')

    @property
    def companies(self):
        return list({freebie.company for freebie in self.freebies})

    def received_one(self, item_name):
        return any(f.item_name == item_name for f in self.freebies)

    def give_away(self, other_dev, freebie):
        if freebie in self.freebies:
            freebie.dev = other_dev


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)

    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    dev = relationship('Dev', back_populates='freebies')
    company = relationship('Company', back_populates='freebies')

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
