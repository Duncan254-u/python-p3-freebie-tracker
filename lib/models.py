from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', back_populates='company', cascade='all, delete-orphan')

    devs = association_proxy('freebies', 'dev')
    creator= lambda dev: Freebie(dev=dev)

    def __repr__(self):
        return f'<Company {self.name}>'
    
    def give_freebie(self, dev, item_name, value):
        freebie = Freebie(
            item_name=item_name,
            value=value,
            company=self,
            dev=dev
        )
        return freebie
    
    @classmethod
    def oldest_company(cls):
        return cls.quert.order_by(cls.founding_year).first()

    



 class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship('Freebie', back_populates='dev', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Dev {self.name}>'
