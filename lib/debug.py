#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base

def debug_session():
    
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

   
    company = Company(name="TestCorp", founding_year=2005)
    dev = Dev(name="TestDev")
    session.add_all([company, dev])
    session.commit()

    
    freebie = Freebie(
        item_name="TestItem",
        value=50,
        company=company,
        dev=dev
    )
    session.add(freebie)
    session.commit()

    print("Test objects created:")
    print(f"- company: {company}")
    print(f"- dev: {dev}")
    print(f"- freebie: {freebie}")
    print("\nTry these commands:")
    print("freebie.print_details()")
    print("company.freebies")
    print("dev.companies")
    print("Company.oldest_company(session)")  
    print("dev.received_one('TestItem')")
    print("dev.give_away(other_dev, freebie, session)") 

    import ipdb; ipdb.set_trace()

if __name__ == '__main__':
    debug_session()