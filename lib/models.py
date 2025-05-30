from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    founding_year = Column(Integer)

    freebies = relationship("Freebie", back_populates="company")
    devs = association_proxy('freebies', 'dev',
        creator=lambda dev: Freebie(dev=dev))

    def __repr__(self):
        return f'<Company {self.name}>'

    def give_freebie(self, dev, item_name, value, db_session):
        freebie = Freebie(
            item_name=item_name,
            value=value,
            company=self,
            dev=dev
        )
        db_session.add(freebie)
        db_session.commit()
        return freebie

    @classmethod
    def oldest_company(cls, db_session):
        return db_session.query(cls).order_by(cls.founding_year).first()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    freebies = relationship("Freebie", back_populates="dev")
    companies = association_proxy('freebies', 'company',
        creator=lambda company: Freebie(company=company))

    def __repr__(self):
        return f'<Dev {self.name}>'

    def received_one(self, item_name):
        return any(f.item_name == item_name for f in self.freebies)

    def give_away(self, dev, freebie, db_session):
        if freebie in self.freebies:
            freebie.dev = dev
            db_session.commit()
            return True
        return False

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'))
    dev_id = Column(Integer, ForeignKey('devs.id'))

    company = relationship("Company", back_populates="freebies")
    dev = relationship("Dev", back_populates="freebies")

    def __repr__(self):
        return f'<Freebie {self.item_name}>'

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"