#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base

def debug_session():
    # Setup database connection
    engine = create_engine('sqlite:///freebies.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create test data
    company = Company(name="TestCorp", founding_year=2005)
    dev = Dev(name="TestDev")
    session.add_all([company, dev])
    session.commit()

    # Create freebie using the session
    freebie = Freebie(
        item_name="TestItem",
        value=50,
        company=company,
        dev=dev
    )
    session.add(freebie)
    session.commit()

    # Alternative: If you want to keep using give_freebie method,
    # modify your Company class to either:
    # 1. Accept session parameter (current implementation), or
    # 2. Create its own session internally

    # Debug output
    print("Test objects created:")
    print(f"- company: {company}")
    print(f"- dev: {dev}")
    print(f"- freebie: {freebie}")
    print("\nTry these commands:")
    print("freebie.print_details()")
    print("company.freebies")
    print("dev.companies")
    print("Company.oldest_company(session)")  # Now properly passed
    print("dev.received_one('TestItem')")
    print("dev.give_away(other_dev, freebie, session)")  # Added session

    import ipdb; ipdb.set_trace()

if __name__ == '__main__':
    debug_session()